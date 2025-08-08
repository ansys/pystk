ProjectionRasterStreamPluginProxy
=================================

.. py:class:: ansys.stk.core.graphics.ProjectionRasterStreamPluginProxy

   A proxy class provides access to the raster and projection streams implemented by a plugin. Proxies are instantiated using projection raster stream plugin activator.

.. py:currentmodule:: ProjectionRasterStreamPluginProxy

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ProjectionRasterStreamPluginProxy.is_projection_stream_supported`
              - Return true if the projection streaming is supported.
            * - :py:attr:`~ansys.stk.core.graphics.ProjectionRasterStreamPluginProxy.is_raster_stream_supported`
              - Return true if the raster streaming is supported.
            * - :py:attr:`~ansys.stk.core.graphics.ProjectionRasterStreamPluginProxy.projection_stream`
              - Return a projection stream.
            * - :py:attr:`~ansys.stk.core.graphics.ProjectionRasterStreamPluginProxy.raster_stream`
              - Return a raster stream.
            * - :py:attr:`~ansys.stk.core.graphics.ProjectionRasterStreamPluginProxy.real_plugin_object`
              - Return a pointer to plugin object's IUnknown interface.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ProjectionRasterStreamPluginProxy


Property detail
---------------

.. py:property:: is_projection_stream_supported
    :canonical: ansys.stk.core.graphics.ProjectionRasterStreamPluginProxy.is_projection_stream_supported
    :type: bool

    Return true if the projection streaming is supported.

.. py:property:: is_raster_stream_supported
    :canonical: ansys.stk.core.graphics.ProjectionRasterStreamPluginProxy.is_raster_stream_supported
    :type: bool

    Return true if the raster streaming is supported.

.. py:property:: projection_stream
    :canonical: ansys.stk.core.graphics.ProjectionRasterStreamPluginProxy.projection_stream
    :type: ProjectionStream

    Return a projection stream.

.. py:property:: raster_stream
    :canonical: ansys.stk.core.graphics.ProjectionRasterStreamPluginProxy.raster_stream
    :type: IRasterStream

    Return a raster stream.

.. py:property:: real_plugin_object
    :canonical: ansys.stk.core.graphics.ProjectionRasterStreamPluginProxy.real_plugin_object
    :type: typing.Any

    Return a pointer to plugin object's IUnknown interface.


