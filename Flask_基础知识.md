---
title: Flask_基础知识
comments: true
date: 2018-06-13 10:21:02
tags: 
- Flask
- Python
categories:
- Flask
password:
summary_img:
---
<!-- more -->


##  Flask 框架（一）

### Flask介绍

	- Flask：短小精悍，内部没有太多组件，但是有非常多的扩展，可定制性强。
	- Django： 重武器，内部有非常多的组件，ORM、form、model form、缓存、session、中间件
	- TOrando：重要的用途异步非堵塞

### Flask快速入门

	- 安装flask
		- pip3 install flask

### 初识Flask

``` python
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)  # 初始化

USER_DATA = {
    1:{"name":"dove", "age":18, "text":"做个俗人，追求爱和自由"},
    2:{"name":"sove", "age":28, "text":"做个俗人，活得像狗，爱与被爱"}
}
@app.route("/", methods=["GET"])  # 使用methods来添加问模式，以字典的形式，如果默认使用get方法
def index():
    """首页"""
    # 使用render_template来导入模板，默认模板放在templates文件夹中，也可修改。
    return render_template("index.html")

# 使用endpoint 可以给url起一个别名，通过url_for反向生成
@app.route("/login", methods=["GET", "POST"])
def login():
    """登陆页面"""
    # 使用request.method 来获取用户请求方式
    # 使用request.query_string 来获取url信息
    print(request.query_string)
    if request.method == "GET":
        # 通过url_for 反向生成 /login 适用于url比较长的情况
        #url = url_for("login")
        return render_template("login.html")
    # 使用request.form 来获取表单信息
    username = request.form.get("name")
    password = request.form.get("psw")
    if username == "dove" and password == "123":
    # 模块redirect可以跳转到任意网页或者路由
        return redirect("/data")
    return render_template("login.html", error = "输入用户名或密码错误！")
@app.route("/data", methods=["GET"])
def data():
    """用户登陆成功显示用户列表，并有查看详情的功能"""
    # ps: 当render_template传入一个字典时，可以用for循环但是，要写成data.items()加括号
    return render_template("data.html", data=USER_DATA)
@app.route("/data/<int:nid>")  # 在路由中<>可以输入参数，也可以筛选类型。
def data_sting(nid):
    data = USER_DATA.get(nid)
    return render_template("data_string.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
```
>  这个初识有点难啊，😂

### 1. 程序的基本结构

#### 1.1 初始化
		- 初始化： 实例化一个Flask对象
		- app = Flask(__name__) 其中__name__ 是传入文件名称
		- 路由和视图函数
			- 其中路由是@app.route("这是路由地址", methods=["GET","POST"]) methods是用户请求方式，有多种请求方式，用列表包含起来。路由是处理url和视图函数之间关系的程序。
			- 视图函数就是:被装饰器装饰的函数。就是这么简单明了，😄
		- 启动服务： 就是
