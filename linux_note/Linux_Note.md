# Linux_Note

## 终端常用命令

+ 压缩：zip -q -r cache.zip ./cachesim

+ 删除： rm -f  [文件名]

  rm -rf *  删除当前目录下所有文件wenjianjia

  rm -rf  [文件夹名]

+ .deb 删除软件:

  安装： sudo dpkg  -i  package_name.deb
  
  显示所有以.deb的软件： sudo dpkg-query -l  ，得到software_name
  
  删除软件：sudo dpkg -r  software_name  
  
+ ls -a 显示隐藏文件

## vim使用笔记

+ normal模式下，d剪切，y复制，p粘贴，u撤销

+ 在别处(如浏览器中使用 ctrl+c 或 在vim中用y选定内容)复制的，可在normal模式下在当前 shift+insert粘贴过来



## git使用笔记

### 基本概念

commit: 一次提交，在本地处理

branch: 一串不分叉的commit

remote: 一些branch聚在一起

git pull :更新origin,然后把master与origin/master合并，相当于：

​     git fetch origin

​     git merge origin/master

### git log

```c
git log --oneline:      //输出一行
git log --stat:        //输出文件增删改的统计数据
git log -p:            //输出形式以diff的形式给出
git log --author=ZRZ    //给出作者的log
git log --filename     //只显示这个文件的改动情况
git log --graph      //用图的方式查看
git diff        //显示哪些文件被改动了
git diff --word-diff      //单词级别的改动
```



### git add

```c
git status:          //与当前存档相比哪些文件发生了变化
git add file.c:        //增加file.c加入跟踪列表
git add -A:          //一次添加所有未被跟踪的文件
git rm --cached filename  //取消追踪一个文件
```

### git pull

```c
git pull origin master        //拉取远程服务器origin的master分支到本地
```

### git clone

```c
git clone https://.../.git       将改仓库克隆到本地
```

### git push

```c
git push origin master   //将本地的master分支的修改push到远程服务器origin
```

### git commit

```c
git commit --allow-empty -am "commit info"  //可以忽略nothing to commit
git rev-list --all --count     //查看总commit数量
```

### git 分支整理

```c
git branch           //查看当前分支
git checkout master   // 转到分支master
git merge pa0            // 将pa0中的内容merge到master中
git checkout -b pa1       //创建分支pa1并转到pa1 -b/-B:若无分支则创建，否则重置分支
git reset --hard xxxx:         //读档，hash code前缀（8个）
git branch -d pa0    //删除分支pa0
//远程仓库相关

git clone [http]           //用https形式克隆到本地
git remote -v          //查看当前的远程仓库
git remote add [name] [http]        //增加一个别名为name的远程仓库
git push [远程主机名] [本地分支名]:[远程分支名]  //要输入密码
//使用这条命令后再push/pull输入一次密码后即可不用再输入,会在本地生成一个文本记录账号与密码
git config --global credential.helper store
```



## 环境变量

+ 在home目录下 打开 .bashrc文件:  vi .bashrc
+ 在文件的最后加入环境变量,如： export STUID=181220076
+ 保存退出，运行： source .bashrc即可
+ 查看: echo \$STUID





## M1:pstree

+ 进程编号pid_t 是int

+ 进程信息在/proc/[pid]/stat 中，Stat 进程状态。如：
   6873 (a.out) R 6723 6873 6723 34819 6873
   各字段含义：
  + pid=6873 进程(包括轻量级进程，即线程)号
     comm=a.out 应用程序或命令的名字
     task_state=R 任务的状态：R:runnign, S:sleeping (TASK_INTERRUPTIBLE), D:disk  sleep (TASK_UNINTERRUPTIBLE), T: stopped, T:tracing stop,Z:zombie,  X:dead
  + ppid=6723 父进程ID
     pgid=6873 线程组号
     sid=6723 c该任务所在的会话组ID

+ 有些/proc下的数字文件代表的进程并未出现在它父亲的孩子文件中，故需要扫描整个/proc文件夹将其添加到树中

+ ```c
   void main(){
     fprintf(stderr,"stderr!");
     fprintf(stdout,"stdout!");
     printf("printf!");
   }
   执行上述代码，./a.out可以发现屏幕上出现了相应的语句 stderr!stdout!printf!
   但如果重定向到一个文件中或使用 less 命令，
   则屏幕上显示stderr!，文件中显示后面的
       
   stdout -- 标准输出设备(printf("..")) 同 stdout。
   stderr -- 标准错误输出设备 两者默认向屏幕输出。
   但如果用转向标准输出到磁盘文件，则可看出两者区别。stdout输出到磁盘文件，stderr在屏幕。
   ```

+ 

## L0:amgame

+ char font8x8_basic是根据字符的asicII码来渲染单个字符

+ 贪吃蛇：每次移动时只需计算出新蛇头的位置，插入蛇列表头，根据是否吃到食物来判断是否删除尾部

+ 流程：

  ```c
  init_screen();
  init_snake();
  
  while(1){
      mov=get_key_down();
      snake_update(mov);
      render_screen();
  }
  snake_update(mov){
      switch(mov){
          case 0: mov direct,insert(head)
          case 1:insert(head)
      }
      if(get_food){
          update_food();
      }
      else delete(tail);
  }
  ```

  

+ keycode: w:30, s:44, a:43, d:45, space:70, p:38

+ bug： 要赋值edge1 1时写成了edge0 1，导致边界出错

  有时候屏幕更新不及时，吃了食物后食物不变

  食物会出现在蛇身

## M2_libco













