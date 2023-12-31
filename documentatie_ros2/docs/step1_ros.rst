Basic talker tutorial
=====================

Now that we have our setup complete, we can start experimenting with the tools ``ROS2`` has to offer.

.. contents:: Table of Contents
   :depth: 2
   :local:

Creating a talker using python 
------------------------------

What is a talker?
^^^^^^^^^^^^^^^^^

A talker node is used to send data to a ``topic``. This data can be sensor values, commands, camera frames, etc..

In order to create one we need to go inside our project directory that we've built in the previous chapter.

Inside that directory we'll find some configuration files that we will discuss later in this tutorial and another directory named exactly like the package name.

Inside that directory we want to create our python script::

    touch talker.py && chmod 700 talker.py

Now you can use any code editor you preffer. I recommend ``VSCode``::

    code talker.py

Full code
^^^^^^^^^

Inside it place this code:

.. literalinclude:: ../src/scripts/talker.py
    :language: python

Explaining the code
^^^^^^^^^^^^^^^^^^^

Now let's make a quick walktrough:

For every ``node`` in ROS2 you need to specify the path of the interpretter.

.. literalinclude:: ../src/scripts/talker.py
    :language: python
    :lines: 1

``Argparse`` is a built-in python library that enables a script to receive arguments directly from a console.

``rclpy`` is the main library that we'll use for ROS.

``rclpy.node.Node`` is a class from rclpy that we will inherit every time we want to build a node, this will give us tons of tools that can be easily implemented in out code.

``geometry_msgs`` is a library from ROS that contains many classes with the purpose of storing a specific message.

``Twist`` is a message type that we we'll send over to a topic below.

``random`` is another python built-in module that helps us generate random numbers, we'll use it to create unique messages to send


.. literalinclude:: ../src/scripts/talker.py
    :language: python
    :lines: 3-7

The first step in creating a node is inheriting the Node class mentioned above and using the ``super()`` method. 

The text inside the super() method is what will the node be seen as inside rqt_graph

Line 4 is the message the node will return on the terminal if it has started succesfully.

When runnning the node, we will use the topic name we want to assign as an argument that we'll use below.

``self.publisher_`` is an object that we'll use to send Twist type messages in the ``self.topic``
topic while "10" is the queue size for the output buffer, "10" is the most commonly used value.

``self.timer_`` is an object that will call a chosen function every "1" second.


.. literalinclude:: ../src/scripts/talker.py
    :language: python
    :lines: 9-15

``msg`` will be the message that we want to send, we declare it as an object of the Twist() class

``Twist()`` has 6 internal variables that we can use as messages: linear and angualar velocities for every axis

We edit those using the ``random`` module to generate unique numbers

After that, we use the .publish method of our ``self.publisher_`` object we created earlier to send the message in the topic

.. literalinclude:: ../src/scripts/talker.py
    :language: python
    :lines: 17-28

This is the main function. This is the function that ROS will call in order to activate the node.

``rclpy.init()`` and ``rclpy.shutdown()`` are 2 functions that need to be called every single time you want to start a node of any kind in ROS and
and they must be placed at the beginning and at the end of the main function.

Next, we'll use argparse to create a parser for the input, which will be the name of the target topic in our case.

We initialize an object of our class we've just created and send the topic name as an argument for it.

``rclpy.spin()`` is a function that makes the node keep working after the first iteration until we manually close it.


.. literalinclude:: ../src/scripts/talker.py
    :language: python
    :lines: 30-40

Adding dependencies to the ROS package
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the ``src/"your_package_name"`` you will find a file named ``package.xml``, open it:

Inside the file there is a section that has ``<depend></depend>`` tags.

You want to add the following dependencies::

    <depend>random</depend>
    <depend>rclpy</depend>
    <depend>geometry_msgs</depend>
    <depend>argparse</depend>

Now save and close the file.

Editing the entry points in setup.py
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the same directory you will find a file named setup.py, open it.

At the bottom of the code you should have the ``entry_points``.

In ``console_scripts add the following line``::

    "publisher = my_package_name.my_publisher_file_name:main"

Replace ``my_package_name`` with the name you have chosen for your ROS project name
and ``my_publisher_file_name`` with the name of the file your publisher code is.

It should look like this::

    entry_points={
        'console_scripts':[
            "publisher = my_package.publisher:main"
        ],
    },

Keep in mind that "publisher" is the name of the executable we will use to call this node.

Building and running the node
-----------------------------

Now that everything has been coded, all we have to do is to go back into our ``src`` directory
and execute this command::

    colcon build --symlink-install

Using ``--symlink-install`` is not mandatory, but if you use it, you won't have to build the project everytime you modify the code of this node.
(you still have to rebuild it if you add another node)

Now in order to run it you need to use this command::

    ros2 run <my_package_name> <executable_name> <topic_name>

In order to see the messages that are being sent, use the following command inside another terminal::

    ros2 topic echo <topic_name>

You can also visualize the node and the topic using::

    rqt_graph

And::

    ros2 topic list














