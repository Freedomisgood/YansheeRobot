#!/usr/bin/python
# -*- coding:utf-8 -*-
import RobotApi
import pyaudio,wave
# from aip import AipSpeech
from ApiFunction.chatEach import chatEach
import time
from config import s
import myturn


''' 百度语音识别 APPID AK SK '''
APP_ID = '15484819'
API_KEY = 'UGti0HnhIDnq1ETx8dje23AX'
SECRET_KEY = 'yFOVvyP8GE5bV9WcGdkbq8BPHa5kK69t '

# client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

def audioRecord():
    '''
    录音,将音频保存,给百度API解析
    '''
        pa=pyaudio.PyAudio()
        stream=pa.open(format=pyaudio.paInt16,channels=1,rate=16000,input=True,frames_per_buffer=2000)
        save_buffer=''
        wf=wave.open('record.pcm','wb')
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(16000)
        try:
                while True:
                        string_audio_data=stream.read(1000)
                        save_buffer+=string_audio_data
                        if len(save_buffer)>=160000:
                                wf.writeframes(save_buffer)
                                break
        except:
                wf.close()
        else:
                data = analyzeAudio()


        try:
                say(chatEach(data))
        except Exception as e:
                print("调试",e)
        else:
                pass

def analyzeAudio():
        ret = client.asr(get_file_content('record.pcm'), 'pcm', 16000, {
         'dev_pid': 1536,
        })
        return ret.get("result")[0]

# 读取文件
def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
                return fp.read()



def takephoto():
    RobotApi.ubtTakeAPhoto("xhy",12)



def VisionDetect():
        '''
        检测是否含有人脸
        :return: None
        '''
        val = 0
        ret=RobotApi.ubtVisionDetect("face",val,2)
        if val:
                RobotApi.ubtVoiceTTS(1,"没有人脸")
        else:
                RobotApi.ubtVoiceTTS(1,"成功检测到人脸")
        if(ret!=0):
                RobotApi.ubtVoiceTTS(1,"无法检测人脸")
                return 0


def FaceCompare():
        '''
        人脸判别
        :return: None
        '''
        ID = 'nofounda'
        ret2=RobotApi.ubtFaceCompare(2,ID)
        if ( ID  == 'nofound\x00' ):
                RobotApi.ubtVoiceTTS(1,"无法分辨身份")
        else:
                RobotApi.ubtVoiceTTS(1,ID)
        time.sleep(1)
        broadCast('forward')


def getRobotFaceExpression():
        '''
        获得面部表情,选择可能性最大的
        :return: 最可能的表情
        '''
        faceInfo=RobotApi.UBTEDU_FACEEXPRE_T()
        ret3=RobotApi.ubtFaceExpression(2,faceInfo)
        if(ret3!=0):
                RobotApi.ubtVoiceTTS(1,"表情检测错误")
                return 0
        else:
                # 这边存在逻辑错误,相同的值会重复, 但实际操作如果碰到两个最大的也只能是随机取一个,就没有什么影响
                expressions={}

                expressions[faceInfo.fHappinessValue]='Happiness'
                expressions[faceInfo.fSurpriseValue]='Surprise'
                expressions[faceInfo.fAngerValue]='Anger'
                expressions[faceInfo.fSadnessValue]='Sadness'
                expressions[faceInfo.fNeutralValue]='Neutral'
                expressions[faceInfo.fDisgustValue]='Disgust'
                expressions[faceInfo.fFearValue]='Fear'           

                expressions[faceInfo.fHappinessValue]='Happiness'
                expressions[faceInfo.fSurpriseValue]='Surprise'
                expressions[faceInfo.fAngerValue]='Anger'
                expressions[faceInfo.fSadnessValue]='Sadness'
                expressions[faceInfo.fNeutralValue]='Neutral'
                expressions[faceInfo.fDisgustValue]='Disgust'
                expressions[faceInfo.fFearValue]='Fear'

                value = max(faceInfo.fHappinessValue,faceInfo.fSurpriseValue,faceInfo.fAngerValue,faceInfo.fSadnessValue,faceInfo.fNeutralValue,faceInfo.fDisgustValue,faceInfo.fFearValue)
        
                return value


def say(speak):
        '''
        使用TTS说话
        :param speak: str,说话内容
        :return: None
        '''
        RobotApi.ubtVoiceTTS(0,speak)


