#!/usr/bin/env python2

import rospy
from std_msgs.msg import Float32


result = 0
q = 0.15

def callback(data):
    global result, q
    
    result = data.data/q
    #rospy.loginfo(result)

def nodeB():

    rospy.Subscriber("/vdovec", Float32, callback)
    rate = rospy.Rate(20) #hz
    pub = rospy.Publisher("/kthfs/result", Float32, queue_size= 20)

    while not rospy.is_shutdown():

       pub.publish(result)
       rate.sleep()
    

    rospy.spin()

    
if __name__ == '__main__':

    rospy.init_node('nodeB', anonymous= True)

    nodeB()

