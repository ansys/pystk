ProfileLambertProfile
=====================

.. py:class:: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IProfile`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The Lambert profile.

.. py:currentmodule:: ProfileLambertProfile

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.set_target_coord_type`
              - Select a target coordinate type.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.coord_system_name`
              - Gets or sets the coordinate system.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_coordinate_type`
              - Get the target coordinate type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.enable_second_maneuver`
              - Enable to calculate second maneuver at destination.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_position_x`
              - Gets or sets the X component of the target position for the end of the Lambert transfer.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_position_y`
              - Gets or sets the Y component of the target position for the end of the Lambert transfer.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_position_z`
              - Gets or sets the Z component of the target position for the end of the Lambert transfer.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_velocity_x`
              - Gets or sets the X component of the target velocity for the end of the Lambert transfer.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_velocity_y`
              - Gets or sets the Y component of the target velocity for the end of the Lambert transfer.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_velocity_z`
              - Gets or sets the Z component of the target velocity for the end of the Lambert transfer.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_semimajor_axis`
              - Gets or sets the target semimajor axis for the end of the Lambert transfer.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_eccentricity`
              - Gets or sets the target eccentricity for the end of the Lambert transfer.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_inclination`
              - Gets or sets the target inclination for the end of the Lambert transfer.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_right_ascension_of_ascending_node`
              - Gets or sets the target right ascension of the ascending node for the end of the Lambert transfer.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_argument_of_periapsis`
              - Gets or sets the target argument of periapsis for the end of the Lambert transfer.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_true_anomaly`
              - Gets or sets the target true anomaly for the end of the Lambert transfer.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.solution_option`
              - Lambert solution calculation type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.time_of_flight`
              - Gets or sets the time of flight between departure and arrival for the Lambert solution.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.revolutions`
              - Gets or sets the number of revolutions. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.orbital_energy`
              - Gets or sets the orbital energy for the Lambert solution.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.direction_of_motion`
              - Gets or sets the direction of motion (long or short) for the Lambert solution.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.central_body_collision_altitude_padding`
              - Gets or sets the minimum altitude below which the Lambert algorithm will consider the spacecraft to have hit the central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.enable_write_to_first_maneuver`
              - Set this to true to write the Delta-V solution from Lambert at the start of the transfer to the linked maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.first_maneuver_segment`
              - Gets or sets the first maneuver segment to manipulate that occurs at the start of the transfer.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.enable_write_duration_to_propagate`
              - Set this to true to write the Lambert duration of transfer to the 'LambertDuration' stopping condition in the linked propagate segment.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.disable_non_lambert_propagate_stop_conditions`
              - Set this to true to disable all non-LambertDuration stopping conditions in the propagate segment.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.propagate_segment`
              - Gets or sets the propagate segment to manipulate that contains the transfer duration.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.enable_write_to_second_maneuver`
              - Set this to true to write the Delta-V solution from Lambert at the end of the transfer to the linked maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.second_maneuver_segment`
              - Gets or sets the second maneuver segment to manipulate that occurs at the end of the transfer.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ProfileLambertProfile


Property detail
---------------

.. py:property:: coord_system_name
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.coord_system_name
    :type: str

    Gets or sets the coordinate system.

.. py:property:: target_coordinate_type
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_coordinate_type
    :type: LAMBERT_TARGET_COORDINATE_TYPE

    Get the target coordinate type.

.. py:property:: enable_second_maneuver
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.enable_second_maneuver
    :type: bool

    Enable to calculate second maneuver at destination.

.. py:property:: target_position_x
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_position_x
    :type: float

    Gets or sets the X component of the target position for the end of the Lambert transfer.

.. py:property:: target_position_y
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_position_y
    :type: float

    Gets or sets the Y component of the target position for the end of the Lambert transfer.

.. py:property:: target_position_z
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_position_z
    :type: float

    Gets or sets the Z component of the target position for the end of the Lambert transfer.

.. py:property:: target_velocity_x
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_velocity_x
    :type: float

    Gets or sets the X component of the target velocity for the end of the Lambert transfer.

