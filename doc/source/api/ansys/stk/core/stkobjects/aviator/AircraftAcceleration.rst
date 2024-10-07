AircraftAcceleration
====================

.. py:class:: ansys.stk.core.stkobjects.aviator.AircraftAcceleration

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogItem`

   Class defining the aircraft acceleration category of an Aviator aircraft.

.. py:currentmodule:: AircraftAcceleration

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAcceleration.get_built_in_model`
              - Get the built-in model.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAcceleration.get_basic_acceleration_by_name`
              - Get the basic acceleration model with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAcceleration.get_advanced_acceleration_by_name`
              - Get the advanced acceleration model with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAcceleration.get_as_catalog_item`
              - Get the catalog item interface for this object.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AircraftAcceleration



Method detail
-------------

.. py:method:: get_built_in_model(self) -> AircraftBasicAccelerationModel
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAcceleration.get_built_in_model

    Get the built-in model.

    :Returns:

        :obj:`~AircraftBasicAccelerationModel`

.. py:method:: get_basic_acceleration_by_name(self, name: str) -> AircraftBasicAccelerationModel
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAcceleration.get_basic_acceleration_by_name

    Get the basic acceleration model with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~AircraftBasicAccelerationModel`

.. py:method:: get_advanced_acceleration_by_name(self, name: str) -> AircraftAdvancedAccelerationModel
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAcceleration.get_advanced_acceleration_by_name

    Get the advanced acceleration model with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~AircraftAdvancedAccelerationModel`

.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAcceleration.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`

