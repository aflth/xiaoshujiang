---
title: 关于Linux使用socket5代理
tags:
  -  socket代理
categories:
  - Linux
  - Linux配置
photos:
  - https://res.cloudinary.com/aflthblog/image/upload/v1546598715/webimage/penguingun-600x600.jpg
---

<blockquote class="blockquote-center"> 尽管人群拥挤，每个人都是沉默的，孤独的</blockquote>

---

# terminal终端使用socket代理

## 配置

	- 在 .bashrc 或 .zshrc 中加入如下配置

```bash
export https_proxy="socket5://127.0.0.1:1080"
export http_porxy="socket5://127.0.0.1:1080"

```


		- 然后重载配置**source .bashrc**

![Linux](https://res.cloudinary.com/aflthblog/image/upload/v1546598728/webimage/gopher-tux-1.png)