---
layout: page
title: python:基础
categories: [工程能力]
tags: [cs]
keywords: 
description: 摘要描述
mathjax: true
---

## 引入

python 是一种 dynamically-typed language，以牺牲类型安全性（在 compile time 无法做类型检查，只有在 run time 才能去确定对象的类型）为代价，换来了编码上的灵活性（可以不用声明直接用——[duck typing](https://en.wikipedia.org/wiki/Duck_typing) ）

### 名字空间

当一行代码要使用变量 `x` 的值时，Python会到所有可用的名字空间去查找变量，按照如下顺序：

1. 局部名字空间 - 特指当前函数或类的方法。如果函数定义了一个局部变量 `x`，Python将使用这个变量，然后停止搜索。
2. 全局名字空间 - 特指当前的模块。如果模块定义了一个名为 `x` 的变量，函数或类，Python将使用这个变量然后停止搜索。
3. 内置名字空间 - 对每个模块都是全局的。作为最后的尝试，Python将假设 `x` 是内置函数或变量。

Python使用名字空间来记录变量的轨迹。名字空间是一个 字典，它的键就是变量名，字典的值就是那些变量的值。局部名字空间可以通过内置的 `locals()` 函数来访问。全局（模块级别，包括内置名字空间）名字空间可以通过 `globals()` 函数来访问。

### 模块

1. [python中模块的`__all__`](https://www.cnblogs.com/wxlog/p/10566628.html)：`__all__`为一元组，每一个元素为一字符串，为该模块中的变量、方法、类，当模块为一单一py文件时可定义于模块内部，当模块为一文件夹时，可定义于*\__init__.py*文件中。

   * 其功能类似于c中的头文件，起显示声明权限作用，具体为被导入模块若定义了`__all__`属性，则只有`__all__`内指定的属性、方法、类可被导入，若没定义，则导入模块内的所有公有属性，方法和类。
* 有隐式声明权限的默认方式，以单下划线开头为protected，以双下划线开头为private，`from pak import * `的方法无法导入，但当`import pak`时，仍可使用`pak._func`和`pak.__func`直接访问。

2. 


## 粘合剂

### linux bash cmd

```python
cmdline = "echo test, test, test, OK!"
print(os.popen(cmdline).read())
```

### c++

