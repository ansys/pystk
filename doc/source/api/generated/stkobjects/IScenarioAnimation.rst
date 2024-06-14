IScenarioAnimation
==================

.. py:class:: IScenarioAnimation

   object
   
   IAgScAnimation Interface for Scenario-level properties that control the animation cycle, animation step definition and the intervals between refresh updates in the 2D and 3D windows.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_time_array_component`
              - Configure the time array using the specified time component. Allowed are only event arrays.
            * - :py:meth:`~set_time_array_qualified_path`
              - Configure the time array using the specified time component. Allowed are only event arrays. QualifiedPath format adheres to the format used throughout VGT API (i.e. \"Scenario/Scenario1 OneMinuteSampleTimes EventArray\").
            * - :py:meth:`~get_time_array_component`
              - Return a time array component used to configure the time array or null if component has not been configured yet.
            * - :py:meth:`~get_time_array_qualified_path`
              - Return the time array component's qualified path or null if no component has been configured yet.
            * - :py:meth:`~reset_time_array_component`
              - Remove and resets the display configuration by unsetting currently set time array component (if any).

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~start_time`
            * - :py:meth:`~enable_anim_cycle_time`
            * - :py:meth:`~anim_cycle_time`
            * - :py:meth:`~anim_step_value`
            * - :py:meth:`~refresh_delta`
            * - :py:meth:`~anim_cycle_type`
            * - :py:meth:`~refresh_delta_type`
            * - :py:meth:`~anim_step_type`
            * - :py:meth:`~continue_x_realtime_from_pause`
            * - :py:meth:`~time_period`
            * - :py:meth:`~time_array_increment`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IScenarioAnimation


Property detail
---------------

.. py:property:: start_time
    :canonical: ansys.stk.core.stkobjects.IScenarioAnimation.start_time
    :type: typing.Any

    Animation start time. Uses DateFormat Dimension.

.. py:property:: enable_anim_cycle_time
    :canonical: ansys.stk.core.stkobjects.IScenarioAnimation.enable_anim_cycle_time
    :type: bool

    Enable a selection between end time and loop-at time.

.. py:property:: anim_cycle_time
    :canonical: ansys.stk.core.stkobjects.IScenarioAnimation.anim_cycle_time
    :type: typing.Any

    Animation end time. Uses DateFormat Dimension.

.. py:property:: anim_step_value
    :canonical: ansys.stk.core.stkobjects.IScenarioAnimation.anim_step_value
    :type: float

    Animation time step. Dimension depends on context.

.. py:property:: refresh_delta
    :canonical: ansys.stk.core.stkobjects.IScenarioAnimation.refresh_delta
    :type: float

    Amount of time between refresh updates. The actual refresh delta is limited by the minimum time necessary to draw the scenario. The refresh time varies with processor performance, graphics hardware and scenario complexity. Uses Time Dimension.

.. py:property:: anim_cycle_type
    :canonical: ansys.stk.core.stkobjects.IScenarioAnimation.anim_cycle_type
    :type: "SCENARIO_END_LOOP_TYPE"

    Animation end time or loop-at time. A member of the AgEScEndLoopType enumeration.

.. py:property:: refresh_delta_type
    :canonical: ansys.stk.core.stkobjects.IScenarioAnimation.refresh_delta_type
    :type: "SCENARIO_REFRESH_DELTA_TYPE"

    Refresh Delta or high speed. A member of the AgEScRefreshDeltaType enumeration.

.. py:property:: anim_step_type
    :canonical: ansys.stk.core.stkobjects.IScenarioAnimation.anim_step_type
    :type: "SCENARIO_TIME_STEP_TYPE"

    Time step, real time (with offset) or a multiple of real time. A member of the AgEScTimeStepType enumeration.

.. py:property:: continue_x_realtime_from_pause
    :canonical: ansys.stk.core.stkobjects.IScenarioAnimation.continue_x_realtime_from_pause
    :type: bool

    Animation XRealtime Continue from Paused Time.

.. py:property:: time_period
    :canonical: ansys.stk.core.stkobjects.IScenarioAnimation.time_period
    :type: "IAgScAnimationTimePeriod"

    Allows the user to configure the scenario's animation time period.

.. py:property:: time_array_increment
    :canonical: ansys.stk.core.stkobjects.IScenarioAnimation.time_array_increment
    :type: int

    Animation Time Array Increment.


Method detail
-------------






















.. py:method:: set_time_array_component(self, component:"IAnalysisWorkbenchComponent") -> None

    Configure the time array using the specified time component. Allowed are only event arrays.

    :Parameters:

    **component** : :obj:`~"IAnalysisWorkbenchComponent"`

    :Returns:

        :obj:`~None`

.. py:method:: set_time_array_qualified_path(self, qualifiedPath:str) -> None

    Configure the time array using the specified time component. Allowed are only event arrays. QualifiedPath format adheres to the format used throughout VGT API (i.e. \"Scenario/Scenario1 OneMinuteSampleTimes EventArray\").

    :Parameters:

    **qualifiedPath** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: get_time_array_component(self) -> "IAnalysisWorkbenchComponent"

    Return a time array component used to configure the time array or null if component has not been configured yet.

    :Returns:

        :obj:`~"IAnalysisWorkbenchComponent"`

.. py:method:: get_time_array_qualified_path(self) -> str

    Return the time array component's qualified path or null if no component has been configured yet.

    :Returns:

        :obj:`~str`

.. py:method:: reset_time_array_component(self) -> None

    Remove and resets the display configuration by unsetting currently set time array component (if any).

    :Returns:

        :obj:`~None`

