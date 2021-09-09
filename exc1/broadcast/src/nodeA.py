#!/usr/bin/env python2

import rospy
from std_msgs.msg import Float32

def nodeA():
    pub = rospy.Publisher('/vdovec',Float32, queue_size= 20)
    
    rate = rospy.Rate(20) #hz

    k = 1
    n = 4
    while not rospy.is_shutdown():

       #rospy.loginfo(k)
       pub.publish(k)
       k += n
       rate.sleep()

if __name__ == '__main__':

    rospy.init_node("nodeA")

    nodeA()
