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