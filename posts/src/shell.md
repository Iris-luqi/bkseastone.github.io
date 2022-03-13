---
layout: page
title: shell
categories: [工程能力]
tags: [cs]
keywords: 
description: 摘要描述
mathjax: true
---

## sed

相对于vim 采用的是交互式文本编辑模式，我们可以用键盘命令来交互性地插入、删除或替换数据中的文本。sed 采用的是流编辑模式，最明显的特点是，在 sed 处理数据之前，需要预先提供一组规则，sed 会按照此规则来编辑数据。

sed 会根据脚本命令来处理文本文件中的数据，这些命令要么从命令行中输入，要么存储在一个文本文件中，此命令执行数据的顺序如下：

1. 每次仅读取一行内容；
2. 根据提供的规则命令匹配并修改数据。注意，sed 默认不会直接修改源文件数据，而是会将数据复制到缓冲区中，修改也仅限于缓冲区中的数据；
3. 将执行结果输出。

当一行数据匹配完成后，它会继续读取下一行数据，并重复这个过程，直到将文件中所有数据处理完毕。

sed [OPTION]... {script-only-if-no-other-script} [input-file]...

OPTION：

- -i，直接修改源文件
- -n，仅显示script处理后的结果

### sed s 替换脚本命令

此命令的基本格式为：

[address]s/pattern/replacement/flags

其中，address 表示指定要操作的具体行，pattern 指的是需要替换的内容，replacement 指的是要替换的新内容。flags标记及功能如下：

| flags 标记 | 功能                                                         |
| :--------- | :----------------------------------------------------------- |
| n          | 1~512 之间的数字，表示指定要替换的字符串出现第几次时才进行替换，例如，一行中有 3 个 A，但用户只想替换第二个 A，这是就用到这个标记； |
| g          | 对数据中所有匹配到的内容进行替换，如果没有 g，则只会在第一次匹配成功时做替换操作。例如，一行数据中有 3 个 A，则只会替换第一个 A； |
| p          | 会打印与替换命令中指定的模式匹配的行。此标记通常与 -n 选项一起使用。 |
| w file     | 将缓冲区中的内容写到指定的 file 文件中；                     |
| &          | 用正则表达式匹配的内容进行替换；                             |
| \n         | 匹配第 n 个子串，该子串之前在 pattern 中用 \(\) 指定。       |
| \          | 转义（转义替换部分包含：&、\ 等）。                          |

例：

``` shell
$ # 指定要替换的字符串出现第几次时才进行替换
$ echo "This is a test of the test script." | sed 's/test/trial/2'
This is a test of the trial script.
$ # 对一行中所有匹配到的内容进行替换
$ echo -e "This is a test of the test script.\nThis is a different line." | sed 's/test/trial/g'
This is a trial of the trial script.
This is a different line.
$ # 只输出被替换命令修改过的行
$ echo -e "This is a test of the test script.\nThis is a different line." | sed -n 's/test/trial/gp'
This is a trial of the trial script.
$ # 对正则表达式匹配到的内容进行前后修饰
$ echo -e "h1Helloh1\nh2Helloh2\nh3Helloh3" | sed '/h[0-9]/{s//\<&\>/1;s//\<&\>/2}'
<h1>Hello<h1>
<h2>Hello<h2>
<h3>Hello<h3>
```

### sed d 替换脚本命令

删除文本中的特定行

例：

```shell
$ # 删除某个区间内的行
$ echo -e "line1\nline2\nline3\nline4\nline5\nline6" | sed '2,4d'
line1
line5
line6
$ # 删除从某行开始到文件末尾的所有的内容
$ echo -e "line1\nline2\nline3\nline4\nline5\nline6" | sed '2,$d'
line1
```

### sed a 和 i 脚本命令

a 命令表示在指定行的后面附加一行，i 命令表示在指定行的前面插入一行。

例：

``` shell
$ # 在指定行的后面附加
$ echo -e "line1\nline2\nline3\nline4" | sed '3a\This is one line of new text.\nThis is another line of new text.'
line1
line2
line3
This is one line of new text.
This is another line of new text.
line4
$ # 在指定行的前面插入一行
$ echo -e "line1\nline2\nline3\nline4" | sed '3i\This is one line of new text.\nThis is another line of new text.'
line1
line2
This is one line of new text.
This is another line of new text.
line3
line4
```

### sed c 替换脚本命令

c 命令表示将指定行中的所有内容，替换成该选项后面的字符串。

``` shell
$ echo -e "line1\nline2\nline3\nline4" | sed '3c\This is a changed line of text.'
line1
line2
This is a changed line of text.
line4
```

### sed y 转换脚本命令

y 转换命令是唯一可以处理单个字符的 sed 脚本命令。`[address]y/inchars/outchars/`转换命令会对 inchars 和 outchars 值进行一对一的映射，即 inchars 中的第一个字符会被转换为 outchars 中的第一个字符，第二个字符会被转换成 outchars 中的第二个字符...这个映射过程会一直持续到处理完指定字符。如果 inchars 和 outchars 的长度不同，则 sed 会产生一条错误消息。

转换命令是一个全局命令，也就是说，它会文本行中找到的所有指定字符自动进行转换，而不会考虑它们出现的位置，我们无法限定只转换在特定地方出现的字符。

例：

