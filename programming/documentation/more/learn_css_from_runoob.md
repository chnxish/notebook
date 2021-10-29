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

## CSS中的各种属性

  + 背景（background）

| Property | Name |
| -------- | ---- |
| background ||
| 背景颜色 | background-color |
| 背景图像 | background-image |
|  ||
|||
|||
|||
|||
|||

```css
/* background */
background-color: #b0c4de;
background-image: url("paper.gif");
```
