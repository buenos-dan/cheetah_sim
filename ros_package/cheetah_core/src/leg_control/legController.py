#!/usr/bin/env python

#created on: July 14,2019
#author    : buenos
#e-mail    : buenos@buaa.edu.cn

import sys,math,time
sys.path.append("../")
import rospy
from std_msgs.msg import Float64
from lib.InverseKinematics import inverseKinematics
from lib.settings import *

class LegController(object):
    def __init__(self,name):
        self.name = name
        self.joint_name = ["hip","thigh","calf"]
        self.offset = JOINT_OFFSET[self.name]
        self.pos_puber = [self._instancePuber(index) for index in range(3)]
        pass

    def _instancePuber(self,index):
        topic = "/cheetah/"+self.name+"_joint"+str(index+1)+"_position_controller/command"
        pub = rospy.Publisher(topic,Float64,queue_size=5)
        return pub

    def _writeJointPosInDeg(self,index,deg):
        rad = math.radians(deg)+self.offset[index]
        msg = Float64(rad)
        self.pos_puber[index].publish(msg)

    def _writeJointPosInRad(self,index,rad):
        rad = rad+self.offset[index]
        msg = Float64(rad)
        self.pos_puber[index].publish(msg)
        
    def writeEndPos(self,EndPos):
        alpha = inverseKinematics(EndPos)
        for i in range(3):
            self._writeJointPosInRad(i,alpha[i])


if __name__=="__main__":
    lc = LegController("RF")
    for i in range(10):
        lc.writeEndPos([72.20,0.,-300.])
        time.sleep(0.1)
    print "hello world"
