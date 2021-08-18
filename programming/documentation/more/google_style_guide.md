# Google开源项目风格指南
每个较大的开源项目都有自己的风格指南：关于如何为该项目编写代码的一系列约定（有时候会比较武断）。当所有的代码均保持一致的风格，在理解大型代码库时更为轻松。

  + [Google Style Guide](https://github.com/google/styleguide)

  + [Google Style Guide -zh](https://github.com/zh-google-styleguide/zh-google-styleguide)

  + [Google C++ 风格指南](#google-c-风格指南)

    - [0.背景](#0背景)

    - [1.头文件](#1头文件)

    - [2.作用域](#2作用域)

## Google C++ 风格指南

***

### 0.背景

***

  + 使代码易于管理的方法之一是加强代码一致性，让任何程序员都可以快速读懂你的代码这点非常重要，保持统一编程风格并遵守约定意味着可以很容易根据“模式匹配”规则来推断各种标识符的含义，创建通用、必需的习惯用语和模式可以使代码更容易理解。在一些情况下可能有充分的理由改变某些编程风格，但我们还是应该遵循一致性原则，尽量不这么做。

  + 本指南的另一观点是C++特性的臃肿。C++是一门包含大量高级特性的庞大语言。某些情况下，我们会限制甚至禁用某些特性，这样做是为了保持代码清爽，避免这些特性可能导致的各种问题。指南中举例了这类特性，并解释为什么这些特性被限制使用。

### 1.头文件

***

  + 正确使用头文件可令代码在可读性、文件大小和性能上大为改观。

  + 头文件应该自给自足，如果.h文件声明了一个模版或内联函数，同时也该在该文件加以定义。

  + #define保护

    - 所有头文件都应该使用#define来防止头文件被多重包含，命名格式为：<PROJECT>_<PATH>_<FILE>_H_

  + 前置声明

    - 尽可能地避免使用前置声明。使用#include包含需要的头文件即可。

    - 尽量避免前置声明那些定义在其他项目中的实体。

    - 函数：总是使用#include

    - 类模板：优先使用#include

  + 内联函数

    - 一个较为合理的经验准则：不要内联超过10行的函数。谨慎对待构造函数和析构函数，构造函数和析构函数往往比其表面看起来更长，因为有隐含的成员、基类构造函数和基类析构函数被调用。

    - 另一个实用的经验准则：内联那些包含循环或switch语句的函数常常是得不偿失（除非在大多数情况下，这些循环或switch函数从不被执行）。

    - 有些函数即使声明为内联的也不一定会被编译器内联。

  + #include的路径及顺序

    - 使用标准的头文件包含顺序可增强可读性，避免隐藏依赖：

      - 相关头文件

      - C库

      - C++库

      - 其他库的.h文件

      - 本项目内.h文件

      - 平台特定（system-specific）代码需要条件编译（conditional includes）

    - 这种优先的顺序排序保证当相关头文件（foo.h）遗漏包含某些必要的库时，相关源文件（foo_test.cc）的构造会立刻中止。

    - 按字母顺序分别对每种类型的头文件进行二次排序是不错的主意。注意较老的代码可不符合这条规则，要在方便的时候改正它们。

```c++
// 举例来说，google-awesome-project/src/foo/internal/fooserver.cc

#include "foo/public/fooserver.h"

#include <sys/types.h>

#include <unistd.h>

#include <hash_map>

#include <vector>

#include "base/basictypes.h"

#include "base/commandlineflags.h"

#include "foo/public/bar.h"
```

### 2.作用域

***

  + 命名空间

    - 鼓励在.cc文件内使用匿名命名空间或static声明。使用具名的命名空间时，其名称可基于项目名或相对路径。禁止使用using指示（using-directive）。禁止使用内联命名空间（inline namespace）.

    - 根据下文将要提到的策略合理使用命名空间：

      - 遵守命名空间命名中的规则

      - 像之前的几个例子中一样，在命名空间的最后注释出命名空间的名字。

      - 用命名空间把文件包含，gflags的声明/定义，以及类的前置声明以外的整个源文件封装起来，以区别于其他命名空间。

      - 不要在命名空间std内声明任何东西，包括标准库的类前置声明。在std命名空间声明实体是未定义行为，会导致如不可移植。声明标准库下的实体，需要包含对应的头文件。

      - 不应该使用using指示引入整个命名空间的标识符号。

      - 不要在头文件中使用命名空间别名，除非显式标记内部命名空间使用。因为任何在头文件中引入命名空间都会成为公开API的一部分。

      - 禁止用内联命名空间

```c++
// .h 文件
namespace mynamespace {

// 所有声明都置于命名空间中
// 注意不要使用缩进
class MyClass {
    public:
    ...
    void Foo();
};

} // namespace mynamespace
```

```c++
// .cc 文件
namespace mynamespace {

// 函数定义都置于命名空间中
void MyClass::Foo() {
    ...
}

} // namespace mynamespace
```

```c++
#include "a.h"

DEFINE_FLAG(bool, someflag, false, "dummy flag");

namespace a {

...code for a...                // 左对齐

} // namespace a
```

```c++
// 禁止 —— 污染命名空间
using namespace foo;
```

```c++
// 在 .cc 中使用别名缩短常用的命名空间
namespace baz = ::foo::bar::baz;
```

```c++
namespace librarian {
namespace impl {  // 仅限内部使用
namespace sidetable = ::pipeline_diagnostics::sidetable;
}  // namespace impl

inline void my_inline_function() {
  // 限制在一个函数中的命名空间别名
  namespace baz = ::foo::bar::baz;
  ...
}
}  // namespace librarian
```

  + 匿名命名空间和静态变量

    - 在.cc文件中定义一个不需要被外部引用的变量时，可以将它们放在匿名命名空间或声明为static。但是不要在.h文件中这么做。

    - 推荐、鼓励在.cc中对于不需要在其他地方引用的标识符使用内部链接性声明，但是不要在.h中使用。

    - 匿名命名空间的声明和具名的格式相同，在最后注释上namespace。

```c++
namespace {
...
}  // namespace
```

  + 非成员函数、静态成员函数和全局函数

    - 使用静态成员函数或命名空间内的非成员函数，尽量不要用裸的全局函数。将一系列函数直接置于命名空间中，不要用类的静态方法模拟出命名空间的效果，类的静态方法应当和类的实体或静态数据紧密相关。

    - 有时，把函数的定义同类的实例脱钩是有益的，甚至是必要的。这样的函数可以被定义成静态成员，或是非成员函数。非成员函数不应依赖于外部变量，应尽量置于某个命名空间内。相比单纯为了封装若干不共享任何静态数据的静态成员函数而创建类，不如使用命名空间。

```c++
// Right
namespace myproject {
namespace foo_bar {
void Function1();
void Function2();
}  // namespace foo_bar
}  // namespace myproject
```

```c++
// Wrong
namespace myproject {
class FooBar {
 public:
  static void Function1();
  static void Function2();
};
}  // namespace myproject
```

  + 局部变量

    - 将函数变量尽可能置于最小作用域内，并在变量声明时进行初始化。

    - 属于if, while和for语句的变量应当在这些语句中正常地声明，这样子这些变量的作用域就被限制在这些语句中了。

    - 有一个例外，如果变量是一个对象，每次进入作用域都要调用其构造函数，每次退出作用域都要调用其析构函数。这会导致效率降低。

  + 静态变量和全局变量

    - 禁止定义静态储存周期非POD变量，禁止使用含有副作用的函数初始化POD全局变量，因为多编译单元中的静态变量执行时的构造和析构顺序是未明确的，这将导致代码的不可移植。
