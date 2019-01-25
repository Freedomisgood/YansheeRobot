import RobotApi
from time import sleep

def myturn():
    ret=RobotApi.ubtStartRobotAction("myturn",1)
    RobotApi.ubtStartRobotAction("reset",1)

