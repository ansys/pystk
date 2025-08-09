ScenarioAnimation
=================

.. py:class:: ansys.stk.core.stkobjects.ScenarioAnimation

   Class defining the animation properties of a Scenario.

.. py:currentmodule:: ScenarioAnimation

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioAnimation.set_time_array_component`
              - Configure the time array using the specified time component. Allowed are only event arrays.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioAnimation.set_time_array_qualified_path`
              - Configure the time array using the specified time component. Allowed are only event arrays. QualifiedPath format adheres to the format used throughout VGT API (i.e. ``Scenario/Scenario1 OneMinuteSampleTimes EventArray``).
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioAnimation.get_time_array_component`
              - Return a time array component used to configure the time array or null if component has not been configured yet.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioAnimation.get_time_array_qualified_path`
              - Return the time array component's qualified path or null if no component has been configured yet.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioAnimation.reset_time_array_component`
              - Remove and resets the display configuration by unsetting currently set time array component (if any).

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioAnimation.start_time`
              - Animation start time. Uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioAnimation.enable_anim_cycle_time`
              - Enable a selection between end time and loop-at time.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioAnimation.animation_cycle_time`
              - Animation end time. Uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioAnimation.animation_step_value`
              - Animation time step. Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioAnimation.refresh_delta`
              - Amount of time between refresh updates. The actual refresh delta is limited by the minimum time necessary to draw the scenario. The refresh time varies with processor performance, graphics hardware and scenario complexity. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioAnimation.animation_end_loop_type`
              - Animation end time or loop-at time. A member of the ScenarioEndLoopType enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioAnimation.refresh_delta_type`
              - Refresh Delta or high speed. A member of the ScenarioRefreshDeltaType enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioAnimation.animation_step_type`
              - Time step, real time (with offset) or a multiple of real time. A member of the ScenarioTimeStepType enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioAnimation.continue_x_real_time_from_pause`
              - Animation XRealtime Continue from Paused Time.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioAnimation.time_period`
              - Allow the user to configure the scenario's animation time period.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioAnimation.time_array_increment`
              - Animation Time Array Increment.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ScenarioAnimation


Property detail
---------------

.. py:property:: start_time
    :canonical: ansys.stk.core.stkobjects.ScenarioAnimation.start_time
    :type: typing.Any

    Animation start time. Uses DateFormat Dimension.

.. py:property:: enable_anim_cycle_time
    :canonical: ansys.stk.core.stkobjects.ScenarioAnimation.enable_anim_cycle_time
    :type: bool

    Enable a selection between end time and loop-at time.

.. py:property:: animation_cycle_time
    :canonical: ansys.stk.core.stkobjects.ScenarioAnimation.animation_cycle_time
    :type: typing.Any

    Animation end time. Uses DateFormat Dimension.

.. py:property:: animation_step_value
    :canonical: ansys.stk.core.stkobjects.ScenarioAnimation.animation_step_value
    :type: float

    Animation time step. Dimension depends on context.

.. py:property:: refresh_delta
    :canonical: ansys.stk.core.stkobjects.ScenarioAnimation.refresh_delta
    :type: float

    Amount of time between refresh updates. The actual refresh delta is limited by the minimum time necessary to draw the scenario. The refresh time varies with processor performance, graphics hardware and scenario complexity. Uses Time Dimension.

.. py:property:: animation_end_loop_type
    :canonical: ansys.stk.core.stkobjects.ScenarioAnimation.animation_end_loop_type
    :type: ScenarioEndLoopType

    Animation end time or loop-at time. A member of the ScenarioEndLoopType enumeration.

.. py:property:: refresh_delta_type
    :canonical: ansys.stk.core.stkobjects.ScenarioAnimation.refresh_delta_type
    :type: ScenarioRefreshDeltaType

    Refresh Delta or high speed. A member of the ScenarioRefreshDeltaType enumeration.

.. py:property:: animation_step_type
    :canonical: ansys.stk.core.stkobjects.ScenarioAnimation.animation_step_type
    :type: ScenarioTimeStepType

    Time step, real time (with offset) or a multiple of real time. A member of the ScenarioTimeStepType enumeration.

.. py:property:: continue_x_real_time_from_pause
    :canonical: ansys.stk.core.stkobjects.ScenarioAnimation.continue_x_real_time_from_pause
    :type: bool

    Animation XRealtime Continue from Paused Time.

.. py:property:: time_period
    :canonical: ansys.stk.core.stkobjects.ScenarioAnimation.time_period
    :type: ScenarioAnimationTimePeriod

    Allow the user to configure the scenario's animation time period.

.. py:property:: time_array_increment
    :canonical: ansys.stk.core.stkobjects.ScenarioAnimation.time_array_increment
    :type: int

    Animation Time Array Increment.


Method detail
-------------






















.. py:method:: set_time_array_component(self, component: IAnalysisWorkbenchComponent) -> None
    :canonical: ansys.stk.core.stkobjects.ScenarioAnimation.set_time_array_component

    Configure the time array using the specified time component. Allowed are only event arrays.

    :Parameters:

        **component** : :obj:`~IAnalysisWorkbenchComponent`


    :Returns:

        :obj:`~None`

.. py:method:: set_time_array_qualified_path(self, qualified_path: str) -> None
    :canonical: ansys.stk.core.stkobjects.ScenarioAnimation.set_time_array_qualified_path

    Configure the time array using the specified time component. Allowed are only event arrays. QualifiedPath format adheres to the format used throughout VGT API (i.e. ``Scenario/Scenario1 OneMinuteSampleTimes EventArray``).

    :Parameters:

        **qualified_path** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: get_time_array_component(self) -> IAnalysisWorkbenchComponent
    :canonical: ansys.stk.core.stkobjects.ScenarioAnimation.get_time_array_component

    Return a time array component used to configure the time array or null if component has not been configured yet.

    :Returns:

        :obj:`~IAnalysisWorkbenchComponent`

.. py:method:: get_time_array_qualified_path(self) -> str
    :canonical: ansys.stk.core.stkobjects.ScenarioAnimation.get_time_array_qualified_path

    Return the time array component's qualified path or null if no component has been configured yet.

    :Returns:

        :obj:`~str`

.. py:method:: reset_time_array_component(self) -> None
    :canonical: ansys.stk.core.stkobjects.ScenarioAnimation.reset_time_array_component

    Remove and resets the display configuration by unsetting currently set time array component (if any).

    :Returns:

        :obj:`~None`

