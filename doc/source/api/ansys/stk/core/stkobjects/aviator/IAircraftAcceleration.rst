IAircraftAcceleration
=====================

.. py:class:: IAircraftAcceleration

   object
   
   Interface used to access the acceleration options for an aircraft in the Aviator catalog.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~get_built_in_model`
              - Get the built-in model.
            * - :py:meth:`~get_basic_acceleration_by_name`
              - Get the basic acceleration model with the given name.
            * - :py:meth:`~get_advanced_acceleration_by_name`
              - Get the advanced acceleration model with the given name.
            * - :py:meth:`~get_as_catalog_item`
              - Get the catalog item interface for this object.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAircraftAcceleration



Method detail
-------------

.. py:method:: get_built_in_model(self) -> IAircraftBasicAccelerationModel
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAcceleration.get_built_in_model

    Get the built-in model.

    :Returns:

        :obj:`~IAircraftBasicAccelerationModel`

.. py:method:: get_basic_acceleration_by_name(self, name: str) -> IAircraftBasicAccelerationModel
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAcceleration.get_basic_acceleration_by_name

    Get the basic acceleration model with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IAircraftBasicAccelerationModel`

.. py:method:: get_advanced_acceleration_by_name(self, name: str) -> IAircraftAdvancedAccelerationModel
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAcceleration.get_advanced_acceleration_by_name

    Get the advanced acceleration model with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IAircraftAdvancedAccelerationModel`

.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAcceleration.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`

