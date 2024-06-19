IVehicleHPOPDragModelPlugin
===========================

.. py:class:: IVehicleHPOPDragModelPlugin

   IVehicleHPOPDragModel
   
   Plugin Drag Model.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~plugin_name`
            * - :py:meth:`~plugin_settings`
            * - :py:meth:`~available_plugins`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleHPOPDragModelPlugin


Property detail
---------------

.. py:property:: plugin_name
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPDragModelPlugin.plugin_name
    :type: str

    Gets or sets the complete name of the plugin.

.. py:property:: plugin_settings
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPDragModelPlugin.plugin_settings
    :type: IAgVeHPOPDragModelPluginSettings

    Get the parameters of the selected plugin.

.. py:property:: available_plugins
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPDragModelPlugin.available_plugins
    :type: list

    Get the list of all the available plugins.


