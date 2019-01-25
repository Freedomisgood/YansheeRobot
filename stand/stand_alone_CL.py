import RobotApi 
import time 

def stand():
    RobotApi.ubtRobotInitialize()
    ret=RobotApi.ubtRobotConnect("SDK","1","127.0.0.1")
    if(0!=ret):
        print("return value:%d" % ret)
        exit(1)

    #control duoji
    servoAngle=RobotApi.UBTEDU_ROBOTSERVO_T()

    servoAngle.SERVO11_ANGLE= 80  # left angle
    RobotApi.ubtSetRobotServo(servoAngle,30)

    # Action : left arm -- yeah
    servoAngle.SERVO2_ANGLE= 20
    servoAngle.SERVO3_ANGLE= 10

    # Action : keep right arm straight
    servoAngle.SERVO4_ANGLE= 10
    servoAngle.SERVO5_ANGLE= 100
    servoAngle.SERVO6_ANGLE= 160

    # Action :stand alone
    servoAngle.SERVO9_ANGLE= 95  # left knee
    servoAngle.SERVO10_ANGLE= 90  # left leg

    servoAngle.SERVO16_ANGLE= 75  # left angle
    servoAngle.SERVO12_ANGLE= 80  # right body
    servoAngle.SERVO7_ANGLE= 80   # left body

    # set 
    RobotApi.ubtSetRobotServo(servoAngle,100)

    # left leg detail
    servoAngle.SERVO13_ANGLE= 145
    RobotApi.ubtSetRobotServo(servoAngle,50)
    servoAngle.SERVO14_ANGLE= 140
    RobotApi.ubtSetRobotServo(servoAngle,50)
    servoAngle.SERVO15_ANGLE= 150
    RobotApi.ubtSetRobotServo(servoAngle,50)
    time.sleep(0.5)

    #---------------------



    # play an action
    RobotApi.ubtSetRobotMotion("come on","left",2,1)
    # cut

    time.sleep(1)

        
    servoAngle=RobotApi.UBTEDU_ROBOTSERVO_T()


    servoAngle.SERVO13_ANGLE= 120
    servoAngle.SERVO14_ANGLE= 105
    servoAngle.SERVO15_ANGLE= 70
    servoAngle.SERVO16_ANGLE= 90


    RobotApi.ubtSetRobotServo(servoAngle,100)

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

    RobotApi.ubtSetRobotServo(servoAngle,200)

    #oldservoAngle.SERVO9_ANGLE = 65
    #???

    #RobotApi.ubtSetRobotServo(servoAngle,40)
    print("done")

    RobotApi.ubtRobotDisconnect("SDK","1","127.0.0.1")
    RobotApi.ubtRobotDeinitialize()


if __name__ == '__main__':
    stand()