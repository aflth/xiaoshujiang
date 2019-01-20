---
title: 关于Python生成器
tags:
  -  生成器
categories:
  - Python
  - Python基础
photos:
  - /images/图片名称
---

<blockquote class="blockquote-center">有人帮助你，是你的幸运；无人帮助你，是公正的命运；没有人该对你做什么，因为生命是你自己的，你得自己负责。</blockquote>

---

# 一、什么是生成器

## 在Python中一边循环一边计算的机制，成为生成器，generator


# 二、 为什么要用生成器

## 我们可以通过列表生成式创建一个列表，但是受到内存的限制，列表容量肯定是有限的。而且创建包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要前面几个元素，那么后面的绝大多数空间都白白浪费，如果列表元素可以通过某种算法推算出来后续的元素，这样就不必创建完整的list，从而节省大量空间。就这样生成器出现了。

# 三、 怎么创建生成器

## 1. 把列表生成式，[ ]  改为 （）

```python
In [2]: l = [x * 2 for x in range(5)]  # 列表生成式

In [3]: G = (x * 2 for x in range(5))  # 生成器

In [4]: l  # 列表生成式的打印结果
Out[4]: [0, 2, 4, 6, 8]

In [5]: G  # 生成器的打印结果
Out[5]: <generator object <genexpr> at 0x7fe7da3bb6d0>

In [6]: next(G)
Out[6]: 0

In [7]: next(G)
Out[7]: 2

In [8]: next(G)
Out[8]: 4

In [9]: next(G)
Out[9]: 6

In [10]: next(G)
Out[10]: 8

In [11]: next(G)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-11-b4d1fcb0baf1> in <module>()
----> 1 next(G)

StopIteration: 

# ---
In [12]:     next(l)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-12-cdc8a39da60d> in <module>()
----> 1 next(l)

TypeError: 'list' object is not an iterator

```

### 区别： 
	- 列表生成式打印为 list ； 生成器打印为 一片内存地址
	- 生成器可以使用**next()**方法，当打印完在次调用next（）方法时会报StopIteration错误； 列表生成式不可以使用next()方法，使用会报TypeError错误。

### 相同：
	- 都是可迭代对象都可以使用for循环


# 四、 生成器函数（generator function）

## 生成器函数是将函数中的return改为yield（这也是一个魔法），这个魔法将函数的状态冻住，等待下一次调用。

```python
In [20]: def test():
    ...:     yield 1
    ...:     yield 2
    ...:     

In [21]: for x in test():
    ...:     print(x)
    ...:     
1
2

In [22]: t = test()  # 这里要注意，现在test（）是一个内存地址



In [24]: next(t)
Out[24]: 1

In [25]: next(t)
Out[25]: 2

In [26]: next(t)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-26-f843efe259be> in <module>()
----> 1 next(t)

StopIteration: 

```


# 五、 总结

## 生成器是这样一个函数，它记住上一次返回时在函数体中的位置，对生成器第二次调用跳转至该函数的中间，而上次调用所有局部变量保持不变。

## 生成器不仅记住他的数据状态，生成器还记住他在流控制构造？

## 特点

	- 节约内存
	- 迭代到下一次调用时， 所有参数都是第一次所有保留下来的，即是说：在整个所有函数调用的函数都是第一次调用保留的，而不是新创的。