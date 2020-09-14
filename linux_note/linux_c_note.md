# linux c 编程笔记

+ 命令行解析：

  ```c
  for(int i=1;i<argc;i++){
      strcmp(argv[i],str1)==0;  //判断第i个参数是不是str1
  }
  ```

  

+ 结构体：

  ```c
  struct proc{
      int a;
      struct node *child;   //proc的child可以是一个链表
  }root={.a=1};
  struct node{
      struct proc *p;
      struct node *next;
  }
  struct *proc p=malloc(sizeof(struct proc));
  ```

  malloc不可以在函数外给常量申请空间



+ ```c
  printf("%s%d%c");  //对应char[],int,char
  sprintf(path,"/proc/%d/s",pid);  //将字符写入path(覆盖)
  
  ```

+ 文件操作

  ```c
  FILE *fp=fopen(path,"r");    //r为只读
  fscanf(fp,"%d,%s,%c",a,b,c);  //将内容读到a,b,c中，当无内容时，返回EOF
  fclose(fp);
  
  DIR *dir=opendir(path);
  struct dirent *entry;
  while((entry=readdir(dir))!=NULL){};  
  closedir(dir);
  ```

+ 判断字符是否全为数字:iota为win中函数

  ```c
  strspn(ch,"0123456789")==strlen(ch);
  size_t strspn(const char *str1, const char *str2);
  //返回str1中第一个不在str2中出现的字符下标，若都出现，则返回str1的长度
  ```

+ 