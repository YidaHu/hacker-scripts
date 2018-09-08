#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/7 20:16
# @Author  : Huyd
# @Site    : 
# @File    : esteelauder.py
# @Software: PyCharm

import requests
import json
from pandas.core.frame import DataFrame


def spider(country, city):
    url = "https://www.esteelauder.com.hk/rpc/jsonrpc.tmpl"

    querystring = {"dbgmethod": "locator.doorsandevents"}
    # city = 'Wien'
    # country = 'Austria'
    # payload = "JSONRPC=%5B%7B%22method%22%3A%22locator.doorsandevents%22%2C%22id%22%3A9%2C%22params%22%3A%5B%7B%22fields%22%3A%22DOOR_ID%2C%20DOORNAME%2C%20EVENT_NAME%2C%20EVENT_START_DATE%2C%20EVENT_END_DATE%2C%20EVENT_IMAGE%2C%20EVENT_FEATURES%2C%20EVENT_TIMES%2C%20SERVICES%2C%20STORE_HOURS%2C%20ADDRESS%2C%20ADDRESS2%2C%20STATE_OR_PROVINCE%2C%20CITY%2C%20COUNTRY%2C%20REGION%2C%20LANGUAGE%2C%20ZIP_OR_POSTAL%2C%20PHONE1%22%2C%22radius%22%3A20%2C%22show_stores_list%22%3A%22all%22%2C%22uom%22%3A%22km%22%2C%22zip%22%3A%22%22%2C%22state%22%3A%22%22%2C%22city%22%3A%22%E5%A4%AA%E5%8F%A4%E5%9F%8E%22%2C%22country%22%3A%22Hong%20Kong%22%2C%22region_id%22%3A%229%22%2C%22language_id%22%3A%22176%22%7D%5D%7D%5D"
    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"JSONRPC\"\r\n\r\n[{\"method\":\"locator.doorsandevents\",\"id\":2,\"params\":[{\"fields\":\"DOOR_ID, DOORNAME, EVENT_NAME, EVENT_START_DATE, EVENT_END_DATE, EVENT_IMAGE, EVENT_FEATURES, EVENT_TIMES, SERVICES, STORE_HOURS, ADDRESS, ADDRESS2, STATE_OR_PROVINCE, CITY, COUNTRY, ZIP_OR_POSTAL, PHONE1\",\"radius\":20,\"show_stores_list\":\"all\",\"uom\":\"mile\",\"zip\":\"\",\"state\":\"\",\"city\":\"" + city + "\",\"country\":\"" + country + "\"}]}]\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'cache-control': "no-cache",
        'postman-token': "890910cc-1c12-3e52-ef29-c10886e5f092"
    }
    # payload.encode('latin1')  # Throws UnicodeEncodeError, proves that this can't be expressed in ISO-8859-1.
    payload.encode('utf-8')
    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    print(response.text)
    jsonstr = json.loads(response.text)
    print(jsonstr)

    list = []
    title_list = []
    content_list = []
    if 'results' in jsonstr[0]['result']['value'].keys():
        for key in jsonstr[0]['result']['value']['results']:
            list.append(key)
        print("->")
        print(list)
        print(jsonstr[0]['result']['value']['results'])
        for key in jsonstr[0]['result']['value']['results'][list[0]]:
            title_list.append(key)
        lists.append(title_list)
        if len(list) != 0:

            for i in range(len(list)):
                for key in jsonstr[0]['result']['value']['results'][list[i]]:
                    content_list = []
                    for j in range(len(title_list)):
                        content_list.append(jsonstr[0]['result']['value']['results'][list[i]][title_list[j]])
                    lists.append(content_list)
                # print(list)
                # print(title_list)
                # print(lists)


lists = []
lists.append(
    ['ADDRESS2', 'EVENT_END_DATE', 'SERVICES', 'LONGITUDE', 'DOORNAME', 'EVENT_IMAGE', 'ZIP_OR_POSTAL', 'LATITUDE',
     'CITY', 'COUNTRY', 'EVENT_START_DATE', 'EVENT_NAME', 'STORE_HOURS', 'PHONE1', 'DOOR_ID', 'DISTANCE',
     'EVENT_TIMES', 'ADDRESS', 'EVENT_FEATURES', 'STATE_OR_PROVINCE'])
city_lists = []
with open("hk.txt",encoding='UTF-8') as input:
    lines = input.readlines()
for i in range(len(lines)):
    c_list = lines[i].replace('\n', '').split('\t')
    city_lists.append(c_list)
print(city_lists)

for i in range(len(city_lists)):
    try:
        spider(city_lists[i][0], city_lists[i][1])
    except:
        pass
    continue
data = DataFrame(lists)
data.to_excel("abc.xlsx", sheet_name="esteelauder", index=False, header=True)
