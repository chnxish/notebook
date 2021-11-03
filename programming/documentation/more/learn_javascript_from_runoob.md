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

  + 变量

    - 声明却不赋初值的变量，其值为undefined。

    - 在ES6之前，JavaScript只有两种作用域：全局变量和函数内的局部变量。var关键字声明的变量不具备块级作用域，let关键字声明的变量具备块级作用域。

    - const定义的变量并非常量，并非不可变，它定义了一个常量引用一个值。使用const定义的对象或者数组，可以修改对象内的值，但是不能重新赋值新对象。

  + 数据类型

    - 基本类型：字符串（String），数字（Number），布尔（Boolean），空（Null），未定义（Undefined），Symbol。

    - 引用数据类型：对象（Object），数组（Array），函数（Function）。

    - constructor

```javascript
function isArray(myArray) {
  return myArray.constructor.toString().indexOf('Array') > -1;
}
```

  + 输出

```javascript
console.log('new content');
window.alert('new content');
document.write('new content');
document.getElementById('demo').innerHTML = 'new content';
```

  + 数组

```javascript
var cars = Array();
car[0] = 'BMW';

var num = (1, 2, 3);
```

  + 对象

```javascript
var person = {
  firstName : 'John';
  lastName : 'Doe';
  id : 5555;
  fullName : function () {
    return this.firstName + ' ' + this.lastName;
  }
};
// function() { return this.firstName + ' ' + this.lastName; }
console.log(person.fullName);
// John Doe
console.log(person.fullName());
```

 + 函数

