IVehiclePluginPropagator
========================

.. py:class:: ansys.stk.core.stkobjects.IVehiclePluginPropagator

   object
   
   Interface for propagator plugin.

.. py:currentmodule:: IVehiclePluginPropagator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePluginPropagator.get_raw_plugin_object`
              - Get a raw pointer to the instance of the plugin.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePluginPropagator.apply_plugin_changes`
              - Apply the changes made to the plugin's configuration.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePluginPropagator.use_plugin`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePluginPropagator.plugin_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePluginPropagator.plugin_settings`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePluginPropagator.available_plugins`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehiclePluginPropagator


Property detail
---------------

.. py:property:: use_plugin
    :canonical: ansys.stk.core.stkobjects.IVehiclePluginPropagator.use_plugin
    :type: bool

    Opt whether to use a plugin.

.. py:property:: plugin_name
    :canonical: ansys.stk.core.stkobjects.IVehiclePluginPropagator.plugin_name
    :type: str

    Gets or sets the complete name of the plugin.

.. py:property:: plugin_settings
    :canonical: ansys.stk.core.stkobjects.IVehiclePluginPropagator.plugin_settings
    :type: IVehiclePluginSettings

    Get the parameters of the selected plugin.

.. py:property:: available_plugins
    :canonical: ansys.stk.core.stkobjects.IVehiclePluginPropagator.available_plugins
    :type: list

    Get the list of all the available plugins.


Method detail
-------------






.. py:method:: get_raw_plugin_object(self) -> typing.Any
    :canonical: ansys.stk.core.stkobjects.IVehiclePluginPropagator.get_raw_plugin_object

    Get a raw pointer to the instance of the plugin.

    :Returns:

        :obj:`~typing.Any`

.. py:method:: apply_plugin_changes(self) -> None
    :canonical: ansys.stk.core.stkobjects.IVehiclePluginPropagator.apply_plugin_changes

    Apply the changes made to the plugin's configuration.

    :Returns:

        :obj:`~None`


