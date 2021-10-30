# 从Runoob上学习CSS

## CSS简介

  + CSS是用来表现HTML或XML等文件样式的一种语言：

    - CSS指层叠样式表：Cascading Style Sheets。

    - 样式定义如何显示HTML元素。

    - 样式通常存储在样式表中。

    - 把样式添加到HTML 4.0中，是为了解决内容与表现分离的问题。

    - 外部样式表可以极大提高工作效率。

    - 外部样式表通常存储在CSS文件中。

    - 多个样式定义可层叠为一个。

  + CSS规则：选择器 { 属性: 值; 属性: 值; ... }

    - 选择器指需要改变样式的HTML元素。

    - 每条声明由一个属性和一个值组成。

    - 属性（property）指希望设置的样式属性（style attribute）。每个属性有一个值。属性和值被冒号分开。

  + CSS注释：/* 注释内容 */

  + CSS选择器：元素选择器，选择器分组，类选择器，ID选择器，属性选择器，后代选择器，子元素选择器，相邻兄弟选择器。

```html
<style type="text/css">
/* 元素选择器 */
html { color: black; }
h1 { font-family: sans-serif; }
/* 选择器分组 */
h1, h2, h3, h4, h5, h6 {
  color: gray;
  background: white;
  padding: 10px;
  border: 1px solid black;
  font-family: Verdana;
}
/*
类选择器，class
<p class="important"></p>
<h1 class="important"></h1>
*/
.important { color: red; }
h1.important { color: red; }
/* 
多类选择器 
<p class="important warning"></p>
*/
.important.warning { background: silver; }
/* 
ID选择器，id
<p id="intro"></p>
*/
#intro { font-weight: bold; }
/* 
属性选择器
<h2 title="Hello">Hello</h2>
<a href="https://w3school.com.cn">W3School</a>
<a href="https://baidu.com" title="baidu">Baidu</a>
*/
[title] { color: red; }
a[href] { color: blue; }
a[href="https://baidu.com"][title="baidu"] { color: yellow; }
/*
后代选择器
<p>This is a <em>important</em> paragraph.</p>
*/
p em { color: red; }
/*
子元素选择器
<h1>This is <strong>very</strong> <strong>very</strong> important.</h1>
*/
h1 > strong { color: red; }
/*
相邻兄弟选择器：选择紧接在另一个元素后的元素
<h1>This is a heading.</h1>
<p>This is paragraph.</p>
*/
h1 + p { margin-top: 50px; }
</style>
```

  + CSS创建

    - 外部样式表（External Style Sheet）

```html
<head>
<link rel="stylesheet" type="text/css" href="mystyle.css">
</head>
```

    - 内部样式表（Internal Style Sheet）

```html
<head>
<style>
p { margin-left: 20px; }
body { background-image: url("images/back.gif"); }
</style>
</head>
```

    - 内联样式（Inline Style）

```html
<p style="color: sienna; margin-left: 20px"></p>
```

    - 多重样式优先级：内联样式 > 内部样式 > 外部样式 > 浏览器默认样式。

  + CSS中颜色定义

    - 十六进制：#ff00ff

    - RGB：rgb(255, 0, 255)

    - 颜色名称：red

  + 盒子模型（Box Model）

    - ![Box Model](./resources/css_box_model.png)

    - Margin（外边距或边距）：清除边框外的区域，外边框是透明的。

    - Border（边框）：围绕在内边距和内容外的边框。

    - Padding（内边距或填充）：清除内容周围的区域，内边距是透明的。

    - Content（内容）：盒子的内容，显示文本和图像。

## CSS中的各种属性

  + 背景（Background），文本（Text），字体（Font），链接（Link），表格（Table），边框（Border），轮廓（Outline），尺寸（Dimension），显示（Display），定位（Position）

  + ![Web Safe Fonts](./resources/web_safe_fonts.jpg)

