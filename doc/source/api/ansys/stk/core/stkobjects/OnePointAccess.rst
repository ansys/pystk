OnePointAccess
==============

.. py:class:: ansys.stk.core.stkobjects.OnePointAccess

   One Point Access.

.. py:currentmodule:: OnePointAccess

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.OnePointAccess.compute`
              - Compute one point access results using the StartTime, StopTime, StepSize, and SummaryOption.
            * - :py:attr:`~ansys.stk.core.stkobjects.OnePointAccess.remove`
              - Remove the one point access component that was created.
            * - :py:attr:`~ansys.stk.core.stkobjects.OnePointAccess.compute_first_satisfaction`
              - Compute and reports the first N satisfaction intervals (where N <= MaxNumAccessesToFind) over the specified interval whose spans meet the specified minimum duration. Does not use output file.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.OnePointAccess.summary_option`
              - Summary option that specifies the level of detail to provide in the computed results.
            * - :py:attr:`~ansys.stk.core.stkobjects.OnePointAccess.start_time`
              - Get or set the start time. Uses current animation time if none is entered.
            * - :py:attr:`~ansys.stk.core.stkobjects.OnePointAccess.stop_time`
              - Get or set the stop time. Uses current animation time if none is entered.  Set this to the same value as StartTime to report at a single time.
            * - :py:attr:`~ansys.stk.core.stkobjects.OnePointAccess.step_size`
              - Get or set the step size. Default is 60 seconds.
            * - :py:attr:`~ansys.stk.core.stkobjects.OnePointAccess.output_to_file`
              - Whether to output to a file.
            * - :py:attr:`~ansys.stk.core.stkobjects.OnePointAccess.output_filename`
              - If set to do so, results will be output to a file with this name.



Examples
--------

Compute an access for one point

.. code-block:: python

    # ISTKObject facility: Facility object
    onePtAccess = facility.create_one_point_access("Satellite/MySatellite")

    # Configure properties (if necessary)
    onePtAccess.start_time = root.current_scenario.start_time
    onePtAccess.stop_time = root.current_scenario.stop_time
    onePtAccess.step_size = 600
    onePtAccess.summary_option = OnePointAccessSummary.DETAILED

    # Compute results
    results = onePtAccess.compute()

    # Print results
    for i in range(0, results.count):
        result = results.item(i)
        print("Time: %s HasAccess: %s" % (result.time, str(result.access_is_satisfied)))

        for j in range(0, result.constraints.count):
            constraint = result.constraints.item(j)
            print(
                "Constraint: %s Object: %s Status: %s Value:%s"
                % (
                    constraint.constraint,
                    constraint.object_path,
                    constraint.status,
                    str(constraint.value),
                )
            )


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import OnePointAccess


Property detail
---------------

.. py:property:: summary_option
    :canonical: ansys.stk.core.stkobjects.OnePointAccess.summary_option
    :type: OnePointAccessSummary

    Summary option that specifies the level of detail to provide in the computed results.

.. py:property:: start_time
    :canonical: ansys.stk.core.stkobjects.OnePointAccess.start_time
    :type: typing.Any

    Get or set the start time. Uses current animation time if none is entered.

.. py:property:: stop_time
    :canonical: ansys.stk.core.stkobjects.OnePointAccess.stop_time
    :type: typing.Any

    Get or set the stop time. Uses current animation time if none is entered.  Set this to the same value as StartTime to report at a single time.

.. py:property:: step_size
    :canonical: ansys.stk.core.stkobjects.OnePointAccess.step_size
    :type: float

    Get or set the step size. Default is 60 seconds.

.. py:property:: output_to_file
    :canonical: ansys.stk.core.stkobjects.OnePointAccess.output_to_file
    :type: bool

    Whether to output to a file.

.. py:property:: output_filename
    :canonical: ansys.stk.core.stkobjects.OnePointAccess.output_filename
    :type: str

    If set to do so, results will be output to a file with this name.


Method detail
-------------

.. py:method:: compute(self) -> OnePointAccessResultCollection
    :canonical: ansys.stk.core.stkobjects.OnePointAccess.compute

    Compute one point access results using the StartTime, StopTime, StepSize, and SummaryOption.

    :Returns:

        :obj:`~OnePointAccessResultCollection`

.. py:method:: remove(self) -> None
    :canonical: ansys.stk.core.stkobjects.OnePointAccess.remove

    Remove the one point access component that was created.

    :Returns:

        :obj:`~None`













.. py:method:: compute_first_satisfaction(self, start_time: typing.Any, stop_time: typing.Any, max_num_accesses_to_find: int, min_duration: float) -> TimeIntervalCollectionReadOnly
    :canonical: ansys.stk.core.stkobjects.OnePointAccess.compute_first_satisfaction

    Compute and reports the first N satisfaction intervals (where N <= MaxNumAccessesToFind) over the specified interval whose spans meet the specified minimum duration. Does not use output file.

    :Parameters:

        **start_time** : :obj:`~typing.Any`

        **stop_time** : :obj:`~typing.Any`

        **max_num_accesses_to_find** : :obj:`~int`

        **min_duration** : :obj:`~float`


    :Returns:

        :obj:`~TimeIntervalCollectionReadOnly`

