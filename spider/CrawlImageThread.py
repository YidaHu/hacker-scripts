#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/22 21:03
# @Author  : Huyd
# @Site    : 
# @File    : CrawlImageThread.py
# @Software: PyCharm

# coding=utf-8
import requests
from bs4 import BeautifulSoup
import os
from multiprocessing import Pool
import sys


# 获取最大页数
def find_MaxPage():
    all_url = 'http://www.mzitu.com'
    start_html = requests.get(all_url,
                              headers=header)  # 使用requests中的get方法来获取all_url(就是：http://www.mzitu.com/all这个地址)的内容 header为上面设置的请求头、请务必参考requests官方文档解释
    # 找寻最大页数
    soup = BeautifulSoup(start_html.text, "html.parser")  # 使用自带的html.parser解析，速度慢但通用
    page = soup.find_all('a', class_='page-numbers')
    max_page = page[-2].text  # 查找所有的<a>标签获取<a>标签中的文本也就是最后倒数第二个,为网站最大页数。
    return max_page


# 下载
def Download(href, header, title, path):
    html = requests.get(href, headers=header)
    soup = BeautifulSoup(html.text, 'html.parser')
    pic_max = soup.find_all('span')
    pic_max = pic_max[10].text  # 最大页数
    # win不能创建带？的目录
    if (os.path.exists(path + title.strip().replace('?', '')) and len(
            os.listdir(path + title.strip().replace('?', ''))) >= int(pic_max)):
        print('已完毕，跳过' + title)
        return 1
    print("开始扒取：" + title)
    os.makedirs(path + title.strip().replace('?', ''))  # 创建一个存放套图的文件夹
    os.chdir(path + title.strip().replace('?', ''))  # 切换到上面创建的文件夹
    # 输出每个图片页面的地址
    for num in range(1, int(pic_max) + 1):
        pic = href + '/' + str(num)
        # print(pic)
        html = requests.get(pic, headers=header)
        mess = BeautifulSoup(html.text, "html.parser")

        # 图片地址在img标签alt属性和标题一样的地方
        pic_url = mess.find('img', alt=title)
        html = requests.get(pic_url['src'], headers=header)
        # 获取图片的名字方便命名
        file_name = pic_url['src'].split(r'/')[-1]
        f = open(file_name, 'wb')  # 写入多媒体文件必须要 b 这个参数！！必须要！！
        f.write(html.content)  # 多媒体文件要是用conctent,图片不是文本文件，以二进制格式写入，所以是html.content
        f.close()
    print('完成' + title)


'''
#安卓端需要此语句reload(sys)
sys.setdefaultencoding('utf-8')
'''

if __name__ == '__main__':
    if (os.name == 'nt'):
        print(u'你正在使用win平台')
    else:
        print(u'你正在使用linux平台')

    # 设置headers，网站会根据这个判断你的浏览器及操作系统，很多网站没有此信息将拒绝你访问
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
    # http请求头
    path = 'E:/mzitu/'
    max_page = find_MaxPage()
    same_url = 'http://www.mzitu.com/page/'

    # 线程池中线程数
    pool = Pool(5)
    for n in range(1, int(max_page) + 1):
        each_url = same_url + str(n)
        start_html = requests.get(each_url, headers=header)
        soup = BeautifulSoup(start_html.text, "html.parser")
        # 实际上是第一个class = 'postlist'的div里的所有a 标签是我们要找的信息
        all_a = soup.find('div', class_='postlist').find_all('a', target='_blank')
        print("--------------->",all_a)
        for a in all_a:
            title = a.get_text()  # 提取a标签文本
            print("++++++++++++>>>>",title)
            if (title != ''):
                href = a['href']

                # pool.apply_async(Download, args=(href, header, title, path))
    pool.close()
    pool.join()
    print('所有图片已下完')
