#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

class turtleControllerNode(Node):
    def __init__(self):
        super().__init__("My_turtle_controller")
        self.cmd_vel_publisher_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.get_logger().info("Turtle Controller has been started")
        self.pose_sub_ = self.create_subscription(Pose, "turtle1/pose", self.pose_callback, 10)

    def pose_callback(self, msg: Pose):
        cmd = Twist()
        if msg.x > 9.00 or msg.x < 2.00 or msg.y > 9.00 or msg.y < 2.00:
            cmd.linear.x = 1.00
            cmd.angular.z = 0.90
        
        else:
            cmd.linear.x = 8.00
            cmd.angular.z = 0.00
        
        
        self.cmd_vel_publisher_.publish(cmd)

def main(args = None):
    rclpy.init(args = args)
    node = turtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()