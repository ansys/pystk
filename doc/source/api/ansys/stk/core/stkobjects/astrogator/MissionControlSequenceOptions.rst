MissionControlSequenceOptions
=============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceOptions

   The MCS Options.

.. py:currentmodule:: MissionControlSequenceOptions

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceOptions.draw_trajectory_in_2d`
              - If true, Astrogator will draw the trajectory in the 2D Graphics windows as the ephemeris is calculated during the current run.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceOptions.draw_trajectory_in_3d`
              - If true, Astrogator will draw the trajectory in the 3D Graphics windows as the ephemeris is calculated during the current run.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceOptions.update_animation_time_for_all_objects`
              - If true, all other objects will be animated so that they appear at the proper position for the time being computed as the trajectory is calculated.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceOptions.clear_dwc_graphics_before_each_run`
              - If true, Astrogator will automatically clear all target iteration graphics of the previous run - in all graphics windows - before the current run draws new calculations.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceOptions.clear_additional_b_plane_points`
              - If true, Astrogator will clear all additional B-Plane points from any previous run - in all graphics windows - before the current run.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceOptions.propagate_on_apply`
              - If true, Astrogator will propagate trajectories whenever you click OK or Apply on the Orbit page. If you want to close the Properties Browser for the satellite without running the MCS, make certain this option is disabled.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceOptions.enable_trajectory_segment_colors`
              - If true, trajectory segments are displayed in the 2D Graphics window in the colors selected for the respective segments; otherwise the color of the trajectory is defined by the 2D Graphics Attributes page.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceOptions.save_numbers_in_raw_format`
              - If true, Astrogator will store satellite information in binary format - to preserve the maximum amount of precision.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceOptions.stopping_condition_time_tolerance`
              - Gets or sets the time tolerance, which will be applied with respect to desired trip values throughout the MCS. If this value is set to zero, time tolerance will not be applied.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceOptions.enable_segment_controls`
              - If true, Astrogator will automatically add independent variables to differential correctors.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceOptions.enable_segment_results`
              - If true, Astrogator will automatically add dependent variables to differential correctors.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceOptions.enable_logging`
              - If true, target sequences can be set to produce 'run history' log files for differential corrector profiles. By default, a target sequence does not produce a log file.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceOptions.graphics_update_rate`
              - Gets or sets the rate (between 0 and 1) at which to update graphics. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceOptions.promote_controls`
              - If true, a target sequence will be able to affect controls and results within a nested target sequence in addition to its own.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceOptions.use_nominal_settings`
              - If true, components or segments that are modified by a target sequence will be restored to their nominal values as soon as the target sequence completes its run.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceOptions.min_ephem_step`
              - Gets or sets the minimum step size for saving ephemeris. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceOptions.generate_ephemeris`
              - If true, Astrogator will generate ephemeris.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceOptions.user_variables`
              - Interface used to add/remove user variables.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MissionControlSequenceOptions.smart_run_mode`
              - Controls whether the run will attempt to only run changed segments.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import MissionControlSequenceOptions


Property detail
---------------

.. py:property:: draw_trajectory_in_2d
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceOptions.draw_trajectory_in_2d
    :type: bool

    If true, Astrogator will draw the trajectory in the 2D Graphics windows as the ephemeris is calculated during the current run.

.. py:property:: draw_trajectory_in_3d
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceOptions.draw_trajectory_in_3d
    :type: bool

    If true, Astrogator will draw the trajectory in the 3D Graphics windows as the ephemeris is calculated during the current run.

.. py:property:: update_animation_time_for_all_objects
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceOptions.update_animation_time_for_all_objects
    :type: bool

    If true, all other objects will be animated so that they appear at the proper position for the time being computed as the trajectory is calculated.

.. py:property:: clear_dwc_graphics_before_each_run
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceOptions.clear_dwc_graphics_before_each_run
    :type: bool

    If true, Astrogator will automatically clear all target iteration graphics of the previous run - in all graphics windows - before the current run draws new calculations.

.. py:property:: clear_additional_b_plane_points
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceOptions.clear_additional_b_plane_points
    :type: bool

    If true, Astrogator will clear all additional B-Plane points from any previous run - in all graphics windows - before the current run.

.. py:property:: propagate_on_apply
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceOptions.propagate_on_apply
    :type: bool

    If true, Astrogator will propagate trajectories whenever you click OK or Apply on the Orbit page. If you want to close the Properties Browser for the satellite without running the MCS, make certain this option is disabled.

.. py:property:: enable_trajectory_segment_colors
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceOptions.enable_trajectory_segment_colors
    :type: bool

    If true, trajectory segments are displayed in the 2D Graphics window in the colors selected for the respective segments; otherwise the color of the trajectory is defined by the 2D Graphics Attributes page.

.. py:property:: save_numbers_in_raw_format
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceOptions.save_numbers_in_raw_format
    :type: bool

    If true, Astrogator will store satellite information in binary format - to preserve the maximum amount of precision.

.. py:property:: stopping_condition_time_tolerance
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceOptions.stopping_condition_time_tolerance
    :type: float

    Gets or sets the time tolerance, which will be applied with respect to desired trip values throughout the MCS. If this value is set to zero, time tolerance will not be applied.

.. py:property:: enable_segment_controls
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceOptions.enable_segment_controls
    :type: bool

    If true, Astrogator will automatically add independent variables to differential correctors.

.. py:property:: enable_segment_results
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceOptions.enable_segment_results
    :type: bool

    If true, Astrogator will automatically add dependent variables to differential correctors.

.. py:property:: enable_logging
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceOptions.enable_logging
    :type: bool

    If true, target sequences can be set to produce 'run history' log files for differential corrector profiles. By default, a target sequence does not produce a log file.

.. py:property:: graphics_update_rate
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceOptions.graphics_update_rate
    :type: float

    Gets or sets the rate (between 0 and 1) at which to update graphics. Dimensionless.

.. py:property:: promote_controls
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceOptions.promote_controls
    :type: bool

    If true, a target sequence will be able to affect controls and results within a nested target sequence in addition to its own.

.. py:property:: use_nominal_settings
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceOptions.use_nominal_settings
    :type: bool

    If true, components or segments that are modified by a target sequence will be restored to their nominal values as soon as the target sequence completes its run.

.. py:property:: min_ephem_step
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceOptions.min_ephem_step
    :type: float

    Gets or sets the minimum step size for saving ephemeris. Uses Time Dimension.

.. py:property:: generate_ephemeris
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceOptions.generate_ephemeris
    :type: bool

    If true, Astrogator will generate ephemeris.

.. py:property:: user_variables
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceOptions.user_variables
    :type: UserVariableDefinitionCollection

    Interface used to add/remove user variables.

.. py:property:: smart_run_mode
    :canonical: ansys.stk.core.stkobjects.astrogator.MissionControlSequenceOptions.smart_run_mode
    :type: SMART_RUN_MODE

    Controls whether the run will attempt to only run changed segments.


