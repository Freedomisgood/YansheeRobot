# !/usr/bin/python
# -*- coding:utf-8 -*-
import requests
def getWeather():
	html = requests.get('https://free-api.heweather.net/s6/weather/now?location=118.938,32.1157&key=HE1901241544261223')
	try:
		data = html.json().get('HeWeather6')[0].get("now")
	except:
		return "神机妙算的我现在也无法解决天气问题啦"
	else:
		pass

	cond_txt =data.get('cond_txt') 
	tmp = data.get('tmp')
	hum = data.get('hum')
	pcpn = data.get('pcpn')
	pres = data.get('pres')
	words = '现在天气是{},温度为{}摄氏度,湿度为{},降雨量为{},大气压强为{}千帕'.format(cond_txt,tmp,hum,pcpn,pres)
	return words

if __name__ == '__main__':
	print(getWeather())