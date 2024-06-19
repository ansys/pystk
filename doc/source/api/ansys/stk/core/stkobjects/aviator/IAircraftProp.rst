IAircraftProp
=============

.. py:class:: IAircraftProp

   object
   
   Interface used to access the propulsion options for the Basic Acceleration Model of an aircraft.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~prop_strategy`
            * - :py:meth:`~mode_as_simple`
            * - :py:meth:`~mode_as_basic_fixed_wing`
            * - :py:meth:`~mode_as_external`
            * - :py:meth:`~lift_factor`
            * - :py:meth:`~drag_factor`
            * - :py:meth:`~mode_as_ramjet`
            * - :py:meth:`~mode_as_turbojet`
            * - :py:meth:`~mode_as_rocket`


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
    :type: IAgAvtrAircraftSimpleProp

    Get the interface for a simple propulsion strategy.

.. py:property:: mode_as_basic_fixed_wing
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftProp.mode_as_basic_fixed_wing
    :type: IAgAvtrAircraftBasicFixedWingProp

    Get the interface for a basic fixed wing propulsion strategy.

.. py:property:: mode_as_external
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftProp.mode_as_external
    :type: IAgAvtrAircraftExternalProp

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
    :type: IAgAvtrMissileRamjetProp

    Get the interface for a Ramjet propulsion strategy.

.. py:property:: mode_as_turbojet
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftProp.mode_as_turbojet
    :type: IAgAvtrMissileTurbojetProp

    Get the interface for a Turbojet propulsion strategy.

.. py:property:: mode_as_rocket
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftProp.mode_as_rocket
    :type: IAgAvtrMissileRocketProp

    Get the interface for a Rocket propulsion strategy.


