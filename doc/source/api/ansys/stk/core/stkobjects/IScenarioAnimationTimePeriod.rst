IScenarioAnimationTimePeriod
============================

.. py:class:: IScenarioAnimationTimePeriod

   object
   
   IAgScAnimationTimePeriod defines methods and properties to configure the scenario's animation time.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~start_time`
            * - :py:meth:`~stop_time`
            * - :py:meth:`~duration`
            * - :py:meth:`~use_analysis_start_time`
            * - :py:meth:`~use_analysis_stop_time`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IScenarioAnimationTimePeriod


Property detail
---------------

.. py:property:: start_time
    :canonical: ansys.stk.core.stkobjects.IScenarioAnimationTimePeriod.start_time
    :type: "IAgTimePeriodValue"

    Gets the animation's start time. Uses DateFormat Dimension.

.. py:property:: stop_time
    :canonical: ansys.stk.core.stkobjects.IScenarioAnimationTimePeriod.stop_time
    :type: "IAgTimePeriodValue"

    Gets the animation's stop time. Uses DateFormat Dimension.

.. py:property:: duration
    :canonical: ansys.stk.core.stkobjects.IScenarioAnimationTimePeriod.duration
    :type: typing.Any

    A time duration. The value is a relative duration (i.e. \"+1 day\", \"+1 hour\").

.. py:property:: use_analysis_start_time
    :canonical: ansys.stk.core.stkobjects.IScenarioAnimationTimePeriod.use_analysis_start_time
    :type: bool

    Whether the animation start time is the same as the analysis's start time.

.. py:property:: use_analysis_stop_time
    :canonical: ansys.stk.core.stkobjects.IScenarioAnimationTimePeriod.use_analysis_stop_time
    :type: bool

    Whether the animation stop time is the same as the analysis's stop time.


