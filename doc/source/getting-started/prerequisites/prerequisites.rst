Prerequisites
#############

You can use PySTK locally on Windows and Linux operating systems, or by using Windows-based or Linux-based Docker containers.  

Local Prerequisites
===================

To get started using PySTK locally, the following is required:

- Python
- STK Desktop or STK Engine

Install Python
--------------

A working Python environment using Python version 3.10 or greater is required. You can download and install Python from https://www.python.org/downloads.

Additionally, you can install Jupyter Notebooks by downloading an install from
https://jupyter.org/install.

Install STK Desktop or STK Engine
---------------------------------

STK Desktop or STK Engine must be installed and licensed on your machine.

Install STK Desktop
-------------------

STK desktop is available on Windows platforms. It provides a physics-based modeling environment for analyzing platforms and payloads in a realistic mission context.  Refer to the `STK installation
instructions <https://help.agi.com/stk/Content/install/installingSTK.htm>`_ for details
on installing STK.

Install STK Engine
------------------

STK Engine is available on Windows and Linux platforms. It enables you to build an app that harnesses the analytical power and visual capabilities of STK. 

- For Windows installations, refer to the `STK Engine Installation
instructions <https://help.agi.com/stkdevkit/Content/stkEngine/Getting_Started.htm>`_ for details on installing STK Engine.

- For Linux installations, refer to the `STK Engine Installation
instructions <https://help.agi.com/stkEngineOnUNIX/index.htm#stkEngineUX/Getting_Started_with_EngineOnLinux.htm#Installing>`_ for details on installing STK Engine on Linux.

.. note::

    If using the remote API, modules ``grpcio`` and ``protobuf`` are required. They can be obtained from PyPI and installed using pip.

Docker Prerequisites
====================
You can use PySTK inside a Windows-based Docker container or inside a Linux-based Docker container. To get started, you must have Docker installed on your operation system. Refer to the links below to install Docker on your desired operating system:

- `Install Docker Desktop on Windows <https://docs.docker.com/desktop/install/windows-install/>`_
- `Install Docker Desktop on Linux <https://docs.docker.com/desktop/install/linux/>`_