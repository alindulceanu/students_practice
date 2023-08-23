Making a ros2 subscriber
=========================

.. code-block:: python

	#!/usr/bin/env python3
	import rclpy
	from rclpy.node import Node
	from geometry_msgs.msg import Twist
	import random
	import argparse
	import pandas as pd

	class Subscriber(Node):

	    def __init__(self, topic:str):
		super().__init__("subscriber")
		self.topic = topic
		self.df=pd.DataFrame(columns=["TOPIC","LX", "LY", "LZ", "AX", "AY", "AZ"])
		self.subscriber = self.create_subscription(Twist, self.topic, self.pose_callback, 10)

	    def pose_callback(self, msg: Twist):
		self.get_logger().info("Transfered")
		row={"TOPIC": self.topic, "LX": msg.linear.x, "LY": msg.linear.y, "LZ": msg.linear.z, "AX": msg.angular.x, "AY": msg.angular.y, "AZ": msg.angular.z, 'msg':msg}
		self.df.loc[len(self.df)]=row
		print(self.df.to_string())
		self.df.to_csv()

	def main(args=None):
	    rclpy.init(args=args)
	    parser = argparse.ArgumentParser(description=__doc__)
	    parser.add_argument("input", help="add topic")
	    args = parser.parse_args()
	    node = Subscriber(str(args.input))
	    rclpy.spin(node)
	    rclpy.shutdown()

	if __name__ == '__main__':
	    main()
