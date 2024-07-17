BasicManeuverStrategyBarrelRoll
===============================

.. py:class:: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBarrelRoll

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategy`

   Class defining the barrel roll strategy for a basic maneuver procedure.

.. py:currentmodule:: BasicManeuverStrategyBarrelRoll

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBarrelRoll.set_airspeeds`
              - Set the speeds at the top and bottom of the loop.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBarrelRoll.helix_angle`
              - Gets or sets the helix angle for the barrel roll. The angle that the aircraft travels around the velocity vector.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBarrelRoll.helix_angle_mode`
              - Gets or sets the helix angle mode for the barrel roll.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBarrelRoll.top_load_factor`
              - Gets or sets the load factor at the top of the loop.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBarrelRoll.bottom_load_factor`
              - Gets or sets the load factor at the bottom of the loop.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBarrelRoll.torsion_angle`
              - Gets or sets the torsion angle for the barrel roll. The angle of the turn from the aircraft's velocity vector.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBarrelRoll.hold_init_tas`
              - Gets or sets the option to hold the initial true airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBarrelRoll.airspeed_type`
              - Get the airspeed type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBarrelRoll.top_airspeed`
              - Get the speed at the top of the loop.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBarrelRoll.bottom_airspeed`
              - Get the speed at the bottom of the loop.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import BasicManeuverStrategyBarrelRoll


Property detail
---------------

.. py:property:: helix_angle
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBarrelRoll.helix_angle
    :type: typing.Any

    Gets or sets the helix angle for the barrel roll. The angle that the aircraft travels around the velocity vector.

.. py:property:: helix_angle_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBarrelRoll.helix_angle_mode
    :type: ANGLE_MODE

    Gets or sets the helix angle mode for the barrel roll.

.. py:property:: top_load_factor
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBarrelRoll.top_load_factor
    :type: float

    Gets or sets the load factor at the top of the loop.

.. py:property:: bottom_load_factor
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBarrelRoll.bottom_load_factor
    :type: float

    Gets or sets the load factor at the bottom of the loop.

.. py:property:: torsion_angle
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBarrelRoll.torsion_angle
    :type: typing.Any

    Gets or sets the torsion angle for the barrel roll. The angle of the turn from the aircraft's velocity vector.

.. py:property:: hold_init_tas
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBarrelRoll.hold_init_tas
    :type: bool

    Gets or sets the option to hold the initial true airspeed.

.. py:property:: airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBarrelRoll.airspeed_type
    :type: AIRSPEED_TYPE

    Get the airspeed type.

.. py:property:: top_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBarrelRoll.top_airspeed
    :type: float

    Get the speed at the top of the loop.

.. py:property:: bottom_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBarrelRoll.bottom_airspeed
    :type: float

    Get the speed at the bottom of the loop.


Method detail
-------------
















.. py:method:: set_airspeeds(self, airspeedType: AIRSPEED_TYPE, topAirspeed: float, bottomAirspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBarrelRoll.set_airspeeds

    Set the speeds at the top and bottom of the loop.

    :Parameters:

    **airspeedType** : :obj:`~AIRSPEED_TYPE`
    **topAirspeed** : :obj:`~float`
    **bottomAirspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`