``` shell
$ echo "This 1 is a test of 1 try." | sed 'y/123/456/'
This 4 is a test of 4 try
```

### sed p 打印脚本命令

p 命令表示搜索符号条件的行，并输出该行的内容。

``` shell
$ # 打印包含匹配文本模式的行
$ echo -e "line1\nline2\nline3\nline4" | sed -n '/.*3$/p'
line3
$ # 查找包含数字 3 的行，然后执行两条命令。首先，脚本用 p 命令来打印出原始行；然后它用 s 命令替换文本，并用 p 标记打印出替换结果。
$ echo -e "line1\nline2\nline3\nline4" | sed -n '/.*3$/{p;s/line/test/p}'
line3
test3
```

### sed r 脚本命令

r 命令用于将一个独立文件的数据插入到当前数据流的指定位置，`[address]r filename`会将 filename 文件中的内容插入到 address 指定行的后面。

### sed 脚本命令的寻址方式

默认情况下，sed 命令会作用于文本数据的所有行。如果只想将命令作用于特定行或某些行，则必须写明 address 部分，表示的方法有以下 2 种：

1. 以数字形式指定行区间；如`echo -e "line1\nline2\nline3\nline4\nline5\nline6" | sed '2,4d'`。
2. 用文本模式指定具体行区间；如`echo -e "h1Helloh1\nh2Helloh2\nh3Helloh3" | sed '/h[0-9]/{s//\<&\>/1;s//\<&\>/2}'`。



## awk



## curl

[curl](<http://www.codebelief.com/article/2017/05/linux-command-line-curl-usage/>)

不加任何选项使用 curl 时，默认会发送 GET 请求来获取链接内容到标准输出，使用 -d 则默认为发送 POST 请求，-X 可显示地指定发送数据的方式。其他选项如下：

1. -l 只显示 HTTP 头，而不显示文件内容（若要同时显示 HTTP 头和文件内容，使用 -i 选项）;
2. -A 使用自定义 User-Agent 来对网页进行请求；
3. -d 用于指定发送的数据，可用程序内嵌数据-d “somedata”，也可从文件中读取-d “@data.txt”，

## requests

[requests](<https://www.jianshu.com/p/d78982126318>)

`requests.request(method,url,**kwargs)`：

`method`：新建Request对象要使用的HTTP方法，包括：GET，POST，PUT，DELETE等
`url`：新建Request对象的URL链接
`**kwargs`：13个控制访问的可选参数

* params：字典或字节序列，作为参数增加到url中
* data：字典、字节序列、文件，作为Request对象body的内容
* json：JSON格式的数据，作为Request对象body的内容
* headers：字典格式，HTTP请求头，作为Request对象Header的内容
* cookies：字典或CookieJar，Request中的cookie
* files：字典，形式为{filename: fileobject}，用于多文件上传
* auth：Auth 句柄或 (user, pass) 元组
* timeout：等待服务器数据的超时限制，是一个浮点数，或是一个(connect timeout, read timeout) 元组
* allow_redirects：True/False，默认为Ture，重定向开关,为True时表示允许POST/PUT/DELETE方法重定向
* proxies：字典类型，用于将协议映射为代理的URL
* verify：True/False，默认为True，认证SSL证书开关；为True时会验证SSL证书，也可以使用cert参数提供一个CA_BUNDLE路径；为False时，忽略SSL验证
* stream：True/False，默认为True，获取body立即下载开关，为False会立即下载响应头和响应体；为True时会先下载响应头，当Reponse调用content方法时才下载响应体
* cert：为字符串时应是 SSL 客户端证书文件的路径(.pem格式，文件路径包含密钥和证书)，如果是元组，就应该是一个(‘cert’, ‘key’) 二元值对

## shell 中的括号

### ${var}

限定变量名称范围

``` bash
#!/bin/sh
# test.sh
var=test
echo ${var}12
```

效果如下

``` bash
$ ./test.sh
$ var12
```

### $(cmd)

命令替换

``` bash
#!/bin/sh
# test.sh
echo $(ls)
```

运行效果与 `ls` 相同

### {}或()

一串命令的执行

``` bash
$ { echo 1;echo "A";} > tmp
$ cat ./tmp
$ 1
$ A
```

### \${var:-string},\${var:+string},\${var:=string},\${var:?string}

几种特殊的替换结构

#### ${var:-string}
若`var`为空，则结果为`"string"`，否则结果为`$var`。

#### ${var:=string}
若`var`为空，则结果为`"string"`，并将该字符串赋给`var`，否则结果为`$var`。

#### ${var:+string}
若`var`不为空，则结果为`"string"`，否则结果为`$var`。

#### ${var:?string}
若`var`不为空，则结果为`$var`，否则将`"string"`输出到标准错误中，并从脚本退出。

### $((exp))

POSIX标准的扩展计算，只要符合C的运算符都可用在$((exp))，甚至是三目运算符。

### \${var%pattern},\${var%%pattern},\${var#pattern},\${var##pattern}

四种模式匹配替换结构

### []或[[]]

类似test

### ()

在子shell中运行

### {}

{1..30} 就是1-30，或者是/{,s}bin/表示/bin/和/sbin/，ab{c,d,e}表示abc、abd、abe

>[reference](http://www.jb51.net/article/60326.htm)
