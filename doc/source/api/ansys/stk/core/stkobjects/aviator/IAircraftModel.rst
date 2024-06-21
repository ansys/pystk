IAircraftModel
==============

.. py:class:: ansys.stk.core.stkobjects.aviator.IAircraftModel

   object
   
   Interface used to access the aircraft options in the Aviator catalog.

.. py:currentmodule:: IAircraftModel

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftModel.get_as_catalog_item`
              - Get the catalog item interface for this object.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftModel.perf_model_types`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftModel.acceleration`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftModel.climb`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftModel.cruise`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftModel.descent`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftModel.landing`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftModel.takeoff`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftModel.default_configuration`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftModel.advanced_fixed_wing_tool`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftModel.vtol`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftModel.terrain_follow`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAircraftModel


Property detail
---------------

.. py:property:: perf_model_types
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftModel.perf_model_types
    :type: list

    Get the types of performance models.

.. py:property:: acceleration
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftModel.acceleration
    :type: IAircraftAcceleration

    Get the acceleration interface.

.. py:property:: climb
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftModel.climb
    :type: IAircraftClimb

    Get the climb interface.

.. py:property:: cruise
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftModel.cruise
    :type: IAircraftCruise

    Get the cruise interface.

.. py:property:: descent
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftModel.descent
    :type: IAircraftDescent

    Get the descent interface.

.. py:property:: landing
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftModel.landing
    :type: IAircraftLanding

    Get the landing interface.

.. py:property:: takeoff
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftModel.takeoff
    :type: IAircraftTakeoff

    Get the takeoff interface.

.. py:property:: default_configuration
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftModel.default_configuration
    :type: IConfiguration

    Get the aircraft's default configuration as saved in the catalog.

.. py:property:: advanced_fixed_wing_tool
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftModel.advanced_fixed_wing_tool
    :type: IAdvancedFixedWingTool

    Get the Advanced Fixed Wing Tool for the aircraft.

.. py:property:: vtol
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftModel.vtol
    :type: IAircraftVTOL

    Get the VTOL interface.

.. py:property:: terrain_follow
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftModel.terrain_follow
    :type: IAircraftTerrainFollow

    Get the TerrainFollow interface.


Method detail
-------------










.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftModel.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`



