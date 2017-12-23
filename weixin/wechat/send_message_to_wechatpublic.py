#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/14 8:58
# @Author  : Huyd
# @Site    : 
# @File    : send_message_to_wechatpublic.py
# @Software: PyCharm

import itchat

itchat.auto_login(hotReload=True)
# 返回完整的公众号列表
mps = itchat.get_mps()
## 获取名字中含有特定字符的公众号，也就是按公众号名称查找,返回值为一个字典的列表
mps = itchat.search_mps(name='')
print(mps)
# 发送方法和上面一样
userName = mps[0]['UserName']

for num in range(5):
    itchat.send("Hello", toUserName=userName)
