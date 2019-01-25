import RobotApi
from time import sleep
def stand():
    servoAngle=RobotApi.UBTEDU_ROBOTSERVO_T()

    servoAngle.SERVO1_ANGLE=90
    RobotApi.ubtSetRobotServo(servoAngle,100)
    servoAngle.SERVO2_ANGLE=139
    RobotApi.ubtSetRobotServo(servoAngle,100)
    servoAngle.SERVO3_ANGLE=165
    RobotApi.ubtSetRobotServo(servoAngle,100)
    servoAngle.SERVO4_ANGLE=88
    RobotApi.ubtSetRobotServo(servoAngle,100)
    servoAngle.SERVO5_ANGLE=39
    RobotApi.ubtSetRobotServo(servoAngle,100)
    servoAngle.SERVO6_ANGLE=15
    RobotApi.ubtSetRobotServo(servoAngle,100)
    servoAngle.SERVO7_ANGLE=94
    RobotApi.ubtSetRobotServo(servoAngle,100)
    servoAngle.SERVO8_ANGLE=70
    RobotApi.ubtSetRobotServo(servoAngle,100)
    servoAngle.SERVO9_ANGLE=65
    RobotApi.ubtSetRobotServo(servoAngle,100)
    servoAngle.SERVO10_ANGLE=125
    RobotApi.ubtSetRobotServo(servoAngle,100)
    servoAngle.SERVO11_ANGLE=77
    RobotApi.ubtSetRobotServo(servoAngle,100)
    servoAngle.SERVO12_ANGLE=116
    RobotApi.ubtSetRobotServo(servoAngle,100)
    servoAngle.SERVO13_ANGLE=105
    RobotApi.ubtSetRobotServo(servoAngle,100)
    servoAngle.SERVO14_ANGLE=148
    RobotApi.ubtSetRobotServo(servoAngle,100)
    servoAngle.SERVO15_ANGLE=69
    RobotApi.ubtSetRobotServo(servoAngle,100)
    servoAngle.SERVO16_ANGLE=88
    RobotApi.ubtSetRobotServo(servoAngle,100)
    servoAngle.SERVO17_ANGLE=89
    RobotApi.ubtSetRobotServo(servoAngle,100)
    sleep(2)

    servoAngle.SERVO1_ANGLE=90
    RobotApi.ubtSetRobotServo(servoAngle,100)
    servoAngle.SERVO2_ANGLE=90
    RobotApi.ubtSetRobotServo(servoAngle,100)
    servoAngle.SERVO3_ANGLE=90
    RobotApi.ubtSetRobotServo(servoAngle,100)
    servoAngle.SERVO4_ANGLE=90
    RobotApi.ubtSetRobotServo(servoAngle,100)
    servoAngle.SERVO5_ANGLE=90
    RobotApi.ubtSetRobotServo(servoAngle,100)
    servoAngle.SERVO6_ANGLE=90
    RobotApi.ubtSetRobotServo(servoAngle,100)
    sleep(2.5)


    RobotApi.ubtStartRobotAction("reset",1)

