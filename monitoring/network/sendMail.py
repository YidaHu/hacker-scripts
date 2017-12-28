#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 12/28/2017 2:37 PM
# @Author  : Huyd
# @Site    : 
# @File    : sendMail.py
# @Software: PyCharm

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


def sendMail():
    mail_host = "smtp.163.com"  # 设置邮件服务器
    mail_user = "xxx@163.com"  # 用户名
    mail_pass = "xxxx"  # 口令

    sender = 'xxxxx@163.com'  # 发送邮件的邮箱
    receivers = 'xxx@xxx' # 接收邮件的邮箱，可设置为你的QQ邮箱或者其他邮箱，多个邮箱用,分隔开来

    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = "xxx"  # 邮件发送人
    message['To'] = "xxxx"  # 邮件接收人
    subject = '测试监测结果'  # 邮件主题
    message['Subject'] = Header(subject, 'utf-8')

    # 邮件正文内容
    message.attach(MIMEText('测试监测有机器未能ping通，详细结果见附件……', 'plain', 'utf-8'))

    # 构造附件1，传送附件文件
    att1 = MIMEText(open("result.txt", 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="Result.txt"'
    message.attach(att1)

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")