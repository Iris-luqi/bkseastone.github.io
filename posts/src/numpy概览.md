---
layout: page
title: numpy概览
categories: [工程能力]
tags: [cs]
keywords: 
description: 摘要描述
mathjax: true
---
## 术语



## numpy数据类型

>[python中的数据类型详解](https://www.cnblogs.com/busui/p/7283137.html?utm_source=itdadao&utm_medium=referral)

numpy中自定义的数据类型需用元组表示：

```python
np.array([[ ( np.array([...]), np.array([...]) )
		]], dtype=[('inputs', 'O'), ('targets', 'O')])
```
用`[[]]`将自定义的数据类型包裹起来的优点是，可用`[0,0]`的索引方式将`object`类型的数据解析出来。

**ref >>** [numpy dtype类详解](http://blog.csdn.net/qq_16234613/article/details/65935279)

