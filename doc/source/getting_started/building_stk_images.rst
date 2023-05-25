.. _building_stk_images:

Building STK images
###################

PySTK provides various `Dockerfiles`_ to build `Docker images`_ that
containerize STK. Some of these files include additional utilities such as
`Python`_.

All the Dockerfiles are collected in the `docker/ directory`_ of the `PySTK
repository`_. These files are organized according to the operating system,
either Windows or Linux.


.. grid:: 2

    .. grid-item-card:: Dockefiles for Windows :fab:`windows`
        :link: https://github.com/ansys-internal/pystk/tree/main/docker/windows
        
        STKEngine and STKDesktop are supported.

    .. grid-item-card:: Dockefiles for Linux :fab:`linux`
        :link: https://github.com/ansys-internal/pystk/tree/main/docker/linux
        

        Only STKEngine is supported.


Architecture of the images
==========================

There are some minor differences between Windows and Linux images for
containerizing STK.

Comparing their capabilities, Windows images support both
:py:class:`ansys.stk.core.stkdesktop.STKDesktop` and
:py:class:`ansys.stk.core.stkengine.STKEngine` whereas Linux images only support
the later one.

From the architecture perspective, the following diagrams provide an overview on
the relation between the different Docker images:

.. tab-set::

    .. tab-item:: STK images for Windows
        :sync: windows

        .. figure:: https://help.agi.com/stkdevkit/Content/automationTree/images/Windows_Container_Heirarchy.png

    .. tab-item:: STK images for Linux
        :sync: linux

        .. figure:: https://help.agi.com/stkdevkit/Content/automationTree/images/ContainerizationDiagram.png


Building images
===============

All the images in the `docker/ directory`_ of the repository include:

* ``Dockerfile`` for building the image
* ``docker-compose.yml`` for orchestrating the building
* ``README.rst`` file providing some guidance and instructions


The available images are:

.. jinja:: docker_images

    .. tab-set:: 

        .. tab-item:: Windows
            :sync: windows

            {% for image in windows_images %}
            * {{ image }}
            {% endfor %}

        .. tab-item:: Linux
            :sync: linux

            {% for image in linux_images %}
            * {{ image }}
            {% endfor %}

End of the tab


.. tab-set::

    .. tab-item:: Windows
        :sync: windows

        #. Clone the repository by running:

           .. code-block::
           
               git clone https://github.com/pyansys/pystk

        #. Navigate to the ``docker/windows/`` directory

        #. Create a directory named ``distributions/`` inside the ``stk-engine/`` directory

        #. Place the STK artifacts inside the ``stk-engine/distributions/`` folder

        #. Build all the images by running:

           .. code-block::
               
               docker compose build

        #. Build a single images by running:

           .. code-block::
               
               docker compose build <image-name>


    .. tab-item:: Linux
        :sync: linux

        #. Clone the repository by running:

           .. code-block::
           
               git clone https://github.com/pyansys/pystk

        #. Navigate to the ``docker/linux/`` directory

        #. Create a directory named ``distributions/`` inside the ``stk-engine/`` directory

        #. Place the STK artifacts inside the ``stk-engine/distributions/`` folder

        #. Build all the images by running:

           .. code-block::
               
               docker compose build

        #. Build a single images by running:

           .. code-block::
               
               docker compose build <image-name>


Running containers from images
==============================

In Docker, containers are created based on images. To run a container, it is
important to consider whether any of the following need to be shared:
environment variables, network resources, or volumes (directories).

Best practices recommend running a container in detached mode with an
interactive teletypewriter (TTY) session. This allows for connecting to the
container at any time without blocking the current shell session.

Syntax
------

.. code-block:: text

    docker run \
      --detach --interactive --tty \
      --network="host" \
      --env ANSYSLMD_LICENSE_FILE=$ANSYSLMD_LICENSE_FILE \
      --name <container-name> \
      --entrypoint <entrypoint> \
      <image-name>


Images can be run by creating a Docker container. Before
creating a new container, verify if you require to share any of the following:

- Environment variables
- Network resources
- Volumes (directories)

It is advised to run a container in detached mode with an interactive
teletypewriter (TTY) session. This allows to connect to the container at any
point without blocking the current shell session.

To create a container from the desired Docker image, run the following command:

.. code-block:: text

    docker run \
     --detach --interactive --tty \
     --network="host" \
     --env LICENSE_FILE=$LICENSE_FILE \
     --name <container-name> \
     --entrypoint <entrypoint> \
     <image-name>


Command breakdown
-----------------

The docker run command is utilized to create and run a container from a Docker
image. Various options are available to customize the container creation
process.

- ``--detach`` Runs the container in detached mode, allowing it to run in the background.
- ``--interactive`` Enables interactive mode, providing a TTY session for connecting to the container.
- ``--tty`` Allocates a pseudo-TTY, ensuring proper formatting and display of the container's output.
- ``--network="host"`` Shares the host's network stack with the container, enabling network connectivity.
- ``--env ANSYSLMD_LICENSE_FILE=$ANSYSLMD_LICENSE_FILE`` Specifies environment variable(s) to be shared with the container.
- ``--name <container-name>`` Assigns a name to the container for easy identification and reference.
- ``--entrypoint <entrypoint>`` Defines the command or script to be executed when the container starts.
- ``<image-name>`` Specifies the name or ID of the Docker image to be used for creating the container.


Usage example
-------------

.. code-block:: text

    docker run \
      --detach --interactive --tty \
      --network="host" \
      --env ANSYSLMD_LICENSE_FILE=$ANSYSLMD_LICENSE_FILE \
      --name stk-python3.10 \
      --entrypoint /bin/bash \
      ansys/stk:latest-centos7-python3.10

In this example, a container is created from the
``ansys/stk:latest-centos7-python3.10`` Docker image. It runs in detached mode
with an interactive TTY session, shares the host's network stack, sets the
``ANSYSLMD_LICENSE_FILE`` environment variable, and assigns the name
``skt-python3.10`` to the container. The container starts by executing the
``/bin/bash`` command.


Executing commands in containers
================================

In a Docker environment, it is essential to be able to execute shell commands
within a running container. This feature enables interaction with the
container's environment and facilitates various operations.

Syntax
------

.. code-block:: text

    docker exec \
     --interactive --tty \
     <container-name> \
     <command>


Command breakdown
-----------------

The ``docker exec`` command is used to execute commands within a Docker
container. It provides several options to enhance the execution experience.

- ``--interactive`` Allows interactive mode, enabling interaction with the command executed within the container.
- ``--tty`` Allocates a pseudo-TTY, ensuring proper formatting and display of the executed command's output.
- ``<container-name>`` Specifies the name or ID of the target container in which the command should be executed.
- ``<command>`` Represents the shell command that you want to execute within the container.


Usage example
-------------

To illustrate the execution of a command within a Docker container running STK,
consider the following example:


.. code-block:: text

    docker exec \
      --interactive --tty \
      stk-python3.10 \
      /bin/bash -c \
      "python examples/hello_pystk.py"


In this example, the command ``python scripts/hello_pystk.py`` is executed
within the container named ``stk-python3.10``. This command executes the script
``hello_pystk.py`` contained in a volume named ``scripts`` that gets shared with
the container.
