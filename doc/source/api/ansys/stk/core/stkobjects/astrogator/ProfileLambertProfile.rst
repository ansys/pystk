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

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.central_body_collision_altitude_padding`
              - Get or set the minimum altitude below which the Lambert algorithm will consider the spacecraft to have hit the central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.coord_system_name`
              - Get or set the coordinate system.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.direction_of_motion`
              - Get or set the direction of motion (long or short) for the Lambert solution.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.disable_non_lambert_propagate_stop_conditions`
              - Set this to true to disable all non-LambertDuration stopping conditions in the propagate segment.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.enable_second_maneuver`
              - Enable to calculate second maneuver at destination.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.enable_write_duration_to_propagate`
              - Set this to true to write the Lambert duration of transfer to the 'LambertDuration' stopping condition in the linked propagate segment.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.enable_write_to_first_maneuver`
              - Set this to true to write the Delta-V solution from Lambert at the start of the transfer to the linked maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.enable_write_to_second_maneuver`
              - Set this to true to write the Delta-V solution from Lambert at the end of the transfer to the linked maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.first_maneuver_segment`
              - Get or set the first maneuver segment to manipulate that occurs at the start of the transfer.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.orbital_energy`
              - Get or set the orbital energy for the Lambert solution.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.propagate_segment`
              - Get or set the propagate segment to manipulate that contains the transfer duration.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.revolutions`
              - Get or set the number of revolutions. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.second_maneuver_segment`
              - Get or set the second maneuver segment to manipulate that occurs at the end of the transfer.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.solution_option`
              - Lambert solution calculation type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_argument_of_periapsis`
              - Get or set the target argument of periapsis for the end of the Lambert transfer.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_coordinate_type`
              - Get the target coordinate type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_eccentricity`
              - Get or set the target eccentricity for the end of the Lambert transfer.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_inclination`
              - Get or set the target inclination for the end of the Lambert transfer.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_position_x`
              - Get or set the X component of the target position for the end of the Lambert transfer.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_position_y`
              - Get or set the Y component of the target position for the end of the Lambert transfer.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_position_z`
              - Get or set the Z component of the target position for the end of the Lambert transfer.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_right_ascension_of_ascending_node`
              - Get or set the target right ascension of the ascending node for the end of the Lambert transfer.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_semimajor_axis`
              - Get or set the target semimajor axis for the end of the Lambert transfer.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_true_anomaly`
              - Get or set the target true anomaly for the end of the Lambert transfer.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_velocity_x`
              - Get or set the X component of the target velocity for the end of the Lambert transfer.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_velocity_y`
              - Get or set the Y component of the target velocity for the end of the Lambert transfer.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_velocity_z`
              - Get or set the Z component of the target velocity for the end of the Lambert transfer.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.time_of_flight`
              - Get or set the time of flight between departure and arrival for the Lambert solution.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ProfileLambertProfile


Property detail
---------------

.. py:property:: central_body_collision_altitude_padding
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.central_body_collision_altitude_padding
    :type: float

    Get or set the minimum altitude below which the Lambert algorithm will consider the spacecraft to have hit the central body.

.. py:property:: coord_system_name
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.coord_system_name
    :type: str

    Get or set the coordinate system.

.. py:property:: direction_of_motion
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.direction_of_motion
    :type: LambertDirectionOfMotionType

    Get or set the direction of motion (long or short) for the Lambert solution.

.. py:property:: disable_non_lambert_propagate_stop_conditions
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.disable_non_lambert_propagate_stop_conditions
    :type: bool

    Set this to true to disable all non-LambertDuration stopping conditions in the propagate segment.

.. py:property:: enable_second_maneuver
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.enable_second_maneuver
    :type: bool

    Enable to calculate second maneuver at destination.

.. py:property:: enable_write_duration_to_propagate
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.enable_write_duration_to_propagate
    :type: bool

    Set this to true to write the Lambert duration of transfer to the 'LambertDuration' stopping condition in the linked propagate segment.

.. py:property:: enable_write_to_first_maneuver
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.enable_write_to_first_maneuver
    :type: bool

    Set this to true to write the Delta-V solution from Lambert at the start of the transfer to the linked maneuver.

.. py:property:: enable_write_to_second_maneuver
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.enable_write_to_second_maneuver
    :type: bool

    Set this to true to write the Delta-V solution from Lambert at the end of the transfer to the linked maneuver.

.. py:property:: first_maneuver_segment
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.first_maneuver_segment
    :type: str

    Get or set the first maneuver segment to manipulate that occurs at the start of the transfer.

.. py:property:: orbital_energy
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.orbital_energy
    :type: LambertOrbitalEnergyType

    Get or set the orbital energy for the Lambert solution.

.. py:property:: propagate_segment
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.propagate_segment
    :type: str

    Get or set the propagate segment to manipulate that contains the transfer duration.

.. py:property:: revolutions
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.revolutions
    :type: int

    Get or set the number of revolutions. Dimensionless.

.. py:property:: second_maneuver_segment
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.second_maneuver_segment
    :type: str

    Get or set the second maneuver segment to manipulate that occurs at the end of the transfer.

.. py:property:: solution_option
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.solution_option
    :type: LambertSolutionOptionType

    Lambert solution calculation type.

.. py:property:: target_argument_of_periapsis
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_argument_of_periapsis
    :type: float

    Get or set the target argument of periapsis for the end of the Lambert transfer.

.. py:property:: target_coordinate_type
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_coordinate_type
    :type: LambertTargetCoordinateType

    Get the target coordinate type.

.. py:property:: target_eccentricity
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_eccentricity
    :type: float

    Get or set the target eccentricity for the end of the Lambert transfer.

.. py:property:: target_inclination
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_inclination
    :type: float

    Get or set the target inclination for the end of the Lambert transfer.

.. py:property:: target_position_x
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_position_x
    :type: float

    Get or set the X component of the target position for the end of the Lambert transfer.

.. py:property:: target_position_y
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_position_y
    :type: float

    Get or set the Y component of the target position for the end of the Lambert transfer.

.. py:property:: target_position_z
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_position_z
    :type: float

    Get or set the Z component of the target position for the end of the Lambert transfer.

.. py:property:: target_right_ascension_of_ascending_node
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_right_ascension_of_ascending_node
    :type: float

    Get or set the target right ascension of the ascending node for the end of the Lambert transfer.

.. py:property:: target_semimajor_axis
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_semimajor_axis
    :type: float

    Get or set the target semimajor axis for the end of the Lambert transfer.

.. py:property:: target_true_anomaly
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_true_anomaly
    :type: float

    Get or set the target true anomaly for the end of the Lambert transfer.

.. py:property:: target_velocity_x
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_velocity_x
    :type: float

    Get or set the X component of the target velocity for the end of the Lambert transfer.

.. py:property:: target_velocity_y
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_velocity_y
    :type: float

    Get or set the Y component of the target velocity for the end of the Lambert transfer.

.. py:property:: target_velocity_z
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.target_velocity_z
    :type: float

    Get or set the Z component of the target velocity for the end of the Lambert transfer.

.. py:property:: time_of_flight
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.time_of_flight
    :type: float

    Get or set the time of flight between departure and arrival for the Lambert solution.


Method detail
-------------



























.. py:method:: set_target_coord_type(self, element_type: LambertTargetCoordinateType) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileLambertProfile.set_target_coord_type

    Select a target coordinate type.

    :Parameters:

        **element_type** : :obj:`~LambertTargetCoordinateType`


    :Returns:

        :obj:`~None`






























