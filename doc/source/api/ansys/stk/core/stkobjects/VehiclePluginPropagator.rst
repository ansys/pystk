VehiclePluginPropagator
=======================

.. py:class:: ansys.stk.core.stkobjects.VehiclePluginPropagator

   Class defining a propagator plugin for HPOP for customization of the accelerations used in the propagation of the satellite trajectory.

.. py:currentmodule:: VehiclePluginPropagator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePluginPropagator.get_raw_plugin_object`
              - Get a raw pointer to the instance of the plugin.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePluginPropagator.apply_plugin_changes`
              - Apply the changes made to the plugin's configuration.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePluginPropagator.use_plugin`
              - Opt whether to use a plugin.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePluginPropagator.plugin_name`
              - Get or set the complete name of the plugin.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePluginPropagator.plugin_settings`
              - Get the parameters of the selected plugin.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePluginPropagator.available_plugins`
              - Get the list of all the available plugins.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehiclePluginPropagator


Property detail
---------------

.. py:property:: use_plugin
    :canonical: ansys.stk.core.stkobjects.VehiclePluginPropagator.use_plugin
    :type: bool

    Opt whether to use a plugin.

.. py:property:: plugin_name
    :canonical: ansys.stk.core.stkobjects.VehiclePluginPropagator.plugin_name
    :type: str

    Get or set the complete name of the plugin.

.. py:property:: plugin_settings
    :canonical: ansys.stk.core.stkobjects.VehiclePluginPropagator.plugin_settings
    :type: VehiclePluginSettings

    Get the parameters of the selected plugin.

.. py:property:: available_plugins
    :canonical: ansys.stk.core.stkobjects.VehiclePluginPropagator.available_plugins
    :type: list

    Get the list of all the available plugins.


Method detail
-------------






.. py:method:: get_raw_plugin_object(self) -> typing.Any
    :canonical: ansys.stk.core.stkobjects.VehiclePluginPropagator.get_raw_plugin_object

    Get a raw pointer to the instance of the plugin.

    :Returns:

        :obj:`~typing.Any`

.. py:method:: apply_plugin_changes(self) -> None
    :canonical: ansys.stk.core.stkobjects.VehiclePluginPropagator.apply_plugin_changes

    Apply the changes made to the plugin's configuration.

    :Returns:

        :obj:`~None`


