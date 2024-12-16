BasicManeuverStrategyCruiseProfile
==================================

.. py:class:: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyCruiseProfile

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategy`

   Class defining the Cruise profile strategy for a basic maneuver procedure.

.. py:currentmodule:: BasicManeuverStrategyCruiseProfile

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyCruiseProfile.reference_frame`
              - Gets or sets the reference frame the aircraft will use. Earth Frame will force the aircraft to overcome wind effects. Wind frame will allow the maneuver to be perturbed by wind.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyCruiseProfile.use_default_cruise_altitude`
              - Opt whether to use the aircraft's default cruise altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyCruiseProfile.level_off`
              - Opt whether to require the aircraft to level off at the specified altitude. This altitude is only enabled of the Default Cruise Altitude option is not selected.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyCruiseProfile.requested_altitude`
              - Gets or sets the desired MSL Altitude for the maneuver. This altitude is only enabled of the Default Cruise Altitude option is not selected.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyCruiseProfile.cruise_airspeed_options`
              - Get the interface for the cruise airspeed options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyCruiseProfile.stop_after_level_off`
              - Select to stop the maneuver as soon as the aircraft achieves its goal altitude and levels off, regardless if any basic stopping conditions have been triggered.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyCruiseProfile.compensate_for_coriolis_acceleration`
              - Gets or sets the option to compensate for the acceleration due to the Coriolis effect.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import BasicManeuverStrategyCruiseProfile


Property detail
---------------

.. py:property:: reference_frame
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyCruiseProfile.reference_frame
    :type: BasicManeuverReferenceFrame

    Gets or sets the reference frame the aircraft will use. Earth Frame will force the aircraft to overcome wind effects. Wind frame will allow the maneuver to be perturbed by wind.

.. py:property:: use_default_cruise_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyCruiseProfile.use_default_cruise_altitude
    :type: bool

    Opt whether to use the aircraft's default cruise altitude.

.. py:property:: level_off
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyCruiseProfile.level_off
    :type: bool

    Opt whether to require the aircraft to level off at the specified altitude. This altitude is only enabled of the Default Cruise Altitude option is not selected.

.. py:property:: requested_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyCruiseProfile.requested_altitude
    :type: float

    Gets or sets the desired MSL Altitude for the maneuver. This altitude is only enabled of the Default Cruise Altitude option is not selected.

.. py:property:: cruise_airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyCruiseProfile.cruise_airspeed_options
    :type: CruiseAirspeedOptions

    Get the interface for the cruise airspeed options.

.. py:property:: stop_after_level_off
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyCruiseProfile.stop_after_level_off
    :type: bool

    Select to stop the maneuver as soon as the aircraft achieves its goal altitude and levels off, regardless if any basic stopping conditions have been triggered.

.. py:property:: compensate_for_coriolis_acceleration
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyCruiseProfile.compensate_for_coriolis_acceleration
    :type: bool

    Gets or sets the option to compensate for the acceleration due to the Coriolis effect.


