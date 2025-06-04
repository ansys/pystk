AircraftClimb
=============

.. py:class:: ansys.stk.core.stkobjects.aviator.AircraftClimb

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogItem`

   Class defining the aircraft climb category of an Aviator aircraft.

.. py:currentmodule:: AircraftClimb

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftClimb.get_built_in_model`
              - Get the built-in model.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftClimb.get_basic_climb_by_name`
              - Get the basic climb model with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftClimb.get_advanced_climb_by_name`
              - Get the advanced climb model with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftClimb.get_as_catalog_item`
              - Get the catalog item interface for this object.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AircraftClimb



Method detail
-------------

.. py:method:: get_built_in_model(self) -> AircraftBasicClimbModel
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftClimb.get_built_in_model

    Get the built-in model.

    :Returns:

        :obj:`~AircraftBasicClimbModel`

.. py:method:: get_basic_climb_by_name(self, name: str) -> AircraftBasicClimbModel
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftClimb.get_basic_climb_by_name

    Get the basic climb model with the given name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~AircraftBasicClimbModel`

.. py:method:: get_advanced_climb_by_name(self, name: str) -> AircraftAdvancedClimbModel
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftClimb.get_advanced_climb_by_name

    Get the advanced climb model with the given name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~AircraftAdvancedClimbModel`

.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftClimb.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`

