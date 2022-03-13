---
ayout: page
title: 自然语言处理:transformer
categories: [深度学习]
tags: [dl, nlp]
keywords: 
description: 摘要描述
mathjax: true
---

## 背景

Simple RNN：encoder-decoder结构，encoder output作为decoder的initial states的输入，随着decoder长度的增加，encoder output的信息会衰减。

Contextualized RNN：decoder在每个timestep的input上都会加上一个context，以解决decoder逐渐“遗忘”源端序列信息的问题。

Contextualized RNN with soft align (Attention)：为了让每个decoder端的token在解码时用到的context有所侧重，计算当前token与context之间的"相关度"以做一个"attention"操作。

