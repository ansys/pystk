ProfileLambertSearchProfile
===========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IProfile`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The Lambert profile.

.. py:currentmodule:: ProfileLambertSearchProfile

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.set_target_coord_type`
              - Select a target coordinate type.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.coord_system_name`
              - Get or set the coordinate system.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.target_coordinate_type`
              - Get the target coordinate type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.enable_second_maneuver`
              - Enable to calculate second maneuver at destination.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.enable_target_match_phase`
              - Set this to true if the satellite should match the phase of the orbit at the target.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.target_position_x`
              - Get or set the X component of the target position for the end of the Lambert transfer.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.target_position_y`
              - Get or set the Y component of the target position for the end of the Lambert transfer.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.target_position_z`
              - Get or set the Z component of the target position for the end of the Lambert transfer.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.target_velocity_x`
              - Get or set the X component of the target velocity for the end of the Lambert transfer.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.target_velocity_y`
              - Get or set the Y component of the target velocity for the end of the Lambert transfer.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.target_velocity_z`
              - Get or set the Z component of the target velocity for the end of the Lambert transfer.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.target_semimajor_axis`
              - Get or set the target semimajor axis for the end of the Lambert transfer.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.target_eccentricity`
              - Get or set the target eccentricity for the end of the Lambert transfer.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.target_inclination`
              - Get or set the target inclination for the end of the Lambert transfer.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.target_right_ascension_of_ascending_node`
              - Get or set the target right ascension of the ascending node for the end of the Lambert transfer.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.target_argument_of_periapsis`
              - Get or set the target argument of periapsis for the end of the Lambert transfer.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.target_true_anomaly`
              - Get or set the target true anomaly for the end of the Lambert transfer.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.enable_write_departure_delay_to_first_propagate`
              - Set this to true to write the departure delay duration before the Lambert transfer to the 'LambertDuration' stopping condition in the first linked propagate segment.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.disable_first_propagate_non_lambert_stop_conditions`
              - Set this to true to disable all non-LambertDuration stopping conditions in the first propagate segment.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.first_propagate_segment`
              - Get or set the propagate segment to manipulate that contains the departure delay.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.enable_write_to_first_maneuver`
              - Set this to true to write the Delta-V solution from Lambert at the start of the transfer to the linked maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.first_maneuver_segment`
              - Get or set the first maneuver segment to manipulate that occurs at the start of the transfer. It is visible when you select Write Initial Inertial Delta-V to Maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.latest_departure_time`
              - Get or set the latest time from the start of the target sequence for the first Lambert maneuver to occur.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.earliest_arrival_time`
              - Get or set the earliest time from the start of the target sequence that the satellite should arrive at its destination.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.latest_arrival_time`
              - Get or set the latest time from the start of the target sequence that the satellite should arrive at its destination.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.grid_search_time_step`
              - Get or set the time step between Lambert evaluations for searching over both the departure window and arrival window of time.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.max_revolutions`
              - Get or set the maximum number of revolutions for the Lambert solution.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.central_body_collision_altitude_padding`
              - Get or set the minimum altitude below which the Lambert algorithm will consider the spacecraft to have hit the central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.enable_write_duration_to_second_propagate`
              - Set this to true to write the Lambert duration of transfer to the 'LambertDuration' stopping condition in the second linked propagate segment.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.disable_second_propagate_non_lambert_stop_conditions`
              - Set this to true to disable all non-LambertDuration stopping conditions in the second propagate segment. This is visible when you select Write Flight Duration to Second Propagate.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.second_propagate_segment`
              - Get or set the propagate segment to manipulate that contains the transfer duration. It is visible when you select Write Flight Duration to Second Propagate.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.enable_write_to_second_maneuver`
              - Set this to true to write the Delta-V solution from Lambert at the end of the transfer to the linked maneuver. It is visible when you select Calculate Second Maneuver At Destination .
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.second_maneuver_segment`
              - Get or set the second maneuver segment to manipulate that occurs at the end of the transfer. It is visible when you select Write Final Inertial Delta-V to Maneuver.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ProfileLambertSearchProfile


Property detail
---------------

.. py:property:: coord_system_name
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.coord_system_name
    :type: str

    Get or set the coordinate system.

.. py:property:: target_coordinate_type
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.target_coordinate_type
    :type: LambertTargetCoordinateType

    Get the target coordinate type.

.. py:property:: enable_second_maneuver
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.enable_second_maneuver
    :type: bool

    Enable to calculate second maneuver at destination.

.. py:property:: enable_target_match_phase
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.enable_target_match_phase
    :type: bool

    Set this to true if the satellite should match the phase of the orbit at the target.

.. py:property:: target_position_x
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.target_position_x
    :type: float

    Get or set the X component of the target position for the end of the Lambert transfer.

.. py:property:: target_position_y
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.target_position_y
    :type: float

    Get or set the Y component of the target position for the end of the Lambert transfer.

.. py:property:: target_position_z
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.target_position_z
    :type: float

    Get or set the Z component of the target position for the end of the Lambert transfer.