def holdHand():
        '''
        举手,握手
        '''
        servoAngle=RobotApi.UBTEDU_ROBOTSERVO_T()
        sensorValue=RobotApi.UBTEDU_ROBOTINFRARED_SENSOR_T()
        servoAngle=RobotApi.UBTEDU_ROBOTSERVO_T()
        servoAngle.SERVO1_ANGLE= 90
        servoAngle.SERVO2_ANGLE= 140
        servoAngle.SERVO3_ANGLE= 163
        servoAngle.SERVO4_ANGLE= 170
        servoAngle.SERVO5_ANGLE= 17
        servoAngle.SERVO6_ANGLE= 70
        servoAngle.SERVO7_ANGLE= 90
        servoAngle.SERVO8_ANGLE= 60
        servoAngle.SERVO9_ANGLE= 75
        servoAngle.SERV10_ANGLE= 110
        servoAngle.SERV11_ANGLE= 90
        servoAngle.SERV12_ANGLE= 90
        servoAngle.SERV13_ANGLE= 120
        servoAngle.SERV14_ANGLE= 105
        servoAngle.SERV15_ANGLE= 70
        servoAngle.SERV16_ANGLE= 90
        RobotApi.ubtSetRobotServo(servoAngle,50)
        time.sleep(4)
        ret=RobotApi.ubtReadSensorValue("touch",sensorValue,4)
        if(ret!=0): 
                        print("read sensor error")
                        RobotApi.ubtSearchExtendSensor()

        if (sensorValue.iValue != 0):
                RobotApi.ubtSetRobotMotion("wave", "right", 3, 2)

               # 还原
                servoAngle.SERVO1_ANGLE= 90
                servoAngle.SERVO2_ANGLE= 140
                servoAngle.SERVO3_ANGLE= 160
                servoAngle.SERVO4_ANGLE= 90
                servoAngle.SERVO5_ANGLE= 40
                servoAngle.SERVO6_ANGLE= 20
                servoAngle.SERVO7_ANGLE= 90
                servoAngle.SERVO8_ANGLE= 60
                servoAngle.SERVO9_ANGLE= 75
                servoAngle.SERVO10_ANGLE= 110
                servoAngle.SERVO11_ANGLE= 90
                servoAngle.SERVO12_ANGLE= 90
                servoAngle.SERVO13_ANGLE= 120
                servoAngle.SERVO14_ANGLE= 105
                servoAngle.SERVO15_ANGLE= 70
                servoAngle.SERVO16_ANGLE= 90
                RobotApi.ubtSetRobotServo(servoAngle,200)


def avoidHit():
        sensorValue = RobotApi.UBTEDU_ROBOTINFRARED_SENSOR_T()
        # sensorvalue=RobotApi.UBTEDU_ROBOTULTRASONIC_SENSOR_T()
        i = 0
        while True:
                ret = RobotApi.ubtReadSensorValue("infrared", sensorValue, 4)
                # red=RobotApi.ubtReadSensorValue("ultrasonic",sensorvalue,4)
                if (0 != ret):
                        print("read sensor error")
                print("value:%d" % sensorValue.iValue)
                # print("value:%d"%sensorvalue.iValue)
                if (sensorValue.iValue < 350):
                        i = i + 1
                        myturn.myturn()
                else:
                        RobotApi.ubtSetRobotMotion("walk", "front", 3, 1)
                time.sleep(0.3)
                if i >= 6:
                        break
        RobotApi.ubtStartRobotAction("reset", 1)


def allDance():
        broadCast('dan')
        # RobotApi.ubtStartRobotAction("dancing",1)
        # data,client_addr = s.recvfrom(1024)
        # print(data)
        # if( data == 'stop' ):
        #         stopAtOnce()
        # reStart()


def stopAtOnce():
        RobotApi.ubtStopRobotAction()


def reStart():
        servoAngle=RobotApi.UBTEDU_ROBOTSERVO_T()

        servoAngle.SERVO1_ANGLE= 90
        servoAngle.SERVO2_ANGLE= 140
        servoAngle.SERVO3_ANGLE= 160

        # Action : keep right arm straight
        servoAngle.SERVO4_ANGLE= 90
        servoAngle.SERVO5_ANGLE= 40
        servoAngle.SERVO6_ANGLE= 20
        servoAngle.SERVO7_ANGLE= 90
        servoAngle.SERVO8_ANGLE= 60
        servoAngle.SERVO9_ANGLE= 75
        servoAngle.SERVO10_ANGLE= 110
        servoAngle.SERVO11_ANGLE= 90
        servoAngle.SERVO12_ANGLE= 90
        servoAngle.SERVO13_ANGLE= 120
        servoAngle.SERVO14_ANGLE= 105
        servoAngle.SERVO15_ANGLE= 70
        servoAngle.SERVO16_ANGLE= 90
        RobotApi.ubtSetRobotServo(servoAngle,200)



