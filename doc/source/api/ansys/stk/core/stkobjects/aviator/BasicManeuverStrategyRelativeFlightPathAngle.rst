BasicManeuverStrategyRelativeFlightPathAngle
============================================

.. py:class:: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeFlightPathAngle

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategy`

   Class defining the Relative Flight Path Angle strategy for a basic maneuver procedure.

.. py:currentmodule:: BasicManeuverStrategyRelativeFlightPathAngle

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeFlightPathAngle.set_control_limit`
              - Set the method and corresponding value to define the control limits of the aircraft during the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeFlightPathAngle.set_min_absolute_altitude`
              - Set whether to enable and a value for the minimum absolute altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeFlightPathAngle.set_max_absolute_altitude`
              - Set whether to enable and a value for the maximum absolute altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeFlightPathAngle.set_min_altitude_relative_anchor`
              - Set whether to enable and a value for the minimum altitude offset from the target.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeFlightPathAngle.set_max_altitude_relative_anchor`
              - Set whether to enable and a value for the maximum altitude offset from the target.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeFlightPathAngle.flight_path_angle`
              - Gets or sets the flight path angle for the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeFlightPathAngle.anchor_altitude_offset`
              - Gets or sets the goal height above or below the target.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeFlightPathAngle.maneuver_factor`
              - Gets or sets the maneuver factor, a dimensionless factor that determines how tightly or gently the aircraft will maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeFlightPathAngle.control_limit_mode`
              - Get the method to define the control limits of the aircraft during the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeFlightPathAngle.control_limit_pitch_rate`
              - Get the specified pitch rate for a control limit mode of specify max pitch rate.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeFlightPathAngle.airspeed_options`
              - Get the airspeed options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeFlightPathAngle.min_absolute_altitude`
              - Get the minimum absolute altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeFlightPathAngle.use_min_absolute_altitude`
              - Get the option to specify a minimum absolute altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeFlightPathAngle.max_absolute_altitude`
              - Get the maximum absolute altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeFlightPathAngle.use_max_absolute_altitude`
              - Get the option to specify a maximum absolute altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeFlightPathAngle.min_altitude_relative_anchor`
              - Get the minimum altitude offset from the target.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeFlightPathAngle.use_min_altitude_relative_anchor`
              - Get the option to specify a minimum altitude offset from the target.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeFlightPathAngle.max_altitude_relative_anchor`
              - Get the maximum altitude offset from the target.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeFlightPathAngle.use_max_altitude_relative_anchor`
              - Get the option to specify a maximum altitude offset from the target.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeFlightPathAngle.compensate_for_coriolis_acceleration`
              - Gets or sets the option to compensate for the acceleration due to the Coriolis effect.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import BasicManeuverStrategyRelativeFlightPathAngle


Property detail
---------------

.. py:property:: flight_path_angle
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeFlightPathAngle.flight_path_angle
    :type: typing.Any

    Gets or sets the flight path angle for the maneuver.

.. py:property:: anchor_altitude_offset
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeFlightPathAngle.anchor_altitude_offset
    :type: float

    Gets or sets the goal height above or below the target.

.. py:property:: maneuver_factor
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeFlightPathAngle.maneuver_factor
    :type: float

    Gets or sets the maneuver factor, a dimensionless factor that determines how tightly or gently the aircraft will maneuver.

.. py:property:: control_limit_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeFlightPathAngle.control_limit_mode
    :type: PROFILE_CONTROL_LIMIT

    Get the method to define the control limits of the aircraft during the maneuver.

.. py:property:: control_limit_pitch_rate
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeFlightPathAngle.control_limit_pitch_rate
    :type: typing.Any

    Get the specified pitch rate for a control limit mode of specify max pitch rate.

.. py:property:: airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeFlightPathAngle.airspeed_options
    :type: BasicManeuverAirspeedOptions

    Get the airspeed options.

.. py:property:: min_absolute_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeFlightPathAngle.min_absolute_altitude
    :type: float

    Get the minimum absolute altitude.

.. py:property:: use_min_absolute_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeFlightPathAngle.use_min_absolute_altitude
    :type: bool

    Get the option to specify a minimum absolute altitude.

.. py:property:: max_absolute_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeFlightPathAngle.max_absolute_altitude
    :type: float

    Get the maximum absolute altitude.

.. py:property:: use_max_absolute_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeFlightPathAngle.use_max_absolute_altitude
    :type: bool

    Get the option to specify a maximum absolute altitude.

.. py:property:: min_altitude_relative_anchor
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeFlightPathAngle.min_altitude_relative_anchor
    :type: float

    Get the minimum altitude offset from the target.

.. py:property:: use_min_altitude_relative_anchor
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeFlightPathAngle.use_min_altitude_relative_anchor
    :type: bool

    Get the option to specify a minimum altitude offset from the target.

.. py:property:: max_altitude_relative_anchor
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeFlightPathAngle.max_altitude_relative_anchor
    :type: float

    Get the maximum altitude offset from the target.

.. py:property:: use_max_altitude_relative_anchor
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeFlightPathAngle.use_max_altitude_relative_anchor
    :type: bool

    Get the option to specify a maximum altitude offset from the target.

.. py:property:: compensate_for_coriolis_acceleration
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeFlightPathAngle.compensate_for_coriolis_acceleration
    :type: bool

    Gets or sets the option to compensate for the acceleration due to the Coriolis effect.


Method detail
-------------









.. py:method:: set_control_limit(self, controlLimitMode: PROFILE_CONTROL_LIMIT, controlLimitValue: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeFlightPathAngle.set_control_limit

    Set the method and corresponding value to define the control limits of the aircraft during the maneuver.

    :Parameters:

    **controlLimitMode** : :obj:`~PROFILE_CONTROL_LIMIT`
    **controlLimitValue** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`




.. py:method:: set_min_absolute_altitude(self, enable: bool, altitude: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeFlightPathAngle.set_min_absolute_altitude

    Set whether to enable and a value for the minimum absolute altitude.

    :Parameters:

    **enable** : :obj:`~bool`
    **altitude** : :obj:`~float`

    :Returns:

        :obj:`~None`



.. py:method:: set_max_absolute_altitude(self, enable: bool, altitude: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeFlightPathAngle.set_max_absolute_altitude

    Set whether to enable and a value for the maximum absolute altitude.

    :Parameters:

    **enable** : :obj:`~bool`
    **altitude** : :obj:`~float`

    :Returns:

        :obj:`~None`



.. py:method:: set_min_altitude_relative_anchor(self, enable: bool, altitude: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeFlightPathAngle.set_min_altitude_relative_anchor

    Set whether to enable and a value for the minimum altitude offset from the target.

    :Parameters:

    **enable** : :obj:`~bool`
    **altitude** : :obj:`~float`

    :Returns:

        :obj:`~None`



.. py:method:: set_max_altitude_relative_anchor(self, enable: bool, altitude: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyRelativeFlightPathAngle.set_max_altitude_relative_anchor

    Set whether to enable and a value for the maximum altitude offset from the target.

    :Parameters:

    **enable** : :obj:`~bool`
    **altitude** : :obj:`~float`

    :Returns:

        :obj:`~None`



