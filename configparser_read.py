"""
这个脚本用于读取配置文件CONFIG.ini，并赋值给全局变量env
由于env初始化优先于任何函数，并且跨模块的全局变量，利用额外的.py来赋值是最方便的
使用全局变量的模块，只需import该模块即可
"""

#!/usr/bin/env/python3
# coding: utf-8

import configparser

__Author__ = 'Yuanhao Wu'


hosts = []
exclude_hosts = []
passwords = {}
# 配置文件中包含:，需要特别指定ConfigParser的分隔符是=，不然默认是=和:
cfg = configparser.ConfigParser(delimiters=('='))
cfg.read("CONFIG.ini")
for server in cfg.options('hosts'):
    ip = cfg.get('hosts', server)
    hosts.append(ip)
for server in cfg.options('exclude_hosts'):
    ip = cfg.get('exclude_hosts', server)
    exclude_hosts.append(ip)
for server in cfg.options('passwords'):
    passwords[server] = cfg.get('passwords', server)