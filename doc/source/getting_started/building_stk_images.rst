Building an STK image from a Dockerfile
#######################################

PySTK provides various `Dockerfiles`_ to build `Docker images`_ that
containerize STK and can include some additional utilities such us `Python`_ and
`Jupyter Lab`_.

All the Dockerfiles are collected in the `docker/ directory`_ of the `PySTK
repository`_. These files are organized according to the operating system,
either Windows or Linux.


.. grid:: 2

    .. grid-item-card:: Dockefiles for Windows :fab:`windows`
        :link: https://github.com/pyansys/pystk/tree/doc/examples/docker/windows
        
        Include support for STKEngine and STKDesktop

    .. grid-item-card:: Dockefiles for Linux :fab:`linux`
        :link: https://github.com/pyansys/pystk/tree/doc/examples/docker/linux
        

        Include support only for STKEngine


Windows and Linux images
========================

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

        .. figure:: https://help.agi.com/stkdevkit/Content/automationTree/images/Windows_Container_Heirarchy.png

    .. tab-item:: STK images for Linux

        .. figure:: https://help.agi.com/stkdevkit/Content/automationTree/images/ContainerizationDiagram.png


Building an image
=================

All the images in the `docker/ directory` include:

* A `Dockerfile`_ for building the image
* A `docker-compose.yml`_ for orchestrating the building
* A `README.rst` file providing some guidance and instructions


.. dropdown:: Requirements for building an STK image
    :animate: fade-in-slide-down

    * `Docker Engine`_
    * `Docker Compose`_
    * `STK distribution artifacts`_

Make sure you have installed 

To simplify the 
