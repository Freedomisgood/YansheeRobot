#!/usr/bin/python
# -*-coding: UTF-8 -*-

import time
import socket

# Api库导入
import RobotApi

# 自定义模块
import combFunc
from combFunc import say
from ApiFunction.getWeather import getWeather
from ApiFunction.chatEach import chatEach
from ApiFunction.getNews import getNews


def connectRobot():
	'''
	连接机器人
	:return: None
	'''
	RobotApi.ubtRobotInitialize()
	ret=RobotApi.ubtRobotConnect("SDK","1","127.0.0.1")
	if(0!=ret):
		RobotApi.ubtVoiceTTS(0,"无法连接Yanshee")
		exit(1)

def disConnectRobot():
	'''
	断开机器人的连接,只需要执行一次
	:return: None
	'''
	RobotApi.ubtRobotDisconnect("SDK","1","127.0.0.1")
	RobotApi.ubtRobotDeinitialize()



def recerveInfo():
	'''
	接受UDP广播信息
	:return: None
	'''
	while True:
		data,client_addr = s.recvfrom(1024)
		if(data=="stand"):
			say("我们是可以金鸡独立的yanshee")
			time.sleep(1)
			combFunc.standAlone()

		elif(data=="dance"):
			say("让我们给大家跳一支精彩的舞蹈吧，不要爱上我们呦")
			time.sleep(1)
			combFunc.allDance()

		elif(data=="look"):
			say("帅哥美女让我瞧瞧你")
			time.sleep(1)
			combFunc.VisionDetect()

		elif(data=="motion"):
			say("motion")
			time.sleep(1)
			ret = combFunc.getRobotFaceExpression() 
			if( ret == 'Sadness'):
				say(chatEach("讲个笑话"))
			else:
				say(ret)

		elif (data == "look"):
			combFunc.say("帅哥美女让我瞧瞧你")
			time.sleep(1)
			combFunc.VisionDetect()

		elif (data == "motion"):
			combFunc.say("motion")
			time.sleep(1)
			combFunc.getRobotFaceExpression()

		elif (data == "photo"):
			combFunc.say("")
			time.sleep(1)
			combFunc.takephoto()

		# 传感器
		elif(data=="avoid"):
			say("让我们来展示一下避障行走吧")
			time.sleep(1)
			combFunc.avoidHit()

		elif(data=="holdhand"):
			say("我们还是个懂礼貌的好孩子呢")
			time.sleep(1)
			combFunc.holdHand()

		elif(data=="chat"):
			say("接下来我们要演示高难度功能，请勿轻易模仿")
			time.sleep(1)
			say("我们能和你们任意交流呢")
			time.sleep(1)
			data ,client_addr = s.recvfrom(1024)
			# 图灵机器人交流
			say( chatEach(data))

		elif(data=="song"):
			say("评委大大们点首歌吧")
			time.sleep(1)
			combFunc.randomMusic()

		elif(data=="weather"):
			say("我还能播报天气预报呢")
			time.sleep(1)
			say(getWeather())

		elif(data=="follow"):
			say("主人要去哪里，带上我们")
			time.sleep(1)
			combFunc.compare()

		elif(data=="forward"):	
			RobotApi.ubtSetRobotMotion("walk","front",2,1)
			time.sleep(1)

		elif(data=="end"):
			say("我们要断开连接啦，谢谢观看，不要想我们呦")
			time.sleep(1)
			disConnectRobot()

		elif(data == 'dan'):
			RobotApi.ubtStartRobotAction("dancing",1)
			data,client_addr = s.recvfrom(1024)
			print(data)
			if( data == 'stop' ):
				stopAtOnce()
			reStart()

		elif data=='stop':
			combFunc.stopAtOnce()
			time.sleep(1)
		if data == 'restart':
			combFunc.reStart()
		else:
			continue



if __name__ == '__main__':
	connectRobot()

	from config import s
	'''导入网络设置'''

	import sys
	reload(sys) 
	sys.setdefaultencoding('utf-8')
	
	say(getNews()) # 开机骚话

	recerveInfo()

	disConnectRobot()


