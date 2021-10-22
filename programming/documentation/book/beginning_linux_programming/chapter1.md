# 入门

## UNIX、Linux和GNU简介

  + Linux已真正成为一个切实可行的操作系统，特别是在服务器市场上。
  
  + Linux的成功归功于在它之前诞生的系统和应用程序--Unix和GNU软件。
  
  + 严格来说，UNIX是由Open Group管理的一个商标，它指的是一种遵循特定规范的计算机操作系统。这个规范也称为单一UNIX规范，它定义了所有必须的UNIX操作系统函数的名称、接口和行为。
  
  + Linux是一个可以自由发布的类UNIX内核实现，它是一个操作系统的底层核心。Linux是Linus Torvalds开发的，期间得到了互联网上广大UNIX程序员的帮助。
  
  + [The Linux Kernel Archives](https://www.kernel.org)
  
  + Linux社区支持自由软件的概念，即软件本身不应受限，它们应遵守GNU通用公开许可证（GPL）。自由软件基金会（Free Software Foundation）由Richard Stallman创立，他是自由软件这一概念的倡导者，并发起了GNU项目，这个项目的宗旨是：试图创建一个与UNIX系统兼容，但并不受UNIX名字和源代码私有权限制的操作系统和开发环境。
  
  + [GNU's Not UNIX](https://www.gnu.org)
  
  + copyright和copyleft
  
  + Linux发行版：[Distro Watch](https://www.distrowatch.com)

  + Linux程序

    - Linux应用程序表现为两种特殊类型的文件：可执行文件和脚本文件。可执行文件是计算机可以直接运行的程序；脚本文件是一组指令的集合，这些指令将由另一个程序（即解释器）来执行。

    - $PATH：如果PATH变量中包含的其中一个目录包含名为name的程序，在shell中输入name就可以执行这个程序。

    - /bin：二进制文件目录，用于存放启动系统时用到的程序。
    
    - /usr/bin：用户二进制文件目录，用于存放用户使用的标准程序。
    
    - /usr/local/bin：本地二进制文件目录，用于存放软件安装的程序。
    
    - /sbin和/usr/sbin：系统管理员登陆后使用PATH变量可能还包含系统管理程序的目录。
    
    - /opt：可选的操作系统组件和第三方应用程序。
    
    - a.out <=> assembler output

    - Meme（梗）：在UNIX的早期历史中，想在系统上玩游戏的人通常把游戏作为a.out来运行，以避免被系统管理员捉到，因此一些UNIX系统每晚会定期地删除所有名为a.out的文件。

  + 开发系统引导
  
    - 应用程序：系统为正常使用提供的程序，包括用于程序开发的工具，都可在目录/usr/bin中找到；系统管理员为某个特定的主机或本地网络添加的程序通常在目录/usr/local/bin或/opt中找到。
    
    - 头文件：用C语言及其他语言进行程序设计时，你需要用头文件来提供对常量的定义和对系统函数及库函数调用的声明。
    
    - 头文件存储位置：对于C语言来说，这些头文件几乎总是位于/usr/include目录及其子目录中。那些依赖特定linux版本的头文件通常可在目录/usr/include/sys和/usr/include/linux中找到。X视窗系统的/usr/include/X11目录和GNU C++的/usr/include/c++目录。
    
    - gcc -I：包含保存在子目录或非标准位置中的头文件。
    
    - grep：ls | grep *.h 或 grep EXIT_ *.h
    
    - 库文件：库是一组预先编译好的函数的集合，这些函数都是按照可重用的原则编写的。它们通常由一组相互关联的函数组成以执行某项常见的任务。
    
    - 库文件存储位置：标准系统库文件一般存储在/lib和/usr/lib目录中。
    
    - 使用非标准库内库文件：仅把库文件放在标准目录中，就希望编译器能够找到它是不够的，库文件必须遵循特定的命名规范并且需要在命令行中明确制定。
    
    - 库文件的命名：名字总是以lib开头，随后的部分指明这是什么库（例如，c代表C语言库，m代表数学库），文件名的最后部分以.开始。.a代表传统的静态函数库，.so代表共享函数库，函数库通常以静态库和共享库两种格式存在。
    
    - gcc -l或直接输入完成路径：告诉编译器要搜索的库文件。
    
      - gcc -o fred fred.c -lm // lm是简写，代表libm.a函数库
      
    - gcc -L：为编译器添加库的搜索路径。
    
      - gcc -o x11fred -L /usr/openwin/lib x11fred.c -lX11
      
    - 静态库：函数库最简单的一组处于“准备好使用”状态的目标文件。当程序需要使用函数库中的某个函数时，它包含一个声明该函数的头文件。编译器和链接器负责将程序代码和函数库结合在一起以组成一个单独的可执行文件。静态库也称为归档文件(archive)，按惯例它们的文件名都以.a结尾。
    
    - 共享库：静态库的一个缺点是，当你同时运行许多应用程序并且它们都使用来自同一个函数库的函数时，内存中就会有同一函数的多份副本，而且在程序文件自身中也有多份同样的副本。这将消耗大量宝贵的内存和磁盘空间。而使用共享库时，程序本身不再包含函数代码，而是引用运行时可访问的共享代码。当编译好的程序被装载到内存中执行时，函数引用被解析并产生对共享库的调用，如果有必要，共享库才被加载到内存中。
    
    - 动态装载器：对Linux系统来说，负责装载共享库并解析客户程序函数引用的程序是ld.so。
    
    - 标准数学库的共享版本是/usr/lib/libm.so。