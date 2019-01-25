#!/usr/bin/python
# -*-coding: UTF-8 -*-
import json
import requests
from pprint import pprint


def chatEach(msg):
	dataForm = {
	"perception": {
	    "inputText": {
	        "text": msg
	    },
	    "selfInfo": {
	        "location": {
	            "city": "南京",
	            "province": "江苏",
	            "street": "河海路"
	        }
	    }
	},
	"userInfo": {
	    "apiKey": 'f42e3f888d88459ca3d3d3a3775e74cf',
	    "userId": "yanshee"
		}
	}
	dataForm = json.dumps(dataForm)
	html = requests.post("http://openapi.tuling123.com/openapi/api/v2",data=dataForm)
	returnValue = html.json()
	try:
		words = returnValue.get("results")[0].get('values').get("text")
		print(words)
		#pprint(returnValue)
	except:
		words = "网络似乎出了点问题,我不知道如何回答你了"
	else:
		pass
	return words.encode("utf-8")

if __name__ == '__main__':
	print(type(chatEach('唱海阔天空')))


