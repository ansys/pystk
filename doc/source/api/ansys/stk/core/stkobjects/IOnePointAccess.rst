IOnePointAccess
===============

.. py:class:: ansys.stk.core.stkobjects.IOnePointAccess

   object
   
   One Point Access.

.. py:currentmodule:: IOnePointAccess

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IOnePointAccess.compute`
              - Compute one point access results using the StartTime, StopTime, StepSize, and SummaryOption.
            * - :py:attr:`~ansys.stk.core.stkobjects.IOnePointAccess.remove`
              - Remove the one point access component that was created.
            * - :py:attr:`~ansys.stk.core.stkobjects.IOnePointAccess.compute_first_satisfaction`
              - Compute and reports the first N satisfaction intervals (where N <= MaxNumAccessesToFind) over the specified interval whose spans meet the specified minimum duration. Does not use output file.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IOnePointAccess.summary_option`
              - Summary option that specifies the level of detail to provide in the computed results.
            * - :py:attr:`~ansys.stk.core.stkobjects.IOnePointAccess.start_time`
              - Gets or sets the start time. Uses current animation time if none is entered.
            * - :py:attr:`~ansys.stk.core.stkobjects.IOnePointAccess.stop_time`
              - Gets or sets the stop time. Uses current animation time if none is entered.  Set this to the same value as StartTime to report at a single time.
            * - :py:attr:`~ansys.stk.core.stkobjects.IOnePointAccess.step_size`
              - Gets or sets the step size. Default is 60 seconds.
            * - :py:attr:`~ansys.stk.core.stkobjects.IOnePointAccess.output_to_file`
              - Whether to output to a file.
            * - :py:attr:`~ansys.stk.core.stkobjects.IOnePointAccess.output_file`
              - If set to do so, results will be output to a file with this name.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IOnePointAccess


Property detail
---------------

.. py:property:: summary_option
    :canonical: ansys.stk.core.stkobjects.IOnePointAccess.summary_option
    :type: ONE_POINT_ACCESS_SUMMARY

    Summary option that specifies the level of detail to provide in the computed results.

.. py:property:: start_time
    :canonical: ansys.stk.core.stkobjects.IOnePointAccess.start_time
    :type: typing.Any

    Gets or sets the start time. Uses current animation time if none is entered.

.. py:property:: stop_time
    :canonical: ansys.stk.core.stkobjects.IOnePointAccess.stop_time
    :type: typing.Any

    Gets or sets the stop time. Uses current animation time if none is entered.  Set this to the same value as StartTime to report at a single time.

.. py:property:: step_size
    :canonical: ansys.stk.core.stkobjects.IOnePointAccess.step_size
    :type: float

    Gets or sets the step size. Default is 60 seconds.

.. py:property:: output_to_file
    :canonical: ansys.stk.core.stkobjects.IOnePointAccess.output_to_file
    :type: bool

    Whether to output to a file.

.. py:property:: output_file
    :canonical: ansys.stk.core.stkobjects.IOnePointAccess.output_file
    :type: str

    If set to do so, results will be output to a file with this name.


Method detail
-------------

.. py:method:: compute(self) -> IOnePointAccessResultCollection
    :canonical: ansys.stk.core.stkobjects.IOnePointAccess.compute

    Compute one point access results using the StartTime, StopTime, StepSize, and SummaryOption.

    :Returns:

        :obj:`~IOnePointAccessResultCollection`

.. py:method:: remove(self) -> None
    :canonical: ansys.stk.core.stkobjects.IOnePointAccess.remove

    Remove the one point access component that was created.

    :Returns:

        :obj:`~None`













.. py:method:: compute_first_satisfaction(self, startTime: typing.Any, stopTime: typing.Any, maxNumAccessesToFind: int, minDuration: float) -> IImmutableIntervalCollection
    :canonical: ansys.stk.core.stkobjects.IOnePointAccess.compute_first_satisfaction

    Compute and reports the first N satisfaction intervals (where N <= MaxNumAccessesToFind) over the specified interval whose spans meet the specified minimum duration. Does not use output file.

    :Parameters:

    **startTime** : :obj:`~typing.Any`
    **stopTime** : :obj:`~typing.Any`
    **maxNumAccessesToFind** : :obj:`~int`
    **minDuration** : :obj:`~float`

    :Returns:

        :obj:`~IImmutableIntervalCollection`

