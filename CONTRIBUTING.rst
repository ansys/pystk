Contributing
############

Using Tox for testing and development
=====================================

`Tox <https://tox.wiki>`_ is a powerful tool that simplifies and automates the
process of testing and developing your project across multiple environments. It
allows you to define test environments, run tests, and perform various
development tasks in a consistent and reproducible manner. Tox is particularly
useful for ensuring that your project works seamlessly on different Python
versions, interpreters, and platforms.

Installing Tox
--------------

To install Tox, you can use the following command:

.. code-block:: console

    python -m pip install tox

You can verify the installation by running:

.. code-block:: console

   tox --version


Listing Tox environments
------------------------

The configuration for Tox is stored in `the tox.ini file
<https://github.com/ansys-internal/pystk/blob/main/tox.ini>`_. This file
contains various environments. Environments are a collection of commands
executed depending on the platform and the environment.

To list all Tox environments, you can use the following command:

.. code-block:: console

    tox list

Building STK images with Tox
----------------------------

You can build all the Docker images for STK. Two platforms are supported, Linux
and Windows. Use the following command according to your platform:

+----------+---------------------------------+
| Platform | Command                         |
+==========+=================================+
| Linux    | ``tox -e docker-build-linux``   |
| Windows  | ``tox -e docker-build-windows`` |
+----------+---------------------------------+

Running STK containers with Tox
-------------------------------

Once the images are built, you can create a new container using the following
command:

+----------+------------------------------------------------+
| Platform | Command                                        |
+==========+================================================+
| Linux    | ``tox -e docker-run-linux-{py38,py39,py310}``  |
| Windows  | `tox -e docker-run-windows-{py38,py39,py310}`` |
+----------+------------------------------------------------+

In previous command, you need to select the Python version you want to
use.

Launching Jupyter Lab with Tox
------------------------------

Stopping STK containers with Tox
-----------------------------------

Removing STK containers with Tox
-----------------------------------



Additional documentation
========================

For additional documentation refer to the
`PyAnsys Developer's Guide <https://dev.docs.pyansys.com/index.html>`_.
