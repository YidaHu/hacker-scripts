#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/14 18:50
# @Author  : Huyd
# @Site    : 
# @File    : post_request.py
# @Software: PyCharm
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

import re
import schedule
import time


def send_mail(subject, message):
    mail_host = "smtp.163.com"  # 设置邮件服务器
    mail_user = "xxx"  # 用户名
    mail_pass = "xxxxx"  # 口令

    sender = 'xxx@163.com'  # 发送邮件的邮箱
    receivers = 'xxxx@xxx.com'  # 接收邮件的邮箱，可设置为你的QQ邮箱或者其他邮箱，多个邮箱用,分隔开来

    # 创建一个带附件的实例
    message = MIMEText(message, 'plain', 'utf-8')
    message['From'] = "xxx@163.com"  # 邮件发送人
    message['To'] = "xxx@xxxx.com"  # 邮件接收人
    # subject = '测试监测结果'  # 邮件主题
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP()  # 如果Linux使用SMTP_SSL
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号,465为SMTP_SSL端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


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


def job():
    url = "http://ent.sipmch.com.cn:8000/ModuleDefaultCompany/RentManage/SearchRentNo"
    params = {"CertNo": "xxxxxxxx"}  # 参数
    result = post_request(url, params)  # 结果抓取
    result = re.sub(r'</?\w+[^>]*>', '', result)  # 过滤html标签
    subject = "自动化查询优租房排号系统"
    message = result
    send_mail(subject, str(message))  # 发送邮件
    print(result)
    time.sleep(61)


def main(h, m):
    '''h表示设定的小时，m为设定的分钟'''
    while True:
        # 判断是否达到设定时间，例如0:00
        while True:
            now = datetime.datetime.now()
            print(now.hour, ' ', now.minute, ' ', now.microsecond)
            # 到达设定时间，结束内循环
            if now.hour == h and now.minute == m:
                break
            # 不到时间就等20秒之后再次检测
            time.sleep(20)
        # 做正事，一天做一次
        job()


print(time.asctime(time.localtime(time.time())))
main(11, 59)
