BasicManeuverStrategyLoop
=========================

.. py:class:: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLoop

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategy`

   Class defining the loop strategy for a basic maneuver procedure.

.. py:currentmodule:: BasicManeuverStrategyLoop

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLoop.set_airspeeds`
              - Set the speeds at the top and bottom of the loop.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLoop.loop_angle`
              - Get or set the loop angle for maneuver. The total change in pitch angle the aircraft flies.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLoop.loop_angle_mode`
              - Get or set the loop angle mode for the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLoop.top_load_factor`
              - Get or set the load factor at the top of the loop.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLoop.bottom_load_factor`
              - Get or set the load factor at the bottom of the loop.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLoop.hold_init_tas`
              - Get or set the option to hold the initial true airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLoop.airspeed_type`
              - Get the airspeed type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLoop.top_airspeed`
              - Get the speed at the top of the loop.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLoop.bottom_airspeed`
              - Get the speed at the bottom of the loop.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import BasicManeuverStrategyLoop


Property detail
---------------

.. py:property:: loop_angle
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLoop.loop_angle
    :type: typing.Any

    Get or set the loop angle for maneuver. The total change in pitch angle the aircraft flies.

.. py:property:: loop_angle_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLoop.loop_angle_mode
    :type: AngleMode

    Get or set the loop angle mode for the maneuver.

.. py:property:: top_load_factor
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLoop.top_load_factor
    :type: float

    Get or set the load factor at the top of the loop.

.. py:property:: bottom_load_factor
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLoop.bottom_load_factor
    :type: float

    Get or set the load factor at the bottom of the loop.

.. py:property:: hold_init_tas
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLoop.hold_init_tas
    :type: bool

    Get or set the option to hold the initial true airspeed.

.. py:property:: airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLoop.airspeed_type
    :type: AirspeedType

    Get the airspeed type.

.. py:property:: top_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLoop.top_airspeed
    :type: float

    Get the speed at the top of the loop.

.. py:property:: bottom_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLoop.bottom_airspeed
    :type: float

    Get the speed at the bottom of the loop.


Method detail
-------------














.. py:method:: set_airspeeds(self, airspeed_type: AirspeedType, top_airspeed: float, bottom_airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLoop.set_airspeeds

    Set the speeds at the top and bottom of the loop.

    :Parameters:

        **airspeed_type** : :obj:`~AirspeedType`

        **top_airspeed** : :obj:`~float`

        **bottom_airspeed** : :obj:`~float`


    :Returns:

        :obj:`~None`

