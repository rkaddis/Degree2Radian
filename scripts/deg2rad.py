#!/usr/bin/env python3
import rospy
import math
from std_msgs.msg import Float32

def receive_angle_cb(deg):
    multiple = Float32()
    multiple.data = (math.pi/180)
    ang = deg.data * multiple.data
    rospy.loginfo(f"{deg} -> {ang}")

if __name__ == '__main__':
    rospy.init_node('deg2rad')
    sub = rospy.Subscriber('/angle', Float32, receive_angle_cb)
    rospy.spin()