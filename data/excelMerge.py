#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/14 8:36
# @Author  : Huyd
# @Site    : 
# @File    : excelMerge.py
# @Software: PyCharm

import pandas as pd

DATA_INSIDE_PATH = r"data.xlsx"

dd1 = pd.read_excel(DATA_INSIDE_PATH, 'Sheet1')
dd2 = pd.read_excel(DATA_INSIDE_PATH, 'Sheet2')

frame1 = pd.DataFrame(dd1)
frame2 = pd.DataFrame(dd2)

df_result = pd.merge(frame1, frame2, how='right', on=['AID', 'I'])
columns = ['ID', 'AID', 'I', 'A', 'Q']
df_result.to_excel('result.xls', index=False, columns=columns)
