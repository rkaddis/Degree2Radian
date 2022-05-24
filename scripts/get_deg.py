#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32

def get_angle():
    pub = rospy.Publisher('/angle', Float32, queue_size=10)
    rospy.init_node('get_deg', anonymous=True)
    angle = rospy.get_param("/degrees")
    rate = rospy.Rate(0.2)
    while not rospy.is_shutdown():
        pub.publish(angle)
        rate.sleep()

if __name__ == '__main__':
    try:
        get_angle()
    except rospy.ROSInterruptException:
        pass

