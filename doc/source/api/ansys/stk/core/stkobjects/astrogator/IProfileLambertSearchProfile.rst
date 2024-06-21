IProfileLambertSearchProfile
============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile

   IProfile
   
   Properties for a Lambert Search Profile.

.. py:currentmodule:: IProfileLambertSearchProfile

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.set_target_coord_type`
              - Select a target coordinate type.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.coord_system_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.target_coord_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.enable_second_maneuver`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.enable_target_match_phase`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.target_position_x`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.target_position_y`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.target_position_z`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.target_velocity_x`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.target_velocity_y`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.target_velocity_z`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.target_semimajor_axis`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.target_eccentricity`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.target_inclination`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.target_right_ascension_of_ascending_node`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.target_argument_of_periapsis`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.target_true_anomaly`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.enable_write_departure_delay_to_first_propagate`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.disable_first_propagate_non_lambert_stop_conditions`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.first_propagate_segment`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.enable_write_to_first_maneuver`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.first_maneuver_segment`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.latest_departure_time`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.earliest_arrival_time`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.latest_arrival_time`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.grid_search_time_step`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.max_revolutions`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.central_body_collision_altitude_padding`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.enable_write_duration_to_second_propagate`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.disable_second_propagate_non_lambert_stop_conditions`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.second_propagate_segment`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.enable_write_to_second_maneuver`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.second_maneuver_segment`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IProfileLambertSearchProfile


Property detail
---------------

.. py:property:: coord_system_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.coord_system_name
    :type: str

    Gets or sets the coordinate system.

.. py:property:: target_coord_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.target_coord_type
    :type: LAMBERT_TARGET_COORD_TYPE

    Get the target coordinate type.

.. py:property:: enable_second_maneuver
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.enable_second_maneuver
    :type: bool

    Enable to calculate second maneuver at destination.

.. py:property:: enable_target_match_phase
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.enable_target_match_phase
    :type: bool

    Set this to true if the satellite should match the phase of the orbit at the target.

.. py:property:: target_position_x
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.target_position_x
    :type: float

    Gets or sets the X component of the target position for the end of the Lambert transfer.

.. py:property:: target_position_y
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.target_position_y
    :type: float

    Gets or sets the Y component of the target position for the end of the Lambert transfer.

.. py:property:: target_position_z
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.target_position_z
    :type: float

    Gets or sets the Z component of the target position for the end of the Lambert transfer.

.. py:property:: target_velocity_x
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.target_velocity_x
    :type: float

    Gets or sets the X component of the target velocity for the end of the Lambert transfer.

.. py:property:: target_velocity_y
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.target_velocity_y
    :type: float

    Gets or sets the Y component of the target velocity for the end of the Lambert transfer.

.. py:property:: target_velocity_z
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.target_velocity_z
    :type: float

    Gets or sets the Z component of the target velocity for the end of the Lambert transfer.

.. py:property:: target_semimajor_axis
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.target_semimajor_axis
    :type: float

    Gets or sets the target semimajor axis for the end of the Lambert transfer.

.. py:property:: target_eccentricity
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.target_eccentricity
    :type: float

    Gets or sets the target eccentricity for the end of the Lambert transfer.

.. py:property:: target_inclination
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.target_inclination
    :type: float

    Gets or sets the target inclination for the end of the Lambert transfer.

.. py:property:: target_right_ascension_of_ascending_node
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.target_right_ascension_of_ascending_node
    :type: float

    Gets or sets the target right ascension of the ascending node for the end of the Lambert transfer.

.. py:property:: target_argument_of_periapsis
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.target_argument_of_periapsis
    :type: float

    Gets or sets the target argument of periapsis for the end of the Lambert transfer.

.. py:property:: target_true_anomaly
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.target_true_anomaly
    :type: float

    Gets or sets the target true anomaly for the end of the Lambert transfer.

.. py:property:: enable_write_departure_delay_to_first_propagate
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.enable_write_departure_delay_to_first_propagate
    :type: bool

    Set this to true to write the departure delay duration before the Lambert transfer to the 'LambertDuration' stopping condition in the first linked propagate segment.

.. py:property:: disable_first_propagate_non_lambert_stop_conditions
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.disable_first_propagate_non_lambert_stop_conditions
    :type: bool

    Set this to true to disable all non-LambertDuration stopping conditions in the first propagate segment.

.. py:property:: first_propagate_segment
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.first_propagate_segment
    :type: str

    Gets or sets the propagate segment to manipulate that contains the departure delay.

.. py:property:: enable_write_to_first_maneuver
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.enable_write_to_first_maneuver
    :type: bool

    Set this to true to write the Delta-V solution from Lambert at the start of the transfer to the linked maneuver.

.. py:property:: first_maneuver_segment
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.first_maneuver_segment
    :type: str

    Gets or sets the first maneuver segment to manipulate that occurs at the start of the transfer. It is visible when you select Write Initial Inertial Delta-V to Maneuver.

.. py:property:: latest_departure_time
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.latest_departure_time
    :type: float

    Gets or sets the latest time from the start of the target sequence for the first Lambert maneuver to occur.

.. py:property:: earliest_arrival_time
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.earliest_arrival_time
    :type: float

    Gets or sets the earliest time from the start of the target sequence that the satellite should arrive at its destination.

.. py:property:: latest_arrival_time
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.latest_arrival_time
    :type: float

    Gets or sets the latest time from the start of the target sequence that the satellite should arrive at its destination.

.. py:property:: grid_search_time_step
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.grid_search_time_step
    :type: float

    Gets or sets the time step between Lambert evaluations for searching over both the departure window and arrival window of time.

.. py:property:: max_revolutions
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.max_revolutions
    :type: int

    Gets or sets the maximum number of revolutions for the Lambert solution.

.. py:property:: central_body_collision_altitude_padding
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.central_body_collision_altitude_padding
    :type: float

    Gets or sets the minimum altitude below which the Lambert algorithm will consider the spacecraft to have hit the central body.

.. py:property:: enable_write_duration_to_second_propagate
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.enable_write_duration_to_second_propagate
    :type: bool

    Set this to true to write the Lambert duration of transfer to the 'LambertDuration' stopping condition in the second linked propagate segment.

.. py:property:: disable_second_propagate_non_lambert_stop_conditions
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.disable_second_propagate_non_lambert_stop_conditions
    :type: bool

    Set this to true to disable all non-LambertDuration stopping conditions in the second propagate segment. This is visible when you select Write Flight Duration to Second Propagate.

.. py:property:: second_propagate_segment
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.second_propagate_segment
    :type: str

    Gets or sets the propagate segment to manipulate that contains the transfer duration. It is visible when you select Write Flight Duration to Second Propagate.

.. py:property:: enable_write_to_second_maneuver
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.enable_write_to_second_maneuver
    :type: bool

    Set this to true to write the Delta-V solution from Lambert at the end of the transfer to the linked maneuver. It is visible when you select Calculate Second Maneuver At Destination .

.. py:property:: second_maneuver_segment
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.second_maneuver_segment
    :type: str

    Gets or sets the second maneuver segment to manipulate that occurs at the end of the transfer. It is visible when you select Write Final Inertial Delta-V to Maneuver.


Method detail
-------------




.. py:method:: set_target_coord_type(self, elementType: LAMBERT_TARGET_COORD_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertSearchProfile.set_target_coord_type

    Select a target coordinate type.

    :Parameters:

    **elementType** : :obj:`~LAMBERT_TARGET_COORD_TYPE`

    :Returns:

        :obj:`~None`





























































