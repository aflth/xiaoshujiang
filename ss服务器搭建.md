---
title: ss服务器搭建
tags: 新建,模板,小书匠
grammar_cjkRuby: true
---


Shadowsocks
Shadowsocks(ss) 是由 Clowwindy 开发的一款软件，其作用本来是加密传输资料。当然，也正因为它加密传输资料的特性，使得 GFW 没法将由它传输的资料和其他普通资料区分开来，也就不能干扰我们访问那些「不存在」的网站了。

安装
我的服务器是Centos7内核如下：

[root@rootrl var]# uname -a
Linux rootrl 3.10.0-514.26.2.el7.x86_64 #1 SMP Tue Jul 4 15:04:05 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux
我这里使用Go版本shadowsocks，其他版本还有Python，nodejs，libev等，刚开始以为用python版本，但是好像很久没更新了
项目地址：https://github.com/shadowsock...

如果没有Go环境，先安装go
去https://golang.org/dl 下载Archive包

# 下载包：
wget https://storage.googleapis.com/golang/go1.9.1.linux-amd64.tar.gz

# 解压到/usr/local/go
tar -C /usr/local -xzf go1.9.1.linux-amd64.tar.gz

# 导入到系统环境变量
export PATH=$PATH:/usr/local/go/bin
安装Shadowsocks，我这里使用一键安装脚本（https://github.com/iMeiji/sha...）

wget --no-check-certificate https://raw.githubusercontent.com/iMeiji/shadowsocks_install/master/shadowsocks-go.sh
chmod +x shadowsocks-go.sh
./shadowsocks-go.sh 2>&1 | tee shadowsocks-go.log
卸载方法：
使用 root 用户登录，运行以下命令：

./shadowsocks-go.sh uninstall
使用命令：

启动：/etc/init.d/shadowsocks start
停止：/etc/init.d/shadowsocks stop
重启：/etc/init.d/shadowsocks restart
状态：/etc/init.d/shadowsocks status
防火墙
检查防火墙是否允许你设定的端口进行通信

iptables -L -n | grep 8989
如果没有信息的话，就是防火墙不允许该端口进行通信。
需设置：

iptables -I INPUT -p tcp --dport 8989 -j ACCEPT
加速
开启TCP Fast Open
vim /etc/rc.local

# 在最后一行增加以下内容
echo 3 > /proc/sys/net/ipv4/tcp_fastopen

# 然后
vim /etc/sysctl.conf

# 在最后一行增加：
net.ipv4.tcp_fastopen = 3

# 编辑配置文件
vim /etc/shadowsocks/config.json
# 添加一项
"fast_open":true

# 最后重启
/etc/init.d/shadowsocks restart
软件加速
加速有锐速加速和Google BBR加速。我这里使用的是BBR加速

我这里参考的：https://teddysun.com/489.html

安装一键脚本

wget --no-check-certificate https://github.com/teddysun/across/raw/master/bbr.sh
chmod +x bbr.sh
./bbr.sh
安装按成后会提示重启，重启完成后：
查看内核：

uname -r
包含4.13就说明内核替换成功

检查是否开启BBR

sysctl net.ipv4.tcp_available_congestion_control
# 返回值一般为：net.ipv4.tcp_available_congestion_control = bbr cubic reno

sysctl net.ipv4.tcp_congestion_control
# 返回值一般为：net.ipv4.tcp_congestion_control = bbr

sysctl net.core.default_qdisc
# 返回值一般为：net.core.default_qdisc = fq

lsmod | grep bbr
# 返回值有tcp_bbr则说明已经启动