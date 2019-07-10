#!/usr/bin/evn python
'''
    main controller for the cheetah
'''
#created on: July 9,2019
#author    : buenos
#e-mail    : buenos@buaa.edu.cn

import sys,time
sys.path.append("./lib")
import rospy
from std_msgs.msg import Float64
import numpy as np
from settings import *

class LegController:
	def __init__(self,name):
		self.name = name
		self.jointControllers = [rospy.Publisher("/cheetah/"+self.name+"_joint"+str(i+1)+"_position_controller/command",Float64,queue_size=10) for i in xrange(3)]

	
	def writePosMsg(self):
		pass
	
	def setJointPosInDeg(self,index,val):
		msg = Float64(val/180.0*PI)
		self.jointControllers[index].publish(msg)
		
		
		
class Cheetah:
	def __init__(self):
		self.name = "mini_cheetah"
		self.leg_names = ["LF","LB","RF","RB"]
		self.node = rospy.init_node("control_node",anonymous=True)
		self.legControllers = {name:LegController(name) for name in self.leg_names}

	def stand(self):
		offset = {"LF":(0.0   ,1.0   ,1.0),
				  "LB":(0.0   ,25.0  ,-0.0),
				  "RF":(0.0   ,-1.0  ,-1.0),
				  "RB":(0.0   ,-25.0 ,0.0),}
		for leg in self.legControllers:
			for i in range(3):
				self.legControllers[leg].setJointPosInDeg(i,offset[leg][i])


	def run(self):
		while not rospy.is_shutdown():
			self.stand()
			time.sleep(0.01)
		pass


if __name__=="__main__":
	cheetah = Cheetah()
	cheetah.run()
