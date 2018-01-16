#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/16 15:34
# @Author  : Huyd
# @Site    : 
# @File    : textAnalysis.py
# @Software: PyCharm

import jieba.analyse
from os import path

from numpy import unicode
from scipy.misc import imread
import matplotlib as mpl
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

if __name__ == "__main__":
    mpl.rcParams['font.sans-serif'] = ['FangSong']
    # mpl.rcParams['axes.unicode_minus'] = False

    content = open("testing.txt", "rb").read()

    # tags extraction based on TF-IDF algorithm
    jieba.load_userdict("dict.txt")
    tags = jieba.analyse.extract_tags(content, topK=100, withWeight=False)
    text = " ".join(tags)
    text = unicode(text)
    # read the mask
    d = path.dirname(__file__)
    trump_coloring = imread(path.join(d, "china.jpg"))

    wc = WordCloud(font_path='simsun.ttc',
                   background_color="white", max_words=300, mask=trump_coloring,
                   max_font_size=40, random_state=42)

    # generate word cloud
    wc.generate(text)

    # generate color from image
    image_colors = ImageColorGenerator(trump_coloring)

    plt.imshow(wc)
    plt.axis("off")
    plt.show()
