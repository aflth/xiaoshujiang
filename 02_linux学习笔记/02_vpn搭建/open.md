---
title: open
tags:
  -  智商税
categories:
  - linxu
photos:
  - /images/图片名称
---

<blockquote class="blockquote-center">优秀的人，不是不合群，而是他们合群的人里面没有你</blockquote>

---

# 1. 使用教程

- https://www.jinbo123.com/7397.html

- 开启服务器端口 1194


- Linux 安装openvpn
	- sudo apt-get install openvpn
	- sudo apt-get install network-manager-openvpn
	- sudo apt-get install network-manager-openvpn-gnome

- 服务器安装vsftpd
- 开启服务
-$ scp root@149.28.233.237:/root/dove.ovpn /home/aflth/ 下载服务器文件到本地

- 从服务器上下载.ovpn文件
	- 一个文件只能连接一个用户
	- 多客户端创建多个用户

- 修改电脑DNS
		-  cd /etc/resolv.conf
		-  将 nameserver 127.0.0.1 修改为
		-  nameserver 8.8.8.8
		-  nameserver 8.8.4.4
		
			- cd /etc/hosts
			- 将127.0.0.1修改为两个
			- 8.8.8.8和8.8.4.4

配置,ok!
