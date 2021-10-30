# 从Runoob上学习HTML

## HTML简介

  + HTML是用来描述网页的一种语言：

    - HTML指的是超文本标记语言：HyperText Markup Language。

    - HTML不是一种编程语言，而是一种标记语言。

    - 标记语言是一套标记标签（markup tag）。

    - HTML使用标记标签来描述网页。

    - HTML文档包含了HTML标签及文本内容。

    - HTML文档也叫做web页面。

  + HTMl标签

    - HTML标签是由尖括号包围的关键字。

    - HTML标签通常是成对出现的。

    - 标签对中的第一个标签是开始标签，第二个标签是结束标签。

  + HTML元素：开始标签 + 内容 + 结束标签

  + 块级元素和内联元素

    - 块级元素

      - 每个块级元素都从新的一行开始，并且其后的元素也另起一行。

      - 元素的高度、宽高、行高以及顶和底边距都可设置。

      - 元素宽度在不设置的情况下，和父元素的宽度一致。

      - 常见块级元素：div, p, h1...h6, ol, ul, dl, table, form

    - 内联元素

      - 和其他元素都在一行上。

      - 元素的高度、宽度以及顶或底边距不可设置。

      - 元素的宽度就是它包含的文字或图片的宽度，不可改变。

      - 常见内联元素：span, a, br, label, q

  + HTML属性

    - HTML元素可以设置属性。

    - 属性可以在元素中添加附加信息。

    - 属性一般描述于开始标签。

    - 属性总是以名称/值对的形式出现，比如name="value"。

    - 适用于大多数HTML元素的属性：

| Attribute | Description |
| --------- | ----------- |
| class | 为HTML元素定义一个或多个类名（类名从样式文件引入）|
| id | 定义元素的唯一id |
| style | 规定元素的行内样式（inline style） |
| title | 描述了元素的额外信息（作为工具条使用） |

  + HTML颜色

    - resources/html_css_color_value.png

  + HTML字符实体：HTML中的预留字符必须被替换为字符实体。

    - resources/character_entity.png

  + 统一资源定位器（Uniform Resource Locators）

    - URL由字母组成，或互联网协议地址。

    - scheme://host.domain:port/path/filename

      - scheme - 定义互联网服务的类型，最常见的类型是http

      - host - 定义域主机（http的默认主机是www）

      - domain - 定义互联网域名，比如runoob.com

      - port - 定义主机上的端口号（http的默认端口号是80）

      - path - 定义服务器上的路径

      - filename - 定义文档/资源的名称

    - 常见URL Scheme

      - http，超文本传输协议，不加密。

      - https，安全超文本传输协议，加密。

      - ftp，文件传输协议。
  
      - file，您计算机上的文件。

    - URL只能使用ASCII字符集。由于URL常常包含ASCII外的字符集，需要使用“%”其后跟随两位的十六进制数来替换非ASCII字符。

  + HTML标签简写及全称

    - resources/tag.png

## HTML中的各种标签

  + 在head元素中你可以插入脚本（scripts）, 样式文件（CSS），及各种meta信息。可以添加在头部区域的元素标签为title，style，meta，link，script，noscript，base。

  + 链接可以是一个字，一个词，或者一组词，也可以是一幅图像，您可以点击这些内容来跳转到新的文档或者当前文档中的某个部分。

  + 对于文本样式建议使用CSS。

  + CSS (Cascading Style Sheets) 用于渲染HTML元素标签的样式。

    - 内联样式，在HTML元素中使用style属性。

    - 内部样式表，在HTML文档头部head区域使用style元素来包含CSS。

    - 外部引用，使用外部CSS文件。

| Tag | Name |
| --- | ---- |
| 文档 | html |
| head ||
| 头部 | head |
| 标签 | title |
| 基本链接 | base |
| 关联 | link |
| 风格 | style |
| 元数据 | meta |
| 脚本 | script |
| body ||
| 主体 | body |
| 标题 | h1~h6 |
| 段落 | p |
| 链接 | a |
| 图像 | img |
| 换行 | br |
| 定义文档区域 | div |
| 组合文档行内元素 | span |
| table ||
| 定义表格 | table |
| 表格的表头 | th |
| 表格的行 | tr |
| 表格单元 | td |
| list ||
| 定义无序列表 | ul |
| 定义有序列表 | ol |
| 列表的行 | li |
| 定义自定义列表 | dl |
| 自定义列表项 | dt |
| 自定义列表项的定义 | dd |
| form ||
| 定义表单 | form |
| 输入标签 | input |
| frame ||
| 定义框架 | iframe |
| script ||
| 定义脚本 | script |
| 缺失脚本 | noscript |
| style ||
| 粗体 | b |
| 着重 | em |
| 斜体 | i |
| 小号字 | small |
| 加重语气 | strong |
| 下标字 | sub |
| 上标字 | sup |
| 插入字 | ins |
| 删除字 | del |
| eles ||
| 注释 | !-- |
| 水平线 | hr |

