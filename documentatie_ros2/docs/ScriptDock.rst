Making a script to directly open the virtual image with docker and mount itself in vs code
============================================================================================

To achieve this you need 2 things:

 * a Dockerfile
 
 * a devcontainer.json
 
Create these 2 files in the folder of your choice and edit them with this content:

devcontainer.json:

.. code-block:: console
	
	{
		"name": "Ubuntu Docker Dev Container",
		"dockerFile": "dockerfile",
		"extensions": ["ms-vscode-remote.remote-containers"],
		"settings": {
		"terminal.integrated.shell.linux": "/bin/bash"
		},
		// Mounting the docker socket to the containers
		"mounts": [
		  "source=/var/run/docker.sock,target=/var/run/docker.sock,type=bind"
		]
	  }
  	

Dockerfile:

.. code-block:: console
	
	# Use the official Ubuntu 20.04 LTS image as the base image
	FROM ubuntu:latest

	# Dependencies
	RUN apt-get update \
	    && apt-get install -y --no-install-recommends \
	       apt-transport-https \
	       ca-certificates \
	       curl \
	       gnupg-agent \
	       software-properties-common \
	       docker.io

	# Add Docker's official GPG key
	RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

	# Add Docker's official repository
	RUN echo \
	  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
	  $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null

	# Install Docker
	RUN apt-get update \
	    && apt-get install -y --no-install-recommends docker-ce docker-ce-cli containerd.io

	# Install git
	RUN apt-get update \
	    && apt-get install -y git


	# Install sudo
	RUN apt-get update && apt-get install -y sudo

	# Adding new user
	RUN useradd -m -s /bin/bash name \
	    && echo "name ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

	USER name

	# Expose the Docker daemon port
	EXPOSE 2375

	# Start the Docker daemon
	CMD ["dockerd", "--host=unix:///var/run/docker.sock", "--host=tcp://0.0.0.0:2375"]

