---
layout: page
title: TensorFlow常用API总结
categories: [工程能力]
tags: [cs]
keywords: 
description: 摘要描述
mathjax: true
---

## tensor

### [创建](<https://www.jianshu.com/p/2061b221cd8f?utm_campaign=maleskine&utm_content=note&utm_medium=seo_notes&utm_source=recommendation>)

使用`tf.Variable`时，如果检测到命名冲突，系统会自己处理，即tf.Variable() 每次都在创建新对象，所以reuse=True 和它并没有什么关系。

使用`tf.get_variable()`时，且reuse=True， 如果已经创建的变量对象，就把那个对象返回，如果没有创建变量对象的话，就创建一个新的，而当reuse=False，系统不会处理冲突，会报错。

### [shape](<https://blog.csdn.net/baidu_15113429/article/details/81063551>)

``` python
x1 = tf.placeholder(tf.int32,shape=[2,2])
print(tf.shape(x1))  # Tensor("Shape:0", shape=(2,), dtype=int32)
print(x1.get_shape())  # (2, 2)
x2 = tf.placeholder(tf.int32)
x3=tf.reshape(x2,[2,2])
print(tf.shape(x2))  # 
x4 = tf.placeholder(tf.int32)
x4.set_shape([2,2])
```

`shape`返回值是一个tensor；`get_shape`返回的是一个tuple，可以通过as_list()的操作转换成list；`reshape`生成一个新的shape，x3跟x2是一个不同的tensor，常用于将不确定shape的tensor转为确定shape的tensor，其准确性由编码员保证；`set_shape`只是设置placeholder的shape。

### 计算



### [拼接](<https://blog.csdn.net/loseinvain/article/details/79638183>)

`tf.concat`相当于numpy中的`np.concatenate`函数，用于将两个张量在某一个维度(axis)合并起来：`ab=tf.concat([a,b],axis=3)`。

`tf.stack`会在新的张量阶上拼接，产生的张量的阶数将会增加，所以与`tf.concat`不同，axis是决定其层叠(stack)张量的维度方向的。

`tf.unstack`与`tf.stack`的操作相反，是将一个高阶数的张量在某个axis上分解为对应个数的低阶张量。

## operation

