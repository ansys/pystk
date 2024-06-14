IBasicManeuverStrategyRelativeFPA
=================================

.. py:class:: IBasicManeuverStrategyRelativeFPA

   object
   
   Interface used to access options for the Relative Flight Path Angle Strategy of a Basic Maneuver Procedure.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_control_limit`
              - Set the method and corresponding value to define the control limits of the aircraft during the maneuver.
            * - :py:meth:`~set_min_absolute_altitude`
              - Set whether to enable and a value for the minimum absolute altitude.
            * - :py:meth:`~set_max_absolute_altitude`
              - Set whether to enable and a value for the maximum absolute altitude.
            * - :py:meth:`~set_min_altitude_rel_anchor`
              - Set whether to enable and a value for the minimum altitude offset from the target.
            * - :py:meth:`~set_max_altitude_rel_anchor`
              - Set whether to enable and a value for the maximum altitude offset from the target.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~fpa`
            * - :py:meth:`~anchor_altitude_offset`
            * - :py:meth:`~maneuver_factor`
            * - :py:meth:`~control_limit_mode`
            * - :py:meth:`~control_limit_pitch_rate`
            * - :py:meth:`~airspeed_options`
            * - :py:meth:`~min_absolute_altitude`
            * - :py:meth:`~use_min_absolute_altitude`
            * - :py:meth:`~max_absolute_altitude`
            * - :py:meth:`~use_max_absolute_altitude`
            * - :py:meth:`~min_altitude_rel_anchor`
            * - :py:meth:`~use_min_altitude_rel_anchor`
            * - :py:meth:`~max_altitude_rel_anchor`
            * - :py:meth:`~use_max_altitude_rel_anchor`
            * - :py:meth:`~compensate_for_coriolis_accel`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IBasicManeuverStrategyRelativeFPA


Property detail
---------------

.. py:property:: fpa
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelativeFPA.fpa
    :type: typing.Any

    Gets or sets the flight path angle for the maneuver.

.. py:property:: anchor_altitude_offset
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelativeFPA.anchor_altitude_offset
    :type: float

    Gets or sets the goal height above or below the target.

.. py:property:: maneuver_factor
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelativeFPA.maneuver_factor
    :type: float

    Gets or sets the maneuver factor, a dimensionless factor that determines how tightly or gently the aircraft will maneuver.

.. py:property:: control_limit_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelativeFPA.control_limit_mode
    :type: "PROFILE_CONTROL_LIMIT"

    Get the method to define the control limits of the aircraft during the maneuver.

.. py:property:: control_limit_pitch_rate
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelativeFPA.control_limit_pitch_rate
    :type: typing.Any

    Get the specified pitch rate for a control limit mode of specify max pitch rate.

.. py:property:: airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelativeFPA.airspeed_options
    :type: "IAgAvtrBasicManeuverAirspeedOptions"

    Get the airspeed options.

.. py:property:: min_absolute_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelativeFPA.min_absolute_altitude
    :type: float

    Get the minimum absolute altitude.

.. py:property:: use_min_absolute_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelativeFPA.use_min_absolute_altitude
    :type: bool

    Get the option to specify a minimum absolute altitude.

.. py:property:: max_absolute_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelativeFPA.max_absolute_altitude
    :type: float

    Get the maximum absolute altitude.

.. py:property:: use_max_absolute_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelativeFPA.use_max_absolute_altitude
    :type: bool

    Get the option to specify a maximum absolute altitude.

.. py:property:: min_altitude_rel_anchor
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelativeFPA.min_altitude_rel_anchor
    :type: float

    Get the minimum altitude offset from the target.

.. py:property:: use_min_altitude_rel_anchor
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelativeFPA.use_min_altitude_rel_anchor
    :type: bool

    Get the option to specify a minimum altitude offset from the target.

.. py:property:: max_altitude_rel_anchor
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelativeFPA.max_altitude_rel_anchor
    :type: float

    Get the maximum altitude offset from the target.

.. py:property:: use_max_altitude_rel_anchor
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelativeFPA.use_max_altitude_rel_anchor
    :type: bool

    Get the option to specify a maximum altitude offset from the target.

.. py:property:: compensate_for_coriolis_accel
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyRelativeFPA.compensate_for_coriolis_accel
    :type: bool

    Gets or sets the option to compensate for the acceleration due to the Coriolis effect.


Method detail
-------------









.. py:method:: set_control_limit(self, controlLimitMode:"PROFILE_CONTROL_LIMIT", controlLimitValue:typing.Any) -> None

    Set the method and corresponding value to define the control limits of the aircraft during the maneuver.

    :Parameters:

    **controlLimitMode** : :obj:`~"PROFILE_CONTROL_LIMIT"`
    **controlLimitValue** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`




.. py:method:: set_min_absolute_altitude(self, enable:bool, altitude:float) -> None

    Set whether to enable and a value for the minimum absolute altitude.

    :Parameters:

    **enable** : :obj:`~bool`
    **altitude** : :obj:`~float`

    :Returns:

        :obj:`~None`



.. py:method:: set_max_absolute_altitude(self, enable:bool, altitude:float) -> None

    Set whether to enable and a value for the maximum absolute altitude.

    :Parameters:

    **enable** : :obj:`~bool`
    **altitude** : :obj:`~float`

    :Returns:

        :obj:`~None`



.. py:method:: set_min_altitude_rel_anchor(self, enable:bool, altitude:float) -> None

    Set whether to enable and a value for the minimum altitude offset from the target.

    :Parameters:

    **enable** : :obj:`~bool`
    **altitude** : :obj:`~float`

    :Returns:

        :obj:`~None`



.. py:method:: set_max_altitude_rel_anchor(self, enable:bool, altitude:float) -> None

    Set whether to enable and a value for the maximum altitude offset from the target.

    :Parameters:

    **enable** : :obj:`~bool`
    **altitude** : :obj:`~float`

    :Returns:

        :obj:`~None`



