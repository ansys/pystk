IAircraftProp
=============

.. py:class:: ansys.stk.core.stkobjects.aviator.IAircraftProp

   object
   
   Interface used to access the propulsion options for the Basic Acceleration Model of an aircraft.

.. py:currentmodule:: IAircraftProp

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftProp.prop_strategy`
              - Gets or sets the propulsion strategy type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftProp.mode_as_simple`
              - Get the interface for a simple propulsion strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftProp.mode_as_basic_fixed_wing`
              - Get the interface for a basic fixed wing propulsion strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftProp.mode_as_external`
              - Get the interface for an external file propulsion strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftProp.lift_factor`
              - Gets or sets the scalar value applied to the lift for parametric analysis.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftProp.drag_factor`
              - Gets or sets the scalar value applied to the drag for parametric analysis.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftProp.mode_as_ramjet`
              - Get the interface for a Ramjet propulsion strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftProp.mode_as_turbojet`
              - Get the interface for a Turbojet propulsion strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftProp.mode_as_rocket`
              - Get the interface for a Rocket propulsion strategy.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAircraftProp


Property detail
---------------

.. py:property:: prop_strategy
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftProp.prop_strategy
    :type: AIRCRAFT_PROP_STRATEGY

    Gets or sets the propulsion strategy type.

.. py:property:: mode_as_simple
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftProp.mode_as_simple
    :type: IAircraftSimpleProp

    Get the interface for a simple propulsion strategy.

.. py:property:: mode_as_basic_fixed_wing
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftProp.mode_as_basic_fixed_wing
    :type: IAircraftBasicFixedWingProp

    Get the interface for a basic fixed wing propulsion strategy.

.. py:property:: mode_as_external
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftProp.mode_as_external
    :type: IAircraftExternalProp

    Get the interface for an external file propulsion strategy.

.. py:property:: lift_factor
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftProp.lift_factor
    :type: float

    Gets or sets the scalar value applied to the lift for parametric analysis.

.. py:property:: drag_factor
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftProp.drag_factor
    :type: float

    Gets or sets the scalar value applied to the drag for parametric analysis.

.. py:property:: mode_as_ramjet
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftProp.mode_as_ramjet
    :type: IMissileRamjetProp

    Get the interface for a Ramjet propulsion strategy.

.. py:property:: mode_as_turbojet
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftProp.mode_as_turbojet
    :type: IMissileTurbojetProp

    Get the interface for a Turbojet propulsion strategy.

.. py:property:: mode_as_rocket
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftProp.mode_as_rocket
    :type: IMissileRocketProp

    Get the interface for a Rocket propulsion strategy.


