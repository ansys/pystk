Install PySTK in a Windows container
####################################

This guideline covers the  installation of PySTK inside a Windows-based Docker
container.

Download Windows Docker images
==============================

Start by downloading the PySTK Docker images for Windows. The images contain
the latest three stable version of Python.

.. jinja:: docker_images

    .. list-table::
        :widths: auto

        * - **Artifact**
          - `Windows Docker Images <../../../_static/docker/{{ windows_images }}>`_
        * - **Size**
          - {{ windows_images_size }}
        * - **SHA-256**
          - {{ windows_images_hash }}

Download Windows STK Engine artifacts
=====================================

Download the ``STK Engine`` and ``STK Engine Deployment Resources`` artifacts for
Windows platforms from the `https://support.agi.com/downloads
<https://support.agi.com/downloads>`_ page.

Use STK artifacts with Docker images
====================================

Place the AGI STK artifacts inside a directory named `distributions` contained
inside of the `docker/windows/stk-engine`.

.. code-block:: dosbatch

    docker/windows/
    ├── docker-compose.yml
    ├── stk-engine
    │   └── distributions/
    │          └── Place STK Engine artifacts here
    ├── stk-engine-py310
    ├── stk-engine-py311
    ├── stk-engine-py312
    └── stk-engine-pybase

Build Windows Docker images
===========================

Navigate to the ``docker/windows`` directory and use `Docker Compose`_ to build
the image of your choice. Select one of ``docker-engine-py3<minor>`` and run the following command:

.. code-block:: dosbatch

    docker compose build stk-engine-py3<minor>

where ``<minor>`` is one of the minor versions of Python.

Download PySTK wheels for Windows
=================================

Download the PySTK wheels for Windows.

.. jinja:: artifacts

    .. list-table::
        :widths: auto

        * - **Artifact**
          - `{{ wheels }} <_static/artifacts/{{ wheels }}>`_
        * - **Size**
          - {{ wheels_size }}
        * - **SHA-256**
          - {{ wheels_hash }}

Create a working directory
==========================

Create a working directory in your host machine. This directory will be used a
shared volume with the Docker container. Place previously downloaded wheels for
PySTK in this directory.

.. jinja:: artifacts

    .. code-block:: dosbatch
    
        working-directory/
        └── {{ wheels }}

Configure the license
=====================

Open a terminal in your working directory. Make sure you have set the
``ANSYSLMD_LICENSE_FILE`` environment variable by running:

.. tab-set-code::

    .. code-block:: dosbatch
    
        set ANSYSLMD_LICENSE_FILE=<PORT>@<LICENSE_SERVER_IP>

    .. code-block:: PowerShell

        $env:ANSYSLMD_LICENSE_FILE=<PORT>@<LICENSE_SERVER_IP>

where ``PORT`` usually takes the value of ``1055`` and ``LICENSE_SERVER_IP`` is
the Internet Protocol (IP) of the machine hosting the license server.

Start a container
=================

With the artifacts and the license in place, start a Docker container and share
the working directory as a volume. This allows to write scripts using the tools
in the host machine while isolating their execution inside the container.

Start a new container by running:

.. code-block:: text

    docker run \
      --detach --interactive --tty \
      --network="host" \
      --env ANSYSLMD_LICENSE_FILE=$ANSYSLMD_LICENSE_FILE \
      --name <container-name> \
      --entrypoint <entrypoint> \
      <image-name>

Previous options are:

- ``--detach`` Runs the container in detached mode, enabling it to run in the background.
- ``--interactive`` Enables interactive mode, providing a TTY session for connecting to the container.
- ``--tty`` Allocates a pseudo-TTY, ensuring proper formatting and display of the container's output.
- ``--network="host"`` Shares the host's network stack with the container, enabling network connectivity.
- ``--env ANSYSLMD_LICENSE_FILE=$ANSYSLMD_LICENSE_FILE`` Specifies environment variable(s) to be shared with the container.
- ``--name <container-name>`` Assigns a name to the container for easy identification and reference.
- ``--entrypoint <entrypoint>`` Defines the command or script to be executed when the container starts.
- ``<image-name>`` Specifies the name or ID of the Docker image to be used for creating the container.


    










