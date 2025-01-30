MCSLaunch
=========

.. py:class:: ansys.stk.core.stkobjects.astrogator.MCSLaunch

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IMCSSegment`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   The Launch segment.

.. py:currentmodule:: MCSLaunch

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSLaunch.enable_control_parameter`
              - Enable the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSLaunch.disable_control_parameter`
              - Disables the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSLaunch.is_control_parameter_enabled`
              - Sees if the specified control is enabled.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSLaunch.set_display_system_type`
              - Set the display system type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSLaunch.set_burnout_type`
              - Set the burnout type.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSLaunch.central_body_name`
              - Gets or sets the central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSLaunch.step_size`
              - Gets or sets the time interval between calculated ephemeris output points. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSLaunch.pre_launch_time`
              - Gets or sets the amount of time before the spacecraft's launch that it will be created in the scenario. The vehicle will remain at the launch position until beginning of the launch epoch. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSLaunch.epoch`
              - Gets or sets the date and time of the launch. Uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSLaunch.control_parameters_available`
              - Returns whether or not the control parameters can be set.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSLaunch.initial_acceleration`
              - Gets or sets the initial acceleration, for the Quartic Motion Ascent Type. Uses Acceleration Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSLaunch.spacecraft_parameters`
              - Satellite Properties - the spacecraft's physical properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSLaunch.fuel_tank`
              - Get the spacecraft's fuel tank properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSLaunch.display_system_type`
              - Get the launch coordinate type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSLaunch.display_system`
              - Gets the current Display System.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSLaunch.ascent_type`
              - Gets or sets the order of the spline used to generate the motion along the ellipse.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSLaunch.time_of_flight`
              - Gets or sets the time of flight (the time from launch to burnout). Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSLaunch.burnout_type`
              - Get the burnout type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSLaunch.burnout`
              - Get the burnout point definition.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSLaunch.burnout_velocity`
              - Get the burnout velocity definition.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSLaunch.use_previous_segment_state`
              - If true, the previous segment state is used to define the launch location parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSLaunch.set_mission_elapsed_time_epoch`
              - If true, the Mission Elapsed Time epoch will be set to the launch epoch.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSLaunch.user_variables`
              - Interface used to modify user variables for the launch segment.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import MCSLaunch


Property detail
---------------

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSLaunch.central_body_name
    :type: str

    Gets or sets the central body.

.. py:property:: step_size
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSLaunch.step_size
    :type: float

    Gets or sets the time interval between calculated ephemeris output points. Uses Time Dimension.

.. py:property:: pre_launch_time
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSLaunch.pre_launch_time
    :type: float

    Gets or sets the amount of time before the spacecraft's launch that it will be created in the scenario. The vehicle will remain at the launch position until beginning of the launch epoch. Uses Time Dimension.

.. py:property:: epoch
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSLaunch.epoch
    :type: typing.Any

    Gets or sets the date and time of the launch. Uses DateFormat Dimension.

.. py:property:: control_parameters_available
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSLaunch.control_parameters_available
    :type: bool

    Returns whether or not the control parameters can be set.

.. py:property:: initial_acceleration
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSLaunch.initial_acceleration
    :type: float

    Gets or sets the initial acceleration, for the Quartic Motion Ascent Type. Uses Acceleration Dimension.

.. py:property:: spacecraft_parameters
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSLaunch.spacecraft_parameters
    :type: SpacecraftParameters

    Satellite Properties - the spacecraft's physical properties.

.. py:property:: fuel_tank
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSLaunch.fuel_tank
    :type: FuelTank

    Get the spacecraft's fuel tank properties.

.. py:property:: display_system_type
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSLaunch.display_system_type
    :type: LaunchDisplaySystem

    Get the launch coordinate type.

.. py:property:: display_system
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSLaunch.display_system
    :type: IDisplaySystem

    Gets the current Display System.

.. py:property:: ascent_type
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSLaunch.ascent_type
    :type: AscentType

    Gets or sets the order of the spline used to generate the motion along the ellipse.

.. py:property:: time_of_flight
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSLaunch.time_of_flight
    :type: float

    Gets or sets the time of flight (the time from launch to burnout). Uses Time Dimension.

.. py:property:: burnout_type
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSLaunch.burnout_type
    :type: BurnoutType

    Get the burnout type.

.. py:property:: burnout
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSLaunch.burnout
    :type: IBurnout

    Get the burnout point definition.

.. py:property:: burnout_velocity
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSLaunch.burnout_velocity
    :type: BurnoutVelocity

    Get the burnout velocity definition.

.. py:property:: use_previous_segment_state
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSLaunch.use_previous_segment_state
    :type: bool

    If true, the previous segment state is used to define the launch location parameters.

.. py:property:: set_mission_elapsed_time_epoch
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSLaunch.set_mission_elapsed_time_epoch
    :type: bool

    If true, the Mission Elapsed Time epoch will be set to the launch epoch.

.. py:property:: user_variables
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSLaunch.user_variables
    :type: UserVariableCollection

    Interface used to modify user variables for the launch segment.


Method detail
-------------









.. py:method:: enable_control_parameter(self, param: ControlLaunch) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSLaunch.enable_control_parameter

    Enable the specified control parameter.

    :Parameters:

    **param** : :obj:`~ControlLaunch`

    :Returns:

        :obj:`~None`

.. py:method:: disable_control_parameter(self, param: ControlLaunch) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSLaunch.disable_control_parameter

    Disables the specified control parameter.

    :Parameters:

    **param** : :obj:`~ControlLaunch`

    :Returns:

        :obj:`~None`

.. py:method:: is_control_parameter_enabled(self, param: ControlLaunch) -> bool
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSLaunch.is_control_parameter_enabled

    Sees if the specified control is enabled.

    :Parameters:

    **param** : :obj:`~ControlLaunch`

    :Returns:

        :obj:`~bool`







.. py:method:: set_display_system_type(self, display_system_type: LaunchDisplaySystem) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSLaunch.set_display_system_type

    Set the display system type.

    :Parameters:

    **display_system_type** : :obj:`~LaunchDisplaySystem`

    :Returns:

        :obj:`~None`







.. py:method:: set_burnout_type(self, burnout_type: BurnoutType) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSLaunch.set_burnout_type

    Set the burnout type.

    :Parameters:

    **burnout_type** : :obj:`~BurnoutType`

    :Returns:

        :obj:`~None`








