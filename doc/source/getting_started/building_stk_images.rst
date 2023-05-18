.. _building_stk_images:

Building STK images
###################

PySTK provides various `Dockerfiles`_ to build `Docker images`_ that
containerize STK. Some of these files include additional utilities such us
`Python`_.

All the Dockerfiles are collected in the `docker/ directory`_ of the `PySTK
repository`_. These files are organized according to the operating system,
either Windows or Linux.


.. grid:: 2

    .. grid-item-card:: Dockefiles for Windows :fab:`windows`
        :link: https://github.com/ansys-internal/pystk/tree/doc/examples/docker/windows
        
        Include support for STKEngine and STKDesktop

    .. grid-item-card:: Dockefiles for Linux :fab:`linux`
        :link: https://github.com/ansys-internal/pystk/tree/doc/examples/docker/linux
        

        Include support only for STKEngine


.. note:: 

    PySTK can also attach to a running instance of STK in the host machine.
    However, this feature is only supported when the host machine uses Windows.
    For machines using 


Architecture of Windows and Linux images
========================================

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
        :sync: windows

        .. figure:: https://help.agi.com/stkdevkit/Content/automationTree/images/Windows_Container_Heirarchy.png

    .. tab-item:: STK images for Linux
        :sync: linux

        .. figure:: https://help.agi.com/stkdevkit/Content/automationTree/images/ContainerizationDiagram.png


Building an image
=================

All the images in the `docker/ directory`_ of the repository include:

* ``Dockerfile`` for building the image
* ``docker-compose.yml`` for orchestrating the building
* ``README.rst`` file providing some guidance and instructions


The available images are:

.. jinja:: docker_images

    .. tab-set:: 

        .. tab-item:: Windows
            :sync: windows

            {% for image in windows_images %}
            * {{ image }}
            {% endfor %}

        .. tab-item:: Linux
            :sync: linux

            {% for image in linux_images %}
            * {{ image }}
            {% endfor %}

End of the tab


.. tab-set::

    .. tab-item:: Windows
        :sync: windows

        #. Clone the repository by running ``git clone https://github.com/pyansys/pystk``
        #. Navigate to the ``docker/windows/`` directory
        #. Create a directory named ``distributions/`` inside the ``stk-engine/`` directory
        #. Place the STK artifacts inside the ``stk-engine/distributions/`` folder
        #. Run ``docker-compose build`` to build all the images
        #. To build a single image, run ``docker-compose build <image-name>``

    .. tab-item:: Linux
        :sync: linux

        #. Clone the repository by running ``git clone https://github.com/pyansys/pystk``
        #. Navigate to the ``docker/linux/`` directory
        #. Create a directory named ``distributions/`` inside the ``stk-engine/`` directory
        #. Place the STK artifacts inside the ``stk-engine/distributions/`` folder
        #. Run ``docker-compose build`` to build all the images
        #. To build a single image, run ``docker-compose build <image-name>``


Running an image
================


