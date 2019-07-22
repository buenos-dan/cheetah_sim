#!/usr/bin/env python
from __future__ import division
import math
from settings import *

def inverseKinematics(EndPos):
    '''
        input : (x , y, z)
        output: (alpha1, alpha2, alpha3)
    '''
    x = EndPos[0]
    y = EndPos[1]
    z = EndPos[2]
    l1 = LEG_LENGTH["hip"]
    l2 = LEG_LENGTH["thigh"]
    l3 = LEG_LENGTH["calf"]
    
    #XOZ                      ():point      []:line      <>:angle
    #               |Z        
    #               |         
    #         p1    |         p2 = (x,y,z)
    #          *    |         [p0,p1] = l1
    #  X____________|____     line1 = [p0,p2] = sqrt(x**2 + z**2)
    #               |p0       <p0,p1,p2> = PI/2
    #               |         beta1 = <p2,p0,X >
    #               |         beta2 = <p2,p0,p1>
    #      *        |
    #      p2       |
    beta1 = math.atan2(-z,x)
    line1 = math.sqrt(x**2+z**2)
    beta2 = math.acos(l1/line1)
    alpha1 = beta2 - beta1

    #YOZ'                     ():point      []:line      <>:angle
    #            |Z'       
    #  __________|______Y     p2 = (x,y,z')
    #            |p0          [p0,p1] = l2
    #            |            [p1,p2] = l3
    #     p1*    |
    #            |            beta1 = <p2,p0,-Z'>          
    #            |            line1 = [p2,p0] = sqrt(y**2 + z'**2)
    #            | *p2
    #            |
    z_ = math.sqrt(x**2 + z**2 - l1**2) 
    beta1 = math.atan2(y,z_)
    line1 = math.sqrt(y**2 + z_**2)
    beta2 = math.acos((l2**2+line1**2-l3**2)/(2*l2*line1))
    alpha2 = beta1 - beta2
    alpha3 = PI - math.acos((l2**2+l3**2-line1**2)/(2*l2*l3))

    return (alpha1,alpha2,alpha3)
    


if __name__=="__main__":
    pos = (80,-10,-300)
    print inverseKinematics(pos)

