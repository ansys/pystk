ProjectionRasterStreamPluginActivator
=====================================

.. py:class:: ansys.stk.core.graphics.ProjectionRasterStreamPluginActivator

   The Activator class provides methods to load COM plugins that implement projection and raster streaming. For more information about the projection and raster plugins, see the STK Programming Interface.

.. py:currentmodule:: ProjectionRasterStreamPluginActivator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ProjectionRasterStreamPluginActivator.create_from_display_name`
              - Load a projection/raster COM plugin associated with the specified display name and returns a proxy object that allows accessing the raster and projection streams implemented by the plugin.
            * - :py:attr:`~ansys.stk.core.graphics.ProjectionRasterStreamPluginActivator.get_available_display_names`
              - Get a list of available projection/raster plugins' Display Names (Programmatic Identifiers).


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ProjectionRasterStreamPluginActivator



Method detail
-------------

.. py:method:: create_from_display_name(self, display_name: str) -> ProjectionRasterStreamPluginProxy
    :canonical: ansys.stk.core.graphics.ProjectionRasterStreamPluginActivator.create_from_display_name

    Load a projection/raster COM plugin associated with the specified display name and returns a proxy object that allows accessing the raster and projection streams implemented by the plugin.

    :Parameters:

        **display_name** : :obj:`~str`


    :Returns:

        :obj:`~ProjectionRasterStreamPluginProxy`

.. py:method:: get_available_display_names(self) -> list
    :canonical: ansys.stk.core.graphics.ProjectionRasterStreamPluginActivator.get_available_display_names

    Get a list of available projection/raster plugins' Display Names (Programmatic Identifiers).

    :Returns:

        :obj:`~list`

