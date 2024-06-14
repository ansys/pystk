IBasicManeuverStrategyBezier
============================

.. py:class:: IBasicManeuverStrategyBezier

   object
   
   Interface used to access options for a Bezier Strategy of a Basic Maneuver Procedure.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_airspeed`
              - Set the fly to airspeed value and type.
            * - :py:meth:`~set_vertical_velocity`
              - Set the flight path angle or altitude rate.
            * - :py:meth:`~set_stop_altitude_rate`
              - Set whether to enable the altitude rate stopping condition and the corresponding value.
            * - :py:meth:`~set_stop_airspeed`
              - Set whether to enable the airspeed stopping condition and the corresponding value.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~reference_frame`
            * - :py:meth:`~altitude`
            * - :py:meth:`~downrange`
            * - :py:meth:`~airspeed`
            * - :py:meth:`~airspeed_type`
            * - :py:meth:`~vertical_velocity_mode`
            * - :py:meth:`~flight_path_angle`
            * - :py:meth:`~altitude_rate`
            * - :py:meth:`~use_stop_at_altitude_rate`
            * - :py:meth:`~stop_altitude_rate`
            * - :py:meth:`~use_stop_at_airspeed`
            * - :py:meth:`~stop_airspeed`
            * - :py:meth:`~stop_airspeed_type`
            * - :py:meth:`~compensate_for_coriolis_accel`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IBasicManeuverStrategyBezier


Property detail
---------------

.. py:property:: reference_frame
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyBezier.reference_frame
    :type: "BASIC_MANEUVER_REFERENCE_FRAME"

    Gets or sets the reference frame the aircraft will use.

.. py:property:: altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyBezier.altitude
    :type: float

    Gets or sets the aircraft's altitude.

.. py:property:: downrange
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyBezier.downrange
    :type: float

    Gets or sets the ground distance from the beginning of the maneuver.

.. py:property:: airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyBezier.airspeed
    :type: float

    Gets or sets the aircraft's airspeed.

.. py:property:: airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyBezier.airspeed_type
    :type: "AIRSPEED_TYPE"

    Get the airspeed type.

.. py:property:: vertical_velocity_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyBezier.vertical_velocity_mode
    :type: "FLY_TO_FLIGHT_PATH_ANGLE_MODE"

    Get the option to specify the flight path angle or the altitude rate.

.. py:property:: flight_path_angle
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyBezier.flight_path_angle
    :type: typing.Any

    Get the initial pitch angle of the flight path.

.. py:property:: altitude_rate
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyBezier.altitude_rate
    :type: float

    Get the constant rate at which the aircraft will climb or descend.

.. py:property:: use_stop_at_altitude_rate
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyBezier.use_stop_at_altitude_rate
    :type: bool

    Get the option to stop the maneuver if a specified altitude rate is achieved.

.. py:property:: stop_altitude_rate
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyBezier.stop_altitude_rate
    :type: float

    Get the altitude rate stopping condition.

.. py:property:: use_stop_at_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyBezier.use_stop_at_airspeed
    :type: bool

    Get the option to stop the maneuver if a specified airspeed is achieved.

.. py:property:: stop_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyBezier.stop_airspeed
    :type: float

    Get the airspeed stopping condition.

.. py:property:: stop_airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyBezier.stop_airspeed_type
    :type: "AIRSPEED_TYPE"

    Get the airspeed type for the airspeed stopping condition.

.. py:property:: compensate_for_coriolis_accel
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyBezier.compensate_for_coriolis_accel
    :type: bool

    Gets or sets the option to compensate for the acceleration due to the Coriolis effect.


Method detail
-------------









.. py:method:: set_airspeed(self, airspeedType:"AIRSPEED_TYPE", airspeed:float) -> None

    Set the fly to airspeed value and type.

    :Parameters:

    **airspeedType** : :obj:`~"AIRSPEED_TYPE"`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`




.. py:method:: set_vertical_velocity(self, mode:"FLY_TO_FLIGHT_PATH_ANGLE_MODE", value:typing.Any) -> None

    Set the flight path angle or altitude rate.

    :Parameters:

    **mode** : :obj:`~"FLY_TO_FLIGHT_PATH_ANGLE_MODE"`
    **value** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`



.. py:method:: set_stop_altitude_rate(self, enable:bool, altitudeRate:float) -> None

    Set whether to enable the altitude rate stopping condition and the corresponding value.

    :Parameters:

    **enable** : :obj:`~bool`
    **altitudeRate** : :obj:`~float`

    :Returns:

        :obj:`~None`




.. py:method:: set_stop_airspeed(self, enable:bool, airspeedType:"AIRSPEED_TYPE", airspeed:float) -> None

    Set whether to enable the airspeed stopping condition and the corresponding value.

    :Parameters:

    **enable** : :obj:`~bool`
    **airspeedType** : :obj:`~"AIRSPEED_TYPE"`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`



