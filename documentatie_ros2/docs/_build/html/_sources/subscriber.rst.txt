Making a ros2 subscriber
=========================


.. code-block:: python

	class Subscriber(Node):

- The code defines a Python class called `Subscriber`. This class is derived from the `Node` class, which allows it to function as a ROS2 node.

Initialization Method
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

	def __init__(self, topic: str):

- Within the `Subscriber` class, the `__init__` method serves as the constructor. It is called when you create an instance of the class. This method accepts one argument, `topic`, which represents the ROS2 topic to subscribe to.

.. code-block:: python

	super().__init__("subscriber")

- This line invokes the constructor of the parent class, `Node`, to initialize the ROS2 node. The argument `"subscriber"` is the name of the node.

Callback Function
~~~~~~~~~~~~~~~~

.. code-block:: python

	def pose_callback(self, msg: Twist):

- The `pose_callback` method is a callback function that is executed whenever a new message is received on the subscribed ROS2 topic. This method accepts one argument, `msg`, which is a `Twist` message containing linear and angular velocities.

.. code-block:: python

	self.get_logger().info("Transfered")

- Within the callback, this line logs a message to the console indicating that a message has been received. It uses the `get_logger()` method to access the logger associated with the ROS2 node.

.. code-block:: python

	row = {"TOPIC": self.topic, "LX": msg.linear.x, "LY": msg.linear.y, "LZ": msg.linear.z, "AX": msg.angular.x, "AY": msg.angular.y, "AZ": msg.angular.z, 'msg': msg}

- This line constructs a dictionary called `row` that contains various fields extracted from the received `Twist` message. It includes information such as the topic name, linear and angular velocities, and the original message itself.

.. code-block:: python

	self.df.loc[len(self.df)] = row

- This line appends the `row` dictionary to a Pandas DataFrame called `df`. The DataFrame is used to accumulate and store data from received messages.

.. code-block:: python

	print(self.df.to_string())

- Here, the code prints the entire DataFrame to the console, displaying the collected data for debugging and monitoring purposes.

.. code-block:: python

	self.df.to_csv()

- Finally, this line saves the DataFrame to a CSV file. However, it's important to note that this line may produce an error because the `to_csv()` method requires specifying the CSV file path. You should provide a valid file path to save the data properly.

Main Function
~~~~~~~~~~~~~

.. code-block:: python

	def main(args=None):
	    rclpy.init(args=args)
	    parser = argparse.ArgumentParser(description=__doc__)
	    parser.add_argument("input", help="add topic")
	    args = parser.parse_args()
	    node = Subscriber(str(args.input))
	    rclpy.spin(node)
	    rclpy.shutdown()

- The `main` function serves as the entry point for the script.

.. code-block:: python

	rclpy.init(args=args)

- This line initializes the ROS2 client library using `rclpy.init()`. The `args` parameter allows you to pass command-line arguments to ROS2, if necessary.

.. code-block:: python

	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("input", help="add topic")
	args = parser.parse_args()

- Here, an argument parser is set up to handle command-line arguments. It expects one argument, `"input"`, which represents the topic name.

.. code-block:: python

	node = Subscriber(str(args.input))

- An instance of the `Subscriber` class is created, passing the specified topic name as an argument.

.. code-block:: python

	rclpy.spin(node)

- The script enters the ROS2 spin loop using `rclpy.spin(node)`. This loop allows the node to continuously listen for and process incoming messages.

.. code-block:: python

	rclpy.shutdown()

- After the spin loop is terminated (e.g., when you manually stop the script), `rclpy.shutdown()` is called to gracefully shut down the ROS2 node.

Final result
~~~~~~~~~~~~~

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

Execution
---------

To execute this script, follow these steps:

1. Run the script from the command line, providing the desired ROS2 topic as an argument:

.. code-block:: console

	python script_name.py topic_name

   Replace `script_name.py` with the actual name of your Python script, and `topic_name` with the name of the ROS2 topic you want to subscribe to.

2. The script will subscribe to the specified ROS2 topic and start recording incoming messages' data.

3. It will log messages to the console, including the data received from the subscribed topic.

4. The script will also save the recorded data to a CSV file for further analysis.

.. note:: Ensure that you have the necessary ROS2 packages and dependencies installed for the script to work correctly. Additionally, consider providing a valid file path when saving the data to a CSV file in the `pose_callback` method.

Add an entry point
~~~~~~~~~~~~~~~~~~~~~~

Reopen ``setup.py`` and add the entry point for the subscriber node below the publisher's entry point.
The ``entry_points`` field should now look like this:

.. code-block:: python

	entry_points={
	  'console_scripts': [
		  'talker = py_pubsub.publisher_member_function:main',
		  'listener = py_pubsub.subscriber_member_function:main',
	  ],
	},

Make sure to save the file, and then your pub/sub system should be ready.

Build and run
^^^^^^^^^^^^^^^

You likely already have the ``rclpy`` and ``std_msgs`` packages installed as part of your ROS 2 system.
It's good practice to run ``rosdep`` in the root of your workspace (``ros2_ws``) to check for missing dependencies before building:

.. tabs::

   .. group-tab:: Linux

      .. code-block:: console

        rosdep install -i --from-path src --rosdistro {DISTRO} -y

   .. group-tab:: macOS

      rosdep only runs on Linux, so you can skip ahead to next step.

   .. group-tab:: Windows

      rosdep only runs on Linux, so you can skip ahead to next step.


Still in the root of your workspace, ``ros2_ws``, build your new package:

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

      colcon build --packages-select py_pubsub

  .. group-tab:: macOS

    .. code-block:: console

      colcon build --packages-select py_pubsub

  .. group-tab:: Windows

    .. code-block:: console

      colcon build --merge-install --packages-select py_pubsub

Open a new terminal, navigate to ``ros2_ws``, and source the setup files:

.. tabs::

  .. group-tab:: Linux

    .. code-block:: console

      source install/setup.bash

  .. group-tab:: macOS

    .. code-block:: console

      . install/setup.bash

  .. group-tab:: Windows

    .. code-block:: console

      call install/setup.bat

Now run the talker node:

.. code-block:: console

	ros2 run py_pubsub talker

The terminal should start publishing info messages every 0.5 seconds, like so:

.. code-block:: console

  [INFO] [minimal_publisher]: Publishing: "Hello World: 0"
  [INFO] [minimal_publisher]: Publishing: "Hello World: 1"
  [INFO] [minimal_publisher]: Publishing: "Hello World: 2"
  [INFO] [minimal_publisher]: Publishing: "Hello World: 3"
  [INFO] [minimal_publisher]: Publishing: "Hello World: 4"
  ...

Open another terminal, source the setup files from inside ``ros2_ws`` again, and then start the listener node:

.. code-block:: console

	ros2 run py_pubsub listener

The listener will start printing messages to the console, starting at whatever message count the publisher is on at that time, like so:

.. code-block:: console

  [INFO] [minimal_subscriber]: I heard: "Hello World: 10"
  [INFO] [minimal_subscriber]: I heard: "Hello World: 11"
  [INFO] [minimal_subscriber]: I heard: "Hello World: 12"
  [INFO] [minimal_subscriber]: I heard: "Hello World: 13"
  [INFO] [minimal_subscriber]: I heard: "Hello World: 14"

Enter ``Ctrl+C`` in each terminal to stop the nodes from spinning.
