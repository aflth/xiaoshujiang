---
title: 关于Python书写规范的笔记
tags:
  - Python书写规范
categories:
  - Python
photos:
  - /images/图片名称
date: 2018-11-21 21:22:31
---

<blockquote class="blockquote-center">聪明的人嘴藏在心里,愚蠢的人心摆在嘴里</blockquote>


---
# 一、关于Python书写规范的简介

    关于Python书写规范可参考[PEP8](https://www.python.org/dev/peps/pep-0008/),这是Python作者Guido维护的。
    主要概述了Python中的一些标准库的书写规范，以及要注意地方。
    其次，这只是一个规范，并不是强制的，不要因为该文档而破坏向后兼容性。
    

# 二、为什么要有书写规范

* 因为在日常中，读代码的频率要高于写代码的，所以有了书写规范就会更有利于读代码

* 有了书写规范可以让自己的代码更有利于维护和团队开发，也不至于在很久以后在看自己的代码不知道代码的思路


# 三、Python代码规范（含个人喜好）


## (一)代码布局


### 1. 缩进

* 使用4格空格（这是要注意尽量不要使用TAB键，因为在不同的书写环境，会导致错误,python不支持制表符和空格混合使用）

* 当实例化类或函数参数过多时
``` python
# 关于参数过多问题
class Tab(num1, num2, 
          num3, num4,
          num5):
    pass

if (a == b and
    a != 1 or b == 1):
    pass
```

* 关于字符串太多的问题
```python
number_list = [
    1, 2, 3, 
    4, 5, 6
]
```

* 每行最大长度
每行最大长度为79个字符，如果太长可以使用 \ 来进行换行

### 2. 二元运算规范

``` python
num = (num1
    + num2
    - num3
    + num4
    + (num4 - num3))
```

### 3. 空格的使用
* 使用两个空格来分离顶级函数和类
* 类中方法由一个空格来分离
* 在函数中使用空白行来小心的指示逻辑部分

### 4. 在导入模块中

* 在导入模块中分别导入模块
* 并且安装从字符短的到字符长的，从标准库的书序到私有库的顺序

### 5. 何时末尾使用逗号

* 这个不是必需的，但是最好在元素后面加一个， 逗号，因为在以后加入元素时不会因为没有这个逗号而报错

### 6. 命名规则

* 尽量简绍大写字母O，小写字母l和大写字母I用做单个字符变量名
* 在某些字体中1和l；0和O 不太分的清楚

### 7. 包和模块的命名

* 包和模块的命名应当简短，这样能提高可读性

### 8. 类名和函数名的规定

* 类名应当全大写，而函数名则用小写并用下划线分割，提高可读性
* 类中参数应当使用下划线_ 来提示该参数的作用，函数参数似

### 9. 文档字符串规范

```python
def complex(real=0.0, imag=0.0):
    """Form a complex number.

    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)
    """
    if imag == 0.0 and real == 0.0:
        return complex_zero
```
* 函数和类与之相似






















<blockquote class="blockquote-center"> 居中 </blockquote>

{% blockquote 书名, 作者 %}
引用书上
{% endblockquote %}

{% codeblock  %}
代码
{% endcodeblock %}

