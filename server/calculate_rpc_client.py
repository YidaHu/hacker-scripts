#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/14 15:09
# @Author  : Huyida
# @Site    : 
# @File    : calculate_rpc_client.py
# @Software: PyCharm
# @Description:

import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')

print(s.system.listMethods())

print(s.pow(2,3))  # Returns 28
print(s.add(2,3))  # Returns 5
print(s.div(3,2))  # Returns 1
print(s.multiply(4,5)) # Returns 20