---
title: python装饰器-语法糖
comments: true
date: 2018-06-12 15:57:10
tags: 
- python
- 装饰器
categories: Python
password:
summary_img:
---

<!-- more -->

# 我对装饰器的认识

	装饰器，就是函数套函数，并且是将另一个函数当做参数传入另一个函数中，曾有位大佬称，一个是内裤，一个是冬库，当内裤不能够阻止寒冷，而发明了冬裤。
	
	这就是冬裤的作用，当一个函数写好又需要增加功能时，这是装饰器就发挥了很大的用处。
	
	
## 装饰器一般运用场合

- 权限校验
- 插入日志
- 性能测试
- 事务处理

## 插入日志应用

> 现在我们有一个客户要么写一个应用
> 于是你就埋头苦干,终于写完了,交给了客户。
```python

def A():
    print("这是A应用")
    
def B():
    print("这是B应用")
    
def C():
    print("这是C应用")
    
# 还有好多个这样的程序
```

> 这时你的心情我了解， 于是你又开始写。

``` python
def A():
    print("这是A应用的日志")
    print("这时A应用")
    
def B():
    print("这是B应用的日志")
    print("这时B应用")

def C():
    print("这是C应用的日志")
    print("这时C应用")
# 就这样，你改了差不多9999个代码，
```
> 改了9999个程序，女朋友却不见了，哎。。。

### 找回女盆友

> 我知道我们不能这样该，要不然女朋友也会没得，虽然现在还没有，但是不能有了，应为这个在弄丢了，😄
> 装饰器的作用： 找回女朋友

``` python
def logging(func):
    def wapper():
        func()
        print("这是{}应用的日志".format(func.__name__))
    return wapper
@logging    
def A():
    print("这是A应用")
@logging 
def B():
    print("这是B应用")
@logging   
def C():
    print("这是C应用")
    
```
> 啊，一会会儿就完了，终于可以去撩妹了，有女朋友的此步骤跳过。
> 哈哈 就是这样的， 可以减少代码的复用率
### 总结1

    > 刚才我们用一个小的日志程序简单说明了，语法糖--装饰器，但是由于本人是个纯小白，所以有不到位的希望留言，一起进步。
    > 在装饰器就是函数里面有一个函数，并且传入参数传入的是一个函数，记得在python中函数不带括号可以当作参数。相当于一个变量。
    > 但是要给原函数传入参数怎么办呢，下面我们将一起学习，装饰器不带参数，被装饰函数带参数。
    
##  权限验证应用
> 现在有一个拨号程序，要求用户输入id可以进行拨号并进行判断是否有足够的金钱

```python
def root(func):
    def inner(money, id):
        if money > 0:
            func(money, id)
        else:
            print("你的余额不足，请充值！")
    return inner
@root
def dial(money, id):
    print("给{}拨打电话".format(id))

dial(-3, "5214")

```
> 其中，dial函数带参数
> 执行过程，dial = root(dial)

> 在使用原函数带参数的时候，注意一点就可以了，原函数需要的参数，和 装饰器中的构造函数的参数是一样的
> 就拿上面的例子来说，dial(money, id) 和 inner（money，id）参数是一样的，由于我现在刚学也讲不清楚，所以我只能这么告诉你。
> 为什么：没有因为，怪我讲不清楚，😄。当然还可以用 *args **kwargs 一个是元组，一个是字典

##  装饰器带参数	
``` python
# 装饰器-装饰器带参数

def root(len):
    def inner_1(func):
        def inner(name):
            if len == 2:
                print("装饰器带参数{}".format(name))
                func(name)
        return inner
    return inner_1


@root(2)
def wrapper(name):
    print("this is {}".format(name))

wrapper("dove")
```
> 这时装饰器带参数的例子
> 主要应用场景，不同的日志等级， 不同的权限等级。例如你开始家了一个会员的功能，后来又有了超级会员，那么会员就和超级会员有一定的差距

## 总结
>  在python中的装饰器分为：
	>  不带参数的装饰器
	>  原函数带装饰器
	>  装饰器带参数

> 装饰器作用
	> 减少代码重用
	> 遵循？？原则（就是尽量不要改已经写好的代码）
	> 增加新功能（实际）

## 附件

###	当有多个装饰器的时候

```python
@A
@B
@C
def wrapper():
	pass
	
```
> 这时候安装从底下网上的套路wrapper=(a(b(c(wrapper))))
