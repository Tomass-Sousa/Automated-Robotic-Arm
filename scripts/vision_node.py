#!/usr/bin/env python3

import rospy
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from geometry_msgs.msg import PointStamped

class VisionNode:
    def __init__(self):
        rospy.init_node('vision_node')
        self.bridge = CvBridge()
        self.pub = rospy.Publisher('/detected_object_position', PointStamped, queue_size=10)
        rospy.Subscriber('/camera/rgb/image_raw', Image, self.image_callback)
        rospy.loginfo("Vision node started.")
        rospy.spin()

    def image_callback(self, msg):
        image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        # Red object detection
        mask = cv2.inRange(hsv, (0, 150, 50), (10, 255, 255))
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        if contours:
            c = max(contours, key=cv2.contourArea)
            (x, y), _ = cv2.minEnclosingCircle(c)
            point = PointStamped()
            point.header.stamp = rospy.Time.now()
            point.header.frame_id = "camera_link"
            point.point.x = float(x) / 100  # Scale as placeholder
            point.point.y = float(y) / 100
            point.point.z = 0.1
            self.pub.publish(point)
