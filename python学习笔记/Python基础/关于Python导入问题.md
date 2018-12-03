---
title: 关于Python导入问题
tags:
  - python导入模块，import
categories:
  - Python
photos:
  - /images/图片名称
date: 2018-11-21 21:22:31
---

<blockquote class="blockquote-center">成果 = 效率 × 时间</blockquote>

---
# 一、 Python中的模块


## python模块简绍


1. 在Python每一个程序都是一个模块，一个庞大的程序都是由很多小模块组成的，这样不但条例清楚而且耦合性小，利于Python程序的维护，和新功能的开发。

2. 使用模块，可以增强程序性能，因为python在导入模块时，就会直接运行，并且编译成二进制文件。


## Python模块用法


1. 在Python中使用 import 或 from import * 来导入模块（缺少他们之间的差别）

2. import 导入模块时的搜索路径为 **sys.path()** [需要先导入模块sys],由于sys.path()是一个列表，那我们就可以定制模块搜索路径，并添加路径。

3. 如果修改模块需要重新导入模块，有两种方法
    - 重新加载程序
    - 导入 **from imp import \*** ，而后使用reload() 方法将模块重新导入

4. 循环导入（重点）
    
    - 我们应该尽量避免这种循环导入，在顶层设计中应该有体现。
    - 我们可以使用一种框架，仅供参考。
    - 

![module](./attachments/1543817547342.drawio.html)








<blockquote class="blockquote-center"> 居中 </blockquote>

{% blockquote 书名, 作者 %}
