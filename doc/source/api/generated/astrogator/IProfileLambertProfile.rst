IProfileLambertProfile
======================

.. py:class:: IProfileLambertProfile

   IProfile
   
   Properties for a Lambert profile.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_target_coord_type`
              - Select a target coordinate type.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~coord_system_name`
            * - :py:meth:`~target_coord_type`
            * - :py:meth:`~enable_second_maneuver`
            * - :py:meth:`~target_position_x`
            * - :py:meth:`~target_position_y`
            * - :py:meth:`~target_position_z`
            * - :py:meth:`~target_velocity_x`
            * - :py:meth:`~target_velocity_y`
            * - :py:meth:`~target_velocity_z`
            * - :py:meth:`~target_semimajor_axis`
            * - :py:meth:`~target_eccentricity`
            * - :py:meth:`~target_inclination`
            * - :py:meth:`~target_right_ascension_of_ascending_node`
            * - :py:meth:`~target_argument_of_periapsis`
            * - :py:meth:`~target_true_anomaly`
            * - :py:meth:`~solution_option`
            * - :py:meth:`~time_of_flight`
            * - :py:meth:`~revolutions`
            * - :py:meth:`~orbital_energy`
            * - :py:meth:`~direction_of_motion`
            * - :py:meth:`~central_body_collision_altitude_padding`
            * - :py:meth:`~enable_write_to_first_maneuver`
            * - :py:meth:`~first_maneuver_segment`
            * - :py:meth:`~enable_write_duration_to_propagate`
            * - :py:meth:`~disable_non_lambert_propagate_stop_conditions`
            * - :py:meth:`~propagate_segment`
            * - :py:meth:`~enable_write_to_second_maneuver`
            * - :py:meth:`~second_maneuver_segment`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IProfileLambertProfile


Property detail
---------------

.. py:property:: coord_system_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertProfile.coord_system_name
    :type: str

    Gets or sets the coordinate system.

.. py:property:: target_coord_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertProfile.target_coord_type
    :type: "LAMBERT_TARGET_COORD_TYPE"

    Get the target coordinate type.

.. py:property:: enable_second_maneuver
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertProfile.enable_second_maneuver
    :type: bool

    Enable to calculate second maneuver at destination.

.. py:property:: target_position_x
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertProfile.target_position_x
    :type: float

    Gets or sets the X component of the target position for the end of the Lambert transfer.

.. py:property:: target_position_y
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertProfile.target_position_y
    :type: float

    Gets or sets the Y component of the target position for the end of the Lambert transfer.

.. py:property:: target_position_z
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertProfile.target_position_z
    :type: float

    Gets or sets the Z component of the target position for the end of the Lambert transfer.

.. py:property:: target_velocity_x
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertProfile.target_velocity_x
    :type: float

    Gets or sets the X component of the target velocity for the end of the Lambert transfer.

.. py:property:: target_velocity_y
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertProfile.target_velocity_y
    :type: float

    Gets or sets the Y component of the target velocity for the end of the Lambert transfer.

.. py:property:: target_velocity_z
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertProfile.target_velocity_z
    :type: float

    Gets or sets the Z component of the target velocity for the end of the Lambert transfer.

.. py:property:: target_semimajor_axis
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertProfile.target_semimajor_axis
    :type: float

    Gets or sets the target semimajor axis for the end of the Lambert transfer.

.. py:property:: target_eccentricity
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertProfile.target_eccentricity
    :type: float

    Gets or sets the target eccentricity for the end of the Lambert transfer.

.. py:property:: target_inclination
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertProfile.target_inclination
    :type: float

    Gets or sets the target inclination for the end of the Lambert transfer.

.. py:property:: target_right_ascension_of_ascending_node
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertProfile.target_right_ascension_of_ascending_node
    :type: float

    Gets or sets the target right ascension of the ascending node for the end of the Lambert transfer.

.. py:property:: target_argument_of_periapsis
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertProfile.target_argument_of_periapsis
    :type: float

    Gets or sets the target argument of periapsis for the end of the Lambert transfer.

.. py:property:: target_true_anomaly
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertProfile.target_true_anomaly
    :type: float

    Gets or sets the target true anomaly for the end of the Lambert transfer.

.. py:property:: solution_option
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertProfile.solution_option
    :type: "LAMBERT_SOLUTION_OPTION_TYPE"

    Lambert solution calculation type.

.. py:property:: time_of_flight
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertProfile.time_of_flight
    :type: float

    Gets or sets the time of flight between departure and arrival for the Lambert solution.

.. py:property:: revolutions
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertProfile.revolutions
    :type: int

    Gets or sets the number of revolutions. Dimensionless.

.. py:property:: orbital_energy
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertProfile.orbital_energy
    :type: "LAMBERT_ORBITAL_ENERGY_TYPE"

    Gets or sets the orbital energy for the Lambert solution.

.. py:property:: direction_of_motion
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertProfile.direction_of_motion
    :type: "LAMBERT_DIRECTION_OF_MOTION_TYPE"

    Gets or sets the direction of motion (long or short) for the Lambert solution.

.. py:property:: central_body_collision_altitude_padding
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertProfile.central_body_collision_altitude_padding
    :type: float

    Gets or sets the minimum altitude below which the Lambert algorithm will consider the spacecraft to have hit the central body.

.. py:property:: enable_write_to_first_maneuver
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertProfile.enable_write_to_first_maneuver
    :type: bool

    Set this to true to write the Delta-V solution from Lambert at the start of the transfer to the linked maneuver.

.. py:property:: first_maneuver_segment
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertProfile.first_maneuver_segment
    :type: str

    Gets or sets the first maneuver segment to manipulate that occurs at the start of the transfer.

.. py:property:: enable_write_duration_to_propagate
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertProfile.enable_write_duration_to_propagate
    :type: bool

    Set this to true to write the Lambert duration of transfer to the 'LambertDuration' stopping condition in the linked propagate segment.

.. py:property:: disable_non_lambert_propagate_stop_conditions
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertProfile.disable_non_lambert_propagate_stop_conditions
    :type: bool

    Set this to true to disable all non-LambertDuration stopping conditions in the propagate segment.

.. py:property:: propagate_segment
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertProfile.propagate_segment
    :type: str

    Gets or sets the propagate segment to manipulate that contains the transfer duration.

.. py:property:: enable_write_to_second_maneuver
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertProfile.enable_write_to_second_maneuver
    :type: bool

    Set this to true to write the Delta-V solution from Lambert at the end of the transfer to the linked maneuver.

.. py:property:: second_maneuver_segment
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileLambertProfile.second_maneuver_segment
    :type: str

    Gets or sets the second maneuver segment to manipulate that occurs at the end of the transfer.


Method detail
-------------




.. py:method:: set_target_coord_type(self, elementType:"LAMBERT_TARGET_COORD_TYPE") -> None

    Select a target coordinate type.

    :Parameters:

    **elementType** : :obj:`~"LAMBERT_TARGET_COORD_TYPE"`

    :Returns:

        :obj:`~None`





















































