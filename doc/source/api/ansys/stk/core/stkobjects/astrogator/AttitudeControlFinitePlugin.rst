AttitudeControlFinitePlugin
===========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.AttitudeControlFinitePlugin

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFinite`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControl`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The plugin attitude control for a finite maneuver.

.. py:currentmodule:: AttitudeControlFinitePlugin

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFinitePlugin.select_plugin_by_name`
              - Select plugin using the plugin name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFinitePlugin.plugin_name`
              - Get the selected plugin's name.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFinitePlugin.plugin_config`
              - Get the properties of the selected plugin.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import AttitudeControlFinitePlugin


Property detail
---------------

.. py:property:: plugin_name
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFinitePlugin.plugin_name
    :type: str

    Get the selected plugin's name.

.. py:property:: plugin_config
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFinitePlugin.plugin_config
    :type: IPluginProperties

    Get the properties of the selected plugin.


Method detail
-------------

.. py:method:: select_plugin_by_name(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFinitePlugin.select_plugin_by_name

    Select plugin using the plugin name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`