def broadCast(msg,network='<broadcast>',PORT=9999):
        '''
        指定IP,或者<broadcast>
        '''
        s.sendto(msg.encode('utf-8'), (network, PORT))


def randomMusic():
        import random
        import os
        import subprocess
        files = os.listdir('./music')
        n = len(files)
        ranN = random.randint(0,n-1)
        musicToplay = files[ranN]
        subprocess.call('MPID=$(play {})'.format(musicToplay))

        #接收信号,停止语音,好像还有点问题
        data,client_addr = s.recvfrom(1024)
        print(data)
        if data=='stop':
                subprocess.call('pkill -9 $(MPID)')






def trace():
        IDa = 'nofounda'
        ret2=RobotApi.ubtFaceCompare(2,IDa)
        if ( IDa  == 'nofound\x00' ):
                print(IDa)
                RobotApi.ubtVoiceTTS(1,"无法分辨身份")
        else:
                RobotApi.ubtVoiceTTS(1,IDa)
                RobotApi.ubtSetRobotMotion("walk","front",2,3)
                
                servoAngle = RobotApi.UBTEDU_ROBOTSERVO_T()
                servoAngle.SERVO1_ANGLE = 89
                RobotApi.ubtSetRobotServo(servoAngle,50)

                servoAngle = RobotApi.UBTEDU_ROBOTSERVO_T()
                servoAngle.SERVO2_ANGLE = 139
                RobotApi.ubtSetRobotServo(servoAngle,50)

                servoAngle = RobotApi.UBTEDU_ROBOTSERVO_T()
                servoAngle.SERVO3_ANGLE = 163
                RobotApi.ubtSetRobotServo(servoAngle,50)

                servoAngle = RobotApi.UBTEDU_ROBOTSERVO_T()
                servoAngle.SERVO4_ANGLE = 90
                RobotApi.ubtSetRobotServo(servoAngle,50)

                servoAngle = RobotApi.UBTEDU_ROBOTSERVO_T()
                servoAngle.SERVO5_ANGLE = 39
                RobotApi.ubtSetRobotServo(servoAngle,50)

                servoAngle = RobotApi.UBTEDU_ROBOTSERVO_T()
                servoAngle.SERVO6_ANGLE = 15 
                RobotApi.ubtSetRobotServo(servoAngle,50)

                servoAngle = RobotApi.UBTEDU_ROBOTSERVO_T()
                servoAngle.SERVO7_ANGLE = 90
                RobotApi.ubtSetRobotServo(servoAngle,50)

                servoAngle = RobotApi.UBTEDU_ROBOTSERVO_T()
                servoAngle.SERVO8_ANGLE =59
                RobotApi.ubtSetRobotServo(servoAngle,50)

                servoAngle = RobotApi.UBTEDU_ROBOTSERVO_T()
                servoAngle.SERVO9_ANGLE = 75
                RobotApi.ubtSetRobotServo(servoAngle,50)

                servoAngle = RobotApi.UBTEDU_ROBOTSERVO_T()
                servoAngle.SERVO10_ANGLE = 110 
                RobotApi.ubtSetRobotServo(servoAngle,50)

                servoAngle = RobotApi.UBTEDU_ROBOTSERVO_T()
                servoAngle.SERVO11_ANGLE =90
                RobotApi.ubtSetRobotServo(servoAngle,50)

                servoAngle = RobotApi.UBTEDU_ROBOTSERVO_T()
                servoAngle.SERVO12_ANGLE =89
                RobotApi.ubtSetRobotServo(servoAngle,50)

                servoAngle = RobotApi.UBTEDU_ROBOTSERVO_T()
                servoAngle.SERVO13_ANGLE = 120 
                RobotApi.ubtSetRobotServo(servoAngle,50)

                servoAngle = RobotApi.UBTEDU_ROBOTSERVO_T()
                servoAngle.SERVO14_ANGLE = 104
                RobotApi.ubtSetRobotServo(servoAngle,50)

                servoAngle = RobotApi.UBTEDU_ROBOTSERVO_T()
                servoAngle.SERVO15_ANGLE = 69
                RobotApi.ubtSetRobotServo(servoAngle,50)

                servoAngle = RobotApi.UBTEDU_ROBOTSERVO_T()
                servoAngle.SERVO16_ANGLE = 90 
                RobotApi.ubtSetRobotServo(servoAngle,50)
        time.sleep(2)


def standAlone():
        # 执行各自的金鸡独立函数
        from stand import stand_alone_CL,stand_alone_CXQ,stand_alone_SYD
        '''
        用各自的stand()函数
        '''
        stand_alone_CL.stand()
