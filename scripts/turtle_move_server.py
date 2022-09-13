#!/usr/bin/env python3

from final.srv import *
from geometry_msgs.msg import Twist
import math
import rospy
import sys
import os

def move_square(lin_vel):

    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(5) # 5hz
 
    while not rospy.is_shutdown():
        vel = Twist()
        vel.linear.x = lin_vel 
        vel.linear.y = 0
        vel.linear.z = 0
        for i in range(10): # 10 * 5hz = 2sec
            pub.publish(vel)
            rate.sleep()

        vel = Twist()
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = (math.pi / 4) #45 deg/s * 2sec = 90degree
        for i in range(10): # 10 * 5hz = 2sec
            pub.publish(vel)
            rate.sleep()

def move_triangle(lin_vel):
    
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(5) # 3hz
 
    while not rospy.is_shutdown():
        vel = Twist()
        vel.linear.x = lin_vel
        vel.linear.y = 0
        vel.linear.z = 0
        for i in range(10): # 10 * 5hz = 2sec
            pub.publish(vel)
            rate.sleep()

        vel = Twist()
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = ((math.pi)/3) # 60 deg/s * 2sec = 120 degrees
        for i in range(10): # 10 * 5hz = 2sec
            pub.publish(vel)
            rate.sleep()

def move_circle(lin_vel, ang_vel):

    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10) # 10hz
 
    vel = Twist()
    while not rospy.is_shutdown():
        
        vel.linear.x = lin_vel
        vel.linear.y = 0
        vel.linear.z = 0

        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = ang_vel

        pub.publish(vel)

        rate.sleep()

def move_teleop():
    os.system('rosrun turtlesim turtle_teleop_key')

def handle_move_turtle(req):
    if req.data == 'square':
        print("%s를 그리는 중..."%req.data)
        move_square(req.lin_vel)
        return TurtleMoveResponse(1)
    elif req.data == 'triangle':
        print("%s를 그리는 중..."%req.data)
        move_triangle(req.lin_vel)
        return TurtleMoveResponse(2)
    elif req.data == 'circle':
        print("%s를 그리는 중..."%req.data)
        move_circle(req.lin_vel, req.ang_vel)
        return TurtleMoveResponse(3)
    else: 
        print("당신의 상상력을 믿습니다.")
        move_teleop()
        return TurtleMoveResponse(4)


def move_turtle_server():
    rospy.init_node('move_turtle_server')
    s = rospy.Service('move_turtle', TurtleMove, handle_move_turtle)
    print("ㄹㅇ 찐막 안되면 걍 ㄴ트북 부심\n ***Distance 값은 0 - 2.5 값을 추천합니다***")
    rospy.spin()

if __name__ == "__main__":
    move_turtle_server()
