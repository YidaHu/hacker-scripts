#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/16 15:34
# @Author  : Huyd
# @Site    :
# @File    : charset.py
# @Software: PyCharm
# @Description: 文件由JIS编码转UTF-8格式
import codecs

# 读取文件
def ReadFile(filePath, encoding="shift-jis"):
    with codecs.open(filePath, "r", encoding) as f:
        return f.read()

# 写文件
def WriteFile(filePath, u, encoding="utf-8"):
    with codecs.open(filePath, "w", encoding) as f:
        f.write(u)

# JIS转UTF-8
def JIS_2_UTF8(src, dst):
    content = ReadFile(src, encoding="shift-jis")
    WriteFile(dst, content, encoding="utf-8")


if __name__ == "__main__":
    FILENAME = "/USERPRO/MISC/test.txt"
    FILENAME1 = "/USERPRO/MISC/test1.txt"
    JIS_2_UTF8(FILENAME, FILENAME1)
    pass
