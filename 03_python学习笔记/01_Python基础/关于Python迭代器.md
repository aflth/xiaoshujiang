---
title: 关于Python迭代器
tags:
  -  迭代器
categories:
  - Python
  - Python基础
photos:
  - https://res.cloudinary.com/aflthblog/image/upload/v1542423191/Wallions283060.jpg
---

<blockquote class="blockquote-center">优秀的人，不是不合群，而是他们合群的人里面没有你</blockquote>

---


# 一、迭代器

## 迭代是访问集合元素的一种方式

## 迭代器是一个可以记住遍历位置的对象

## 迭代器对象从集合的的第一个元素开始访问，直到所有元素被访问结束，迭代器只能往前不能后退


# 二、 可迭代对象

## 1.  可迭代对象：可以直接使用for循环的对象成为可迭代对象，Iterable

	- 一类是： list 、 tuple 、 str 、 dict 、 set
	- 一类是： generator，包含生成器带yield， generator function（生成器函数）（yield就是把函数状态冻住，所以可以使用for循环，也可以使用next()方法）


## 2. 判断是否可以迭代（判断可迭代对象）

### 可以使用isinstance()判断对象是否为可迭代对象Iterable

```python 
In [28]: from collections import Iterable

In [29]: isinstance ([], Iterable)
Out[29]: True

In [31]: isinstance({}, Iterable)
Out[31]: True
In [32]: isinstance(123, Iterable)
Out[32]: False
```
### 返回Turn为可迭代对象Iterable，返回False未不可迭代对象

# 三、 迭代器

## 可以被next()函数调用并不断返回下一个值的对象，称为迭代器，Iterator

## 使用isinstance()判断是否为迭代器对象Iterator
```python
In [34]: from collections import Iterator

In [35]: isinstance({}, Iterator)
Out[35]: False


In [37]: l = (x for x in range(3))

In [38]: isinstance(l, Iterator)
Out[38]: True

In [39]: isinstance((x*2 for x in range(3)), Iterator)
Out[39]: True

# --- 生成器函数generator function

In [40]: def test():
    ...:     yield 1
    ...:     yield 2
    ...:     

In [41]: a = test()

In [42]: isinstance(a, Iterator)
Out[42]: True

```

# 四、 iter() 函数

## 生成器都是Iterator（迭代器）对象， 但是list、dict、 str是可迭代对象Iterable

## 把list 、 str、 dict等Iterable变成Iterator，可以使用iter() 函数

```python

In [50]: from collections import Iterable, Iterator
# ---
In [51]: a = "genernter"

In [52]: isinstance(a, Iterable)
Out[52]: True

In [53]: isinstance(a, Iterator)
Out[53]: False
# ---
In [57]: a = iter(a)

In [58]: isinstance(a, Iterable)
Out[58]: True

In [59]: isinstance(a, Iterator)
Out[59]: True

```

# 五、 总结

## 凡是可以用for循环的都是可迭代对象Iterable

## 凡是可以用next()方法的都是迭代器对象Iterator

## 集合数据类型 list、 dict 、 str都可以用Iter() 函数转化为迭代器Iterator，但同样也是可迭代对象
