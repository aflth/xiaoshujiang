---
title: 奇思妙想-无人机S形跟踪搜索
tags:
  - 无人机
  - S形跟踪
categories:
  - 奇思妙想
photos:
      -![奇思妙想](https://markdown.xiaoshujiang.com/img/spinner.gif "[[[1545977642424]]]" )
date: 2018-11-21 21:22:31
---

<blockquote class="blockquote-center">优秀的人，不是不合群，而是他们合群的人里面没有你</blockquote>

---


# 一、什么是S形跟踪搜索


## 1. 简绍

- S形跟踪搜索就是利用无人机已车为家，进行定时的S形盘旋
- 已家为X轴，已车辆方向为Y轴
- 利用PX4开源飞控，利用MAVLINK协议，树莓派，地面站进行联合

## 2. 如何通信

- 首先 树莓派 和 PX4 利用 MAVLINK 进行 机载通信， 

    - 树莓派
        - 接收: 飞机此时坐标、磁航向、hone坐标、树莓派生成飞行时间（通过home点后开始计算）
        - 发送: 通过计算发送飞机下一步飞行指令
        
    - 飞机
        - 接收: home坐标
        - 发送: 飞机图传、数传


# 二、 具体实现


## 1. S形跟踪原理

![Diagram](./attachments/1543988255377.drawio.html)

## 2. 大概先这样，等基础充足在去实现。

