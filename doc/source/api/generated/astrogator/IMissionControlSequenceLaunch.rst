IMissionControlSequenceLaunch
=============================

.. py:class:: IMissionControlSequenceLaunch

   object
   
   Properties for a Launch segment.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~enable_control_parameter`
              - Enable the specified control parameter.
            * - :py:meth:`~disable_control_parameter`
              - Disables the specified control parameter.
            * - :py:meth:`~is_control_parameter_enabled`
              - Sees if the specified control is enabled.
            * - :py:meth:`~set_display_system_type`
              - Set the display system type.
            * - :py:meth:`~set_burnout_type`
              - Set the burnout type.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~central_body_name`
            * - :py:meth:`~step_size`
            * - :py:meth:`~pre_launch_time`
            * - :py:meth:`~epoch`
            * - :py:meth:`~control_parameters_available`
            * - :py:meth:`~initial_acceleration`
            * - :py:meth:`~spacecraft_parameters`
            * - :py:meth:`~fuel_tank`
            * - :py:meth:`~display_system_type`
            * - :py:meth:`~display_system`
            * - :py:meth:`~ascent_type`
            * - :py:meth:`~time_of_flight`
            * - :py:meth:`~burnout_type`
            * - :py:meth:`~burnout`
            * - :py:meth:`~burnout_velocity`
            * - :py:meth:`~use_previous_segment_state`
            * - :py:meth:`~set_met_epoch`
            * - :py:meth:`~user_variables`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IMissionControlSequenceLaunch


Property detail
---------------

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceLaunch.central_body_name
    :type: str

    Gets or sets the central body.

.. py:property:: step_size
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceLaunch.step_size
    :type: float

    Gets or sets the time interval between calculated ephemeris output points. Uses Time Dimension.

.. py:property:: pre_launch_time
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceLaunch.pre_launch_time
    :type: float

    Gets or sets the amount of time before the spacecraft's launch that it will be created in the scenario. The vehicle will remain at the launch position until beginning of the launch epoch. Uses Time Dimension.

.. py:property:: epoch
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceLaunch.epoch
    :type: typing.Any

    Gets or sets the date and time of the launch. Uses DateFormat Dimension.

.. py:property:: control_parameters_available
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceLaunch.control_parameters_available
    :type: bool

    Returns whether or not the control parameters can be set.

.. py:property:: initial_acceleration
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceLaunch.initial_acceleration
    :type: float

    Gets or sets the initial acceleration, for the Quartic Motion Ascent Type. Uses Acceleration Dimension.

.. py:property:: spacecraft_parameters
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceLaunch.spacecraft_parameters
    :type: "IAgVASpacecraftParameters"

    Satellite Properties - the spacecraft's physical properties.

.. py:property:: fuel_tank
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceLaunch.fuel_tank
    :type: "IAgVAFuelTank"

    Get the spacecraft's fuel tank properties.

.. py:property:: display_system_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceLaunch.display_system_type
    :type: "LAUNCH_DISPLAY_SYSTEM"

    Get the launch coordinate type.

.. py:property:: display_system
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceLaunch.display_system
    :type: "IAgVADisplaySystem"

    Gets the current Display System.

.. py:property:: ascent_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceLaunch.ascent_type
    :type: "ASCENT_TYPE"

    Gets or sets the order of the spline used to generate the motion along the ellipse.

.. py:property:: time_of_flight
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceLaunch.time_of_flight
    :type: float

    Gets or sets the time of flight (the time from launch to burnout). Uses Time Dimension.

.. py:property:: burnout_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceLaunch.burnout_type
    :type: "BURNOUT_TYPE"

    Get the burnout type.

.. py:property:: burnout
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceLaunch.burnout
    :type: "IAgVABurnout"

    Get the burnout point definition.

.. py:property:: burnout_velocity
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceLaunch.burnout_velocity
    :type: "IAgVABurnoutVelocity"

    Get the burnout velocity definition.

.. py:property:: use_previous_segment_state
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceLaunch.use_previous_segment_state
    :type: bool

    If true, the previous segment state is used to define the launch location parameters.

.. py:property:: set_met_epoch
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceLaunch.set_met_epoch
    :type: bool

    If true, the Mission Elapsed Time epoch will be set to the launch epoch.

.. py:property:: user_variables
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceLaunch.user_variables
    :type: "IAgVAUserVariableCollection"

    Interface used to modify user variables for the launch segment.


Method detail
-------------









.. py:method:: enable_control_parameter(self, param:"CONTROL_LAUNCH") -> None

    Enable the specified control parameter.

    :Parameters:

    **param** : :obj:`~"CONTROL_LAUNCH"`

    :Returns:

        :obj:`~None`

.. py:method:: disable_control_parameter(self, param:"CONTROL_LAUNCH") -> None

    Disables the specified control parameter.

    :Parameters:

    **param** : :obj:`~"CONTROL_LAUNCH"`

    :Returns:

        :obj:`~None`

.. py:method:: is_control_parameter_enabled(self, param:"CONTROL_LAUNCH") -> bool

    Sees if the specified control is enabled.

    :Parameters:

    **param** : :obj:`~"CONTROL_LAUNCH"`

    :Returns:

        :obj:`~bool`







.. py:method:: set_display_system_type(self, displaySystemType:"LAUNCH_DISPLAY_SYSTEM") -> None

    Set the display system type.

    :Parameters:

    **displaySystemType** : :obj:`~"LAUNCH_DISPLAY_SYSTEM"`

    :Returns:

        :obj:`~None`







.. py:method:: set_burnout_type(self, burnoutType:"BURNOUT_TYPE") -> None

    Set the burnout type.

    :Parameters:

    **burnoutType** : :obj:`~"BURNOUT_TYPE"`

    :Returns:

        :obj:`~None`








