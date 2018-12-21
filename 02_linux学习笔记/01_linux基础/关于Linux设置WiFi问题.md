---
title: 关于Linux设置WiFi问题
tags:
  -  树莓派密码
  -  Linux自动连接WiFi
  -  ssh连接权限
  -  ssh连接端口设置
categories:
  - Linux
photos:
  - /images/图片名称
---

<blockquote class="blockquote-center">贫穷并不可怕，可怕的是缺少自强自立的精神</blockquote>

---


# 一、树莓派密码及初始账户

## 1.初始账户
- pi


## 2.初始密码
- raspberry


# 二、Linux设置自动连接WiFi

## 1.要求
- sudo权限
- vim

## 2.操作

```bash
pi@raspberrypi:~ $ cd /etc/ssh/
pi@raspberrypi:/etc/ssh $ sudo nvim sshd_config

# 将以下内容注释删除
Port 22 --(可以修改其他端口号)
addressFamily any
ListenAddress 0.0.0.0
ListenAddress ::
# 以上是开启22 端口和修改端口


PermitRootLogin prohibit-password
StrictModes yes
MaxAuthTries 6
MaxSessions 10
# 以上是同意用root权限远程登录

# 保存修改并退出

```

# 三、Linux（树莓派）WiFi自动连接

## 1. 修改文件同样的要求（如二）

## 2. 操作

```bash

pi@raspberrypi:/etc/wpa_supplicant $ ls
action_wpa.sh  functions.sh  ifupdown.sh  wpa_supplicant.conf

# 使用vim修改 wpa_supplicant.conf

# 打开后可以看到network这个字典（Python中）

同样复制以前连接过得修改WiFi名和密码即可

这样也可以看到以前连接WiFi的密码了

```
