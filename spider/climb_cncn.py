#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/2/2018 10:23 AM
# @Author  : Huyida
# @Site    : 
# @File    : climb_cncn.py
# @Software: PyCharm
'''
从旅游网爬取关于苏州旅游的数据
'''
import codecs
import json
import re
import requests
import bs4
from urllib import request
from http import cookiejar
import pandas as pd


def arr_to_excel(infos):
    '''
    :param infos: 导出到excel的源数据
    :return:
    '''
    title, address, introduce, cost, price = [], [], [], [], []
    for i in range(len(infos)):
        title.append(infos[i]['title'])
        address.append(infos[i]['address'])
        introduce.append(infos[i]['introduce'])
        cost.append(infos[i]['cost'])
        price.append(infos[i]['price'])
    df_empty = pd.DataFrame()
    df_empty['title'] = title
    df_empty['address'] = address
    df_empty['introduce'] = introduce
    df_empty['cost'] = cost
    df_empty['price'] = price
    df_empty.to_excel('result.xls')


if __name__ == '__main__':
    page = ""  # 页数
    links = []  # 目标链接
    infos = []  # 信息

    response = requests.get('http://suzhou.cncn.com/jingdian/')
    soup = bs4.BeautifulSoup(response.text, 'html.parser')  # 解析html
    for tag in soup.find_all("span", class_="text"):  # 找出总页数。<span>下class=text
        page = re.findall(r"\d+\.?\d*", tag.string)[0]  # 总页数
    print(page)
    # links = soup.find_all("a", class_="sister")
    # 遍历所有页数
    for i in range(1, int(page)):
        url = 'http://suzhou.cncn.com/jingdian/1-' + str(i) + '-0-0.html'
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        for tag in soup.find_all('a', class_="pic"):
            links.append(tag["href"])
    print(links)
    for i in range(len(links)):
        info = {}
        response = requests.get(links[i])
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        info["title"] = soup.find_all('h1')[0].text
        info["address"] = soup.find_all('dl', class_="first")[0].text

        # introduce = soup.find_all('dl', class_="introduce")
        # cost = soup.find_all('span', class_="cost")[1].text
        if len(soup.find_all('span', class_="cost")) == 2:
            info["cost"] = soup.find_all('span', class_="cost")[1].text
        else:
            info["cost"] = "no"
        if len(soup.find_all('span', class_="price")) == 2:
            info["price"] = soup.find_all('span', class_="price")[1].text
        else:
            info["price"] = "no"
        url = links[i] + 'profile'
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        info["introduce"] = soup.find_all('div', class_="type")[0].text
        # price = soup.find_all('span', class_="price")[1].text
        print(info)
        infos.append(info)
    arr_to_excel(infos)
    print("SUCCESS")
