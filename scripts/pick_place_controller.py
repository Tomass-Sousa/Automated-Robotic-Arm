#!/usr/bin/env python3

import rospy
import moveit_commander
from geometry_msgs.msg import PointStamped, Pose

class PickPlaceController:
    def __init__(self):
        rospy.init_node('pick_place_controller')
        moveit_commander.roscpp_initialize([])
        self.arm = moveit_commander.MoveGroupCommander("manipulator")
        rospy.Subscriber('/detected_object_position', PointStamped, self.pick_object)
        rospy.loginfo("Pick & Place controller ready.")
        rospy.spin()

    def pick_object(self, msg):
        target = Pose()
        target.position.x = msg.point.x
        target.position.y = msg.point.y
        target.position.z = 0.05
        target.orientation.w = 1.0  # Point down
        self.arm.set_pose_target(target)
        plan = self.arm.go(wait=True)
        self.arm.stop()
        self.arm.clear_pose_targets()

        # Example place
        place_pose = self.arm.get_current_pose().pose
        place_pose.position.y += 0.2
        self.arm.set_pose_target(place_pose)
        self.arm.go(wait=True)
        self.arm.stop()
