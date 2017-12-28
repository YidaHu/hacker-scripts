#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 12/28/2017 1:40 PM
# @Author  : Huyd
# @Site    : 
# @File    : pingtest.py
# @Software: PyCharm
# 监测主机是否存活，如果不存活发送邮件到邮箱

import os
import monitoring.network.script.sendMail as s

# 写数据到文件
def write_txt(all_the_text):
    file_object = open('result.txt', 'a', encoding="utf-8")
    file_object.write(all_the_text)
    file_object.close()

def subping():
    f = open("ip_list.txt", "r")  # 读取IP
    lines = f.readlines()
    for line in lines:
        line = line.strip("\n")
        flag = 1
        # 如果存活一直保持监测
        while (flag == 1):
            if "#" in line:
                print("#")
            else:
                res = os.system("ping -n 1 " + line)
                if res == 0:
                    print(line + " 可用...")
                else:
                    print(line + " 不可用...")
                    write_txt(line + " 不可用...")
                    s.sendMail()
                    flag = 0
    f.close()


subping()
