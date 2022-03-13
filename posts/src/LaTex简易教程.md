---
layout: page
title: LaTex简易教程
categories: [工程能力]
tags: [工具]
keywords: 
description: 摘要描述
mathjax: true
---

# 第一章

## 文章结构控制

* 建立整体框架：
```text
\documentclass{article}
 
\begin{document}
\section{第一节}
\label{sec:sec_1}
\section{第二节}
\label{sec:sec_2}
    \subsection{第二节第一子节}
    \label{sec:sec_2_1}
        something...
\end{document}
```

## 公式控制

* 段落内公式：
```text
    something...$X$ somthing...
```

something...$X$ somthing...

* 独立于段落外的公式：
```text
    \[
    \Delta f\approx (\nabla f, \nabla X)
    \]
```

$$
\Delta f\approx (\nabla f, \nabla X)
$$

* 公式对齐控制：
```text
	\begin{align*}
	\frac{\partial{\mathrm{f}}}{\partial{x}} &= \frac{\partial{f}}{\partial{x^T}}, \\
	\nabla_x\mathrm{f} &= \nabla_{x^T}f.
	\end{align*}
```

$$
\begin{align*}
\frac{\partial{\mathrm{f}}}{\partial{x}} &= \frac{\partial{f}}{\partial{x^T}}, \\
\nabla_x\mathrm{f} &= \nabla_{x^T}f.
\end{align*}
$$

## 列表控制
```text
\begin{enumerate}
    \item 第一项
    \item 第二项
\end{enumerate}
```

或者

```text
\begin{itemize}
    \item 第一项
    \item 第二项
\end{itemize}
```

# 后记：实用工具

## LaTex编译环境

使用[sharelatex](http://sharelatex.com/)即可。
当使用中文时，建议用XeLaTex进行build。

## LaTex特殊符号的查询

可使用[Detexify](http://detexify.kirelabs.org/classify.html)工具得到特殊符号的LaTex语法。

## 公式编辑的实时显示

可使用[Markdown-MathJax-editor-online](<https://www.codecogs.com/latex/eqneditor.php>)
工具检查公式语法的正确性。

> [ref1: LaTex 完整教程](http://www.forkosh.com/mathtextutorial.html)
>
> [ref2:常用数学符号的 LaTeX 表示方法](http://mohu.org/info/symbols/symbols.htm)
