IProjectionRasterStreamPluginProxy
==================================

.. py:class:: IProjectionRasterStreamPluginProxy

   object
   
   A proxy class provides access to the raster and projection streams implemented by a plugin. Proxies are instantiated using projection raster stream plugin activator.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~raster_stream`
            * - :py:meth:`~projection_stream`
            * - :py:meth:`~is_raster_stream_supported`
            * - :py:meth:`~is_projection_stream_supported`
            * - :py:meth:`~real_plugin_object`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IProjectionRasterStreamPluginProxy


Property detail
---------------

.. py:property:: raster_stream
    :canonical: ansys.stk.core.graphics.IProjectionRasterStreamPluginProxy.raster_stream
    :type: "IAgStkGraphicsRasterStream"

    Returns a raster stream.

.. py:property:: projection_stream
    :canonical: ansys.stk.core.graphics.IProjectionRasterStreamPluginProxy.projection_stream
    :type: "IAgStkGraphicsProjectionStream"

    Returns a projection stream.

.. py:property:: is_raster_stream_supported
    :canonical: ansys.stk.core.graphics.IProjectionRasterStreamPluginProxy.is_raster_stream_supported
    :type: bool

    Returns true if the raster streaming is supported.

.. py:property:: is_projection_stream_supported
    :canonical: ansys.stk.core.graphics.IProjectionRasterStreamPluginProxy.is_projection_stream_supported
    :type: bool

    Returns true if the projection streaming is supported.

.. py:property:: real_plugin_object
    :canonical: ansys.stk.core.graphics.IProjectionRasterStreamPluginProxy.real_plugin_object
    :type: typing.Any

    Returns a pointer to plugin object's IUnknown interface.


