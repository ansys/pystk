IProjectionRasterStreamPluginActivatorFactory
=============================================

.. py:class:: IProjectionRasterStreamPluginActivatorFactory

   object
   
   The Activator class provides methods to load COM plugins that implement projection and raster streaming. For more information about the projection and raster plugins, see the STK Programming Interface.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~initialize`
              - Initialize a new instance of the Activator type.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IProjectionRasterStreamPluginActivatorFactory



Method detail
-------------

.. py:method:: initialize(self) -> IProjectionRasterStreamPluginActivator
    :canonical: ansys.stk.core.graphics.IProjectionRasterStreamPluginActivatorFactory.initialize

    Initialize a new instance of the Activator type.

    :Returns:

        :obj:`~IProjectionRasterStreamPluginActivator`

