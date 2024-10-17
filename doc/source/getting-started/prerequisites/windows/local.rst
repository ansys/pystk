Windows local prerequisites
###########################

To get started using PySTK with Windows, the following is required:

- Python
- STK Desktop or STK Engine

Install Python
==============

A working Python environment using Python version 3.10 or greater is required. You can download and install Python from https://www.python.org/downloads.

Additionally, you can install Jupyter Notebooks by downloading an install from
https://jupyter.org/install.

Install STK Desktop or STK Engine
=================================

STK Desktop or STK Engine must be installed and licensed on your machine.

STK Desktop
-----------

STK desktop provides a physics-based modeling environment for analyzing platforms and payloads in a realistic mission context. Refer to the `STK installation
instructions <https://help.agi.com/stk/Content/install/installingSTK.htm>`_ for details
on installing STK.

STK Engine
----------

STK Engine enables you to build an app that harnesses the analytical power and visual capabilities of STK. Refer to the `STK Engine Installation
instructions <https://help.agi.com/stkdevkit/Content/stkEngine/Getting_Started.htm>`_ for details on installing STK Engine.


.. note::

    If using the remote API, modules ``grpcio`` and ``protobuf`` are required. They can be obtained from PyPI and installed using pip.

