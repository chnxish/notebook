# Google开源项目风格指南
每个较大的开源项目都有自己的风格指南：关于如何为该项目编写代码的一系列约定（有时候会比较武断）。当所有的代码均保持一致的风格，在理解大型代码库时更为轻松。

  + [Google Style Guide](https://github.com/google/styleguide)

  + [Google Style Guide -zh](https://github.com/zh-google-styleguide/zh-google-styleguide)

  + [Google C++ 风格指南](#google-c-风格指南)

    - [0.背景](#0背景)

    - [1.头文件](#1头文件)

    - [2.作用域](#2作用域)

    - [3.类](#3类)

    - [4.函数](#4函数)

    - [5.来自Google的奇巧](#5来自google的奇巧)

    - [6.其他C++特性](#6其他c特性)

    - [7.命名约定](#7命名约定)

    - [8.注释](#8注释)

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

    - 有时，平台特定代码需要条件编译，这些代码可以放到其他includes之后。

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

### 3.类

***

  + 构造函数

    - 不要在构造函数中调用虚函数，也不要在无法报错时进行可能失败的初始化。

  + 隐式类型转换

    - 不要定义隐式类型转换，对于转换运算符或但参数构造函数，请使用explicit关键字。

  + 可拷贝类型和可移动类型

    - 如果你的类型需要，就让它们支持拷贝/移动，否则，就把隐式产生的拷贝和移动函数禁止。

  + 结构体和类

    - 仅当只有数据成员时使用struct，其他一概使用class。

  + 继承

    - 使用组合常常比使用继承更合理。

    - 所有继承必须是public的，如果你想使用私有继承，你应该替换成把基类的实例作为成员对象的方式。

    - 必要的话，析构函数声明为virtual。如果你的类有虚函数，则析构函数也应该为虚函数。

    - 对于可能被子类访问的成员函数，不要过度使用protected关键字。注意，数据成员都必须是私有的。

    - 对于重载的虚函数或虚析构函数，使用override、final或virtual的其中之一进行标记。

  + 多重继承

    - 只有一下情况我们才允许使用多重继承：最多只有一个基类是非抽象类；其他基类都是以Interface为后缀的纯接口类。

  + 接口

    - 接口是指满足特定条件的类，这些类以Interface为后缀（不强制）。

    - 当一个类满足一下要求时，称之为纯接口：

      - 只有纯虚函数和静态函数

      - 没有非静态数据成员

      - 没有定义任何构造函数。如果有，也不能带有参数，并且必须是protected。

      - 如果它是一个子类，也只能满足上述条件并以Interface为后缀的类继承。

  + 运算符重载

    - 除少数特定环境外，不要重载运算符，也不要创建用户定义字面量。

  + 存取控制

    - 将所有数据成员声明为private，除非是static const类型成员。出于技术上的原因，在使用<kbd>Google Test</kbd>时我们允许测试固件类中的数据成员为protected。

  + 声明顺序

    - 类定义一般以public:开始，后跟protected:，最后是private:，省略空部分。

    - 在各个部分中，建议将类似的声明放在一起，并且建议以如下的顺序：类型（包括typedef，using和嵌套的结构体与类），常量，工厂函数，构造函数，赋值运算符，析构函数，其他函数，数据成员。

    - 不要将大段的函数定义内联在类定义中，通常，只有那些普通的，或性能关键且短小的函数可以内联在类定义中。

### 4.函数

***

  + 参数顺序

    - 输入参数在先，后跟输出参数（并且一个硬性规定，有时不得不有所变通）。

    - 输入参数通常是值参或const引用，输出参数或输入/输出参数则一般是非const指针。

  + 编写简短函数

    - 我们倾向于编写简短，凝练的函数。

    - 我们承认长函数有时是合理的，因此并不硬性限制函数的长度，如果函数超过40行，可以思索一下能不能在不影响程序结构的前提下对其进行分隔。

    - 即使一个长函数现在工作的非常好，一旦有人对其修改，有可能出现新的问题，甚至导致难以发现的bug。使函数尽量简短，以便于他人阅读和修改代码。

    - 在处理代码时，你可能会发现复杂的长函数。不要害怕修改现有代码：如果证实这些代码使用/调试起来很困难，或者你只需要使用其中的一小段代码，考虑对其分割为更加简短并易于管理的若干函数。

  + 引用参数

    - 在C语言中，如果函数需要修改变量的值，参数必须为指针，如int foo(int *pval)。

    - 在C++中，如果函数需要修改变量的值，可以声明为引用参数，如int foo(int &val)；如果不需要修改变量的值，可以声明为const，如int foo(const int &val)。

    - 特殊情况下，输入参数可以是非const引用参数，比如swap()。有时候，输入参数const T*比const T&更明智。

  + 函数重载

    - 若要使用函数重载，则必须能让读者一看调用点就胸有成竹，而不用花心思猜测调用的重载函数到底是哪一种。这一规则也适用于构造函数。

    - 如果打算重载一个函数，可以试试改在函数名里加上参数信息。例如，用AppendString()和AppendInt()等，而不是一口气重载多个Append()。如果重载函数的目的是为了支持不同数量的同一类型参数，则优先考虑使用std::vector以便使用者可以用列表初始化指定参数。

```c++
class MyClass {
  public:
    void Analyze(const string &text);
    void Analyze(const char *text, size_t textlen);
};
```

  + 缺省参数

    - 只允许在非函数中使用缺省参数，且必须保证缺省参数的值始终一致。

  + 函数返回类型后置语法

### 5.来自Google的奇巧

***

  + 所有权与智能指针

    - 动态分配出的对象最好有单一且固定的所有主，并通过智能指针传递所有权。

    - 所有权是一种登记/管理动态内存和其他资源的技术。动态分配对象的所有主是一个对象或函数，后者负责确保当前者无用时就自动销毁前者。所有权有时可以共享，此时就由最后一个所有主来负责销毁它。甚至也可以不用共享，在代码中直接把所有权传递给其他对象。

    - 如果必须使用动态分配，那么更倾向于所有权保持在分配者手上。如果其他地方要使用这个对象，最好传递它的拷贝，或者传递一个不用改变所有权的指针或引用。倾向于使用std::unique_ptr来明确所有权传递。

    - 如果没有很好的理由，则不要使用共享所有权。这里的理由是可以为了避免开销高昂的拷贝操作，但是只有当性能提升非常明显，并且操作的对象不可变的时候，才能这么做。如果确实要使用共享所有权，建议使用std::shared_ptr。

    - 不要使用std::auto_ptr，使用std::unique_ptr代替它。

  + Cpplint

    - 使用cpplint.py检查风格错误。

### 6.其他C++特性

***

  + 引用参数

    - 所有按引用传递的参数必须加上const。

  + 右值引用

    - 只在定义移动构造函数与移动赋值操作时使用右值引用。不要使用std::forward。

  + 函数重载

    - 若要用好函数重载，最好能让读者一看调用点（call site）就胸有成竹，不用花心思猜测调用的重载函数到底是哪一种。该规则适用于构造函数。

  + 缺省参数

    - 我们不允许使用缺省函数参数，少数极端情况下除外。尽可能改用函数重载。

    - 由于缺点并不是很严重，有些人依旧偏爱缺省参数胜于函数重载。所以除了一下情况，我们要求必须显式提供所有参数。

      - 1.位于.cc文件里的静态函数或匿名空间函数，毕竟都只能在局部文件里调用该函数了。

      - 2.可以在构造函数里用缺省参数，毕竟不可能取得它们的地址。

      - 3.可以用来模拟变长数组。

  + 变长数组和alloca()

    - 我们不允许使用变长数组和alloca()。

    - 改用更安全的分配器（allocator），就像std::vector或std::unique_ptr<T[]>。

  + 友元

    - 我们允许合理的使用友元类及友元函数。

    - 友元扩大了（但没有打破）类的封装边界。某种情况下，相对于将类成员声明为public，使用友元是更好的选择，尤其是如果你只允许另一个类访问该类的私有成员时。当然，大多数类都只应该通过其提供的公有成员进行互操作。

  + 异常

    - 我们不使用C++异常。

    - 译者注：对于异常处理，显然不是短短几句话能够说清楚的，以构造函数为例，很多C++书籍上都提到当构造失败时只有异常可以处理，Google禁止使用异常这一点，仅仅是为了自身的方便，说大了，无非是基于软件管理成本上，实际使用中还是自己决定。

  + 运行时类型识别

    - 我们禁止使用RTTI。

    - RTTI允许程序员在运行时识别C++类对象的类型，它通过使用typeid或者dynamic_cast完成。

    - 如果你的代码需要根据不同的对象类型执行不同的行为的话，请考虑用以下的两种替代方案之一查询类型：

      - 虚函数可以根据子类类型的不同而执行不同代码，这是把工作交给了对象本身去处理。如果这一工作需要在对象之外完成，可以考虑使用双重分发的方案，例如使用访问者设计模式。这就能够在对象之外进行类型判断。

      - 如果程序能够保证给定的基类实例实际上都是某个派生类的实例，那么就可以自由使用dynamic_cast。

  + 类型转换

    - 不要使用C风格类型转换。如int y = (int)x或int y = int(x)等转换方式。

    - 应该使用C++风格：

      - 用static_cast代替C风格的值转换，或某个类指针需要明确的向上转换为父类指针时。

      - 用const_cast去掉const限定符。

      - 用reinterpret_cast指针类型或整型或其他指针之间进行不安全的相互转换。仅在你对所做一切了然于心时使用。

      - 至于dynamic_cast参考<kbd>运行时类型识别</kbd>。

  + 流

    - 不要使用流，除非是日志接口需要。使用printf之类的代替。

    - 使用流还有很多利弊，但代码一致性胜过一切，不要在代码中使用流。

  + 前置自增或自减

    - 不考虑返回值的话，前置自增通常要比后置自增效率更高。因为后置自增需要对表达式的值进行一次拷贝。如果是迭代器或其他非数值类型，拷贝的代价是比较大的。

    - 对简单数值（非对象），两种都无所谓。对迭代器和模版类型，使用前置自增（自减）。

  + const用法

    - 我们强烈建议你在任何可能的情况下都要使用const。此时有时改用C++11推出的constexpr更好。

  + constexpr用法

    - 在C++11里，用constexpr来定义真正的常量，或实现常量初始化。

    - 靠constexpr特性，方才实现了C++在接口上打造真正常量机制的可能。好好用constexpr来定义真常量以及支持常量的函数。

    - 千万别痴心妄想地依靠 constexpr来强制代码<kbd>内联</kbd>。

  + 整型

    - C++内建整型中，仅使用int。如果程序中需要不同大小的变量，可以使用<stdint.h>中长度精确的整型，如int16_t，uint32_t，int64_t。

    - C++没有指定整型的大小，通常人们假设short是16位，int是32位，long是32位，long long是64位。在需要确保整型大小时可以使用<stdint.h>中的类型代替short，unsigned long long等。

    - 在C整型中，只使用int。在合适的情况下，推荐使用标准类型如size_t和ptrdiff_t。

    - 如果整数不会太大，我们常常会使用int。对于大整数，使用int64_t。

    - 小心整型类型转换和整型提升。

    - 使用无符号类型表示非负数，可能会导致bug。

```c++
// 下述循环永远不会推出。有时gcc会发现bug并报错，但大部分情况下都不会。
for (unsigned int i = foo.Length() - 1; i >= 0; --i) ...
```

  + 64位下都可移植性

    - 代码应该对64为和32位系统友好。处理打印，比较，结构体对齐时应切记。

```c++
// printf macros for size_t, in the style of inttypes.h
#ifdef _LP64
#define __PRIS_PREFIX "z"
#else
#define __PRIS_PREFIX
#endif

// Use these macros after a % in a printf format string
// to get correct 32/64 bit behavior, like this:
// size_t size = records.size();
// printf("%"PRIuS"\n", size);
#define PRIdS __PRIS_PREFIX "d"
#define PRIxS __PRIS_PREFIX "x"
#define PRIuS __PRIS_PREFIX "u"
#define PRIXS __PRIS_PREFIX "X"
#define PRIoS __PRIS_PREFIX "o"
```

  + 预处理宏

    - 使用宏时要非常谨慎，尽量以内联函数，枚举和常量代替之。

    - 值得庆幸的是，C++中，宏不像在C中那么必不可少：

      - 宏展开性能关键的代码，现在可以用内联函数代替。

      - 用宏表示常量可被const变量代替。

      - 用宏“缩写”长变量名可被引用代替。

      - 不要使用宏进行条件编译。

    - 下面给出的用法模式可以避免使用宏带来的问题；如果你要宏，尽可能遵守：

      - 不要在.h文件中定义宏。

      - 在马上要使用时才进行#define，使用后要立即#undef。

      - 不要只是对已经存在的宏使用#undef，选择一个不会冲突的名称。

      - 不要视图使用展开后会导致C++构造不稳定的宏，不然也至少要附上文档说明其行为。

      - 不要用##处理函数，类和变量的名字。

  + 0，nullptr和NULL

    - 整数用0，实数用0.0，指针用nullptr(c++11)或NULL(c++03)，字符串用'\0'

  + sizeof

    - 尽可能用sizeof(varname)代替sizeof(type)

  + auto

    - 用auto绕过繁琐的类型名，只要可读性好就继续用，别用在局部变量之外的地方。

  + 列表初始化

    - 在C++03里，聚合类型（aggregate types）就已经可以被列表初始化了，比如数组和不自带构造函数的结构体。

    - 在C++11里，该特性得到进一步的推广，任何对象类型都可以被列表初始化。

```c++
struct Point { int x; int y; };
Point p = {1, 2};
```

```c++
// vector接收了一个初始化列表
vector<string> v{"foo", "bar"};

// 不考虑细节上的微妙差距，大致上相同
// 您可以任选其一
vector<string> v = {"foo", "bar"};

// 可以配合new一起使用
auto p = new vector<string>{"foo", "bar"};

// map接收了一些pair，列表初始化大显神威
map<int, string> m = {{1, "one"}, {2, "2"}};

// 初始化列表也可以用在返回类型上的隐式转换
vector<int> test_function() { return {1, 2, 3}; }

// 初始化列表可迭代
for (int i : {-1, -2, -3}) {}

// 在函数调用里用列表初始化
void TestFunction2(vector<int> v) {}
TestFunction2({1, 2, 3});
```

```c++
class MyType {
  public:
    // std::initializer_list专门接收init列表
    // 得以值传递
    MyType(std::initializer_list<int> init_list) {
      for (int i : init_list) append(i);
    }
    MyType& operator=(std::initializer_list<int> init_list) {
      clear();
      for (int i : init_list) append(i);
    }
};
MyType m{2, 3, 5, 7};
```

```c++
double d{1.23};

// MyOtherType没有std::initializer_list构造函数
// 直接上接收常规类型的构造函数
class MyOtherType {
  public:
    explicit MyOtherType(string):
    MyOtherType(int, string);
};
MyOtherType m = {1, "b"};
// 不过如果构造函数是显式的{explicit}，您就不能用`= {}`了
MyOtherType m{"b"};
```

  + Lambda表达式

    - 适当使用lambda表达式。别用默认的lambda捕获，所有捕获都要显式写出来。

  + 模板编程

    - 不要使用复杂的模板编程。

    - 模板编程有时候能够实现更简洁更易用的接口，但是更多的时候却适得其反。因此模版编程最好只用在少量的基础组件，基础数据结构上，因为模板带来的额外的维护成本会被大量的使用给分担掉。

    - 如果你使用模板编程，你必须考虑尽可能的把复杂度最小化，并且尽量不要让模板对外爆漏。你最好只在实现里面使用模板，然后给用户暴露的接口里面不要使用模板，这样能提高你的接口的可读性，并且你应该在这些使用模板的代码上尽可能详细的注释。

  + Boost库

    - 只使用Boost中被认可的库。Boost代码质量普遍较高，可移植性好，填补了C++标准库的很多空白，如型别的特性，更完善的绑定器，更好的智能指针。某些Boost库提倡的编程实践可读性差，比如元编程和其他高级模板技术，以及过度“函数化”的编程风格。


| Library Name | File Name |
| ------------ | --------- |
| Call Traits | boost/call_traits.hpp |
| Compressed Pair | boost/compressed_pair.hpp |
| The Boost Graph Library | boost/graph |
| Property Map | boost/property_map.hpp |
| Bimap | boost/bimap |
| Statistical Distributions and Functions | boost/math/distributions |
| Multi-index | boost/mylti_index |
| Heap | boost/heap |

  + C++11

    - 适当用C++11（前身是C++0x）的库和语言扩展，在贵项目用C++11特性前三思可移植性。

### 7.命名约定

***

  + 通用命名规则

    - 函数命名，变量命名，文件命名要有描述性；少用缩写。

    - 尽可能使用描述性的命名，别心疼空间，毕竟相比之下让代码易于新读者理解更重要。不要用只有项目开发者能理解的缩写，也不要通过砍掉几个字母来缩写单词。

```c++
int price_count_reader;  // 无缩写
int num_errors;          // "num"是一个常见的写法
int num_dns_connections; // 人人都知道"dns"是什么
```

  + 文件命名

    - 文件名要全部小写，可以包含下划线<kbd>_</kbd>或连字符<kbd>-</kbd>，依照项目的规定，如果没有规定，那么<kbd>_</kbd>更好。

    - C++文件名要以.cc结尾，头文件以.h结尾。专门插入文件的文件则以.inc结尾。

    - 不要使用以及存在于/usr/include下的文件名。

```
my_useful_class.cc
my-useful-class.cc
myusefulclass.cc
myusefulclass_test.cc
```

  + 类型命名

    - 类型名称的每个单词都字母均大写，不包括下划线：MyExcitingClass，MyExcitingEnum。

    - 所有类型命名 -- 类，结构体，类型定义（typedef），枚举，类型模板参数 -- 均使用相同约定。

```c++
// 类和结构体
class UrlTable { ...
class UrlTableTester { ...
struct UrlTableProperties { ...

// 类型定义
typedef hash_map<UrlTableProperties *, string> PropertiesMap;

// using别名
using PropertiesMap = hash_map<URlTableProperties *, string>;

// 枚举
enum UrlTableErrors { ...
```

  + 变量命名

    - 变量（包含函数参数）和数据成员名一律小写，单词之间用下划线连接。类的成员变量以下划线结尾，但结构体的就不用。

```c++
string table_name; // 好 - 用下划线
string tablename;  // 好 - 全小写
string tableName;  // 差 - 混合大小写

class TableInfo {
  ...
  private:
    string table_name_;            // 好
    string tablename_;             // 好
    static Pool<TableInfo>* pool_; // 好
};

struct UrlTablProperties {
  string name;
  int num_entries;
  static Pool<UrlTableProperties>* pool;
};
```

  + 常量命名

    - 声明为constexpr或const的变量，或在程序运行期间始终保持不变，命名时以"k"开头，大小写混合，例如const int kDaysInAWeek = 7;

    - 所有具有静态存储类型的变量（例如静态变量或全局变量）都应当以此方式命名。

  + 函数命名

    - 常规函数使用大小写混合，取值和设值函数则要求变量名匹配：MyExcitingFunction()，MyExcitingMethod()，my_exciting_member_variable()。

```c++
AddTableEntry()
DeleteUrl()
OpenFileOrDie()
```

  + 命名空间命名

    - 命名空间以小写字母命名。最高级命名空间的名字取决于项目名称。要注意避免嵌套命名空间的名字之间和常见的顶级命名空间的名字之间发生冲突。

  + 枚举命名

    - 枚举的命名应当和常量或宏一致：kEnumName或ENUM_NAME。

```c++
enum UrlTableErrors {
  kOK = 0,
  kErrorOutOfMemory,
  kErrorMalformedInput,
};
enum AlternateUrlTableErrors {
  OK = 0,
  OUT_OF_MEMORY = 1,
  MALFORMED_INPUT = 2,
}
```

  + 宏命名

    - 尽量不使用宏，如果你一定要用，如MY_MACRO_THAT_SCARES_SMALL_CHILDREN。

```c++
#define ROUND(x) ...
#define PI_ROUNDED 3.0
```

### 8.注释

***

  + 注释虽然写起来很痛苦，但对保证代码可读性至关重要。下面对规则描述了如何注释以及在哪里注释。当然也要记住：注释固然重要，但最好的代码应当本身就是文档。有意义的类型名和变量名，要远胜过要用注释解释的含糊不清的名字。

  + 注释风格

    - 使用//或/* */，统一就好

  + 文件注释

    - 在每个文件开头加上版权公告。

    - 文件注释描述了该文件的内容。如果一个文件只声明，或实现，或测试了一个对象，并且这个对象已经在它的声明处进行了详细的注释，那么就没有必要再加上文件注释。除此以外的其他文件都需要文件注释。

    - 许可证引用，作者信息，文件内容。

    - 不要在.h和.cc之间复制注释，这样的注释偏离了注释的实际意义。

  + 类注释

    - 每个类的定义都要附带一份注释，描述类的功能和用法，除非它的功能相当明显。

```c++
// Iterates over the contents of a GargantuanTable.
// Example:
//     GargantuanTableIterator* iter = table->NewIterator();
//     for(iter->Seek("foo"); !iter->done(); iter->Next()) {
//         process(iter->key(), iter->value());
//     }
//     delete iter;
class GargantuanTableIterator {
  ...
};
```

  + 函数声明

    - 基本上每个函数声明处前都应当加上注释，描述函数的功能和用途。只有在函数的功能简单而明显才能省略这些注释。

    - 函数声明处注释的内容：

      - 函数的输入输出

      - 对类成员函数而言：函数调用期间对象是否需要保持引用参数，是否会释放这些参数

      - 函数是否分配了必须由调用者释放的空间

      - 参数是否可以为空指针

      - 是否存在函数使用上的性能隐患

      - 如果函数是可重入的，其同步前提是什么？

```c++
// Returns an iterator for this table. It is the client's
// responsibility to delete the iterator when it is done with it,
// and it must not use the iterator once the GargantuanTable object
// on which the iterator was created has been deleted.
//
// The iterator is initially positioned at the beginning of the table.
//
// This method is equivalent to:
//     Iterator* iter = table->NewIterator();
//     iter->Seek("");
//     return iter;
// If you are going to immediately seek to another place in the
// returned iterator, it will be faster to use NewIterator()
// and avoid the extra seek.
Iterator* GetIterator() const;
```

  + 变量注释

    - 通常变量名本身足以很好说明变量用途。某些情况下，也需要额外的注释说明。

```c++
private:
  // Used to bounds-check table accesses. -1 means
  // that we don't yet know how many entries the table has.
  int num_total_entries_;

// The total number of tests cases that we run through in this regression test.
const int kNumTestCases = 6;
```

  + 实现注释

    - 对于代码中巧妙的，晦涩的，有趣的，重要的地方加上注释。

```c++
// Divide result by two, taking into account that x
// contains the carry from the add.
for (int i = 0; i < result->size(); i++) {
  x = (x << 8) + (*result)[i];
  (*result)[i] = x >> 1;
  x &= 1;
}
```

```c++
// If we have enough memory, mmap the data portion too.
mmap_budget = max<int64>(0, mmap_budget - index_->length());
if (mmap_budget >= data_size_ && ! MmapData(mmap_chunk_bytes, mlock))
  return; // Error already logged.
```

```c++
DoSomething();                 // Comment here so the comments line up.
DoSomethingElseThatIsLonger(); // Two spaces between the code and the comment.
{ // One space before comment when opening a new scope is allowed,
  // thus the comment lines up with the following comments and code.
  DoSomethingElse(); // Two Spaces before line Comments normally.
}
std::vector<string> list {
                    // Comments in braced lists describe the next element...
                    "First item",
                    // .. and should be aligned appropriately.
  "Second item"};
DoSomething(); /* For trailing block comments, one space is fine. */
```

  + TODO注释

    - 对那些临时的，短期的解决方案，或已经够好但仍不完美的代码使用TODO注释

```c++
// TODO(kl@gmail.com): Use a "*" here for concatenation operator.
// TODO(Zeke) change this to use relations.
// TODO(bug 12345): remove the "Last visitors" feature
```
