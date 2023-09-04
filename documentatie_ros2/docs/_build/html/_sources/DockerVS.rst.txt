Docker container in VSCode
===========================

To open a Docker container with the image that you want simply navigate to the folder where you wish the container to be initiated and click the bottom left button ``Open a remote window``.

Then you will be prompted to choose an option from the drop down menu.

Choose ``New Dev Container`` and choose the image that you want.

.. note:: Don't forget to install the Docker extension in VSCode.

Now follow the steps below to install Docker on Ubuntu as an example:

Installing Docker on Ubuntu
============================

To get started with Docker Engine on Ubuntu, make sure you meet the prerequisites, and then follow the installation steps.

Prerequisites
***************

.. note:: If you use ufw or firewalld to manage firewall settings, be aware that when you expose container ports using Docker, these ports bypass your firewall rules.

OS requirements:
******************

To install Docker Engine, you need the 64-bit version of one of these Ubuntu versions:

 * Ubuntu Lunar 23.04
 * Ubuntu Kinetic 22.10
 * Ubuntu Jammy 22.04 (LTS)
 * Ubuntu Focal 20.04 (LTS)

Docker Engine for Ubuntu is compatible with x86_64 (or amd64), armhf, arm64, s390x, and ppc64le (ppc64el) architectures.

Uninstall old versions
***********************

Before you can install Docker Engine, you must first make sure that any conflicting packages are uninstalled.

Distro maintainers provide an unofficial distributions of Docker packages in APT. You must uninstall these packages before you can install the official version of Docker Engine.

The unofficial packages to uninstall are:

 * ``docker.io``
 * ``docker-compose``
 * ``docker-doc``
 * ``podman-docker``

Moreover, Docker Engine depends on ``containerd`` and ``runc``. Docker Engine bundles these dependencies as one bundle: ``containerd.io``. If you have installed the ``containerd`` or ``runc`` previously, uninstall them to avoid conflicts with the versions bundled with Docker Engine.

Run the following command to uninstall all conflicting packages:

.. code-block:: console

	$ for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt-get remove $pkg; done

``apt-get`` might report that you have none of these packages installed.

Images, containers, volumes, and networks stored in ``/var/lib/docker/`` aren't
automatically removed when you uninstall Docker. If you want to start with a
clean installation, and prefer to clean up any existing data.

Installation methods
*********************

