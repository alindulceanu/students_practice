#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class publisherNode(Node):
    def __init__(self):
        super().__init__("My_Publisher_NODE")
        self.publisher_ = self.create_publisher(String, "/myTopic", 10)
        self.timer_ = self.create_timer(1, self.publishMessage) 
        self.counter_ = 0
        
    def publishMessage(self):
        msg = String()
        msg.data = "Buna, cf  " + str(self.counter_)
        self.publisher_.publish(msg)
        self.counter_ += 1
         

def main(args = None):
    rclpy.init(args = args)
    node = publisherNode()
    rclpy.spin(node)
    rclpy.shutdown()

