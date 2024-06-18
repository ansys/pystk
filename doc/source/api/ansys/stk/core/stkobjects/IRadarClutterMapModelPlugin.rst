IRadarClutterMapModelPlugin
===========================

.. py:class:: IRadarClutterMapModelPlugin

   object
   
   Do not use this interface, as it is deprecated. Use IAgScatteringPointModelPlugin interface instead. Provides access to the properties and methods defining a radar clutter map plugin model.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~plugin_configuration`
            * - :py:meth:`~raw_plugin_object`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarClutterMapModelPlugin


Property detail
---------------

.. py:property:: plugin_configuration
    :canonical: ansys.stk.core.stkobjects.IRadarClutterMapModelPlugin.plugin_configuration
    :type: "IAgCRPluginConfiguration"

    This property is deprecated. Use PluginConfiguration on IAgScatteringPointModelPlugin instead. Gets the plugin configuration interface.

.. py:property:: raw_plugin_object
    :canonical: ansys.stk.core.stkobjects.IRadarClutterMapModelPlugin.raw_plugin_object
    :type: typing.Any

    This property is deprecated. Use RawPluginObject on IAgScatteringPointModelPlugin instead. Gets the raw plugin IUnknown interface.


