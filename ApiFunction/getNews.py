#!/usr/bin/python
# -*-coding: UTF-8 -*-

import requests
def getNews():
    # 获取金山词霸每日一句，英文和翻译
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    contents = r.json()['content']
    translation = r.json()['translation']
    
    s= contents 
    return s.encode("utf-8")