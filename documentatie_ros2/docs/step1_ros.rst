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

Inside it place this code:

.. literalinclude:: ../src/scripts/talker.py
    :language: python

