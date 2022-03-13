---
layout: page
title: 机器学习:BN/GN
categories: [机器学习]
tags: [ml, dl]
keywords: 
description: 摘要描述
mathjax: true
---

经过 BN 层后，使得输出的均值与方差不再与前面的网络参数有复杂的关联依赖，而只由 BN 层的参数 $\beta , \gamma$ 决定，故前面的网络参数是否学好并不影响后面 BN 层参数 $\beta , \gamma$ 的学习，若前面的网络参数尚未学好，已经学好的 BN 层参数 $\beta , \gamma$ 的存在，会使得最近一层的网络参数更快地朝好的方向发展，进而一步步反传使得所有网络参数达到最优，而不必费心地去考虑网络参数如何初始化最好。

BN 层使得应处于激活函数饱和区的神经元处于饱和区，应处于激活区的神经元处于激活区，即无论网络参数如何，BN 层仍可使得信号进行有效的传播，结合对参数的正则化，学习到的权重便不会过高或过低，从而从根本上解决了因 w 的大小而导致的梯度爆炸或消失问题。

容许较高学习率的原因：

对于通用格式 conv + BN + ReLU 中的 conv 层不加 bias 是因为 BN 已有 bias 功能？：

faster-rcnn 中的 BN 怎么操作的？：

![BN](http://5b0988e595225.cdn.sohucs.com/images/20180324/9b68914ff7da4d14af334668d858a46f.jpeg)

减了对初始化参数的依赖，那么迁移学习的必要性：？

https://docs.google.com/presentation/d/18MiZndRCOxB7g-TcCl2EZOElS5udVaCuxnGznLnmOlE/pub?slide=id.g963e5b4287fb24d_5