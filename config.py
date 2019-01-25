#!/usr/bin/python
# -*-coding: UTF-8 -*-
import socket

'''防止循环调用问题,将s另存一个文件'''
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind( ('',9999) )
