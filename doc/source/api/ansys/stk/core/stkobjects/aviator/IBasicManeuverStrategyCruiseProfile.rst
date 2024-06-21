IBasicManeuverStrategyCruiseProfile
===================================

.. py:class:: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyCruiseProfile

   object
   
   Interface used to access options for a Cruise Profile Strategy of a Basic Maneuver Procedure.

.. py:currentmodule:: IBasicManeuverStrategyCruiseProfile

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyCruiseProfile.reference_frame`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyCruiseProfile.use_default_cruise_altitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyCruiseProfile.level_off`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyCruiseProfile.requested_altitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyCruiseProfile.cruise_airspeed_options`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyCruiseProfile.stop_after_level_off`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyCruiseProfile.compensate_for_coriolis_accel`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IBasicManeuverStrategyCruiseProfile


Property detail
---------------

.. py:property:: reference_frame
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyCruiseProfile.reference_frame
    :type: BASIC_MANEUVER_REFERENCE_FRAME

    Gets or sets the reference frame the aircraft will use. Earth Frame will force the aircraft to overcome wind effects. Wind frame will allow the maneuver to be perturbed by wind.

.. py:property:: use_default_cruise_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyCruiseProfile.use_default_cruise_altitude
    :type: bool

    Opt whether to use the aircraft's default cruise altitude.

.. py:property:: level_off
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyCruiseProfile.level_off
    :type: bool

    Opt whether to require the aircraft to level off at the specified altitude. This altitude is only enabled of the Default Cruise Altitude option is not selected.

.. py:property:: requested_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyCruiseProfile.requested_altitude
    :type: float

    Gets or sets the desired MSL Altitude for the maneuver. This altitude is only enabled of the Default Cruise Altitude option is not selected.

.. py:property:: cruise_airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyCruiseProfile.cruise_airspeed_options
    :type: ICruiseAirspeedOptions

    Get the interface for the cruise airspeed options.

.. py:property:: stop_after_level_off
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyCruiseProfile.stop_after_level_off
    :type: bool

    Select to stop the maneuver as soon as the aircraft achieves its goal altitude and levels off, regardless if any basic stopping conditions have been triggered.

.. py:property:: compensate_for_coriolis_accel
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyCruiseProfile.compensate_for_coriolis_accel
    :type: bool

    Gets or sets the option to compensate for the acceleration due to the Coriolis effect.


