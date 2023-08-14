#!/usr/bin/env python3

import argparse
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class publisherNode(Node):
    def __init__(self, topic: str):
        super().__init__("My_Publisher_NODE")
        self.get_logger().info("Publisher has been started!")
        self.topic = topic
        self.publisher_ = self.create_publisher(Twist, self.topic, 10)
        self.timer_ = self.create_timer(1, self.publishMessage) 
        self.counter_ = 0.00
        
    def publishMessage(self):
        msg = Twist()

        msg.linear.x = self.counter_
        msg.linear.y = self.counter_ + 2.00
        msg.linear.z = self.counter_ + 4.00

        msg.angular.x = self.counter_ + 1.00
        msg.angular.y = self.counter_ + 3.00
        msg.angular.z = self.counter_ + 5.00

        self.publisher_.publish(msg)
        self.counter_ += 1.00

        if self.counter_ >= 35.00:
            self.counter_ = 0.00
         

def main(args = None):
    rclpy.init(args = args)

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="topic name")
    args = parser.parse_args()

    node = publisherNode(str(args.input))
    rclpy.spin(node)

    rclpy.shutdown()

