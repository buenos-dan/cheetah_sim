#!/usr/bin/evn python
'''
send the same msg for stand.
'''

#created on: July 9,2019
#author    : buenos
#e-mail    : buenos@buaa.edu.cn

from __future__ import division
import rospy
from std_msgs.msg import Float64
from leg_control.legController import LegController
        
class Cheetah:
    def __init__(self):
        self.leg_names = ["LF","LB","RF","RB"]
        self.controllers = {name:LegController(name) for name in self.leg_names}

    def backflip(self):
        rospy.sleep(1)
        #prepare
        start_pos = {"LF":-300,"LB":-310,"RF":-300,"RB":-310}
        target_pos = {"LF":[73,0,-270],
                      "LB":[73,-30,-280],
                      "RF":[73,0,-270],
                      "RB":[73,-30,-280],}
        for i in range(50):
            for leg in self.controllers:
                target_pos[leg][2] += (target_pos[leg][2]-start_pos[leg])/50.
                self.controllers[leg].writeEndPos(target_pos[leg])
            rospy.sleep(0.02)

        #jump
        target_pos = {"LF":[73,0,-400],
                      "LB":[73,-30,-310],
                      "RF":[73,0,-400],
                      "RB":[73,-30,-310],}
        for leg in self.controllers:
            self.controllers[leg].writeEndPos(target_pos[leg])

        rospy.sleep(0.1)

        #shoutui
        start_pos = {"LF":-400,"LB":-310,"RF":-400,"RB":-310}
        target_pos = {"LF":[73,0,-280],
                      "LB":[73,-30,-280],
                      "RF":[73,0,-280],
                      "RB":[73,-30,-280],}
        for i in range(40):
            for leg in self.controllers:
                target_pos[leg][2] += (target_pos[leg][2]-start_pos[leg])/40.
                self.controllers[leg].writeEndPos(target_pos[leg])
            rospy.sleep(0.02)

        rospy.sleep(0.1)

        #stand
        start_pos = {"LF":-280,"LB":-280,"RF":-280,"RB":-280}
        target_pos = {"LF":[73,0,-300],
                      "LB":[73,-30,-310],
                      "RF":[73,0,-300],
                      "RB":[73,-30,-310],}
        for i in range(1000):
            for leg in self.controllers:
                target_pos[leg][2] += (target_pos[leg][2]-start_pos[leg])/1000.
                self.controllers[leg].writeEndPos(target_pos[leg])
            rospy.sleep(0.002)

        

    def run(self):
        self.backflip()


if __name__=="__main__":
    node = rospy.init_node("control_node",anonymous=True)
    cheetah = Cheetah()
    cheetah.run()
