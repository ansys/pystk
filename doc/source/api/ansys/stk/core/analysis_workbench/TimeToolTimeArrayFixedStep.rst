TimeToolTimeArrayFixedStep
==========================

.. py:class:: ansys.stk.core.analysis_workbench.TimeToolTimeArrayFixedStep

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ITimeToolTimeArray`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Defined by taking fixed time steps from specified time reference and adding sampled times to array if they fall within specified bounding interval list.

.. py:currentmodule:: TimeToolTimeArrayFixedStep

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeArrayFixedStep.bounding_interval_list`
              - The bounding interval list.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeArrayFixedStep.sampling_time_step`
              - The sampling time step.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeArrayFixedStep.include_interval_edges`
              - Specify whether to include interval edges.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeArrayFixedStep.reference_type`
              - Specify the time reference from which fixed sampling time steps are taken. Note: selecting Start/Stop of each Interval resets the time reference for each interval, whereas other types maintain single reference for entire array.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeArrayFixedStep.reference_time_instant`
              - The reference time instant. Only applicable if the ReferenceType is set to time instant.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import TimeToolTimeArrayFixedStep


Property detail
---------------

.. py:property:: bounding_interval_list
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeArrayFixedStep.bounding_interval_list
    :type: ITimeToolTimeIntervalList

    The bounding interval list.

.. py:property:: sampling_time_step
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeArrayFixedStep.sampling_time_step
    :type: float

    The sampling time step.

.. py:property:: include_interval_edges
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeArrayFixedStep.include_interval_edges
    :type: bool

    Specify whether to include interval edges.

.. py:property:: reference_type
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeArrayFixedStep.reference_type
    :type: SampleReferenceTimeType

    Specify the time reference from which fixed sampling time steps are taken. Note: selecting Start/Stop of each Interval resets the time reference for each interval, whereas other types maintain single reference for entire array.

.. py:property:: reference_time_instant
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeArrayFixedStep.reference_time_instant
    :type: ITimeToolInstant

    The reference time instant. Only applicable if the ReferenceType is set to time instant.


