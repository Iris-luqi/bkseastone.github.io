---
layout: page
title: makefile基础
categories: [工程能力]
tags: [cs]
keywords: 
description: 摘要描述
mathjax: true
---

# 文件基本格式
``` bash
target:prerequisites
[tab] commands
```
* 若prerequisites中有一个文件比target文件新，则执行commands所定义的命令。
若显式指明target为伪目标，即`.PHONY:target`，则`make`命令将跳过文件检查，
直接执行对应的命令，由此避免了因当前目录下有target文件而不会执行命令的问题。

* 若make未指定目标则缺省执行第一个目标。

* 命令按行解析，每行命令都在单独的进程中执行。

* 在[tab]后commands前添加`@`，可关闭回显，常用于`echo`命令。

>`include filename`命令可将其他文件包含进来，若在该命令行首添加`-`，
表示忽略可能会出现的文件包含错误。

# 变量

* 变量在使用时展开，形式上类似宏替换，如此引用`$(var)`，而引用shell变量时用`$$`。
* 变量定义的四种格式：
    - `var=value`在执行时才扩展
    - `var:=value`在定义时便扩展，直接使用右侧的现值
    - `var?=value`若变量为空则设置该值，否则维持原值
    - `var+=value`将值追加到变量尾部，继承上次的操作符，若未定义过则自动解释为`=`
## 特殊变量

* 内置变量`$(CC)`当前使用的编译器

* `$(MAKE)`当前使用的make工具

## 自动变量

* `$@`当前目标

* `$^`所有先决条件，`$?`比目标更新的所有先决条件。

* `$<`第一个先决条件

## 多行变量
``` bash
define var
	commands
endef
```
*主要用于定义命令包，每行命令都在单独的进程中执行，故展开时有可能导致脚本错误。*

## 静态模式：以%通配
``` bash
objs=main.o library.o
all:$(objs)
	$(cc) -o a $(objs)
$(objs):%.o:%.c
	$(CC) -c $< -o $@
```

# 条件判断

## 基本格式

``` bash
conditional-directive
	commands
else
	commands
endif
```

## 可用的条件判断

* `ifeq(var1,var2)` 两参数是否相等
* `ifneq(var1,var2)` 两参数是否不等
* `ifdef var` 变量是否已定义
* `ifndef var` 变量是否未定义

# 循环

*可使用shell循环*
```bash
objs = file1 file2
rulefor:
	for filename in `echo $(objs)`; \
	do \
		touch $$filename; \
	done
```
*`\`保证了多行命令在同一进程下执行，因命令是在shell下执行的，
故`filename`为shell变量，自然用`$$`引用。*

# 字符串替换函数
*示例*
``` bash
comma := ,
empty := 
space := $(empty) $(empty)
str1 := a b c
str2 := $(subst $(space),$(comma),$(str))
result:
	@echo $(str1)
	@echo $(str2)
	@echo "done"
```
