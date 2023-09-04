#!/usr/bin/env python3

import argparse
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import random

class publisherNode(Node):
    def __init__(self, topic: str):
        super().__init__("My_Publisher_NODE")
        self.get_logger().info("Publisher has been started!")
        self.topic = topic
        self.publisher_ = self.create_publisher(Twist, self.topic, 10)
        self.timer_ = self.create_timer(1, self.publishMessage)

    def publishMessage(self):
        msg = Twist()

        msg.linear.x = random.random() + random.randint(10, 99)
        msg.linear.y = random.random() + random.randint(10, 99)
        msg.linear.z = random.random() + random.randint(10, 99)

        msg.angular.x = random.random() + random.randint(10, 99)
        msg.angular.y = random.random() + random.randint(10, 99)
        msg.angular.z = random.random() + random.randint(10, 99)

        self.publisher_.publish(msg)

def main(args = None):
    rclpy.init(args = args)

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="topic name")
    args = parser.parse_args()

    node = publisherNode(str(args.input))
    rclpy.spin(node)

    rclpy.shutdown()