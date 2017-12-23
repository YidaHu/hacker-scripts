#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/14 8:56
# @Author  : Huyd
# @Site    : 
# @File    : send_message_to_friend.py
# @Software: PyCharm

import itchat

itchat.auto_login(hotReload=True)

# 给谁发信息，先查找到这个朋友,name后填微信备注即可
users = itchat.search_friends(name='一号')
# 获取好友全部信息,返回一个列表,列表内是一个字典
print(users)
# 获取`UserName`,用于发送消息
userName = users[0]['UserName']
for num in range(5):
    itchat.send("hello", toUserName=userName)
