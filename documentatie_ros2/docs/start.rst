Getting started
===============

Now that we have ROS2 installed and working (hopefully!) we can start building our project!

Introduction
------------

.. contents:: Table of Contents
   :depth: 2
   :local:

The target of this tutorial is to understand what nodes, topics and rosbags are and create a project that stores the data received by those node into a pandas dataframe.

What is ROS2?
^^^^^^^^^^^^^

``ROS2`` stands for "Robot Operating System 2" and is a free, open-source software development tool mainly used in robotics.

The purpose of ROS 2 is to offer a standard software platform to developers across industries that will carry them from research and prototyping through to deployment and production. ROS 2 builds on the success of ROS 1, which is used today in myriad robotics applications around the world.

What is a node?
^^^^^^^^^^^^^^^

``Nodes`` are processes that perform some computation or task. The nodes themselves are really software processes but with the capability to register with the ROS Master node and communicate with other nodes in the system. The ROS design idea is that each node is independent and interacts with other nodes using the ROS communication capability.

What is a topic?
^^^^^^^^^^^^^^^^

Some nodes provide information for other nodes, as a camera feed would do, for example. Such a node is said to publish information that can be received by other nodes. The information in ROS is called a topic. A topic defines the types of messages that will be sent concerning that topic.

The nodes that transmit data publish the topic name and the type of message to be sent. The actual data is published by the node. A node can subscribe to a topic and transmitted messages on that topic are received by the node subscribing.

Continuing with the camera example, the camera node can publish the image on the ``camera/image_raw topic``.

Image data from the ``camera/image_raw`` topic can be used by a node that shows the image on the computer screen. The node that receives the information is said to subscribe to the topic being published, in this case ``camera/image_raw``.


Creating our first ros2 project
-------------------------------

Creating the workspace
^^^^^^^^^^^^^^^^^^^^^^

In order to create a workspace we need a directory with the sole purpose of containing all the files required for ROS2 to work::

   mkdir ros2_ws
   cd ros2_ws

In that directory we want to create a source directory::

   mkdir src 
   cd src

Now, we can go back to the root



