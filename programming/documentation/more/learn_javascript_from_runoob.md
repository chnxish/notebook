# 从Runoob上学习JavaScript

## JavaScript简介

  + JavaScript是脚本语言

    - JavaScript是一种轻量级的编程语言。

    - JavaScript是可插入HTML页面的编程代码。

    - JavaScript插入HTML页面后，可由所有的现代浏览器执行。

  + JavaScript用法

    - 脚本可位于body和head部分中，或者同时存在于两个部分中。脚本会在页面加载时执行。

```html
<script>
function hello() {
  document.getElementById('demo').innerHTML='Hello World';
}
<script>

<script src='my_script.js'></script>
```

## JavaScript语法和函数

  + 输出

```js
console.log('new content');
window.alert('new content');
document.write('new content');
document.getElementById('demo').innerHTML = 'new content';
```

  + 变量

    - 声明却不赋初值的变量，其值为undefined。

    - 在ES6之前，JavaScript只有两种作用域：全局变量和函数内的局部变量。var关键字声明的变量不具备块级作用域，let关键字声明的变量具备块级作用域。

    - const定义的变量并非常量，并非不可变，它定义了一个常量引用一个值。使用const定义的对象或者数组，可以修改对象内的值，但是不能重新赋值新对象。
