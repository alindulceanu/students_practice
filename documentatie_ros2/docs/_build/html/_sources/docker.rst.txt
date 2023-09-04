What is Docker?
=================

Wikipedia defines Docker as an open-source project that automates the deployment of software applications inside containers by providing an additional layer of abstraction and automation of OS-level virtualization on Linux.

Wow! That's a mouthful. In simpler words, Docker is a tool that allows developers, sys-admins etc. to easily deploy their applications in a sandbox (called containers) to run on the host operating system i.e. Linux. The key benefit of Docker is that it allows users to package an application with all of its dependencies into a standardized unit for software development. Unlike virtual machines, containers do not have high overhead and hence enable more efficient usage of the underlying system and resources.

What are containers?
********************

The industry standard today is to use Virtual Machines (VMs) to run software applications. VMs run applications inside a guest Operating System, which runs on virtual hardware powered by the server’s host OS.

VMs are great at providing full process isolation for applications: there are very few ways a problem in the host operating system can affect the software running in the guest operating system, and vice-versa. But this isolation comes at great cost — the computational overhead spent virtualizing hardware for a guest OS to use is substantial.

Containers take a different approach: by leveraging the low-level mechanics of the host operating system, containers provide most of the isolation of virtual machines at a fraction of the computing power.

Why use containers?
*******************

Containers offer a logical packaging mechanism in which applications can be abstracted from the environment in which they actually run. This decoupling allows container-based applications to be deployed easily and consistently, regardless of whether the target environment is a private data center, the public cloud, or even a developer’s personal laptop. This gives developers the ability to create predictable environments that are isolated from the rest of the applications and can be run anywhere.

From an operations standpoint, apart from portability containers also give more granular control over resources giving your infrastructure improved efficiency which can result in better utilization of your compute resources.

Due to these benefits, containers (& Docker) have seen widespread adoption. Companies like Google, Facebook, Netflix and Salesforce leverage containers to make large engineering teams more productive and to improve utilization of compute resources. In fact, Google credited containers for eliminating the need for an entire data center.

HELLO WORLD
***************

Playing with Busybox
********************

Now that we have everything setup, it's time to get our hands dirty. In this section, we are going to run a Busybox container on our system and get a taste of the ``docker run`` command.

To get started, let's run the following in our terminal:

.. code-block:: console

	$ docker pull busybox

.. note:: `Depending on how you've installed docker on your system, you might see a permission denied error after running the above command. If you're on a Mac, make sure the Docker engine is running. If you're on Linux, then prefix your docker commands with sudo. Alternatively, you can create a docker group to get rid of this issue.`

The ``pull`` command fetches the busybox image from the Docker registry and saves it to our system. You can use the ``docker images`` command to see a list of all images on your system.

.. code-block:: console

	$ docker images
	REPOSITORY              TAG                 IMAGE ID            CREATED             VIRTUAL SIZE
	busybox                 latest              c51f86c28340        4 weeks ago         1.109 MB
	
Docker Run
**********

Great! Let's now run a Docker container based on this image. To do that we are going to use the almighty ``docker run`` command.

.. code-block:: console

	$ docker run busybox
	$
	
Wait, nothing happened! Is that a bug? Well, no. Behind the scenes, a lot of stuff happened. When you call ``run``, the Docker client finds the image (busybox in this case), loads up the container and then runs a command in that container. When we run ``docker run`` busybox, we didn't provide a command, so the container booted up, ran an empty command and then exited. Well, yeah - kind of a bummer. Let's try something more exciting.

.. code-block:: console

	$ docker run busybox echo "hello from busybox"
	hello from busybox
	
Nice - finally we see some output. In this case, the Docker client dutifully ran the ``echo`` command in our busybox container and then exited it. If you've noticed, all of that happened pretty quickly. Imagine booting up a virtual machine, running a command and then killing it. Now you know why they say containers are fast! Ok, now it's time to see the ``docker ps`` command. The ``docker ps`` command shows you all containers that are currently running.

.. code-block:: console

	$ docker ps
	CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
	
Since no containers are running, we see a blank line. Let's try a more useful variant: ``docker ps -a``

.. code-block:: console

	$ docker ps -a
	CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                      PORTS               NAMES
	305297d7a235        busybox             "uptime"            11 minutes ago      Exited (0) 11 minutes ago                       distracted_goldstine
	ff0a5c3750b9        busybox             "sh"                12 minutes ago      Exited (0) 12 minutes ago                       elated_ramanujan
	14e5bd11d164        hello-world         "/hello"            2 minutes ago       Exited (0) 2 minutes ago                        thirsty_euclid
	
