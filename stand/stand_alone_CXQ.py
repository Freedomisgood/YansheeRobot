#!/user/bin/python
#_*_coding: utf-8 -*-
import RobotApi 
from time  import sleep
def stand():
    ret = RobotApi.ubtSetRobotLED("camera","red","on")
    if(0 != ret):
        print("led_error")
        exit(1)

    servoAngle = RobotApi.UBTEDU_ROBOTSERVO_T()
    servoAngle.SERVO8_ANGLE =22
    RobotApi.ubtSetRobotServo(servoAngle,50)

    servoAngle = RobotApi.UBTEDU_ROBOTSERVO_T()
    servoAngle.SERVO10_ANGLE = 106
    RobotApi.ubtSetRobotServo(servoAngle,50)

    servoAngle = RobotApi.UBTEDU_ROBOTSERVO_T()
    servoAngle.SERVO16_ANGLE = 108
    RobotApi.ubtSetRobotServo(servoAngle,50)

    sleep(1)

    servoAngle = RobotApi.UBTEDU_ROBOTSERVO_T()
    servoAngle.SERVO12_ANGLE = 101 
    RobotApi.ubtSetRobotServo(servoAngle,50)
    sleep(1)

    servoAngle = RobotApi.UBTEDU_ROBOTSERVO_T()
    servoAngle.SERVO1_ANGLE = 89
    RobotApi.ubtSetRobotServo(servoAngle,50)

    servoAngle = RobotApi.UBTEDU_ROBOTSERVO_T()
    servoAngle.SERVO2_ANGLE = 65
    RobotApi.ubtSetRobotServo(servoAngle,50)
    sleep(1)
    servoAngle = RobotApi.UBTEDU_ROBOTSERVO_T()
    servoAngle.SERVO3_ANGLE = 91
    RobotApi.ubtSetRobotServo(servoAngle,50)

    servoAngle = RobotApi.UBTEDU_ROBOTSERVO_T()
    servoAngle.SERVO4_ANGLE = 96
    RobotApi.ubtSetRobotServo(servoAngle,50)
    
    servoAngle = RobotApi.UBTEDU_ROBOTSERVO_T()
    servoAngle.SERVO5_ANGLE = 82
    RobotApi.ubtSetRobotServo(servoAngle,50)

    servoAngle = RobotApi.UBTEDU_ROBOTSERVO_T()
    servoAngle.SERVO6_ANGLE = 91 
    RobotApi.ubtSetRobotServo(servoAngle,50)
    
    servoAngle = RobotApi.UBTEDU_ROBOTSERVO_T()
    servoAngle.SERVO7_ANGLE = 80
    RobotApi.ubtSetRobotServo(servoAngle,50)



    servoAngle = RobotApi.UBTEDU_ROBOTSERVO_T()
    servoAngle.SERVO9_ANGLE = 43
    RobotApi.ubtSetRobotServo(servoAngle,50)


    
    servoAngle = RobotApi.UBTEDU_ROBOTSERVO_T()
    servoAngle.SERVO11_ANGLE = 101
    RobotApi.ubtSetRobotServo(servoAngle,20)



    servoAngle = RobotApi.UBTEDU_ROBOTSERVO_T()
    servoAngle.SERVO13_ANGLE = 156 
    RobotApi.ubtSetRobotServo(servoAngle,20)
    
    servoAngle = RobotApi.UBTEDU_ROBOTSERVO_T()
    servoAngle.SERVO14_ANGLE = 163
    RobotApi.ubtSetRobotServo(servoAngle,20)

    servoAngle = RobotApi.UBTEDU_ROBOTSERVO_T()
    servoAngle.SERVO15_ANGLE = 50
    RobotApi.ubtSetRobotServo(servoAngle,20)


    
    servoAngle = RobotApi.UBTEDU_ROBOTSERVO_T()
    servoAngle.SERVO17_ANGLE = 89
    RobotApi.ubtSetRobotServo(servoAngle,20)
    sleep(5)
    aservoAngle = RobotApi.UBTEDU_ROBOTSERVO_T()
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
    
    servoAngle = RobotApi.UBTEDU_ROBOTSERVO_T()
    servoAngle.SERVO17_ANGLE = 90
    RobotApi.ubtSetRobotServo(servoAngle,50)

    sleep(1)


if __name__ == '__main__':
    independent()
