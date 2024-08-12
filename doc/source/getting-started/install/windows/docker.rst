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

.. code-block:: text

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

.. code-block:: python

    docker compose build stk-engine-py3<minor>

where ``<minor>`` is one of the minor versions of Python.
