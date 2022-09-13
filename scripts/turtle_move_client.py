#!/usr/bin/env python3

import sys
import rospy
import os
import string
from final.srv import *

 

def move_turtle_client(x, y, z):
    rospy.wait_for_service('move_turtle')
    try:
        move_turtle = rospy.ServiceProxy('move_turtle', TurtleMove)
        resp = move_turtle(x, y, z)
        return resp
       
    except rospy.ServiceException as e:
        print ("Service call failed: %s"%e)

def usage():
    return "%s [x y z]"%sys.argv[0]


if __name__ == "__main__":
    print('Enter Mode : ')
    x = str(input())
    if x == "square":
        print('Distace : ')
        y = int(input())
        z = 0
    elif x == "triangle":
        print('Distance : ')
        y = int(input())
        z = 0
    elif x == "circle":
        print('Lin_vel, Ang_vel : ')
        y = int(input())
        z = int(input())
    else:
        x,y,z = 0
    move_turtle_client(x, y, z)
