IRadarClutterGeometryModelPlugin
================================

.. py:class:: ansys.stk.core.stkobjects.IRadarClutterGeometryModelPlugin

   Do not use this interface, as it is deprecated. Use IAgScatteringPointProviderPlugin interface instead. Provides access to the properties and methods defining a radar clutter geometry plugin model.

.. py:currentmodule:: IRadarClutterGeometryModelPlugin

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarClutterGeometryModelPlugin.plugin_configuration`
              - This property is deprecated. Use PluginConfiguration on IAgScatteringPointProviderPlugin instead. Gets the plugin configuration interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarClutterGeometryModelPlugin.raw_plugin_object`
              - This property is deprecated. Use RawPluginObject on IAgScatteringPointProviderPlugin instead. Gets the raw plugin IUnknown interface.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarClutterGeometryModelPlugin


Property detail
---------------

.. py:property:: plugin_configuration
    :canonical: ansys.stk.core.stkobjects.IRadarClutterGeometryModelPlugin.plugin_configuration
    :type: CRPluginConfiguration

    This property is deprecated. Use PluginConfiguration on IAgScatteringPointProviderPlugin instead. Gets the plugin configuration interface.

.. py:property:: raw_plugin_object
    :canonical: ansys.stk.core.stkobjects.IRadarClutterGeometryModelPlugin.raw_plugin_object
    :type: typing.Any

    This property is deprecated. Use RawPluginObject on IAgScatteringPointProviderPlugin instead. Gets the raw plugin IUnknown interface.


