Preparations
============

Installing Docker Desktop
**************************

First go to the official Docker Desktop page and download it:

https://www.docker.com/products/docker-desktop/

After installation test your Docker installation by running the following:

.. code-block:: console

	$ docker run hello-world

It should display this message:

.. code-block:: console

	Hello from Docker.
	This message shows that your installation appears to be working correctly.
	...

If you get an error:

.. code-block:: console

	docker: error during connect: this error may indicate that the docker daemon is not running:
	Post "<http://%2F%2F.%2Fpipe%2Fdocker_engine/v1.24/containers/create>":
	open //./pipe/docker_engine: The system cannot find the file specified.
	See 'docker run --help'.
	  
Make sure that you are running Docker.

Installing MobaXTerm
*********************

To install it simply download the installer and run it:

https://mobaxterm.mobatek.net/download.html

WSL Instalation
****************

.. contents:: Table of Contents
   :depth: 2
   :local:

``WSL2`` (Windows Subsystem for Linux) is a tool that allows you to use linux commands directly on your windows machine without using a VM.

WSL comes preinstalled in every windows system, but it is not activated. 

Installation
------------

In order to activate WSL2 in your machine you just need to type this command in CMD as administrator::

    wsl --install

This command will automatically choose Ubuntu as the defaul distro, if you want another linux distro do this instead::

    wsl --install -d <Distro_Name>

If you want to see a list of Distros that are available in the microsoft store, do the following::

    wsl -l -o 

Where -l stands for ``list`` and -o for ``online``


Setting up the linux user
-------------------------

Now that you have WSL2 installed, you will be asked to enter a UNIX user and password.

.. note::
    The credidentials you use do not need to be related to your windows account.

    When typing your password nothing will display on your screen. This is called blind typing and is completely normal.

    The username must be between one and eight characters long, must start with a lowercase letter or an underscore, it can contain lowercase letters, digits, underscores and dashes and can end with a dollar sign.
    
    In RegEx: ``[a-z_][a-z0-9_-]*[$]?``

    Passwords must be at least 8 characters long, they cannot be dictionary words or the same as the username, you also have to use at least 3 of 4 character sets: uppercase, lowercase, digits, symbols.

    Do not use spaces in your password!!

Now that your WSL2 setup is ready to go, don't forget to do::

    sudo apt update && sudo apt upgrade

once in a while

Installing Oracle VM VirtualBox and Extension Packs
****************************************************

Oracle VM VirtualBox comes in many different packages, and installation depends on your host OS. If you have installed software before, installation should be straightforward. On each host platform, Oracle VM VirtualBox uses the installation method that is most common and easy to use.

Oracle VM VirtualBox is split into the following components:

 * Base package. The base package consists of all open source components and is licensed under the GNU General Public License V2.

 * Extension packs. Additional extension packs can be downloaded which extend the functionality of the Oracle VM VirtualBox base package. Currently, Oracle provides a single extension pack, available from: http://www.virtualbox.org. The extension pack provides the following added functionality:

	 * VirtualBox Remote Desktop Protocol (VRDP) support.

	 * Host webcam passthrough.
	
	 * Intel PXE boot ROM.

	 * Disk image encryption with AES algorithm.

	 * Cloud integration features.


In order to get started we first need to install ``ros2`` in our system.

Ubuntu (Debian packages)
------------------------

.. contents:: Table of Contents
   :depth: 2
   :local:

Debian packages for ROS 2 Iron are currently available for Ubuntu Jammy.
The Rolling Ridley distribution will change target platforms from time to time as new platforms are selected for development.
The target platforms are defined in `REP 2000 <https://github.com/ros-infrastructure/rep/blob/master/rep-2000.rst>`__
Most people will want to use a stable ROS distribution.

Resources
---------

* Status Page:

  * ROS 2 Iron (Ubuntu Jammy): `amd64 <http://repo.ros2.org/status_page/ros_iron_default.html>`__\ , `arm64 <http://repo.ros2.org/status_page/ros_iron_ujv8.html>`__
* `Jenkins Instance <http://build.ros2.org/>`__
* `Repositories <http://repo.ros2.org>`__

System setup
------------

Set locale
^^^^^^^^^^

.. include:: _Ubuntu-Set-Locale.rst

Enable required repositories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: _Apt-Repositories.rst

.. _linux-install-debians-install-ros-2-packages:

Install development tools (optional)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We recommend installing developer tools as well:

.. code-block:: bash

   sudo apt update && sudo apt install ros-dev-tools

Install ROS 2
-------------

Update your apt repository caches after setting up the repositories.

.. code-block:: bash

   sudo apt update

.. include:: _Apt-Upgrade-Admonition.rst

.. warning::

   Due to early updates in Ubuntu 22.04 it is important that ``systemd`` and ``udev``-related packages are updated before installing ROS 2.
   The installation of ROS 2's dependencies on a freshly installed system without upgrading can trigger the **removal of critical system packages**.

   Please refer to `ros2/ros2#1272 <https://github.com/ros2/ros2/issues/1272>`_ and `Launchpad #1974196 <https://bugs.launchpad.net/ubuntu/+source/systemd/+bug/1974196>`_ for more information.

Desktop Install (Recommended): ROS, RViz, demos, tutorials.

.. code-block:: bash

   sudo apt install ros-{DISTRO}-desktop

ROS-Base Install (Bare Bones): Communication libraries, message packages, command line tools.
No GUI tools.

.. code-block:: bash

   sudo apt install ros-{DISTRO}-ros-base

Install additional RMW implementations (optional)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The default middleware that ROS 2 uses is ``Fast DDS``, but the middleware (RMW) can be replaced at runtime.
See the :doc:`guide <../How-To-Guides/Working-with-multiple-RMW-implementations>` on how to work with multiple RMWs.

Setup environment
-----------------

Set up your environment by sourcing the following file.

.. code-block:: bash

   # Replace ".bash" with your shell if you're not using bash
   # Possible values are: setup.bash, setup.sh, setup.zsh
   source /opt/ros/{DISTRO}/setup.bash

Try some examples
-----------------

If you installed ``ros-{DISTRO}-desktop`` above you can try some examples.

In one terminal, source the setup file and then run a C++ ``talker``\ :

.. code-block:: bash

   source /opt/ros/{DISTRO}/setup.bash
   ros2 run demo_nodes_cpp talker

In another terminal source the setup file and then run a Python ``listener``\ :

.. code-block:: bash

   source /opt/ros/{DISTRO}/setup.bash
   ros2 run demo_nodes_py listener

You should see the ``talker`` saying that it's ``Publishing`` messages and the ``listener`` saying ``I heard`` those messages.
This verifies both the C++ and Python APIs are working properly.
Hooray!
