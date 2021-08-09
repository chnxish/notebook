# Linux下的C/C++编译器

## Linux下的库

  + libc是Linux下原来的标准C库。
 
  + glibc是GNU C Library，主流的Linux操作系统都使用的是glibc（或者其变种）。
 
    - glibc是Linux系统中最底层的API，几乎其他任何的运行库都要依赖glibc。
  
    - glibc最主要的功能就是对系统调用的封装，glibc可以与上层应用程序和系统调用交互。
  
    - glibc自身也提供了一些上层应用函数必要的功能
  
  + eglibc是glibc的变种，e是Embedded的意思。
 
    - eglibc的主要特性是为了更好的支持嵌入式架构，支持不同的Shell。
  
    - eglibc二进制兼容glibc。
  
    - Ubuntu系统使用的是eglibc。
  
  + glib也是C程序库，和glibc没有什么关系。
 
    - glib将C语言中的数据类型统一封装成自己的数据类型。
  
    - glib提供了C语言常用的数据结构的定义以及处理函数，有趣的宏以及可移植的封装等。
  
  + libstdc++是针对GCC编译器特别重写的C++标准库，libc++是针对Clang编译器特别重写的C++标准库
  
***
 
## GCC、gcc和g++
 
  + GCC:GNU Compiler Collection(GUN 编译器集合)，它可以编译C、C++、JAVA、Fortran、Pascal、Object-C、Ada等语言。gcc是GCC中的GUN C Compiler（C 编译器）。g++是GCC中的GUN C++ Compiler（C++编译器）。

    - gcc和g++并不是编译器，也不是编译器的集合，它们只是一种驱动器。gcc调用了C Compiler，而g++调用了C++ Compiler。
  
    - 用gcc编译一个c文件的话，会有以下几个步骤：

      - Step1：Call a preprocessor, like cpp.

      - Step2：Call an actual compiler, like cc or cc1.

      - Step3：Call an assembler, like as.

      - Step4：Call a linker, like ld
  
    - gcc和g++的主要区别

      - 对于*.c和*.cpp文件，gcc分别当做c和cpp文件编译（c和cpp的语法强度是不一样的）。

      - 对于*.c和*.cpp文件，g++则统一当做cpp文件编译。

      - 使用g++编译文件时，g++会自动链接标准库STL，而gcc不会自动链接STL。

      - gcc在编译C文件时，可使用的预定义宏是比较少的。

    - gcc在编译cpp文件时/g++在编译c文件和cpp文件时（这时候gcc和g++调用的都是cpp文件的编译器），会加入一些额外的宏，这些宏如下：

      - #define __GXX_WEAK__ 1
      - #define __cplusplus 1
      - #define __DEPRECATED 1
      - #define __GNUG__ 4
      - #define __EXCEPTIONS 1
      - #define __private_extern__ extern

    - 在用gcc编译c++文件时，为了能够使用STL，需要加参数–lstdc++，但这并不代表gcc –lstdc++和g++等价，它们的区别不仅仅是这个。

***
