Recording a rosbag
==================

.. contents:: Table of Contents
    :depth: 2
    :local:

In this chapter we'll understand what a rosbag is, how to use it and it's aplications.

What is a rosbag?
-----------------

A rosbag is a tool made by ROS that is mainly used for storing real-time data received in topics. It can be used to record multiple topics in the same time as well, keeping track of time using ``UNIX time``.

How to use it
-------------

Firstly, in order to record topics we actually need running publishers so why not use our publisher node that we've created earlier?

.. code-block::

    ros2 run <my_project_name> publisher /topic1 & \
    ros2 run <my_project_name> publisher /topic2 & \
    ros2 run <my_project_name> publisher /topic3

We can check if everything runs as planned by using::

    ros2 topic list

With this command you should see all the active topics.

Let's create a directory to store our rosbags::

    mkdir rosbags

.. note::

    Keep in mind that this directory can be created anywhere on you system and is not limited to this project!

Then browse inside it::

    cd rosbags

Now that we have 3 publishers on 3 different topics at the same time and out rosbag directory, we can start recording using::

    rosbag record -a

.. note::
    -a tells rosbag to record every topic that is currently being published in!

Wait for enough data to accumulate inside the rosbag(I recommend at least 1 minute) and then you can simply use ctrl+c on the terminal to stop recording.

Nice! Now that your out rosbag created you can check the info about it using::

    rosbag info <rosbag_name>

In the next guide we'll teach you how to read the stored data and append it to a pandas dataframe!






