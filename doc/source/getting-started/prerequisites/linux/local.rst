Linux local prerequisites
#########################

To get started using PySTK with Linux, the following is required:

- Your machine meets the minimum system requirements
- Python
- STK Engine installation


Minimum system requirements
===========================

The following table lists the specific distributions and versions tested, and for which installation directions are provided. Other Linux distributions are likely to work as well, assuming the required dependencies are installed and available.

.. list-table::
    :widths: auto
    :header-rows: 1

    * - **Operating system**
      - **Latest update or service pack tested**

    * - Red Hat Enterprise Linux / Rocky
      - 8.9

    * - Ubuntu Desktop
      - 22.04

Hardware and software requirements
----------------------------------

The following table lists the hardware and software requirements.

.. list-table::
    :widths: auto
    :header-rows: 1

    * - **Hardware/Software**
      - **Requirements**

    * - Development disk space
      - 1.76 GB

    * - Deployment disk space
      - 1.25 GB minimum, possibly more depending on specific application requirements
	 
	* - OpenGL / Video card
      - 
        * Desktop Application High-end, OpenGL-compatible card (512+ MB RAM) that supports OpenGL 2.0+. Note that it is possible for Nouveau drivers, which are the default NVidia drivers on Ubuntu Linux, to cause STK to terminate when using STK in graphics mode. If this problem occurs, it is recommended that you install the proprietary NVidia drivers.
	    * Compute Node, with graphics - OpenGL 1.1+ using mesa software driver (possibly provided by xvfb)
		* Compute Node, no graphics - No video card/GPU requirement, OpenGL not used

    * - Python
      - Python version 3.6 or greater (Required if developing a Python application) and the Python API
	  
	* - libstdc++.so
      - 6.0.19 minimum

    * - Fortran Runtime
      - The 64-bit version of libgfortran.so.5 is required only for Fortran-dependent features, such as Astrogator SNOPT/IPOPT Search Profile plugins, VOACAP, and the IRI2016 Ionosphere library. Note that you can use the following commands to find the package that provides a library: RHEL/Rocky: `yum` what provides libgfortran.so.5. On the Ubuntu website, you can search the 'Ubuntu Packages Search' page at https://packages.ubuntu.com/ for the contents of the packages by providing the file name (e.g., libgfortran.so.5) as a keyword.
	  
	* - MODTRAN
      - The 6.0.2.3 version of MODTRAN is required only if you wish to use Spectral Science Inc.'s MODTRAN atmospheric model for optical, infared, and ultra-violet frequencies.

Video card considerations
^^^^^^^^^^^^^^^^^^^^^^^^^

If you are developing an interactive desktop application that integrates the STK Engine 2D and 3D controls, the following recommendations apply to the video card:

- STK uses OpenGL for all 2D and 3D rendering. For best rendering performance, high-end OpenGL-compatible cards (512+ MB RAM) that support OpenGL 2.0+ are recommended.

- For optimal performance, it is critical that the drivers for the video card be kept up to date. A good practice to follow is to update video drivers whenever the version of STK is updated.

- STK will automatically use OpenGL 1.1 on systems that do not support OpenGL 1.2 extensions. Some capabilities will not be available.

- Video cards based on chipsets from NVidia have shown excellent performance and compatibility with STK.

Supplementary data requirements
-------------------------------

.. list-table::
    :widths: auto
    :header-rows: 1

    * - **Supplementary data**
      - **Requirement**

    * - AGI Planetary Data
      - 542 MB

    * - World Terrain
      - 252 MB

    * - MODTRAN data
      - 357 MB


Install Python
==============

A working Python environment using Python version 3.10 or greater is required. You can download and install Python from https://www.python.org/downloads.

Additionally, you can install Jupyter Notebooks by downloading an install from
https://jupyter.org/install.


STK Engine installation
=======================

STK Engine enables you to build an app that harnesses the analytical power and visual capabilities of STK. Refer to the `STK Engine Installation
instructions <https://help.agi.com/stkdevkit/Content/stkEngine/Getting_Started.htm>`_ for details on installing STK Engine.

.. note::

    If using the remote API, modules ``grpcio`` and ``protobuf`` are required. They can be obtained from PyPI and installed using pip.
