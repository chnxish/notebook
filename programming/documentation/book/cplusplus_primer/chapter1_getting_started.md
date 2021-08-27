# 开始

  + [问题](#问题)

## 问题

***

  + 访问main函数返回值的方法依赖于系统

    - UNIX系统下：echo $?

    - Windows系统下：echo %ERRORLEVEL%

  + 换行问题

    - 有符号连接，可以直接换行

    - 字符串连接，推荐符号连接，不能使用反斜杠

    - define宏定义，推荐反斜杠

```c++
#define PRINT_NAME(x) \
    std::cout << "Name: " + x << std::endl;

char USERNAME1[] = "abcdefghijklmn"
                   "opqrstuvwxyz";

std::cout << "Hello, Xish. I'm name is "
          << USERNAME1 << std::endl;

// 不推荐
char USERNAME2[] = "abcdefghijklmn\
                   opqrstuvwxyz";
```

  + 文件重定向

```
add_items <infile >outfile
```

  + 编译

    - 指定g++编译器版本为c++11

      - g++ -std=c++11 -o test test.cc (g++ version is greater than or equal to 4.8)