```python
if __name__ == "__main__":
	app.run()
	# 这就是为了防止在当模块调用时，执行两次。
```
+ Flask扩展
- Flask扩展有很多， 可以在官网上查看
- 其实最重要的就是Flask的扩展，这才是他自己的强大之处。
### 1.2 模板
- Flask使用jinja2模板
- 使用render_template来导入模板，默认模板放在templates文件夹中，也可修改。其中可以查看源码，是怎么定义的。
- 在statics文件夹中调用css，js等文件
- 模板的渲染：就在模板中设置变量用来占位置，真实值替换变量，在返回字符串的过程。
- 变量：在模板中使用 {{ 变量名称 }} ,在render_tenpalte("模板.html", 变量名称=真实值） 用这样的方法传入变量。
- 结构控制：在模板中也可使用for循环，if判断，等控制结构，

```html
# html 中的控制结构
info = {
1:{ "name":"haha", "age":23, },
1:{ "name":"llalaj", "age":23, },
1:{ "name":"nana", "age":23, },
{% for k,v in info.itmes() %}
<h1>	{{ k }} </h1>
<h1>	{{ v.name}} </h1>
<h1>	{{ v.get("name"}} </h1>
<h1>	{{ v.["name"]}} </h1>
{% endfor %}
# 这是在html中使用字典，获取字典中的键值对，其中注意的是，获取v的三种方式。
```

- **jinja2模板中的变量控制器**
	- 在jinja2中变量控制器的使用：{{ 变量|safe }} 这表示在渲染模板时，对变量不进行转移
	- safe -- 渲染值不转义(ps: 在不可信任的值不可使用）
	- cpitalize -- 把值的首字母转化成大写，其他字母转换成小写
	- lower -- 把值转化成小写形式
	- upper -- 把值转化成大写形式
	- title -- 把值中每个单词的首字母都转化成大写（注意与cpiltalize的区别）
	- trim -- 把值的首位空格去掉
	- striptags -- 渲染之前把值中所有的HTML标签都删掉
#### 1.2.1 自定义页面错误：自定义颜面
-自定义页面错误是，修改浏览器的错误页面，为了美化。
```python
# 定义404错误页面
@app.errorhandler(404)
def page_not_found():
	return render_template("404.html"),404
# 定义500 错误页面
@app.errorhandler(500)
def page_not_found():
	return render_template("500.html"),404
```
- 这时只需要修改404.HTML，就可以修改浏览器的404错误页面。

#### 1.2.2 模板的继承
- 这个比较重要但是还没会， 😄

#### 1.2.3 链接

- url_for() 这个方法作用就是给url起一个别名，默认视图函数的名称。
- @app.route("/a/b/c/d/e/f", methods=["POST"], endpoint="别名")
- 这就是用法，默认 "别名" 为视图函数名称。



### 1.3 session与Cooke

- session,cooke是记录用户登陆状态的一种机制，但是一个是存储在服务器，一个存储在浏览器中，通过验证这两个值来确定用户信息。
- 为了防止session被篡改，使用加盐的方式来对数据进行加密。
- 设置盐： app.secret_key = " 所加的盐"


### 1.4 Flask的配置文件

#### 1.4.1 三种常用的配置文件引入

+ 直接在主函数中配置
+ 配置文件进行配置
+ 加载配置对象进行配置

##### 1.4.2 直接在主函数中配置文件
- 通过app.config["DEBUG"] = True 进行配置

```python 

from flask import Flask, render_template, redirect
"""
第一种配置方法：
    直接配置
"""
app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "直接配置进行配置session密钥"
@app.route("/", methods=["GET"])
def index():
    print(app.config)
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
```
##### 1.4.3 通过配置文件进行配置
- 通过app.config.from_pyfile("config.py) 进行配置，其中config.py 要和主函数在一个文件夹中，在config.py 中用 **DEBUG=True**的方式来设置值

```python
from flask import Flask, render_template, redirect

"""
第二种配置方式：
    通过配置文件进行配置
    配置文件为： config.py
"""
app = Flask(__name__)
#
app.config.from_pyfile("./config.py")
@app.route("/", methods=["GET"])
def index():
    print(app.config)
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
```
##### 1.4.4 通过引入类进行配置，（常用）
- 通过 form app.Configlist import * 导入模块（这里使用app.Configlist 是因为我的所有文件都在app的文件夹中放置）
- 通过app.config.from_object(Configlist中的类名）之所以有两种调用方式，是因为类名太长，通过字典键值对，来进行映射。
- 通过类进行引入配置，可以减少主函数代码中的改动，利用类的继承，从而进行配置文件调换。

```python
from flask import Flask, render_template
# 要对配置文件进行导入.Ps: 在导入模块时注意模块的路径。
from app.Configlist import *
"""
第二种配置方式：
    通过对象加载配置 （常用的一种方式）
    配置文件为： Configlist.py
"""
app = Flask(__name__)
# 第一种调用方式
#app.config.from_object(ProductionConfig)
# 第二种调用
app.config.from_object(config["Dev"])
@app.route("/", methods=["GET"])
def index():
    print(app.config)
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
```
#### 1.5 __init__方法的使用(FLask中的蓝图）
>  通过__init__方法的学习引出蓝图（Blueprint)

##### 1.5.1

- __init__.py 文件的作用：就是将一个文件夹变成一个python模块，python模块中都有__init__.py文件。
-  这其中包括 导入的几种方式：
	-  1. import 导入 ：直接导入模块，但是防止二次运行，if  __name__  判断，缺点： 每次都要输入类名(可以用 import 类名 as 新类名)，并且导入一个模块中多个类的时候，不是很方便..
	-  2. from 模块 import 类名，  这样就可以直接 类名.方法() 使用 ， 也可以方便的看出哪个方法在那个类中。
	-  3. from 模块 import * ， 调用所用模块中的方法，但是要注意的是全局命名， 如果，与类中的方法命名相同可能报错，或者，出现意想不到的结果。

##### 1.5.2  利用__init__方法 来创建 blueprint 




# 今天最重要的是 **开放封闭**原则。
# 装饰器的functools.wrgs(func)，保存函数的元信息
# 以及如何使用配置来实现开放封闭原则的实现。