So what we see above is a list of all containers that we ran. Do notice that the STATUS column shows that these containers exited a few minutes ago.

You're probably wondering if there is a way to run more than just one command in a container. Let's try that now:

.. code-block:: console

	$ docker run -it busybox sh
	/ # ls
	bin   dev   etc   home  proc  root  sys   tmp   usr   var
	/ # uptime
	 05:45:21 up  5:58,  0 users,  load average: 0.00, 0.01, 0.04
	 
Running the ``run`` command with the -it flags attaches us to an interactive tty in the container. Now we can run as many commands in the container as we want. Take some time to run your favorite commands.

.. note:: Danger Zone: If you're feeling particularly adventurous you can try rm -rf bin in the container. Make sure you run this command in the container and not in your laptop/desktop. Doing this will make any other commands like ls, uptime not work. Once everything stops working, you can exit the container (type exit and press Enter) and then start it up again with the ``docker run`` -it busybox sh command. Since Docker creates a new container every time, everything should start working again.

That concludes a whirlwind tour of the mighty ``docker run`` command, which would most likely be the command you'll use most often. It makes sense to spend some time getting comfortable with it. To find out more about run, use ``docker run`` --help to see a list of all flags it supports. As we proceed further, we'll see a few more variants of ``docker run``.

Before we move ahead though, let's quickly talk about deleting containers. We saw above that we can still see remnants of the container even after we've exited by running ``docker ps -a``. Throughout this tutorial, you'll run ``docker run`` multiple times and leaving stray containers will eat up disk space. Hence, as a rule of thumb, I clean up containers once I'm done with them. To do that, you can run the ``docker rm`` command. Just copy the container IDs from above and paste them alongside the command.

.. code-block:: console

	$ docker rm 305297d7a235 ff0a5c3750b9
	305297d7a235
	ff0a5c3750b9
	
On deletion, you should see the IDs echoed back to you. If you have a bunch of containers to delete in one go, copy-pasting IDs can be tedious. In that case, you can simply run -

.. code-block:: console

	$ docker rm $(docker ps -a -q -f status=exited)
	
This command deletes all containers that have a status of ``exited``. In case you're wondering, the ``-q`` flag, only returns the numeric IDs and ``-f`` filters output based on conditions provided. One last thing that'll be useful is the ``--rm`` flag that can be passed to ``docker run`` which automatically deletes the container once it's exited from. For one off docker runs, ``--rm`` flag is very useful.

.. note:: In later versions of Docker, the ``docker container prune`` command can be used to achieve the same effect.

.. code-block:: console

	$ docker container prune
	WARNING! This will remove all stopped containers.
	Are you sure you want to continue? [y/N] y
	Deleted Containers:
	4a7f7eebae0f63178aff7eb0aa39f0627a203ab2df258c1a00b456cf20063
	f98f9c2aa1eaf727e4ec9c0283bcaa4762fbdba7f26191f26c97f64090360

	Total reclaimed space: 212 B
	
Lastly, you can also delete images that you no longer need by running ``docker rmi``.

Terminology
****************

In the last section, we used a lot of Docker-specific jargon which might be confusing to some. So before we go further, let me clarify some terminology that is used frequently in the Docker ecosystem.

 * Images - The blueprints of our application which form the basis of containers. In the demo above, we used the docker pull command to download the busybox image.

 * Containers - Created from Docker images and run the actual application. We create a container using ``docker run`` which we did using the busybox image that we downloaded. A list of running containers can be seen using the ``docker ps`` command.

 * Docker Daemon - The background service running on the host that manages building, running and distributing Docker containers. The daemon is the process that runs in the operating system which clients talk to.

 * Docker Client - The command line tool that allows the user to interact with the daemon. More generally, there can be other forms of clients too - such as Kitematic which provide a GUI to the users.

 * Docker Hub - A registry of Docker images. You can think of the registry as a directory of all available Docker images. If required, one can host their own Docker registries and can use them for pulling images.

WEBAPPS WITH DOCKER
********************

Great! So we have now looked at ``docker run``, played with a Docker container and also got a hang of some terminology.
Our First Image
****************