.. py:property:: target_velocity_x
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.target_velocity_x
    :type: float

    Get or set the X component of the target velocity for the end of the Lambert transfer.

.. py:property:: target_velocity_y
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.target_velocity_y
    :type: float

    Get or set the Y component of the target velocity for the end of the Lambert transfer.

.. py:property:: target_velocity_z
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.target_velocity_z
    :type: float

    Get or set the Z component of the target velocity for the end of the Lambert transfer.

.. py:property:: target_semimajor_axis
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.target_semimajor_axis
    :type: float

    Get or set the target semimajor axis for the end of the Lambert transfer.

.. py:property:: target_eccentricity
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.target_eccentricity
    :type: float

    Get or set the target eccentricity for the end of the Lambert transfer.

.. py:property:: target_inclination
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.target_inclination
    :type: float

    Get or set the target inclination for the end of the Lambert transfer.

.. py:property:: target_right_ascension_of_ascending_node
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.target_right_ascension_of_ascending_node
    :type: float

    Get or set the target right ascension of the ascending node for the end of the Lambert transfer.

.. py:property:: target_argument_of_periapsis
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.target_argument_of_periapsis
    :type: float

    Get or set the target argument of periapsis for the end of the Lambert transfer.

.. py:property:: target_true_anomaly
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.target_true_anomaly
    :type: float

    Get or set the target true anomaly for the end of the Lambert transfer.

.. py:property:: enable_write_departure_delay_to_first_propagate
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.enable_write_departure_delay_to_first_propagate
    :type: bool

    Set this to true to write the departure delay duration before the Lambert transfer to the 'LambertDuration' stopping condition in the first linked propagate segment.

.. py:property:: disable_first_propagate_non_lambert_stop_conditions
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.disable_first_propagate_non_lambert_stop_conditions
    :type: bool

    Set this to true to disable all non-LambertDuration stopping conditions in the first propagate segment.

.. py:property:: first_propagate_segment
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.first_propagate_segment
    :type: str

    Get or set the propagate segment to manipulate that contains the departure delay.

.. py:property:: enable_write_to_first_maneuver
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.enable_write_to_first_maneuver
    :type: bool

    Set this to true to write the Delta-V solution from Lambert at the start of the transfer to the linked maneuver.

.. py:property:: first_maneuver_segment
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.first_maneuver_segment
    :type: str

    Get or set the first maneuver segment to manipulate that occurs at the start of the transfer. It is visible when you select Write Initial Inertial Delta-V to Maneuver.

.. py:property:: latest_departure_time
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.latest_departure_time
    :type: float

    Get or set the latest time from the start of the target sequence for the first Lambert maneuver to occur.

.. py:property:: earliest_arrival_time
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.earliest_arrival_time
    :type: float

    Get or set the earliest time from the start of the target sequence that the satellite should arrive at its destination.

.. py:property:: latest_arrival_time
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.latest_arrival_time
    :type: float

    Get or set the latest time from the start of the target sequence that the satellite should arrive at its destination.

.. py:property:: grid_search_time_step
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.grid_search_time_step
    :type: float

    Get or set the time step between Lambert evaluations for searching over both the departure window and arrival window of time.

.. py:property:: max_revolutions
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.max_revolutions
    :type: int

    Get or set the maximum number of revolutions for the Lambert solution.

.. py:property:: central_body_collision_altitude_padding
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.central_body_collision_altitude_padding
    :type: float

    Get or set the minimum altitude below which the Lambert algorithm will consider the spacecraft to have hit the central body.

.. py:property:: enable_write_duration_to_second_propagate
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.enable_write_duration_to_second_propagate
    :type: bool

    Set this to true to write the Lambert duration of transfer to the 'LambertDuration' stopping condition in the second linked propagate segment.

.. py:property:: disable_second_propagate_non_lambert_stop_conditions
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.disable_second_propagate_non_lambert_stop_conditions
    :type: bool

    Set this to true to disable all non-LambertDuration stopping conditions in the second propagate segment. This is visible when you select Write Flight Duration to Second Propagate.

.. py:property:: second_propagate_segment
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.second_propagate_segment
    :type: str

    Get or set the propagate segment to manipulate that contains the transfer duration. It is visible when you select Write Flight Duration to Second Propagate.

.. py:property:: enable_write_to_second_maneuver
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.enable_write_to_second_maneuver
    :type: bool

    Set this to true to write the Delta-V solution from Lambert at the end of the transfer to the linked maneuver. It is visible when you select Calculate Second Maneuver At Destination .

.. py:property:: second_maneuver_segment
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.second_maneuver_segment
    :type: str

    Get or set the second maneuver segment to manipulate that occurs at the end of the transfer. It is visible when you select Write Final Inertial Delta-V to Maneuver.


Method detail
-------------




.. py:method:: set_target_coord_type(self, element_type: LambertTargetCoordinateType) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertSearchProfile.set_target_coord_type

    Select a target coordinate type.

    :Parameters:

    **element_type** : :obj:`~LambertTargetCoordinateType`

    :Returns:

        :obj:`~None`





























































