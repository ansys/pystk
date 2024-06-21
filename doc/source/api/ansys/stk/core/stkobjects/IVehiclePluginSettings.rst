IVehiclePluginSettings
======================

.. py:class:: ansys.stk.core.stkobjects.IVehiclePluginSettings

   object
   
   Interface for HPOP plugin settings.

.. py:currentmodule:: IVehiclePluginSettings

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePluginSettings.get_property`
              - Get a property.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePluginSettings.set_property`
              - Set a property.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePluginSettings.available_properties`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehiclePluginSettings


Property detail
---------------

.. py:property:: available_properties
    :canonical: ansys.stk.core.stkobjects.IVehiclePluginSettings.available_properties
    :type: list

    Available properties.


Method detail
-------------

.. py:method:: get_property(self, path: str) -> typing.Any
    :canonical: ansys.stk.core.stkobjects.IVehiclePluginSettings.get_property

    Get a property.

    :Parameters:

    **path** : :obj:`~str`

    :Returns:

        :obj:`~typing.Any`

.. py:method:: set_property(self, path: str, val: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.IVehiclePluginSettings.set_property

    Set a property.

    :Parameters:

    **path** : :obj:`~str`
    **val** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`


