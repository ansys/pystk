IAircraftModel
==============

.. py:class:: IAircraftModel

   object
   
   Interface used to access the aircraft options in the Aviator catalog.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~get_as_catalog_item`
              - Get the catalog item interface for this object.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~perf_model_types`
            * - :py:meth:`~acceleration`
            * - :py:meth:`~climb`
            * - :py:meth:`~cruise`
            * - :py:meth:`~descent`
            * - :py:meth:`~landing`
            * - :py:meth:`~takeoff`
            * - :py:meth:`~default_configuration`
            * - :py:meth:`~advanced_fixed_wing_tool`
            * - :py:meth:`~vtol`
            * - :py:meth:`~terrain_follow`


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
    :type: IAgAvtrAircraftAcceleration

    Get the acceleration interface.

.. py:property:: climb
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftModel.climb
    :type: IAgAvtrAircraftClimb

    Get the climb interface.

.. py:property:: cruise
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftModel.cruise
    :type: IAgAvtrAircraftCruise

    Get the cruise interface.

.. py:property:: descent
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftModel.descent
    :type: IAgAvtrAircraftDescent

    Get the descent interface.

.. py:property:: landing
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftModel.landing
    :type: IAgAvtrAircraftLanding

    Get the landing interface.

.. py:property:: takeoff
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftModel.takeoff
    :type: IAgAvtrAircraftTakeoff

    Get the takeoff interface.

.. py:property:: default_configuration
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftModel.default_configuration
    :type: IAgAvtrConfiguration

    Get the aircraft's default configuration as saved in the catalog.

.. py:property:: advanced_fixed_wing_tool
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftModel.advanced_fixed_wing_tool
    :type: IAgAvtrAdvFixedWingTool

    Get the Advanced Fixed Wing Tool for the aircraft.

.. py:property:: vtol
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftModel.vtol
    :type: IAgAvtrAircraftVTOL

    Get the VTOL interface.

.. py:property:: terrain_follow
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftModel.terrain_follow
    :type: IAgAvtrAircraftTerrainFollow

    Get the TerrainFollow interface.


Method detail
-------------










.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftModel.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`



