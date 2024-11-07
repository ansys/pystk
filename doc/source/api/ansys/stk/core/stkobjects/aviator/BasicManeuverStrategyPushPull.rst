BasicManeuverStrategyPushPull
=============================

.. py:class:: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPushPull

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategy`

   Class defining the Push/Pull strategy for a basic maneuver procedure.

.. py:currentmodule:: BasicManeuverStrategyPushPull

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPushPull.set_stop_altitude`
              - Set whether to enable the altitude stopping condition and the corresponding value.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPushPull.set_stop_altitude_rate`
              - Set whether to enable the altitude rate stopping condition and the corresponding value.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPushPull.set_stop_airspeed`
              - Set whether to enable the airspeed stopping condition and the corresponding value.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPushPull.reference_frame`
              - Gets or sets the reference frame the aircraft will use.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPushPull.push_pull`
              - Gets or sets the option to push over or pull up.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPushPull.push_pull_g`
              - Gets or sets the G force of the maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPushPull.acceleration_mode`
              - Gets or sets the option to accelerate, decelerate, or maintain the current airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPushPull.acceleration_deceleration_g`
              - Gets or sets the specific G force rate to accelerate/decelerate at.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPushPull.maintain_airspeed_type`
              - Gets or sets the airspeed type for the maintain airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPushPull.maintain_airspeed`
              - Get the airspeed to maintain.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPushPull.stop_flight_path_angle`
              - Gets or sets the flight path angle the maneuver will stop at if achieved.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPushPull.use_stop_at_altitude`
              - Get the option to stop the maneuver if a specified altitude is achieved.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPushPull.stop_altitude`
              - Get the altitude stopping condition.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPushPull.use_stop_at_altitude_rate`
              - Get the option to stop the maneuver if a specified altitude rate is achieved.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPushPull.stop_altitude_rate`
              - Get the altitude rate stopping condition.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPushPull.use_stop_at_airspeed`
              - Get the option to stop the maneuver if a specified airspeed is achieved.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPushPull.stop_airspeed`
              - Get the airspeed stopping condition.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPushPull.stop_airspeed_type`
              - Get the airspeed type for the airspeed stopping condition.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPushPull.compensate_for_coriolis_acceleration`
              - Gets or sets the option to compensate for the acceleration due to the Coriolis effect.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import BasicManeuverStrategyPushPull


Property detail
---------------

.. py:property:: reference_frame
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPushPull.reference_frame
    :type: BASIC_MANEUVER_REFERENCE_FRAME

    Gets or sets the reference frame the aircraft will use.

.. py:property:: push_pull
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPushPull.push_pull
    :type: PUSH_PULL

    Gets or sets the option to push over or pull up.

.. py:property:: push_pull_g
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPushPull.push_pull_g
    :type: float

    Gets or sets the G force of the maneuver.

.. py:property:: acceleration_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPushPull.acceleration_mode
    :type: ACCELERATION_MODE

    Gets or sets the option to accelerate, decelerate, or maintain the current airspeed.

.. py:property:: acceleration_deceleration_g
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPushPull.acceleration_deceleration_g
    :type: float

    Gets or sets the specific G force rate to accelerate/decelerate at.

.. py:property:: maintain_airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPushPull.maintain_airspeed_type
    :type: AIRSPEED_TYPE

    Gets or sets the airspeed type for the maintain airspeed.

.. py:property:: maintain_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPushPull.maintain_airspeed
    :type: float

    Get the airspeed to maintain.

.. py:property:: stop_flight_path_angle
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPushPull.stop_flight_path_angle
    :type: typing.Any

    Gets or sets the flight path angle the maneuver will stop at if achieved.

.. py:property:: use_stop_at_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPushPull.use_stop_at_altitude
    :type: bool

    Get the option to stop the maneuver if a specified altitude is achieved.

.. py:property:: stop_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPushPull.stop_altitude
    :type: float

    Get the altitude stopping condition.

.. py:property:: use_stop_at_altitude_rate
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPushPull.use_stop_at_altitude_rate
    :type: bool

    Get the option to stop the maneuver if a specified altitude rate is achieved.

.. py:property:: stop_altitude_rate
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPushPull.stop_altitude_rate
    :type: float

    Get the altitude rate stopping condition.

.. py:property:: use_stop_at_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPushPull.use_stop_at_airspeed
    :type: bool

    Get the option to stop the maneuver if a specified airspeed is achieved.

.. py:property:: stop_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPushPull.stop_airspeed
    :type: float

    Get the airspeed stopping condition.

.. py:property:: stop_airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPushPull.stop_airspeed_type
    :type: AIRSPEED_TYPE

    Get the airspeed type for the airspeed stopping condition.

.. py:property:: compensate_for_coriolis_acceleration
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPushPull.compensate_for_coriolis_acceleration
    :type: bool

    Gets or sets the option to compensate for the acceleration due to the Coriolis effect.


Method detail
-------------


















.. py:method:: set_stop_altitude(self, enable: bool, altitude_rate: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPushPull.set_stop_altitude

    Set whether to enable the altitude stopping condition and the corresponding value.

    :Parameters:

    **enable** : :obj:`~bool`
    **altitude_rate** : :obj:`~float`

    :Returns:

        :obj:`~None`



.. py:method:: set_stop_altitude_rate(self, enable: bool, altitude_rate: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPushPull.set_stop_altitude_rate

    Set whether to enable the altitude rate stopping condition and the corresponding value.

    :Parameters:

    **enable** : :obj:`~bool`
    **altitude_rate** : :obj:`~float`

    :Returns:

        :obj:`~None`




.. py:method:: set_stop_airspeed(self, enable: bool, airspeed_type: AIRSPEED_TYPE, airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyPushPull.set_stop_airspeed

    Set whether to enable the airspeed stopping condition and the corresponding value.

    :Parameters:

    **enable** : :obj:`~bool`
    **airspeed_type** : :obj:`~AIRSPEED_TYPE`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`



