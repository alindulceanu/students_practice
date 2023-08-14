#!/usr/bin/env python3

import argparse
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import pandas as pd
from rclpy.serialization import serialize_message


class subscriberNode(Node):
    def __init__(self, topic: str):
        super().__init__("My_subscriber_node")
        self.topic = topic
        
        self.df = pd.DataFrame(columns=["TOPIC", "linX", "linY", "linZ", "angX", "angY", "angZ"])

        self.subscriber_ = self.create_subscription(Twist, self.topic, self.printMessage, 10)       # Initializing subscriber object

    def printMessage(self, msg: Twist):                                             # Callback function
        self.get_logger().info("Received")

        new_row = {"TOPIC": self.topic, "linX": msg.linear.x, "linY": msg.linear.y, "linZ": msg.linear.z, "angX": msg.angular.x, "angY": msg.angular.y, "angZ": msg.angular.z}
        self.df.loc[len(self.df)] = new_row

        print(self.df.to_string())

        self.df.to_csv("~/ros2_ws/src/my_robot_controller/data.csv")



def main(args = None):
    rclpy.init(args = args)

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="add topic")

    args = parser.parse_args()

    node = subscriberNode(str(args.input))
    rclpy.spin(node)

    rclpy.shutdown()

if __name__ == "__main__":
    main()


#def memorize_communication()
#    return df 

#def return_frame_data(df, x)
#    return dataframe (x)

#hdf5