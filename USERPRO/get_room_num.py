#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/14 22:34
# @Author  : Huyd
# @Site    : 
# @File    : get_room_num.py
# @Software: PyCharm

import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

import re
import schedule
import time


def post_request(url, params):
    import requests
    import json

    headers = {
        'cache-control': "no-cache",
        'postman-token': "98217169-d5f1-930e-6e1c-d7951495f3fb"
    }
    response = requests.request("POST", url, headers=headers, params=params)
    json_data = json.loads(str(response.text))
    result = json_data['prompWord']
    return result


def job(list):
    url = "http://ent.sipmch.com.cn:8000/ModuleDefaultCompany/RentManage/SearchRentNo"
    params = {"CertNo": "321322199201154032"}  # 参数
    result = post_request(url, params)  # 结果抓取
    result = re.sub(r'</?\w+[^>]*>', '', result)  # 过滤html标签
    result = re.findall(r"\d+\.?\d*", result)
    list.append(result[0])
    with open("data.txt", "a") as f:
        if len(list) == 1:
            f.write(result[0] + "\t" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        if len(list) > 1 and list[len(list) - 2] != result[0]:
            f.write("\n" + list[len(list) - 1] + "\t" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    print(list[len(list) - 1])
    time.sleep(600)

list = []
if __name__ == '__main__':
    while True:
        job(list)
