BasicManeuverStrategyBezier
===========================

.. py:class:: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBezier

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategy`

   Class defining the Bezier strategy for a basic maneuver procedure.

.. py:currentmodule:: BasicManeuverStrategyBezier

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBezier.set_airspeed`
              - Set the fly to airspeed value and type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBezier.set_vertical_velocity`
              - Set the flight path angle or altitude rate.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBezier.set_stop_altitude_rate`
              - Set whether to enable the altitude rate stopping condition and the corresponding value.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBezier.set_stop_airspeed`
              - Set whether to enable the airspeed stopping condition and the corresponding value.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBezier.reference_frame`
              - Get or set the reference frame the aircraft will use.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBezier.altitude`
              - Get or set the aircraft's altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBezier.downrange`
              - Get or set the ground distance from the beginning of the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBezier.airspeed`
              - Get or set the aircraft's airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBezier.airspeed_type`
              - Get the airspeed type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBezier.vertical_velocity_mode`
              - Get the option to specify the flight path angle or the altitude rate.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBezier.flight_path_angle`
              - Get the initial pitch angle of the flight path.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBezier.altitude_rate`
              - Get the constant rate at which the aircraft will climb or descend.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBezier.use_stop_at_altitude_rate`
              - Get the option to stop the maneuver if a specified altitude rate is achieved.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBezier.stop_altitude_rate`
              - Get the altitude rate stopping condition.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBezier.use_stop_at_airspeed`
              - Get the option to stop the maneuver if a specified airspeed is achieved.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBezier.stop_airspeed`
              - Get the airspeed stopping condition.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBezier.stop_airspeed_type`
              - Get the airspeed type for the airspeed stopping condition.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBezier.compensate_for_coriolis_acceleration`
              - Get or set the option to compensate for the acceleration due to the Coriolis effect.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import BasicManeuverStrategyBezier


Property detail
---------------

.. py:property:: reference_frame
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBezier.reference_frame
    :type: BasicManeuverReferenceFrame

    Get or set the reference frame the aircraft will use.

.. py:property:: altitude
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBezier.altitude
    :type: float

    Get or set the aircraft's altitude.

.. py:property:: downrange
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBezier.downrange
    :type: float

    Get or set the ground distance from the beginning of the maneuver.

.. py:property:: airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBezier.airspeed
    :type: float

    Get or set the aircraft's airspeed.

.. py:property:: airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBezier.airspeed_type
    :type: AirspeedType

    Get the airspeed type.

.. py:property:: vertical_velocity_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBezier.vertical_velocity_mode
    :type: FlyToFlightPathAngleMode

    Get the option to specify the flight path angle or the altitude rate.

.. py:property:: flight_path_angle
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBezier.flight_path_angle
    :type: typing.Any

    Get the initial pitch angle of the flight path.

.. py:property:: altitude_rate
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBezier.altitude_rate
    :type: float

    Get the constant rate at which the aircraft will climb or descend.

.. py:property:: use_stop_at_altitude_rate
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBezier.use_stop_at_altitude_rate
    :type: bool

    Get the option to stop the maneuver if a specified altitude rate is achieved.

.. py:property:: stop_altitude_rate
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBezier.stop_altitude_rate
    :type: float

    Get the altitude rate stopping condition.

.. py:property:: use_stop_at_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBezier.use_stop_at_airspeed
    :type: bool

    Get the option to stop the maneuver if a specified airspeed is achieved.

.. py:property:: stop_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBezier.stop_airspeed
    :type: float

    Get the airspeed stopping condition.

.. py:property:: stop_airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBezier.stop_airspeed_type
    :type: AirspeedType

    Get the airspeed type for the airspeed stopping condition.

.. py:property:: compensate_for_coriolis_acceleration
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBezier.compensate_for_coriolis_acceleration
    :type: bool

    Get or set the option to compensate for the acceleration due to the Coriolis effect.


Method detail
-------------









.. py:method:: set_airspeed(self, airspeed_type: AirspeedType, airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBezier.set_airspeed

    Set the fly to airspeed value and type.

    :Parameters:

    **airspeed_type** : :obj:`~AirspeedType`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`




.. py:method:: set_vertical_velocity(self, mode: FlyToFlightPathAngleMode, value: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBezier.set_vertical_velocity

    Set the flight path angle or altitude rate.

    :Parameters:

    **mode** : :obj:`~FlyToFlightPathAngleMode`
    **value** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`



.. py:method:: set_stop_altitude_rate(self, enable: bool, altitude_rate: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBezier.set_stop_altitude_rate

    Set whether to enable the altitude rate stopping condition and the corresponding value.

    :Parameters:

    **enable** : :obj:`~bool`
    **altitude_rate** : :obj:`~float`

    :Returns:

        :obj:`~None`




.. py:method:: set_stop_airspeed(self, enable: bool, airspeed_type: AirspeedType, airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyBezier.set_stop_airspeed

    Set whether to enable the airspeed stopping condition and the corresponding value.

    :Parameters:

    **enable** : :obj:`~bool`
    **airspeed_type** : :obj:`~AirspeedType`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`