.. py:property:: target_velocity_y
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_velocity_y
    :type: float

    Gets or sets the Y component of the target velocity for the end of the Lambert transfer.

.. py:property:: target_velocity_z
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_velocity_z
    :type: float

    Gets or sets the Z component of the target velocity for the end of the Lambert transfer.

.. py:property:: target_semimajor_axis
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_semimajor_axis
    :type: float

    Gets or sets the target semimajor axis for the end of the Lambert transfer.

.. py:property:: target_eccentricity
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_eccentricity
    :type: float

    Gets or sets the target eccentricity for the end of the Lambert transfer.

.. py:property:: target_inclination
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_inclination
    :type: float

    Gets or sets the target inclination for the end of the Lambert transfer.

.. py:property:: target_right_ascension_of_ascending_node
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_right_ascension_of_ascending_node
    :type: float

    Gets or sets the target right ascension of the ascending node for the end of the Lambert transfer.

.. py:property:: target_argument_of_periapsis
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_argument_of_periapsis
    :type: float

    Gets or sets the target argument of periapsis for the end of the Lambert transfer.

.. py:property:: target_true_anomaly
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_true_anomaly
    :type: float

    Gets or sets the target true anomaly for the end of the Lambert transfer.

.. py:property:: solution_option
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.solution_option
    :type: LAMBERT_SOLUTION_OPTION_TYPE

    Lambert solution calculation type.

.. py:property:: time_of_flight
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.time_of_flight
    :type: float

    Gets or sets the time of flight between departure and arrival for the Lambert solution.

.. py:property:: revolutions
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.revolutions
    :type: int

    Gets or sets the number of revolutions. Dimensionless.

.. py:property:: orbital_energy
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.orbital_energy
    :type: LAMBERT_ORBITAL_ENERGY_TYPE

    Gets or sets the orbital energy for the Lambert solution.

.. py:property:: direction_of_motion
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.direction_of_motion
    :type: LAMBERT_DIRECTION_OF_MOTION_TYPE

    Gets or sets the direction of motion (long or short) for the Lambert solution.

.. py:property:: central_body_collision_altitude_padding
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.central_body_collision_altitude_padding
    :type: float

    Gets or sets the minimum altitude below which the Lambert algorithm will consider the spacecraft to have hit the central body.

.. py:property:: enable_write_to_first_maneuver
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.enable_write_to_first_maneuver
    :type: bool

    Set this to true to write the Delta-V solution from Lambert at the start of the transfer to the linked maneuver.

.. py:property:: first_maneuver_segment
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.first_maneuver_segment
    :type: str

    Gets or sets the first maneuver segment to manipulate that occurs at the start of the transfer.

.. py:property:: enable_write_duration_to_propagate
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.enable_write_duration_to_propagate
    :type: bool

    Set this to true to write the Lambert duration of transfer to the 'LambertDuration' stopping condition in the linked propagate segment.

.. py:property:: disable_non_lambert_propagate_stop_conditions
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.disable_non_lambert_propagate_stop_conditions
    :type: bool

    Set this to true to disable all non-LambertDuration stopping conditions in the propagate segment.

.. py:property:: propagate_segment
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.propagate_segment
    :type: str

    Gets or sets the propagate segment to manipulate that contains the transfer duration.

.. py:property:: enable_write_to_second_maneuver
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.enable_write_to_second_maneuver
    :type: bool

    Set this to true to write the Delta-V solution from Lambert at the end of the transfer to the linked maneuver.

.. py:property:: second_maneuver_segment
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.second_maneuver_segment
    :type: str

    Gets or sets the second maneuver segment to manipulate that occurs at the end of the transfer.


Method detail
-------------




.. py:method:: set_target_coord_type(self, element_type: LAMBERT_TARGET_COORDINATE_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.set_target_coord_type

    Select a target coordinate type.

    :Parameters:

    **element_type** : :obj:`~LAMBERT_TARGET_COORDINATE_TYPE`

    :Returns:

        :obj:`~None`





















































