#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class myNode(Node):
    def __init__(self):
        super().__init__("firstNode")
        self.get_logger().info("Hello from ROS2")

def main(args = None):
    rclpy.init(args = args)

    node = myNode()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__ == '__main__':
    main()

