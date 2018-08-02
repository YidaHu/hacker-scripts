#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2/5/2018 3:00 PM
# @Author  : Huyd
# @Site    : 
# @File    : zhihuQA.py
# @Software: PyCharm
import codecs
import json
import re
import requests
import bs4
from urllib import request
from http import cookiejar

# 登录后主页未异步的单页数据URL
URL = 'https://www.zhihu.com/search?type=content&q=%E8%8B%8F%E5%B7%9E%E7%BE%8E%E9%A3%9F'
# 知乎传递参数API接口，可获取多页数据
URL1 = 'https://www.zhihu.com/api/v4/search_v3'
session = requests.Session()
# 拿到浏览器设置的用户代理
User_Agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
# 定义header，注意：header里的key是固定的
# 单页包头
header = {
    "HOST": "www.zhihu.com",
    "Referer": "https://www.zhihu.com/?next=%252Ftopic",
    "User-Agent": User_Agent
}
# 多页包头
header1 = {
    "HOST": "www.zhihu.com",
    "Referer": "https://www.zhihu.com/search?type=content&q=%E8%8B%8F%E5%B7%9E%E7%BE%8E%E9%A3%9F",
    "User-Agent": User_Agent
}
# cookie值
cookie = {
    'Cookie': '_zap=6371c0da-0400-4478-8aee-13f470bc1983; q_c1=339e1572e6ed4fffa9b9227d5d341b39|1516002069000|1516002069000; aliyungf_tc=AQAAAGkU/kSb9gQAQuTwOnQqNtss0XiO; d_c0="ALArEBMGGQ2PTk6TL6U87p6R46Jt4lK_Gr0=|1517797613"; _xsrf=ea255e75-555b-4caf-b014-c764604a1a4d; l_cap_id="ZjUzZWU3OGVjZDJkNGQwNzliMDhkNDNkMmMxNzMyOTI=|1517813170|778ec670a79001d83d35775d09693478fa67270a"; r_cap_id="ZTMzYjY2YjRlODJjNGM4NTg4YTg3Nzk4YWZiNDQ1OWM=|1517813170|d1a0a03b7d27d2e244a4a5914bd5132e7db2a526"; cap_id="NzRiMmRjYzBmNTM5NGQyNDgwNmYwYjc2N2Q4MTZjMGM=|1517813170|3cf75415f28df38f8958723b2373347217133728"; capsion_ticket="2|1:0|10:1517813183|14:capsion_ticket|44:MWRhMWQyMmVhOTQzNGFmNTg0NGQ0NDRjZjVlZjJhMGI=|4c28be03e9494d8bec63bdd81e008831422584d9219834fa4e02d0c69bbf9899"; z_c0="2|1:0|10:1517813211|4:z_c0|92:Mi4xWU92ZUFRQUFBQUFBc0NzUUV3WVpEU1lBQUFCZ0FsVk4yMHRsV3dDZXBhdHowVE9KVlhBR2RzUmN1czN6dW5mSGhR|67b0039bcf207871ac14ec735078204976cd04d5f426280b834c7dae2ba13444"'}


def write_to_file(str):
    '''
        字符串存到文件中
    '''
    with codecs.open("data.txt", 'a', encoding='utf-8') as f:
        f.writelines(str)
        # 关闭打开的文件
        f.close()


def get_zhihu_data(offset):
    '''
    根据登录的cookie爬取知乎主题下的标题
    :param offset:页数
    :return:
    '''
    d = {'t': 'general', 'q': '苏州美食', 'correction': '1', 'search_hash_id': '79ce27dadcd4b9244e8bc9ecf5981c73',
         'offset': offset, 'limit': '10'}
    html = session.get(URL1, data=d, headers=header1,
                       cookies=cookie).content
    print(html.decode('utf-8'))
    # response = requests.get('https://www.zhihu.com/search?type=content&q=%E8%8B%8F%E5%B7%9E%E7%BE%8E%E9%A3%9F')
    results = json.loads(html.decode('utf-8'))
    #
    list = results['data']
    lists = []
    for i in range(len(list)):
        result = list[i]['highlight']['title']
        # lists.append(result)
        print(result)
        write_to_file(str(result) + '\n')
    print(lists)


if __name__ == '__main__':
    index = 5
    # 由于知乎默认每次异步10条数据，所以每次传参+10
    while index <= 105:
        get_zhihu_data(index)
        index = index + 10

# soup = bs4.BeautifulSoup(html, 'html.parser')
#
# # links = soup.find_all('span',{'class': 'Highlight'})
# span = soup.find('span', attrs={'class': 'Highlight'})
# print(span)

# 匹配带有class属性的tr标签
# soup = soup.find_all('div', attrs={'class': re.compile("(List-item)|()")})
# for trtag in taglist:
#     tdlist = trtag.find_all('span')  #在每个tr标签下,查找所有的td标签
#     for t in tdlist.find_all(True):
#         print(t.string)

# tag = soup.select('.Highlight')
# print(tag)

# for title in soup.select('.Highlight'):
#     print(title.get_text())
