Prerequisites
#############

You can use PySTK locally on Windows and Linux operating systems, or by using Windows-based or Linux-based Docker containers.  

Local prerequisites
===================

To get started using PySTK locally, the following is required:

- Python 
- A licensed version of the Ansys STK® desktop application or STK Engine

Install Python
^^^^^^^^^^^^^^

.. jinja::
    
    A working Python environment using Python version {{ SUPPORTED_PYTHON_VERSIONS[0] }} or greater is required. You can download and install Python from https://www.python.org/downloads.

Additionally, you can install Jupyter Notebooks by downloading an install from
https://jupyter.org/install.

.. note::

    If using the remote API, modules ``grpcio`` and ``protobuf`` are required. They can be obtained from PyPI and installed using pip.

Install the STK Desktop application or STK Engine
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The STK desktop application or STK Engine must be installed and licensed on your machine.

Install the STK Desktop application
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

STK desktop software is available on Windows platforms. It provides a physics-based modeling environment for analyzing platforms and payloads in a realistic mission context. Refer to the `STK installation instructions <https://help.agi.com/stk/Content/install/installingSTK.htm>`_ for details on installing the STK application.

.. note::

    Once installed, refer to the `Licensing STK help topic <https://help.agi.com/stk/Content/licensing/licensing.htm>`_ for information on licensing STK software.

Install STK Engine
^^^^^^^^^^^^^^^^^^

STK Engine is available on Windows and Linux platforms. It enables you to build an app that harnesses the analytical power and visual capabilities of the STK application. 

- For Windows installations, refer to the `STK Engine installation instructions <https://help.agi.com/stkdevkit/Content/stkEngine/Getting_Started.htm>`_ for details on installing STK Engine. 

- For Linux installations, refer to the `STK Engine on Linux installation instructions <https://help.agi.com/stkEngineOnUNIX/Content/stkEngineUX/Getting_Started_with_EngineOnLinux.htm>`_ for details on installing STK Engine on Linux. 

.. note::

    Once installed, refer to the `Obtaining and registering AGI licenses help topic <https://help.agi.com/stkEngineOnUNIX/Content/stkEngineUX/Getting_Started_with_EngineOnLinux.htm>`_ and navigate to the Obtaining and Registering AGI Licenses section for information on licensing STK Engine.

Docker prerequisites
====================
You can use PySTK inside a Windows-based Docker container or inside a Linux-based Docker container. To get started, you must have Docker installed. Refer to the links below to install Docker on your desired operating system:

- `Install Docker Desktop on Windows <https://docs.docker.com/desktop/install/windows-install/>`_  
- `Install Docker Desktop on Linux <https://docs.docker.com/desktop/install/linux/>`_   



