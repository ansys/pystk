Getting Started with the STK Python API
=======================================

About the STK Python API
------------------------

Historically interacting with STK Desktop and STK Engine from Python has
been achieved using the `win32com <https://pypi.org/project/pywin32/>`__
or `comtypes <https://pypi.org/project/comtypes/>`__ Python modules.
While these methods still work and are still supported, the STK Python
API offers the following advantages:

-  **Cross-platform support**: Code written using the new API
   interacting with STK Engine can be used on Windows and on Linux
   without modifications, assuming the usual cross platform Python
   guidelines are followed.

-  **Usability improvements**:

      -  STK object model types have built-in support for the Python
         help function.
      -  The new API provides definitions for all enumerations. With
         win32com, enumerations had to be defined manually based on the
         corresponding numerical value.
      -  Better IDE support through type hints (based on the
         `typing <https://docs.python.org/3/library/typing.html>`__
         module).

      **Remotable API using gRPC**: In addition to traditional OLE
      communication with STK, the STK Python API has optional gRPC
      communication for out-of-process or remote interaction with STK.

Prerequisites
-------------

The instructions in this section assume that you have a working Python
environment on your machine. Python version3.8 or greater is required.
You can download and install Python from
https://www.python.org/downloads.

You can install Jupyter Notebooks by downloading an install from
https://jupyter.org/install.

It is also assumed that STK or STK Engine is properly installed and
licensed. Refer to the `STK Installation
instructions <https://help.agi.com/stk/index.htm#install/installingSTK.htm>`__\ `STK
Installation
instructions <../../../Content/install/installingSTK.htm>`__ for details
on installing STK. It is also assumed that STK Engine is properly
installed and licensed. refer to the `Installation
instructions <../stkEngineUX/Getting_Started_with_EngineOnLinux.htm#Installing>`__.

If using the remotable API, modules grpcio and protobuf are required.
They can be obtained from PyPI and installed using pip.

Install the wheel file
----------------------

The STK Python API is packaged as a wheel file that can be installed
using pip. The wheel file is included with the STK install in the
bin/AgPythonAPI directory.

Using pip may require an SSL certification, please contact your system
administration to provide this file.

.. container:: cmdPrompt

   python -m pip install "<STK installation
   directory>/bin/AgPythonAPI/agi.stk--py3-none-any.whl"

Verify the installation
-----------------------

The final step to ensure a working development setup is to run a simple
program that exercises the API. In a Python file, copy and paste the
code below and run it. Everything is set up for developing applications
with STK.

.. container:: LanguageSpecific
   :name: Example_Python

   +-----------------------------------+-----------------------------------+
   | [Python - STK API]                |                                   |
   +===================================+===================================+
   | .. container:: LanguageSpecific   |                                   |
   |    :name: Code_Python             |                                   |
   |                                   |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   |                                   |                                   |
   |  | ``from agi.stk.              | |                                   |
   |                                   |                                   |
   |  | stkengine import STKEngine`` | |                                   |
   |                                   |                                   |
   |  | ``stk = STKEngine.StartAp    | |                                   |
   |                                   |                                   |
   |  | plication(noGraphics=True)`` | |                                   |
   |                                   |                                   |
   |  | ``print(stk.Version)``       | |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   +-----------------------------------+-----------------------------------+

This will print the version of STK currently installed on your machine.

Install Jupyter Notebooks
-------------------------

Using a command line you can install Jupyter Notebooks:

.. container:: cmdPrompt

   python -m pip install notebook

If you want to launch Jupyter Notebooks, you need to do that outside of
STK.

Next steps
----------

Once you have completed the `installation <#InstallWheelFile>`__, refer
to the `Programmer’s Guide <pythonProgrammingGuide.htm>`__ as needed. If
you have existing Python scripts using win32com or comtypes, refer to
the `Migration Guide <pythonMigrationGuide.htm>`__.
