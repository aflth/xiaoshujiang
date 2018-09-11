---
title: Linux 
tags: vim
grammar_cjkRuby: true
---

# 介绍

**此文档为linux使用而创建

## 一. vim spacevim

### 1. 使用spacevim

* 使用 url -sLf https://spacevim.org/install.sh | bash 命令安装spacevim
* 安装后配置文件在  ~/.Spacevim.d/init.toml  在其中可以更改配置
* vim主题网站 http://vimcolors.com/ 
* 使用spacevim是 第一步 你要在Noraml 模式下 按下space（空格） 而后 根据英文选择你要的项目
*  

## 二.neovim

* neovim是vim的升级版但他依然是一个vim，与spacevim不同 的是spacevim是一个配置文件

* neovim安装
	* 由于各个版本的不同使用的安装命令也不同，具体访问https://github.com/neovim/neovim/wiki/Installing-Neovim
	* ubuntu和树莓派安装方法：

命令：
```
sudo apt-get install software-properties-common
sudo apt-add-repository ppa:neovim-ppa/stable
sudo apt-get update
sudo apt-get install neovim
```
*使用 **nvim** 调用neovim

### 配置文件

* 配置文件在.config 中创建nvim文件夹，在创建init.vim在init.vim中配置
* 也可使用vim的配置（但是我不会）
* 树莓派具体插件安装配置

```
1.创建文件夹

首先在 ~/.config 创建一个名为nvim的文件件
其次在nvim文件夹中创建autoload
创建命令为 mkdir nvim 与 mkdir autoload
最后在nvim文件夹中创建init.vim文件，此文件为配置文件 使用命令touch init.vim

2. 修改配置文件与拷贝插件

在autovim中放置vim-plug.vim文件，可能官方给的命令不成功，就先拷贝下载，在移动到autovim文件中。git 要会使用，使用sudo cp 要不然权限不够
修改配置文件，打开文件init.vim输入
call plug#begin('~/.config/nvim/autoload') 这其中为刚才保存plug.vim的路径，每个人可能不同

Plug '你要加载的插件‘

call plug#end()

保存文件并退出

3. 安装插件

打开nvim
在浏览模式下（就是刚进去的那个模式，按shift+：  此时在最下面会出现： 在后面输入PlugInstall
就会进入安装界面
安装完，同样按出： q
退出