| Property | Name |
| -------- | ---- |
| background ||
| 背景颜色 | background-color |
| 背景图像 | background-image |
| 背景重复属性 | background-repeat |
| 背景位置属性 | background-position |
| text ||
| 文本颜色 | color |
| 文本对齐 | text-align |
| 文本修饰 | text-decoration |
| 文本转换 | text-transform |
| 文本缩进 | text-indent |
| font ||
| 设置字体类型 | font-family |
| 字体样式 | font-style |
| 字体大小 | font-size |
| 字体宽度 | font-weight |
| link ||
| 链接文本颜色 ||
| 链接文本修饰 ||
| 链接背景颜色 ||
| list ||
| 列表项标记类型 | list-style-type |
| 列表项标记图像 | list-style-image |
| table ||
| 表格边框 | border |
| 表格边框折叠 | border-collapse |
| 表格宽度和高度 | width height |
| 表格文字水平对齐 | text-align |
| 表格文字垂直对齐 | vertical-align |
| 表格填充 | padding |
| 表格颜色 | background-color |
| box model ||
| 边距 | margin |
| 边框 | border |
| 填充 | padding |
| border ||
| 边框样式 | border-style |
| 边框宽度 | border-width |
| 边框颜色 | border-color |
| 单边框设置 ||
| outline ||
| 轮廓样式 | outline-style |
| 轮廓颜色 | outline-color |
| 轮廓宽度 | outline-width |
| dimension ||
| 元素高度 | height |
| 元素宽度 | width |
| 元素最大高度 | max-height |
| 元素最大宽度 | max-width |
| 元素最小高度 | min-height |
| 元素最小宽度 | min-width |
| display ||
| 显示 | display |
| 可见性 | visibility |
| position |
| 定位 | position |

```css
/* background */
body {
  background-color: #b0c4de;
  background-image: url("paper.jpg");
  background-repeat: repeat;
  background-position: right top;
}
body { background: #ffffff url('img_tree.png') no-repeat right top; }
/* text */
p {
  color: red;
  text-align: justify;
  text-decoration: underline;
  text-transform: uppercase;
  text-indent: 50px;
}
/* font */
p {
  font-family: "Times New Roman", Times, serif;
  font-style: italic;
  font-size: 14px;    /* 1em=16px */
  font-weight: normal;
}
/* link */
a:link { /* 未访问链接 */
  color: #000000;
  text-decoration: none;
  background-color: #b2ff99;
}
a:visited { /* 已访问链接 */
  color: #00ff00;
  text-decoration: none;
  background-color: #ffff85;
}
a:hover { /* 鼠标移动到链接上 */
  color: #ff00ff;
  text-decoration: underline;
  background-color: #ff704d;
}
a:active { /* 鼠标点击时 */
  color: #0000ff;
  text-decoration: underline;
  background-color: #ff704d;
}
/* list */
ol.a {
  list-style-type: upper-roman;
}
ol.b {
  list-style-type: lower-alpha;
}
ul {
  list-style-image: url("sqpurple.gif");
}
/* table */
table {
  border-collapse: collapse;
  width: 100%;
}
table, th, td {
  border: 1px solid black;
}
th {
  height: 50px;
  color: white;
  background-color: green;
}
td {
  text-align: right;
  vertical-align: bottom;
  padding: 15px;
}
/* box model */
div {
  width: 220px;
  padding: 10px;
  border: 5px solid gray;
  margin: 0;
}
/* border */
p {
  border-style: solid;
  border-width: 3px;
  border-color: red;
}
p {
  border-top-style: dotted;
  border-right-style: solid;
  border-bottom-style: dotted;
  border-left-style: solid;
}
p {
  border: 5px solid red;
}
/* outline */
p {
	border: 1px solid blue;
	outline-style: solid;
	outline-color: #ff00ff;
	outline-width: thin;
}
p {
  border: 1px solid red;
  outline: green dotted thick;
}
/* dimension */
p {
  height: 100px;
  width: 100px;
}
/* display */
div {
  display: block;   /* 表现为一个块级元素（一般情况下独占一行） */
  display: inline;  /* 表现为一个内联元素（一般情况下不独占一行） */
  display: none;    /* 元素不可见，并且不为其保留相应的位置 */
}
div {
  visibility: visible; /* 元素可见，默认值 */
  visibility: hidden;  /* 元素不可见，但仍然为其保留相应的空间 */
  visibility: inherit; /* 继承上级元素的visibility的值 */
}
/* position */
p {
  position: static;    /* 元素默认值，即没有定位，遵循正常的文档流对象 */
}
p {
  position: fixed;     /* 元素的位置相对于浏览器窗口是固定位置 */
  top: 30px;
  right: 5px;
}
p {
  position: relative;  /* 相对定位，相对于其正常位置 */
  left: 20px;
}
p {
  position: absolute;  /* 绝对定位，相对于父元素的定位 */
  left: 100px;
  top: 150px;
}
p {
  position: sticky;    /* 粘性定位，依赖用户的滚动，在relative和fixed之间切换 */
  position: -webkit-sticky;
  top: 0;
  background-color: green;
  border: 2px solid #4caf50;
}
img {
  position: absolute;
  left: 0px;
  top: 0px;
  z-index: -1;  /* z轴 */
}
```
