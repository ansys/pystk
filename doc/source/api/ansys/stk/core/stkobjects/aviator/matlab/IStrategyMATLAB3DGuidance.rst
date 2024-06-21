IStrategyMATLAB3DGuidance
=========================

.. py:class:: ansys.stk.core.stkobjects.aviator.matlab.IStrategyMATLAB3DGuidance

   object
   
   Interface used to access options for a MATLAB - 3D Guidance Strategy of a Basic Maneuver Procedure.

.. py:currentmodule:: IStrategyMATLAB3DGuidance

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.matlab.IStrategyMATLAB3DGuidance.set_stop_time_to_go`
              - Set the option to use the stop time from target stopping condition and set the according value.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.matlab.IStrategyMATLAB3DGuidance.set_stop_slant_range`
              - Set the option to use the stop slant range stopping condition and set the according value.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.matlab.IStrategyMATLAB3DGuidance.is_function_path_valid`
              - Check if the MATLAB function path is valid.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.matlab.IStrategyMATLAB3DGuidance.cancel_tgt_position_vel`
              - Cancel the position velocity strategies for MATLAB 3D Guidance.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.matlab.IStrategyMATLAB3DGuidance.target_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.matlab.IStrategyMATLAB3DGuidance.valid_target_names`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.matlab.IStrategyMATLAB3DGuidance.target_resolution`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.matlab.IStrategyMATLAB3DGuidance.use_stop_time_to_go`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.matlab.IStrategyMATLAB3DGuidance.stop_time_to_go`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.matlab.IStrategyMATLAB3DGuidance.use_stop_slant_range`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.matlab.IStrategyMATLAB3DGuidance.stop_slant_range`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.matlab.IStrategyMATLAB3DGuidance.function_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.matlab.IStrategyMATLAB3DGuidance.check_for_errors`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.matlab.IStrategyMATLAB3DGuidance.display_output`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.matlab.IStrategyMATLAB3DGuidance.closure_mode`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.matlab.IStrategyMATLAB3DGuidance.hobs_max_angle`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.matlab.IStrategyMATLAB3DGuidance.hobs_angle_tol`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.matlab.IStrategyMATLAB3DGuidance.compute_tas_dot`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.matlab.IStrategyMATLAB3DGuidance.airspeed_options`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.matlab.IStrategyMATLAB3DGuidance.position_vel_strategies`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator.matlab import IStrategyMATLAB3DGuidance


Property detail
---------------

.. py:property:: target_name
    :canonical: ansys.stk.core.stkobjects.aviator.matlab.IStrategyMATLAB3DGuidance.target_name
    :type: str

    Gets or sets the target name.

.. py:property:: valid_target_names
    :canonical: ansys.stk.core.stkobjects.aviator.matlab.IStrategyMATLAB3DGuidance.valid_target_names
    :type: list

    Returns the valid target names.

.. py:property:: target_resolution
    :canonical: ansys.stk.core.stkobjects.aviator.matlab.IStrategyMATLAB3DGuidance.target_resolution
    :type: float

    Gets or sets the target position/velocity sampling resolution.

.. py:property:: use_stop_time_to_go
    :canonical: ansys.stk.core.stkobjects.aviator.matlab.IStrategyMATLAB3DGuidance.use_stop_time_to_go
    :type: bool

    Get the option to specify a time to go stopping condition.

.. py:property:: stop_time_to_go
    :canonical: ansys.stk.core.stkobjects.aviator.matlab.IStrategyMATLAB3DGuidance.stop_time_to_go
    :type: float

    Get the stop time from the target at which the maneuver will stop.

.. py:property:: use_stop_slant_range
    :canonical: ansys.stk.core.stkobjects.aviator.matlab.IStrategyMATLAB3DGuidance.use_stop_slant_range
    :type: bool

    Get the option to specify a range from target stopping condition.

.. py:property:: stop_slant_range
    :canonical: ansys.stk.core.stkobjects.aviator.matlab.IStrategyMATLAB3DGuidance.stop_slant_range
    :type: float

    Get the range from the target at which the maneuver will stop.

.. py:property:: function_name
    :canonical: ansys.stk.core.stkobjects.aviator.matlab.IStrategyMATLAB3DGuidance.function_name
    :type: str

    Gets or sets the name of the MATLAB function.

.. py:property:: check_for_errors
    :canonical: ansys.stk.core.stkobjects.aviator.matlab.IStrategyMATLAB3DGuidance.check_for_errors
    :type: bool

    Gets or sets the option to check the function for errors.

.. py:property:: display_output
    :canonical: ansys.stk.core.stkobjects.aviator.matlab.IStrategyMATLAB3DGuidance.display_output
    :type: bool

    Gets or sets the option to display the output from the MATLAB function.

.. py:property:: closure_mode
    :canonical: ansys.stk.core.stkobjects.aviator.matlab.IStrategyMATLAB3DGuidance.closure_mode
    :type: CLOSURE_MODE

    Gets or sets the closure mode for the guidance strategy.

.. py:property:: hobs_max_angle
    :canonical: ansys.stk.core.stkobjects.aviator.matlab.IStrategyMATLAB3DGuidance.hobs_max_angle
    :type: typing.Any

    Gets or sets the closure high off boresight max angle.

.. py:property:: hobs_angle_tol
    :canonical: ansys.stk.core.stkobjects.aviator.matlab.IStrategyMATLAB3DGuidance.hobs_angle_tol
    :type: typing.Any

    Gets or sets the closure high off boresight angle tolerance.

.. py:property:: compute_tas_dot
    :canonical: ansys.stk.core.stkobjects.aviator.matlab.IStrategyMATLAB3DGuidance.compute_tas_dot
    :type: bool

    Gets or sets the option to allow MATLAB to compute the true airspeed for the aircraft.

.. py:property:: airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.matlab.IStrategyMATLAB3DGuidance.airspeed_options
    :type: IBasicManeuverAirspeedOptions

    Get the airspeed options.

.. py:property:: position_vel_strategies
    :canonical: ansys.stk.core.stkobjects.aviator.matlab.IStrategyMATLAB3DGuidance.position_vel_strategies
    :type: IBasicManeuverTargetPositionVel

    Get the position velocity strategies for MATLAB 3D Guidance.


Method detail
-------------








.. py:method:: set_stop_time_to_go(self, enable: bool, time: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.matlab.IStrategyMATLAB3DGuidance.set_stop_time_to_go

    Set the option to use the stop time from target stopping condition and set the according value.

    :Parameters:

    **enable** : :obj:`~bool`
    **time** : :obj:`~float`

    :Returns:

        :obj:`~None`



.. py:method:: set_stop_slant_range(self, enable: bool, range: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.matlab.IStrategyMATLAB3DGuidance.set_stop_slant_range

    Set the option to use the stop slant range stopping condition and set the according value.

    :Parameters:

    **enable** : :obj:`~bool`
    **range** : :obj:`~float`

    :Returns:

        :obj:`~None`



.. py:method:: is_function_path_valid(self) -> bool
    :canonical: ansys.stk.core.stkobjects.aviator.matlab.IStrategyMATLAB3DGuidance.is_function_path_valid

    Check if the MATLAB function path is valid.

    :Returns:

        :obj:`~bool`















.. py:method:: cancel_tgt_position_vel(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.matlab.IStrategyMATLAB3DGuidance.cancel_tgt_position_vel

    Cancel the position velocity strategies for MATLAB 3D Guidance.

    :Returns:

        :obj:`~None`

