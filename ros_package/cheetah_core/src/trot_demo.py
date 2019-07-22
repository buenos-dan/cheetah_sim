#!/usr/bin/evn python
'''
trot demo
'''

#created on: July 15,2019
#author    : buenos
#e-mail    : buenos@buaa.edu.cn

import math
import rospy
from std_msgs.msg import Float64
from rosgraph_msgs.msg import Clock
from leg_control.legController import LegController
        

class Cheetah:
    def __init__(self):
        self.leg_names = ["LF","LB","RF","RB"]
        self.controllers = {name:LegController(name) for name in self.leg_names}

    def trot(self,t=0):
        T = 0.6
        control_msg = {"RF":[0,  0,  0],
                       "RB":[0,  0,  0],
                       "LF":[0,  0,  0],
                       "LB":[0,  0,  0],}
        res_leg_param = {"RF":[200,-350,120,-270,-0.00],
                         "RB":[200,-350,120,-270,-0.00],
                         "LF":[200,-350,120,-270,-0.00],
                         "LB":[200,-350,120,-270,-0.00],}
        t1 = T*1./4.
        t2 = T*1./4.
        t3 = T*2./4.
        t = t % T
        if t < t1:
            x = -0.5*res_leg_param["RF"][0]+t/t1*(0.5*res_leg_param["RF"][0]+res_leg_param["RF"][2])
            y = ((res_leg_param["RF"][3]-res_leg_param["RF"][1])/(res_leg_param["RF"][2]+0.5*res_leg_param["RF"][0]))*(x+0.5*res_leg_param["RF"][0])+res_leg_param["RF"][1]
            control_msg["RF"] = [72.20,x,y]
            x = -0.5*res_leg_param["LB"][0]+t/t1*(0.5*res_leg_param["LB"][0]+res_leg_param["LB"][2])
            y = ((res_leg_param["LB"][3]-res_leg_param["LB"][1])/(res_leg_param["LB"][2]+0.5*res_leg_param["LB"][0]))*(x+0.5*res_leg_param["LB"][0])+res_leg_param["LB"][1]
            control_msg["LB"] = [72.20,x,y]
        elif (t-t1) < t2:
            x = res_leg_param["RF"][2]+(t-t1)/t2*(-res_leg_param["RF"][2]+0.5*res_leg_param["RF"][0])
            y = ((res_leg_param["RF"][3]-res_leg_param["RF"][1])/(res_leg_param["RF"][2]-0.5*res_leg_param["RF"][0]))*(x-0.5*res_leg_param["RF"][0])+res_leg_param["RF"][1]
            control_msg["RF"] = [72.20,x,y]
            x = res_leg_param["LB"][2]+(t-t1)/t2*(-res_leg_param["LB"][2]+0.5*res_leg_param["LB"][0])
            y = ((res_leg_param["LB"][3]-res_leg_param["LB"][1])/(res_leg_param["LB"][2]-0.5*res_leg_param["LB"][0]))*(x-0.5*res_leg_param["LB"][0])+res_leg_param["LB"][1]
            control_msg["LB"] = [72.20,x,y]
        elif (t-t1-t2)<t3:
            x = 0.5*res_leg_param["RF"][0]+(t-t1-t2)/t3*(-res_leg_param["RF"][0])
            y = res_leg_param["RF"][1]
            control_msg["RF"] = [72.20,x,y]
            x = 0.5*res_leg_param["LB"][0]+(t-t1-t2)/t3*(-res_leg_param["LB"][0])
            y = res_leg_param["LB"][1]
            control_msg["LB"] = [72.20,x,y]

        t_other = t + T/2.
        t_other = t_other%T
        if t_other < t1:
            x = -0.5*res_leg_param["LF"][0]+t_other/t1*(0.5*res_leg_param["LF"][0]+res_leg_param["LF"][2])
            y = ((res_leg_param["LF"][3]-res_leg_param["LF"][1])/(res_leg_param["LF"][2]+0.5*res_leg_param["LF"][0]))*(x+0.5*res_leg_param["LF"][0])+res_leg_param["LF"][1]
            control_msg["LF"] = [72.20,x,y]
            x = -0.5*res_leg_param["RB"][0]+t_other/t1*(0.5*res_leg_param["RB"][0]+res_leg_param["RB"][2])
            y = ((res_leg_param["RB"][3]-res_leg_param["RB"][1])/(res_leg_param["RB"][2]+0.5*res_leg_param["RB"][0]))*(x+0.5*res_leg_param["RB"][0])+res_leg_param["RB"][1]
            control_msg["RB"] = [72.20,x,y]
        elif (t_other-t1) < t2:
            x = res_leg_param["LF"][2]+(t_other-t1)/t2*(-res_leg_param["LF"][2]+0.5*res_leg_param["LF"][0])
            y = ((res_leg_param["LF"][3]-res_leg_param["LF"][1])/(res_leg_param["LF"][2]-0.5*res_leg_param["LF"][0]))*(x-0.5*res_leg_param["LF"][0])+res_leg_param["LF"][1]
            control_msg["LF"] = [72.20,x,y]
            x = res_leg_param["RB"][2]+(t_other-t1)/t2*(-res_leg_param["RB"][2]+0.5*res_leg_param["RB"][0])
            y = ((res_leg_param["RB"][3]-res_leg_param["RB"][1])/(res_leg_param["RB"][2]-0.5*res_leg_param["RB"][0]))*(x-0.5*res_leg_param["RB"][0])+res_leg_param["RB"][1]
            control_msg["RB"] = [72.20,x,y]
        elif (t_other-t1-t2)<t3:
            x = 0.5*res_leg_param["LF"][0]+(t_other-t1-t2)/t3*(-res_leg_param["LF"][0])
            y = res_leg_param["LF"][1]
            control_msg["LF"] = [72.20,x,y]
            x = 0.5*res_leg_param["RB"][0]+(t_other-t1-t2)/t3*(-res_leg_param["RB"][0])
            y = res_leg_param["RB"][1]
            control_msg["RB"] = [72.20,x,y]

        for leg in self.controllers:
            if leg == "RF" or leg == "LF":
                control_msg[leg][1] -= 60
                control_msg[leg][2] += 10
                pass
            else:
                control_msg[leg][1] -= 70
                control_msg[leg][2] -= 10
                pass
            self.controllers[leg].writeEndPos(control_msg[leg])

    def run(self):
        t = rospy.get_time()
        while not rospy.is_shutdown():
            self.trot(rospy.get_time() - t)
            rospy.sleep(0.01)


if __name__=="__main__":
    node = rospy.init_node("control_node",anonymous=True)
    cheetah = Cheetah()
    cheetah.run()