Now that we have a better understanding of images, it's time to create our own. Our goal in this section will be to create an image that sandboxes a simple Flask application. For the purposes of this workshop, I've already created a fun little Flask app that displays a random cat ``.gif`` every time it is loaded - because you know, who doesn't like cats? If you haven't already, please go ahead and clone the repository locally like so -

.. code-block:: console

	$ git clone https://github.com/prakhar1989/docker-curriculum.git
	$ cd docker-curriculum/flask-app
	
.. note:: This should be cloned on the machine where you are running the docker commands and not inside a docker container.

The next step now is to create an image with this web app. As mentioned above, all user images are based on a base image. Since our application is written in Python, the base image we're going to use will be Python 3.

Dockerfile
***********

A Dockerfile is a simple text file that contains a list of commands that the Docker client calls while creating an image. It's a simple way to automate the image creation process. The best part is that the commands you write in a Dockerfile are almost identical to their equivalent Linux commands. This means you don't really have to learn new syntax to create your own dockerfiles.

The application directory does contain a Dockerfile but since we're doing this for the first time, we'll create one from scratch. To start, create a new blank file in our favorite text-editor and save it in the same folder as the flask app by the name of ``Dockerfile``.

We start with specifying our base image. Use the ``FROM`` keyword to do that -

.. code-block:: python

	FROM python:3.8
	
The next step usually is to write the commands of copying the files and installing the dependencies. First, we set a working directory and then copy all the files for our app.

.. code-block:: python

	# set a directory for the app
	WORKDIR /usr/src/app

	# copy all the files to the container
	COPY . .
	
Now, that we have the files, we can install the dependencies.

.. code-block:: python

	# install dependencies
	RUN pip install --no-cache-dir -r requirements.txt
	
The next thing we need to specify is the port number that needs to be exposed. Since our flask app is running on port ``5000``, that's what we'll indicate.

.. code-block:: python

	EXPOSE 5000
	
The last step is to write the command for running the application, which is simply - ``python ./app.py``. We use the CMD command to do that -

.. code-block:: python

	CMD ["python", "./app.py"]
	
The primary purpose of ``CMD`` is to tell the container which command it should run when it is started. With that, our ``Dockerfile`` is now ready. This is how it looks -

.. code-block:: python

	FROM python:3.8

	# set a directory for the app
	WORKDIR /usr/src/app

	# copy all the files to the container
	COPY . .

	# install dependencies
	RUN pip install --no-cache-dir -r requirements.txt

	# define the port number the container should expose
	EXPOSE 5000

	# run the command
	CMD ["python", "./app.py"]
	
Now that we have our ``Dockerfile``, we can build our image. The ``docker build`` command does the heavy-lifting of creating a Docker image from a ``Dockerfile``.

