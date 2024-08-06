AircraftPropulsion
==================

.. py:class:: ansys.stk.core.stkobjects.aviator.AircraftPropulsion

   Class defining the propulsion options for a basic acceleration performance model of an Aviator aircraft.

.. py:currentmodule:: AircraftPropulsion

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftPropulsion.propulsion_strategy`
              - Gets or sets the propulsion strategy type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftPropulsion.mode_as_simple`
              - Get the interface for a simple propulsion strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftPropulsion.mode_as_basic_fixed_wing`
              - Get the interface for a basic fixed wing propulsion strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftPropulsion.mode_as_external`
              - Get the interface for an external file propulsion strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftPropulsion.lift_factor`
              - Gets or sets the scalar value applied to the lift for parametric analysis.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftPropulsion.drag_factor`
              - Gets or sets the scalar value applied to the drag for parametric analysis.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftPropulsion.mode_as_ramjet`
              - Get the interface for a Ramjet propulsion strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftPropulsion.mode_as_turbojet`
              - Get the interface for a Turbojet propulsion strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftPropulsion.mode_as_rocket`
              - Get the interface for a Rocket propulsion strategy.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AircraftPropulsion


Property detail
---------------

.. py:property:: propulsion_strategy
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftPropulsion.propulsion_strategy
    :type: AIRCRAFT_PROPULSION_STRATEGY

    Gets or sets the propulsion strategy type.

.. py:property:: mode_as_simple
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftPropulsion.mode_as_simple
    :type: AircraftSimplePropulsion

    Get the interface for a simple propulsion strategy.

.. py:property:: mode_as_basic_fixed_wing
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftPropulsion.mode_as_basic_fixed_wing
    :type: AircraftBasicFixedWingPropulsion

    Get the interface for a basic fixed wing propulsion strategy.

.. py:property:: mode_as_external
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftPropulsion.mode_as_external
    :type: AircraftExternalPropulsion

    Get the interface for an external file propulsion strategy.

.. py:property:: lift_factor
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftPropulsion.lift_factor
    :type: float

    Gets or sets the scalar value applied to the lift for parametric analysis.

.. py:property:: drag_factor
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftPropulsion.drag_factor
    :type: float

    Gets or sets the scalar value applied to the drag for parametric analysis.

.. py:property:: mode_as_ramjet
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftPropulsion.mode_as_ramjet
    :type: MissileRamjetPropulsion

    Get the interface for a Ramjet propulsion strategy.

.. py:property:: mode_as_turbojet
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftPropulsion.mode_as_turbojet
    :type: MissileTurbojetPropulsion

    Get the interface for a Turbojet propulsion strategy.

.. py:property:: mode_as_rocket
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftPropulsion.mode_as_rocket
    :type: MissileRocketPropulsion

    Get the interface for a Rocket propulsion strategy.


