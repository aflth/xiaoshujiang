---
title: 关于无人机电调（ESC）问题
tags:
  -  无人机电调（ESC）
categories:
  - 无人机
  - 无人机基础
photos:
  - https://res.cloudinary.com/aflthblog/image/upload/v1546661437/webimage/ESClogo.png
---

<blockquote class="blockquote-center"> 其实每个人都有自己的不如意，只是有的人站在阳光下哭花了脸，有的人却躲在暗地里开出了花</blockquote>

---


# 一、前提条件（ESC校准）


## 系统必须包含电源管理模块（px4使用测量电压来确定电池是否连接）


# 步骤

	1. 拆螺旋桨
	2. 点开电池用USB（仅限）连接飞行控制器
	3. 打开QGcroundcontrol setting > power > calibrate （校准）
	4. 出现提示电池连接
	5. 校准自动开始
	6. 校准完成后，系统提示断开电池连接


# ESC固件简绍

## ESC固件是每个ESC（电子速度控制器）都运行的软件，他决定了ESC的性能

	- 推荐几个网址，关于ESC的
[BL32位电调设置启动音教程](http://www.5imx.com/portal.php?mod=view&aid=1930)

[BETAFLIGHT 3.4.0 最新固件“兔蛋”调整设置总结](http://www.5imx.com/portal.php?mod=view&aid=1929)


# ESC协议

## ESC协议是飞行控制器与ESC的通用语言，常见的有 PWM



# 如何选择电子速度控制器（ESC）

## 选择额定电流

- ESC发热
	- 更大kv值
	- 更大的螺旋桨叶
	- 更大的电机尺寸

- ESC两个额定电流
	- 持续额定电流：允许ESC安全处理的最大连续电流
	- 瞬间额定电流：允许ESC短时间内通过最大电流（10S）。电机是从ESC中吸取电流，因此一电机为准陪ESC（原因： 不同的桨会使电机吸取不同电流，可能会导致电流过大烧毁电调，选购的时候也不能太大会增加重量和资金，并且在飞行中油门也不会一直处于100%）
	
- 因此购买比较需要够大的ESC
	- 只是重量合资金的增加，但不会发热而减少效率
	- 在ESC上有FET基本可以完成所有的功能并处理所有高电压

- ESC推荐
	- AIKON
	- DYS
	- FPVMODEL

![四合一电调](https://res.cloudinary.com/aflthblog/image/upload/v1546661462/webimage/dys-f20a-4-in-1-esc-700x700.jpg)