The section below shows you the output of running the same. Before you run the command yourself (don't forget the period), make sure to replace my username with yours. This username should be the same one you created when you registered on Docker hub. If you haven't done that yet, please go ahead and create an account. The ``docker build`` command is quite simple - it takes an optional tag name with ``-t`` and a location of the directory containing the ``Dockerfile``.

.. code-block:: console

	$ docker build -t yourusername/catnip .
	Sending build context to Docker daemon 8.704 kB
	Step 1 : FROM python:3.8
	# Executing 3 build triggers...
	Step 1 : COPY requirements.txt /usr/src/app/
	 ---> Using cache
	Step 1 : RUN pip install --no-cache-dir -r requirements.txt
	 ---> Using cache
	Step 1 : COPY . /usr/src/app
	 ---> 1d61f639ef9e
	Removing intermediate container 4de6ddf5528c
	Step 2 : EXPOSE 5000
	 ---> Running in 12cfcf6d67ee
	 ---> f423c2f179d1
	Removing intermediate container 12cfcf6d67ee
	Step 3 : CMD python ./app.py
	 ---> Running in f01401a5ace9
	 ---> 13e87ed1fbc2
	Removing intermediate container f01401a5ace9
	Successfully built 13e87ed1fbc2
	
If you don't have the ``python:3.8`` image, the client will first pull the image and then create your image. Hence, your output from running the command will look different from mine. If everything went well, your image should be ready! Run ``docker images`` and see if your image shows.

The last step in this section is to run the image and see if it actually works (replacing my username with yours).

.. code-block:: console

	$ docker run -p 8888:5000 yourusername/catnip
	 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
	 
The command we just ran used port 5000 for the server inside the container and exposed this externally on port 8888. Head over to the URL with port 8888, where your app should be live.

Congratulations! You have successfully created your first docker image.

Docker Compose

Till now we've spent all our time exploring the Docker client. In the Docker ecosystem, however, there are a bunch of other open-source tools which play very nicely with Docker. A few of them are -

 * Docker Machine - Create Docker hosts on your computer, on cloud providers, and inside your own data center
 * Docker Compose - A tool for defining and running multi-container Docker applications.
 * Docker Swarm - A native clustering solution for Docker
 * Kubernetes - Kubernetes is an open-source system for automating deployment, scaling, and management of containerized applications.
 
In this section, we are going to look at one of these tools, Docker Compose, and see how it can make dealing with multi-container apps easier.

So what is Compose used for? Compose is a tool that is used for defining and running multi-container Docker apps in an easy way. It provides a configuration file called ``docker-compose.yml`` that can be used to bring up an application and the suite of services it depends on with just one command. Compose works in all environments: production, staging, development, testing, as well as CI workflows, although Compose is ideal for development and testing environments.

Let's see if we can create a ``docker-compose.yml`` file.

The first step, however, is to install Docker Compose. If you're running Windows or Mac, Docker Compose is already installed as it comes in the Docker Toolbox. Linux users can easily get their hands on Docker Compose by following the instructions on the docs. Since Compose is written in Python, you can also simply do ``pip install docker-compose``. Test your installation with -


$ docker-compose --version
docker-compose version 1.21.2, build a133471
Now that we have it installed, we can jump on the next step i.e. the Docker Compose file docker-compose.yml. The syntax for YAML is quite simple and the repo already contains the docker-compose file that we'll be using.

.. code-block:: console

	version: "3"
	services:
	  es:
	    image: docker.elastic.co/elasticsearch/elasticsearch:6.3.2
	    container_name: es
	    environment:
	      - discovery.type=single-node
	    ports:
	      - 9200:9200
	    volumes:
	      - esdata1:/usr/share/elasticsearch/data
	  web:
	    image: yourusername/foodtrucks-web
	    command: python3 app.py
	    depends_on:
	      - es
	    ports:
	      - 5000:5000
	    volumes:
	      - ./flask-app:/opt/flask-app
	volumes:
	  esdata1:
	    driver: local
	    
Let me breakdown what the file above means. At the parent level, we define the names of our services - es and web. The image parameter is always required, and for each service that we want Docker to run, we can add additional parameters. For es, we just refer to the elasticsearch image available on Elastic registry. For our Flask app, we refer to the image that we built at the beginning of this section.

Other parameters such as command and ports provide more information about the container. The volumes parameter specifies a mount point in our web container where the code will reside. This is purely optional and is useful if you need access to logs, etc. We'll later see how this can be useful during development. Refer to the online reference to learn more about the parameters this file supports. We also add volumes for the es container so that the data we load persists between restarts. We also specify depends_on, which tells docker to start the es container before web. You can read more about it on docker compose docs.

.. note:: You must be inside the directory with the docker-compose.yml file in order to execute most Compose commands.

Great! Now the file is ready, let's see ``docker-compose`` in action. But before we start, we need to make sure the ports and names are free. So if you have the Flask and ES containers running, lets turn them off.

.. code-block:: console

	$ docker stop es foodtrucks-web
	es
	foodtrucks-web

	$ docker rm es foodtrucks-web
	es
	foodtrucks-web
	
Now we can run ``docker-compose``. Navigate to the food trucks directory and run ``docker-compose up``.

.. code-block:: console

	$ docker-compose up
	Creating network "foodtrucks_default" with the default driver
	Creating foodtrucks_es_1
	Creating foodtrucks_web_1
	Attaching to foodtrucks_es_1, foodtrucks_web_1
	es_1  | [2016-01-11 03:43:50,300][INFO ][node                     ] [Comet] version[2.1.1], pid[1], build[40e2c53/2015-12-15T13:05:55Z]
	es_1  | [2016-01-11 03:43:50,307][INFO ][node                     ] [Comet] initializing ...
	es_1  | [2016-01-11 03:43:50,366][INFO ][plugins                  ] [Comet] loaded [], sites []
	es_1  | [2016-01-11 03:43:50,421][INFO ][env                      ] [Comet] using [1] data paths, mounts [[/usr/share/elasticsearch/data (/dev/sda1)]], net usable_space [16gb], net total_space [18.1gb], spins? [possibly], types [ext4]
	es_1  | [2016-01-11 03:43:52,626][INFO ][node                     ] [Comet] initialized
	es_1  | [2016-01-11 03:43:52,632][INFO ][node                     ] [Comet] starting ...
	es_1  | [2016-01-11 03:43:52,703][WARN ][common.network           ] [Comet] publish address: {0.0.0.0} is a wildcard address, falling back to first non-loopback: {172.17.0.2}
	es_1  | [2016-01-11 03:43:52,704][INFO ][transport                ] [Comet] publish_address {172.17.0.2:9300}, bound_addresses {[::]:9300}
	es_1  | [2016-01-11 03:43:52,721][INFO ][discovery                ] [Comet] elasticsearch/cEk4s7pdQ-evRc9MqS2wqw
	es_1  | [2016-01-11 03:43:55,785][INFO ][cluster.service          ] [Comet] new_master {Comet}{cEk4s7pdQ-evRc9MqS2wqw}{172.17.0.2}{172.17.0.2:9300}, reason: zen-disco-join(elected_as_master, [0] joins received)
	es_1  | [2016-01-11 03:43:55,818][WARN ][common.network           ] [Comet] publish address: {0.0.0.0} is a wildcard address, falling back to first non-loopback: {172.17.0.2}
	es_1  | [2016-01-11 03:43:55,819][INFO ][http                     ] [Comet] publish_address {172.17.0.2:9200}, bound_addresses {[::]:9200}
	es_1  | [2016-01-11 03:43:55,819][INFO ][node                     ] [Comet] started
	es_1  | [2016-01-11 03:43:55,826][INFO ][gateway                  ] [Comet] recovered [0] indices into cluster_state
	es_1  | [2016-01-11 03:44:01,825][INFO ][cluster.metadata         ] [Comet] [sfdata] creating index, cause [auto(index api)], templates [], shards [5]/[1], mappings [truck]
	es_1  | [2016-01-11 03:44:02,373][INFO ][cluster.metadata         ] [Comet] [sfdata] update_mapping [truck]
	es_1  | [2016-01-11 03:44:02,510][INFO ][cluster.metadata         ] [Comet] [sfdata] update_mapping [truck]
	es_1  | [2016-01-11 03:44:02,593][INFO ][cluster.metadata         ] [Comet] [sfdata] update_mapping [truck]
	es_1  | [2016-01-11 03:44:02,708][INFO ][cluster.metadata         ] [Comet] [sfdata] update_mapping [truck]
	es_1  | [2016-01-11 03:44:03,047][INFO ][cluster.metadata         ] [Comet] [sfdata] update_mapping [truck]
	web_1 |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
	
Head over to the IP to see your app live. That was amazing wasn't it? Just a few lines of configuration and we have two Docker containers running successfully in unison. Let's stop the services and re-run in detached mode.

.. code-block:: console

	web_1 |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
	Killing foodtrucks_web_1 ... done
	Killing foodtrucks_es_1 ... done

	$ docker-compose up -d
	Creating es               ... done
	Creating foodtrucks_web_1 ... done

	$ docker-compose ps
	      Name                    Command               State                Ports
	--------------------------------------------------------------------------------------------
	es                 /usr/local/bin/docker-entr ...   Up      0.0.0.0:9200->9200/tcp, 9300/tcp
	foodtrucks_web_1   python3 app.py                   Up      0.0.0.0:5000->5000/tcp
	
Unsurprisingly, we can see both the containers running successfully. Where do the names come from? Those were created automatically by Compose. But does Compose also create the network automatically? Good question! Let's find out.

First off, let us stop the services from running. We can always bring them back up in just one command. Data volumes will persist, so it’s possible to start the cluster again with the same data using docker-compose up. To destroy the cluster and the data volumes, just type ``docker-compose down -v``.

.. code-block:: console

	$ docker-compose down -v
	Stopping foodtrucks_web_1 ... done
	Stopping es               ... done
	Removing foodtrucks_web_1 ... done
	Removing es               ... done
	Removing network foodtrucks_default
	Removing volume foodtrucks_esdata1
	
While we're are at it, we'll also remove the ``foodtrucks`` network that we created last time.

.. code-block:: console

	$ docker network rm foodtrucks-net
	$ docker network ls
	NETWORK ID          NAME                 DRIVER              SCOPE
	c2c695315b3a        bridge               bridge              local
	a875bec5d6fd        host                 host                local
	ead0e804a67b        none                 null                local
	
Great! Now that we have a clean slate, let's re-run our services and see if Compose does its magic.

.. code-block:: console

	$ docker-compose up -d
	Recreating foodtrucks_es_1
	Recreating foodtrucks_web_1

	$ docker container ls
	CONTAINER ID        IMAGE                        COMMAND                  CREATED             STATUS              PORTS                    NAMES
	f50bb33a3242        yourusername/foodtrucks-web  "python3 app.py"         14 seconds ago      Up 13 seconds       0.0.0.0:5000->5000/tcp   foodtrucks_web_1
	e299ceeb4caa        elasticsearch                "/docker-entrypoint.s"   14 seconds ago      Up 14 seconds       9200/tcp, 9300/tcp       foodtrucks_es_1

So far, so good. Time to see if any networks were created.

.. code-block:: console

	$ docker network ls
	NETWORK ID          NAME                 DRIVER
	c2c695315b3a        bridge               bridge              local
	f3b80f381ed3        foodtrucks_default   bridge              local
	a875bec5d6fd        host                 host                local
	ead0e804a67b        none                 null                local
	
You can see that compose went ahead and created a new network called ``foodtrucks_default`` and attached both the new services in that network so that each of these are discoverable to the other. Each container for a service joins the default network and is both reachable by other containers on that network, and discoverable by them at a hostname identical to the container name.

.. code-block:: console

	$ docker ps
	CONTAINER ID        IMAGE                                                 COMMAND                  CREATED              STATUS              PORTS                              NAMES
	8c6bb7e818ec        docker.elastic.co/elasticsearch/elasticsearch:6.3.2   "/usr/local/bin/dock…"   About a minute ago   Up About a minute   0.0.0.0:9200->9200/tcp, 9300/tcp   es
	7640cec7feb7        yourusername/foodtrucks-web                           "python3 app.py"         About a minute ago   Up About a minute   0.0.0.0:5000->5000/tcp             foodtrucks_web_1

	$ docker network inspect foodtrucks_default
	[
	    {
		"Name": "foodtrucks_default",
		"Id": "f3b80f381ed3e03b3d5e605e42c4a576e32d38ba24399e963d7dad848b3b4fe7",
		"Created": "2018-07-30T03:36:06.0384826Z",
		"Scope": "local",
		"Driver": "bridge",
		"EnableIPv6": false,
		"IPAM": {
		    "Driver": "default",
		    "Options": null,
		    "Config": [
		        {
		            "Subnet": "172.19.0.0/16",
		            "Gateway": "172.19.0.1"
		        }
		    ]
		},
		"Internal": false,
		"Attachable": true,
		"Ingress": false,
		"ConfigFrom": {
		    "Network": ""
		},
		"ConfigOnly": false,
		"Containers": {
		    "7640cec7feb7f5615eaac376271a93fb8bab2ce54c7257256bf16716e05c65a5": {
		        "Name": "foodtrucks_web_1",
		        "EndpointID": "b1aa3e735402abafea3edfbba605eb4617f81d94f1b5f8fcc566a874660a0266",
		        "MacAddress": "02:42:ac:13:00:02",
		        "IPv4Address": "172.19.0.2/16",
		        "IPv6Address": ""
		    },
		    "8c6bb7e818ec1f88c37f375c18f00beb030b31f4b10aee5a0952aad753314b57": {
		        "Name": "es",
		        "EndpointID": "649b3567d38e5e6f03fa6c004a4302508c14a5f2ac086ee6dcf13ddef936de7b",
		        "MacAddress": "02:42:ac:13:00:03",
		        "IPv4Address": "172.19.0.3/16",
		        "IPv6Address": ""
		    }
		},
		"Options": {},
		"Labels": {
		    "com.docker.compose.network": "default",
		    "com.docker.compose.project": "foodtrucks",
		    "com.docker.compose.version": "1.21.2"
		}
	    }
	]
	
CONCLUSION
***************

And that's a wrap! After a long, exhaustive but fun tutorial you are now ready to take the container world by storm! If you followed along till the very end then you should definitely be proud of yourself. You learned how to setup Docker and how to run your own containers.

I hope that finishing this tutorial makes you more confident in your abilities to deal with servers. When you have an idea of building your next app, you can be sure that you'll be able to get it in front of people with minimal effort.
