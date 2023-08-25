Making a ros2 talker
=====================

.. code-block:: python

	#!/usr/bin/env python3
	import rclpy
	from rclpy.node import Node
	from geometry_msgs.msg import Twist
	import random
	import argparse

	class Randomiser(Node):

	    def __init__(self, topic:str):
		self.topic = topic
		super().__init__("Generator")
		self.cmd_vel_pub = self.create_publisher(Twist, self.topic, 10)
		self.get_logger().info("Generating...")
		self.counter = 0
		self.timer = self.create_timer(1.0, self.send_velocity_command)
	    
	    def send_velocity_command(self):
		msg = Twist()
		msg.linear.x = random.random() * random.randint(-10,10)
		msg.angular.x = random.random() * random.randint(-10,10)
		msg.linear.y = random.random() * random.randint(-10,10)
		msg.angular.y = random.random() * random.randint(-10,10)
		msg.linear.z = random.random() * random.randint(-10,10)
		msg.angular.z = random.random() * random.randint(-10,10)
		self.cmd_vel_pub.publish(msg)
		self.counter += 1 

	def main(args=None):
	    rclpy.init(args=args)
	    parser = argparse.ArgumentParser(description=__doc__)
	    parser.add_argument("input",help="topic name")
	    args = parser.parse_args()
	    node = Randomiser(str(args.input))
	    rclpy.spin(node)
	    rclpy.shutdown()

	if __name__ == '__main__':
	    main()
