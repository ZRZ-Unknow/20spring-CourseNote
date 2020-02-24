# C1:应用眼中的操作系统（1）

- 什么是程序？：
  
  >+ 可执行文件和其他数据文件: Linux中有多种可执行文件格式，ELF最常用
  >
  >+ 运行的程序称为 **进程**

- ```shell
  file <filename>     #查看文件
  ```

- 常见应用程序

  - Core Utilities(核心工具包)

  - 系统、工具程序
  
    ```shell
  ip address
    ps
  ...
    ```
    
  - ubuntu packages: 可以搜索包
  
- 可执行文件也可以被看作文本文件，其中ELF文件以`0x7f`开头

- 可以用vim,cat,xxd等命令查看可执行文件

  ```shell
  vim /bin/ls    # 乱码,但可以看到字符串常量
  xxd /bin/ls    # 字节码 ，可以看到文件以'\x7f''ELF'开头
  ```
```

## ELF文件

关注信息：

- ELF Header  

  - 文件内容分布、指令集体系结构、入口地址

  ```shell
  readelf -h <elf file>  #-h显示elf的头部
```

- Program Header

  - 决定ELF文件应当被如何加载

  ```
  readelf -l <elf file>
  ```

+ `/usr/include/elf.h` elf的一些定义

## Hello OS World!

- ```shell
  gcc -c hello.c     #生成可重定位文件hello.o
  .c -> (preprocess) -> .i -> (compile) -> .s -> (assembly) -> .o -> (link) -> a.out
  ```

#### 尝试1

- 尝试链接: `ld hello.o`

```shell
(base) ➜  [/home/derek/test] git:(b2) ✗ ld main.o
ld: warning: cannot find entry symbol _start; defaulting to 00000000004000b0
main.o: In function `main':
main.c:(.text+0xc): undefined reference to `puts'
```

- 出现该问题是因为在`-O0`优化下编译器仍会把`printf`优化为`puts`，而此处没有与`libc.a`链接，之后会处理该问题。这里我们把`printf`注释掉。
- _start 是链接器默认的入口，可以手工指定入口：`ld -e main hello.o` 将main作为入口

#### 尝试2

- 这里我们把`printf`注释掉，把include注释掉，只有一个main。重新编译并链接,得到a.out。

```shell
(base) ➜  [/home/derek/test] git:(b2) ✗ ./a.out 
[1]    27462 segmentation fault (core dumped)  ./a.out
```

- 尝试gdb调试，发现是因为无人调用`main`，然而`main`在`ret`时返回地址存在且越界 
- gdb 的 starti 命令可以在程序的第一条指令停下来
- 单步调试后，发现return出错，栈上没有返回地址，返回访问了非法的地址

#### 尝试3

- 不用`main.c`, 编写一段汇编minimal.S
- gcc -c minimal.S  得到  minimal.o , 链接后得到 a.out

#### main之前发生了什么

+ 一个C程序执行的第一条指令在哪里？

  > + ld-linux-x86-64.so加载了libc
  >
  > + 之后libc完成了自己的初始化

- 首先是操作系统动态链接器，加载了libc
- 然后是libc完成了初始化
- 最后是`main`
- 在`main`函数执行前，会先调用`constructors`构造器，`main`结束后会调用`destructors`析构器

## objdump

- 用于展示目标文件的信息
- 参数
  - -d：展示反汇编
  - -S：如果目标文件使用-g选项编译，-S可以同时展示源代码和汇编: objdump -S a.out

## strace

```
strace <program>
```

- 打印程序的系统调用序列

```
strace -f gcc main.c #可获取子进程的系统调用
```

- `strace ./a.out` 

+ `strace ./a.out > /dev/null` ，将标准输出重定向到null
+ `strace -f gcc a.c 2>&1  |  grep execve`,将标准错误输出重定向到标准输出，并用grep查看execve的系统调用情况:
+ collect2系统调用：收集器，合成构造器与析构器

## 图形界面 Demo

- GUI编辑器`xedit`
- 通过`strace`查看`xedit`的系统调用

```
recvmsg(3, {msg_namelen=0}, 0)          = -1 EAGAIN (Resource temporarily unavailable)
poll([{fd=3, events=POLLIN|POLLOUT}], 1, -1) = 1 ([{fd=3, revents=POLLOUT}])
```





# 并发：共享内存多线程（1）

+ **并发 (Concurrency)** 多个执行流可以不按照一个特定的顺序执行
+ **并行 (Parallelism)**：允许多个执行流同时执行 (多个处理器)
+ **线程**：多个执行流并发/并行执行，并且它们==共享内存==
  - 两个执行流共享代码和所有全局变量 (数据、堆区)
  - 线程之间指令的执行顺序是不确定 (*non-deterministic*) 的

+ ```c
  extern int x;
  int foo() {
    int volatile t = x;
    t += 1;
    x = t;
  }
  // foo的代码可以共享，t和x可以共享，但两个线程的寄存器，堆栈是独享的
  ```

+ 不同线程：

  >+ 共享代码：所有线程的代码都来自当前进程的代码
  >+ 共享数据：全局数据/堆区可以自由引用
  >+ 独立堆栈：每个线程有独立的堆栈

+ atexit()函数
+ `gcc a.c -I.`可以让`#include <threads.h>`也搜索当前目录
+ 

