#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from nav_msgs.msg import Odometry
 
def callback(data):
     rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def callback_p(msg):
     print msg.pose.pose
     
def listener():
 
     # In ROS, nodes are uniquely named. If two nodes with the same
     # name are launched, the previous one is kicked off. The
     # anonymous=True flag means that rospy will choose a unique
     # name for our 'listener' node so that multiple listeners can
     # run simultaneously.
     rospy.init_node('listener', anonymous=True)
 
     rospy.Subscriber("chatter", String, callback)
 
     # spin() simply keeps python from exiting until this node is stopped
     rospy.spin()

def pose():
     rospy.init_node('check_odometry')
     odom_sub = rospy.Subscriber('/odom', Odometry, callback_p)
     rospy.spin()
 
if __name__ == '__main__':
     listener()
     pose()
