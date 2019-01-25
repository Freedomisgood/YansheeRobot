#!/usr/bin/python
# -*-coding: UTF-8 -*-
from threading import Thread

def async(f):
    '''
    异步执行该函数
    :param f: 函数
    :return:
    '''
    def wrapper(*args, **kwargs):
        thr = Thread(target = f, args = args, kwargs = kwargs)
        thr.start()
    return wrapper

