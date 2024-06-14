IAttitudeControlFinitePlugin
============================

.. py:class:: IAttitudeControlFinitePlugin

   IAttitudeControlFinite
   
   Properties for the Plugin attitude control for a Finite Maneuver.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~select_plugin_by_name`
              - Select plugin using the plugin name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~plugin_name`
            * - :py:meth:`~plugin_config`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IAttitudeControlFinitePlugin


Property detail
---------------

.. py:property:: plugin_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlFinitePlugin.plugin_name
    :type: str

    Get the selected plugin's name.

.. py:property:: plugin_config
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlFinitePlugin.plugin_config
    :type: "IAgVAPluginProperties"

    Get the properties of the selected plugin.


Method detail
-------------

.. py:method:: select_plugin_by_name(self, name:str) -> None

    Select plugin using the plugin name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`



