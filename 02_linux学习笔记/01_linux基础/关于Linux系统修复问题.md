---
title: 关于Linux系统修复问题
tags:
  -  Linux问题
categories:
  - Linux
  - Linux基础 
photos:
  - https://res.cloudinary.com/aflthblog/image/upload/v1546598712/webimage/Linux-on-dark-background.jpg
---

<blockquote class="blockquote-center"> 最终我们没有走到一起，尽管你未嫁我未娶</blockquote>

---


# 一、环境变量设置错误

## 1. 现象

	- 无限重启
	- 所有命令无法使用，显示命令找不到

## 解决方案 1

	- 开机时进入命令行模式
	- /usr/bin/sudo vi /etc/profile (由于sudo 模式不能使用，所以必须使用全路径）
	- 在末尾添加

```bash
export PATH=$PATH:/sbin:/usr/bin:/usr/sbin
```
	- 重启或者执行 **soure /etc/profile**


## 解决方案 2 

	- 在命令行输入

```bash
export PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
```

	- 重启

## 问题原因

	- 在配置Java的环境变量时，吧系统环境变量的覆盖，导致系统命令环境变量丢失，但是在/usr/bin下面可以之间输入命令

![拼命改错](https://res.cloudinary.com/aflthblog/image/upload/v1546598736/webimage/linux-1-800x420.jpg)


---



# 二、 独立显卡安装Ubuntu成功，却不能登录


## 1. 现象

	- U盘安装系统（电脑有英伟达独立显卡）安装成功
	- 系统需要重启，重启成功，但.....
	- 对，他就是一直进不去，怎么都进不去


## 解决方案

	- 开机 进入Ubuntu后让你选择进入Ubuntu系统还是高级
	- 这时候按 e 进入 （好像是vi模式）
	- 在屏幕里的待编辑文字中找到＇Splash＇，正常在中下部
	- 在Splash后加入一个空格，再键入＇nomodeset＇
	- 按下Ctrl+X，重启系统，此时可以正常进入系统
	- 进入系统后，打开终端，键入：
```
sudo gedit /boot/grub/grub.cfg
```
	- 随后在打开的文档中，找到所有的＇Splash＇，并在其后加入一个空格，再键入＇nomodeset＇.
	- 保存文档．

## 原因

	 - 就一个 独立显卡问题，具体点，我也不知道.......