You can install Docker Engine in different ways, depending on your needs:

 * Docker Engine comes bundled with
   Docker Desktop for Linux(https://docs.docker.com/desktop/install/linux-install/). This is
   the easiest and quickest way to get started.

 * Set up and install Docker Engine from
   Docker's ``apt`` repository(https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository).

 * Install it manually(https://docs.docker.com/engine/install/ubuntu/#install-from-a-package) and manage upgrades manually.

 * Use a convenience script(https://docs.docker.com/engine/install/ubuntu/#install-using-the-convenience-script). Only
   recommended for testing and development environments.

Install using the apt repository
*********************************

Before you install Docker Engine for the first time on a new host machine, you
need to set up the Docker repository. Afterward, you can install and update
Docker from the repository.

Set up the repository
**********************

1.  Update the ``apt`` package index and install packages to allow ``apt`` to use a
    repository over HTTPS:

.. code-block:: console

	$ sudo apt-get update
	$ sudo apt-get install ca-certificates curl gnupg

2.  Add Docker's official GPG key:

.. code-block:: console

	$ sudo install -m 0755 -d /etc/apt/keyrings
	$ curl -fsSL {{ download-url-base }}/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
	$ sudo chmod a+r /etc/apt/keyrings/docker.gpg

3.  Use the following command to set up the repository:

.. code-block:: console

	$ echo \
	"deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] {{ download-url-base }} \
	"$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
	sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    
.. note:: If you use an Ubuntu derivative distro, such as Linux Mint, you may need to use ``UBUNTU_CODENAME`` instead of ``VERSION_CODENAME``.

4. Update the ``apt`` package index:

.. code-block:: console

	$ sudo apt-get update

Install Docker Engine
***********************

1. Install Docker Engine, containerd, and Docker Compose.

   To install the latest version, run:

.. code-block:: console

	$ sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

2. Verify that the Docker Engine installation is successful by running the
   ``hello-world`` image.

.. code-block:: console

	$ sudo docker run hello-world

This command downloads a test image and runs it in a container. When the
container runs, it prints a confirmation message and exits.

You have now successfully installed and started Docker Engine.

.. note::  Receiving errors when trying to run without root? The docker user group exists but contains no users, which is why you’re required to use sudo to run Docker commands. Continue to Linux postinstall to allow non-privileged users to run Docker commands and for other optional configuration steps.

Uninstall Docker Engine
==========================

1. Uninstall the Docker Engine, CLI, containerd, and Docker Compose packages:

.. code-block:: console

	$ sudo apt-get purge docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin docker-ce-rootless-extras

2. Images, containers, volumes, or custom configuration files on your host
   aren't automatically removed. To delete all images, containers, and volumes:

.. code-block:: console

	$ sudo rm -rf /var/lib/docker
	$ sudo rm -rf /var/lib/containerd

.. note:: You have to delete any edited configuration files manually.

Linux post-installation steps for Docker Engine
==================================================

These optional post-installation procedures shows you how to configure your
Linux host machine to work better with Docker.

Manage Docker as a non-root user
*********************************

The Docker daemon binds to a Unix socket, not a TCP port. By default it's the
``root`` user that owns the Unix socket, and other users can only access it using
``sudo``. The Docker daemon always runs as the ``root`` user.

If you don't want to preface the ``docker`` command with ``sudo``, create a Unix
group called ``docker`` and add users to it. When the Docker daemon starts, it
creates a Unix socket accessible by members of the ``docker`` group. On some Linux
distributions, the system automatically creates this group when installing
Docker Engine using a package manager. In that case, there is no need for you to
manually create the group.

.. note:: The ``docker`` group grants root-level privileges to the user. To run Docker without root privileges, see
https://docs.docker.com/engine/security/rootless/

To create the ``docker`` group and add your user:

1. Create the ``docker`` group.

.. code-block:: console

	$ sudo groupadd docker

2. Add your user to the ``docker`` group.

.. code-block:: console

	$ sudo usermod -aG docker $USER

3. Log out and log back in so that your group membership is re-evaluated.

 * If you're running Linux in a virtual machine, it may be necessary to restart the virtual machine for changes to take effect.

You can also run the following command to activate the changes to groups:

.. code-block:: console

	$ newgrp docker

4. Verify that you can run ``docker`` commands without ``sudo``.

.. code-block:: console

	$ docker run hello-world

This command downloads a test image and runs it in a container. When the
container runs, it prints a message and exits.

If you initially ran Docker CLI commands using ``sudo`` before adding your user
to the ``docker`` group, you may see the following error:

.. code-block:: console
	WARNING: Error loading config file: /home/user/.docker/config.json -
	stat /home/user/.docker/config.json: permission denied

This error indicates that the permission settings for the ``~/.docker/``
directory are incorrect, due to having used the ``sudo`` command earlier.

To fix this problem, either remove the ``~/.docker/`` directory (it's recreated
automatically, but any custom settings are lost), or change its ownership and
permissions using the following commands:

.. code-block:: console

	$ sudo chown "$USER":"$USER" /home/"$USER"/.docker -R
	$ sudo chmod g+rwx "$HOME/.docker" -R

Configure Docker to start on boot with systemd
************************************************

Many modern Linux distributions use [systemd](../../config/daemon/systemd.md) to
manage which services start when the system boots. On Debian and Ubuntu, the
Docker service starts on boot by default. To automatically start Docker and
containerd on boot for other Linux distributions using systemd, run the
following commands:

.. code-block:: console

	$ sudo systemctl enable docker.service
	$ sudo systemctl enable containerd.service

To stop this behavior, use ``disable`` instead.

.. code-block:: console

	$ sudo systemctl disable docker.service
	$ sudo systemctl disable containerd.service

If you need to add an HTTP proxy, set a different directory or partition for the
Docker runtime files, or make other customizations, see
[customize your systemd Docker daemon options](../../config/daemon/systemd.md).
