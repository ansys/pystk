Install PySTK in a Linux container
##################################

This guideline covers the  installation of PySTK inside a Linux-based Docker
container.

Download Dockerfiles
====================

Start by downloading the PySTK Docker images for Linux. The images contain
the latest three stable version of Python.

.. jinja:: docker_images

    .. list-table::
        :widths: auto

        * - **Artifact**
          - `Linux Dockerfiles <../../../_static/docker/{{ docker_recipes_linux }}>`_
        * - **Size**
          - {{ docker_recipes_linux_size }}
        * - **SHA-256**
          - {{ docker_recipes_linux_hash }}

Download STK artifacts
======================

Download the ``STK Engine`` and ``STK Engine Deployment Resources`` artifacts for
Linux platforms from the `https://support.agi.com/downloads
<https://support.agi.com/downloads>`_ page.

Place the artifacts inside a directory named ``distributions``. This directory
must be contained inside of the ``stk-engine`` directory.

.. code-block:: dosbatch

    linux/
    ├── docker-compose.yml
    ├── stk-engine
    │   └── distributions/
    │          └── Place STK Engine artifacts here
    ├── stk-engine-py310
    ├── stk-engine-py311
    ├── stk-engine-py312
    └── stk-engine-pybase

Build Docker images
===================

Navigate to the ``linux`` directory and use `Docker Compose`_ to build the
image of your choice by running:

.. code-block:: dosbatch

    docker compose build stk-engine-py3<minor>

where ``<minor>`` is one of the minor versions of Python.

Download PySTK wheels
=====================

Download the PySTK wheels for Linux.

.. jinja:: artifacts

    .. list-table::
        :widths: auto

        * - **Artifact**
          - `{{ wheels }} <../../../_static/artifacts/{{ wheels }}>`_
        * - **Size**
          - {{ wheels_size }}
        * - **SHA-256**
          - {{ wheels_hash }}

Next, create a working directory in your machine. This directory is used as a
shared volume with future Docker containers. Place the PySTK wheels in this
directory.

.. jinja:: artifacts

    .. code-block:: dosbatch
    
        working-directory/
        └── {{ wheels }}

Configure the license
=====================

Open a terminal in your working directory. Make sure you have set the
``ANSYSLMD_LICENSE_FILE`` environment variable by running:


.. code-block:: bash

    export ANSYSLMD_LICENSE_FILE="<PORT>@<LICENSE_SERVER_IP>"


where ``PORT`` usually takes the value of ``1055`` and ``LICENSE_SERVER_IP`` is
the Internet Protocol (IP) of the machine hosting the license server.

Start a container
=================

With the artifacts and the license in place, start a Docker container and share
the working directory as a volume. This allows to write scripts using the tools
in the host machine while isolating their execution inside the container.

Syntax
------

.. code-block:: bash

    docker run \
      --detach --interactive --tty \
      --network="host" \
      --env ANSYSLMD_LICENSE_FILE=$ANSYSLMD_LICENSE_FILE \
      --name <container-name> \
      --entrypoint <entrypoint> \
      <image-name>

Command breakdown
-----------------

The docker run command is utilized to create and run a container from a Docker
image. Various options are available to customize the container creation
process.

- ``--detach`` Runs the container in detached mode, enabling it to run in the background.
- ``--interactive`` Enables interactive mode, providing a TTY session for connecting to the container.
- ``--tty`` Allocates a pseudo-TTY, ensuring proper formatting and display of the container's output.
- ``--network="host"`` Shares the host's network stack with the container, enabling network connectivity.
- ``--env ANSYSLMD_LICENSE_FILE=$ANSYSLMD_LICENSE_FILE`` Specifies environment variable(s) to be shared with the container.
- ``--name <container-name>`` Assigns a name to the container for easy identification and reference.
- ``--entrypoint <entrypoint>`` Defines the command or script to be executed when the container starts.
- ``--volume <volume>`` Specifies the binding volume between the host and the container.
- ``<image-name>`` Specifies the name or ID of the Docker image to be used for creating the container.

Example
-------

.. code-block:: bash

    docker run \
      --detach --interactive --tty \
      --network="host" \
      --env ANSYSLMD_LICENSE_FILE=$ANSYSLMD_LICENSE_FILE \
      --volume working-directory:/home/stk/pystk
      --name stk-python3.12 \
      --entrypoint /bin/bash \
      ansys/stk:dev-ubuntu22.04-python3.12

Install PySTK in the container
==============================

With a working directory containing the PySTK wheels and shared as a volume
with the container, it is possible to install the package by running:

.. code-block:: bash

    docker exec \
      --interactive --tty \
      stk-python-3.<minor> \
      /bin/bash -c "cd /home/stk && python -m venv .venv && source .venv/bin/activate && python -m pip install --upgrade pip && python -m pip install -e /home/stk/pystk[tests,doc,visualization]"

where ``<minor>`` is the minor version of Python selected when building the
container.

Running scripts in the container
================================

Save your scripts inside the working directory. Then, execute them by running:

.. code-block:: dosbatch

    docker exec \
      --interactive --tty \
      stk-python-3.<minor> \
      /bin/bash -c "python /home/stk/pystk/<script>"

Where ``<script>`` is the name of the Python script you want to execute.
