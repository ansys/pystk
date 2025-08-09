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

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBarrelRoll.airspeed_type`
              - Get the airspeed type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBarrelRoll.bottom_airspeed`
              - Get the speed at the bottom of the loop.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBarrelRoll.bottom_load_factor`
              - Get or set the load factor at the bottom of the loop.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBarrelRoll.helix_angle`
              - Get or set the helix angle for the barrel roll. The angle that the aircraft travels around the velocity vector.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBarrelRoll.helix_angle_mode`
              - Get or set the helix angle mode for the barrel roll.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBarrelRoll.hold_init_tas`
              - Get or set the option to hold the initial true airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBarrelRoll.top_airspeed`
              - Get the speed at the top of the loop.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBarrelRoll.top_load_factor`
              - Get or set the load factor at the top of the loop.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBarrelRoll.torsion_angle`
              - Get or set the torsion angle for the barrel roll. The angle of the turn from the aircraft's velocity vector.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import BasicManeuverStrategyBarrelRoll


Property detail
---------------

.. py:property:: airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBarrelRoll.airspeed_type
    :type: AirspeedType

    Get the airspeed type.

.. py:property:: bottom_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBarrelRoll.bottom_airspeed
    :type: float

    Get the speed at the bottom of the loop.

.. py:property:: bottom_load_factor
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBarrelRoll.bottom_load_factor
    :type: float

    Get or set the load factor at the bottom of the loop.

.. py:property:: helix_angle
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBarrelRoll.helix_angle
    :type: typing.Any

    Get or set the helix angle for the barrel roll. The angle that the aircraft travels around the velocity vector.

.. py:property:: helix_angle_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBarrelRoll.helix_angle_mode
    :type: AngleMode

    Get or set the helix angle mode for the barrel roll.

.. py:property:: hold_init_tas
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBarrelRoll.hold_init_tas
    :type: bool

    Get or set the option to hold the initial true airspeed.

.. py:property:: top_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBarrelRoll.top_airspeed
    :type: float

    Get the speed at the top of the loop.

.. py:property:: top_load_factor
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBarrelRoll.top_load_factor
    :type: float

    Get or set the load factor at the top of the loop.

.. py:property:: torsion_angle
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBarrelRoll.torsion_angle
    :type: typing.Any

    Get or set the torsion angle for the barrel roll. The angle of the turn from the aircraft's velocity vector.


Method detail
-------------











.. py:method:: set_airspeeds(self, airspeed_type: AirspeedType, top_airspeed: float, bottom_airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBarrelRoll.set_airspeeds

    Set the speeds at the top and bottom of the loop.

    :Parameters:

        **airspeed_type** : :obj:`~AirspeedType`

        **top_airspeed** : :obj:`~float`

        **bottom_airspeed** : :obj:`~float`


    :Returns:

        :obj:`~None`






