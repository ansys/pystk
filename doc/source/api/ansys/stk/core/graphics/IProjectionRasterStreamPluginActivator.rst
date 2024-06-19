IProjectionRasterStreamPluginActivator
======================================

.. py:class:: IProjectionRasterStreamPluginActivator

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

            * - :py:meth:`~create_from_display_name`
              - Load a projection/raster COM plugin associated with the specified display name and returns a proxy object that allows accessing the raster and projection streams implemented by the plugin.
            * - :py:meth:`~get_available_display_names`
              - Get a list of available projection/raster plugins' Display Names (Programmatic Identifiers).


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IProjectionRasterStreamPluginActivator



Method detail
-------------

.. py:method:: create_from_display_name(self, displayName: str) -> IProjectionRasterStreamPluginProxy
    :canonical: ansys.stk.core.graphics.IProjectionRasterStreamPluginActivator.create_from_display_name

    Load a projection/raster COM plugin associated with the specified display name and returns a proxy object that allows accessing the raster and projection streams implemented by the plugin.

    :Parameters:

    **displayName** : :obj:`~str`

    :Returns:

        :obj:`~IProjectionRasterStreamPluginProxy`

.. py:method:: get_available_display_names(self) -> list
    :canonical: ansys.stk.core.graphics.IProjectionRasterStreamPluginActivator.get_available_display_names

    Get a list of available projection/raster plugins' Display Names (Programmatic Identifiers).

    :Returns:

        :obj:`~list`

