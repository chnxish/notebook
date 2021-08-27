# 变量和基本类型

  + [基本内置类型](#基本内置类型)

## 基本内置类型

***

  + C++定义了一套包括算术类型和空类型在内的基本数据类型。

    - ![](./resources/basicDataTypes.png)

| 类型 | 含义 | 最小尺寸 | 介绍 |
| :----: | :----: | :----: | :----: |
| bool | 布尔类型 | 未定义 | 取值为true或false |
| char | 字符 | 8位 | char空间应确保存放机器基本字符集中任意字符对应的数字值 |
| wchar_t | 宽字符| 16位 | wchar_t类型用于确保可以存放机器最大扩展字符集中的任意一个字符 |
| char16_t | Unicode字符 | 16位 | 为Unicode字符集服务 |
| char32_t | Unicode字符 | 32位 | 为Unicode字符集服务 |
| short | 短整型 | 16位 | |
| int | 整型 | 16位 | 一个int至少和一个short一样大 |
| long | 长整型 | 32位 | 一个long至少和一个int一样大 |
| long long | 长整型 | 64位 | 一个long long至少和一个long一样大 |
| float | 单精度浮点数 | 6位有效数字 | 以1个字（32比特）来表示 |
| double | 双精度浮点数 | 10位有效数字 | 以2个字（64比特）来表示 |
| long doulbe | 扩展精度浮点数 | 10位有效数字 | 以3个或4个字（96或128比特）来表示 |

  + 无符号类型和有符号类型

    - int、short、long和long long都是带符号的，通常在这些类型名前添加unsigned就可以得到无符号类型，例如unsigned long。类型unsigned int可以缩写为unsigned。

    - 字符型分为三种：char、signed char和unsigned char。类型char实际上会表现为上述两种形式中的一种，具体是哪种由编译器决定。

  + 类型转换（google style guide不推荐C风格类型转换）

    - 当我们把一个非布尔类型的算术值赋给布尔类型时，初始值为0则结果为false，否则结果为true。

    - 当我们把一个布尔值赋给非布尔类型时，初始值为false则结果为0，初始值为true则结果为1。

    - 当我们把一个浮点数赋给整数类型时，进行了近似处理。结果值将仅保留浮点数中小数点之前的部分。