```javascript
function myFunc(a, b) {
  return a * b;
}
console.log(myFunc(1, 2));
```

  + 事件

    - 事件可以用于处理表单验证，用户输入，用户行为及浏览器动作：页面加载时触发事件；页面关闭时触发事件；用户点击按钮执行动作；验证用户输入内容的合法性等等。

    - 可以是哦那个多种方法来执行JavaScript事件代码：HTML事件属性可以直接执行JavaScript代码；HTML事件属性可以调用JavaScript函数；为HTML元素指定自己的事件处理程序等等。

    - [HTML DOM 事件](https://runoob.com/jsref/dom-obj-event.html)

```html
<!-- onchange -->
<body>
  <input type="text" id="fname" onchange="myFunction()" />
  <p>当你离开输入框后，函数将被触发，将小写字母转为大写字母。</p>
<script>
  function myFunction() {
    var x = document.getElementById('fname');
    x.value = x.value.toUpperCase();
  }
</script>
</body>

<!-- onclick -->
<body>
  <button onclick="myFunction()">Click Me</button>
  <p id="demo"></p>
<script>
  function myFunction() {
    document.getElementById('demo').innerHTML = 'hello, world';
  }
</script>
</body>

<!-- onmouseover onmouseout -->
<body>
  <img onmouseover="bigImg(this)" onmouseout="normalImg(this)"
   border="0" src="./resources/color_wheel.jpg" 
   alt="Color Wheel" width="32" height="32"
  />
<script>
  function bigImg(x){
    x.style.height="64px";
    x.style.width="64px";
  }
  function normalImg(x){
    x.style.height="32px";
    x.style.width="32px";
  }
</script>
</body>

<!-- onkeydown -->
<body>
  <input type="text" id="fname" onkeydown="myFunction()">
<script>
  function myFunction() {
    var x = document.getElementById('fname');
    console.log(x.value);
  }
</script>
</body>

<!-- onload -->
<body onload="myFunction()">
  <h1>Hello World</h1>
<script>
  function myFunction() {
    console.log('Hello');
  }
</script>
</body>

<!-- onsubmit -->
<body>
  <form name="form1" action="html_from_action.py" onsubmit="greeting()">
    <input type="text" name="fname" />
    <input type="submit" value="Submit" />
  </form>
<script>
  function greeting() {
    alert('Welcome ' + document.forms['form1']['fname'].value + '!');
  }
</script>
</body>
```

  + 字符串

    - [字符串属性和方法](https://runoob.com/jsref/jsref-obj-string.html)

```javascript
var carname = 'volvo xc60';
var character = carname[6];
var sln = carname.length;

var string_carname = String('volvo xc60');
carname == string_carname;  // true
carname === string_carname; // false
```

  + 运算符

    - 支持自增和自减运算符。

    - ==（等于），===（绝对等于，值和类型均相等）。

  + typeof

```javascript
typeof 'John';                // 返回 string
typeof 3.14;                  // 返回 number
typeof false;                 // 返回 boolean
typeof [1,2,3,4];             // 返回 object
typeof {name:'John', age:34}; // 返回 object
```

  + 类型转换

```javascript
/* Number to String */
String(100 + 23);
(123).toString();
/* Boolean to String */
String(false);
true.toString();
/* Date to String */
Date();
/* String to Number */
Number('3.14');
Number('');      // 0
Number('99 88'); // NaN
/* Boolean to Number*/
Number(false);   // 0
```

  + 错误

```javascript
function myFunction() {
  var messgae, x;
  message = document.getElementById('tips');
  message.innerHTML = '';
  x = document.getElementById('input_demo').value;
  try {
    if (x == '') throw '值是空的';
    if (isNaN(x)) throw '值不是一个数字';
    x = Number(x);
    if (x > 10) throw '太大';
    if (x < 5) throw '大小';
  }
  catch (err) {
    message.innerHTML = '错误：' + err;
  }
  finally {
    document.getElementById('input_demo').value = '';
  }
}
```

  + 表单

```html
<!-- 表单验证 -->
<body>
  <form name="myForm" action="demo_form.py" onsubmit="return validateForm();" method="post">
    名字：<input type="text" name="fname">
    <input type="submit" value="Submit">
  </form>
<script>
  function validateForm() {
    var x = document.forms['myForm']['fname'].value;
    if (x == null || x == '') {
      alert('需要输入名字');
      return false;
    }
  }
</script>
</body>
<!-- 表单验证输入的数字 -->
<body>
  <h1>JavaScript 验证输入</h1>
  <p>请输入 1 到 10 之间的数字：</p>
  <input id="numb" />
  <button type="button" onclick="myFunction()" >提交</button>
  <p id="demo"></p>
<script>
  function myFunction() {
    var x, text;
    x = document.getElementById('numb').value;
    if (isNaN(x) || x < 1 || x > 10) {
      text = '输入错误';
    } else {
      text = '输入正确';
    }
    document.getElementById('demo').innerHTML = text;
  }
</script>
<body>

<!-- 表单自动验证 -->
<form action="demo_form.py" method="post">
  <input type="text" name="fname" required="required">
  <input type="submit" value="提交">
</form>

<!-- E-mail验证 -->
<body>
  <form name="myForm" action="demo_form.py" onsubmit="return validateForm();" method="post">
    Email: <input type="text" name="email" />
    <input type="submit" value="提交" />  
  </form>
<script>
  function validateForm() {
    var x = document.forms['myForm']['email'].value;
    var atpos = x.indexOf('@');
    var dotpos = x.lastIndexOf('.');
    if (atpos < 1 || dotpos < atpos + 2 || dotpos + 2 >= x.length) {
      alert("不是一个有效的e-mail地址");
      return false;
    }
  }
</script>
</body>
```

  + 验证API

```html
<!-- checkValidity -->
<body>
  <p>输入数字并点击验证按钮：</p>
  <input id="id1" type="number" min="100" max="300" required /> 
  <button onclick="myFunction()">验证</button>
  <p>如果输入的数字小于 100 或大于 300 ，会提示错误信息。</p>
  <p id="demo"></p>
<script>
  function myFunction() {
    var inpObj = document.getElementById('id1');
    if (inpObj.checkValidity() == false) {
      document.getElementById('demo').innerHTML = inpObj.validationMessage;
    } else {
      document.getElementById("demo").innerHTML = '输入正确';
    }
  }
</script>
</body>

<!-- validity属性 -->
<body>
  <p>输入数字并点击验证按钮:</p>
  <input id="id1" type="number" min="100" max="200" required />
  <button onclick="myFunction()">验证</button>
  <p>如果输入的数字大于 200 ( input 的 max 属性)，会显示错误信息。</p>
  <p>如果输入的数字小于 100 ( input 的 min 属性), 会显示错误信息。</p>
  <p id="demo"></p>
<script>
  function myFunction() {
    var txt = '';
    var inpObj = document.getElementById('id1');
    if (!isNumeric(inpObj.value)) {
      txt = '你输入的不是数字';
    } else if (inpObj.validity.rangeOverflow) {
      txt = '输入的值太大了';
    } else if (inpObj.validity.rangeUnderflow) {
        txt = '输入的值太小了';
    } else {
      txt = '输入正确';
    }
    document.getElementById('demo').innerHTML = txt;
  }
  // 判断输入是否为数字
  function isNumeric(n) {
    return !isNaN(parseFloat(n)) && isFinite(n);
  }
</script>
</body>
```

  + this

    - 在方法中，this表示该方法所属的对象。

```javascript
var person = {
  firstName: 'John',
  lastName : 'Doe',
  id       : 5566,
  fullName : function() {
    return this.firstName + ' ' + this.lastName;
  }
};
```

    - 在函数中，this表示全局对象。

    - 单独使用时，this表示全局对象。

    - 在事件中，this表示事件的元素。

```html
<button onclick="this.style.display='none';">
点我后我就消失了
</button>
```

    - call, apple, bind

```javascript
var name = 'Alex', age = 17;
var obj1 = {
  name: 'Dylan',
  objAge: this.age,
  myFun: function(fm, t) {
    console.log('Name: ' + this.name + '; Age: ' + this.age
      + '; From ' + fm + ' to ' + t + ';');
  }
};
var obj2 = {
  name: 'Harrison',
  age: 19
}

obj1.myFun.call(obj2, 'England', 'China');    // Name: Harrison; Age: 19; From England to China;
obj1.myFun.apply(obj2, ['England', 'China']); // Name: Harrison; Age: 19; From England to China;
obj1.myFun.bind(obj2, 'England', 'China')();  // Name: Harrison; Age: 19; From England to China;
```

  + JSON(JavaScript Object Notation)

    - JSON是一种轻量级的数据交换格式，是独立的语言。通常用于服务端向网页传递数据。

    - JSON语法规则：数据为key/value对；数据由逗号分隔；大括号保存对象；中括号保存数组。

    - JSON和JavaScript对象可以相互转换。

```json
{"sites": [
    {"name": "Runoob", "url": "www.runoob.com"}, 
    {"name": "Google", "url": "www.google.com"},
    {"name": "Taobao", "url": "www.taobao.com"}
]}
```

```javascript
var text = '{ "sites": [' +
  '{ "name": "Runoob" , "url": "www.runoob.com" },' +
  '{ "name": "Google" , "url": "www.google.com" },' +
  '{ "name": "Taobao" , "url": "www.taobao.com" } ]}';
var obj = JSON.parse(text);
console.log(obj.sites[1].name + ' ' + obj.sites[1].url);
var new_text = JSON.stringify(obj);
console.log(new_text);
```

  + void

```html
<a href="javascript:void(0);">Click Me</a>
```

  + 异步

```javascript
/* setTimeout */
setTimeout(function() {
  console.log('Hello, World!');
}, 3000);

/* Promise */
new Promise(function(resolve, reject) {
  var a = 0;
  var b = 1;
  if (b == 0) reject('Divide zero');
  else resolve(a / b);
}).then(function(value) {
  console.log('a / b = ' + value);
}).catch(function(err) {
  console.log(err);
}).finally(function() {
  console.log('End');
});

/* Counter */
function print(delay, message) {
  return new Promise(function (resolve, reject) {
    setTimeout(function () {
      console.log(message);
      resolve();
    }, delay);
  });
}

print(1000, 'first').then(function() {
  return print(4000, 'second');
}).then(function() {
  print(3000, 'third');
});

async function asyncFunc() {
  await print(1000, 'first');
  await print(4000, 'second');
  await print(3000, 'third');
};
asyncFunc();
```