```html
<html></html>

<head></head>

<title>文档标题</title>

<base href="http://www.w3school.com.cn/i/" />
<base target="_blank" />

<link rel="stylesheet" type="text/css" href="mystyle.css">

<style type="text/css">
body {
  background-color:yellow
}
p { 
  color:blue
}
</style>

<!-- 字符集 -->
<meta charset="utf-8">
<!-- 每30秒刷新当前页面 -->
<meta http-equiv="refresh" content="30">
<!-- 网页作者 -->
<meta name="author" content="Runoob">
<!-- 描述内容 -->
<meta name="description" content="免费 Web & 编程 教程">
<!-- 为搜索引擎定义关键词 -->
<meta name="keywords" content="HTML, CSS, XML, XHTML, JavaScript">

<script>
document.write("Hello World!")
</script> 

<body></body>

<h1>这是一个标题</h1>
<h2>这是一个标题</h2>
<h3>这是一个标题</h3>
<h4>这是一个标题</h4>
<h5>这是一个标题</h5>
<h6>这是一个标题</h6>

<p>这是一个段落。</p>
<p>这是另外一个段落。</p>

<p>这个<br>段落<br>演示了分行的效果</p>

<a href="https://www.runoob.com">这是一个链接</a>
<a href="https://www.runoob.com/" target="_blank">访问菜鸟教程!</a>

<img loading="lazy" src="/images/logo.png" width="258" height="39" alt="logo" />

<p>这是一个普通的文本- <b>这是一个加粗文本</b>。</p>
<em>强调文本</em><br>
<p>He named his car <i>The lightning</i>, because it was very fast.</p>
<p><small> Copyright 1999-2050 by Refsnes Data.</small></p>
<strong>加粗文本</strong><br>
<p>这个文本包含 <sub>下标</sub>文本。</p>
<p>这个文本包含 <sup>上标</sup> 文本。</p>
<p>My favorite color is <del>blue</del> <ins>red</ins>!</p>

<div style="color:#0000FF">
  <h3>这是一个在 div 元素中的标题。</h3>
  <p>这是一个在 div 元素中的文本。</p>
</div>

<p>我的母亲有 <span style="color:blue;font-weight:bold">蓝色</span> 的眼睛，我的父亲有 <span style="color:darkolivegreen;font-weight:bold">碧绿色</span> 的眼睛。</p>

<!-- 带有边框的表格 -->
<table border="1">
  <tr>
    <th>Header 1</th>
    <th>Header 2</th>
  </tr>
  <tr>
    <td>row 1, cell 1</td>
    <td>row 2, cell 2</td>
  </tr>
  <tr>
    <td>row 2, cell 1</td>
    <td>row 2, cell 2</td>
  </tr>
</table>

<!-- 无序列表 -->
<h4>无序列表:</h4>
<ul>
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ul>

<!-- 有序列表，并规定起始值 -->
<ol start="50">
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ol>

<!-- 自定义列表，更像名词与其注释 -->
<dl>
<dt>Coffee</dt>
<dd>- black hot drink</dd>
<dt>Milk</dt>
<dd>- white cold drink</dd>
</dl>

<!-- 表单 -->
<form>
  First name: <input type="text" name="firstname"><br>
  Last name: <input type="text" name="lastname">
</form>

<!-- 框架 -->
<iframe loading="lazy" src="demo_iframe.html" width="200" height="200"></iframe>

<!-- 这是一个注释 -->

<hr>

<!-- CSS -->
<body style="background-color:yellow;">
<h1 style="font-family:verdana;">一个标题</h1>
<h2 style="text-align:center;">居中对齐的标题</h2>
<p>这是一个段落。</p>
<p style="font-family:arial;color:red;font-size:20px;">一个段落。</p>
<p style="background-color:green;">这是一个段落。</p>
```

## 示例

  + 布局（Layout）

    - src: layout_div.html layout_table.html

  + 表单（Form）

    - src: form_input.html

  + 框架（Frame）

    - src: frame.html
