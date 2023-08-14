#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class drawCircle(Node):
    def __init__(self):
        super().__init__("draw_circle")
        self.cmv_vel_pub_1 = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)

        self.timer_ = self.create_timer(0.5, self.sentVelocity)
        self.get_logger().info("Draw circle node has been started")

    def sentVelocity(self):
        msg = Twist()
        msg.linear.x = 1.0
        msg.angular.z = 2.0
        self.cmv_vel_pub_1.publish(msg)

def main(args = None):
    rclpy.init(args = args)
    node = drawCircle()
    rclpy.spin(node)
    rclpy.shutdown()