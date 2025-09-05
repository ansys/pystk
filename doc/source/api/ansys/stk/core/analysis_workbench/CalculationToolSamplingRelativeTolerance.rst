CalculationToolSamplingRelativeTolerance
========================================

.. py:class:: ansys.stk.core.analysis_workbench.CalculationToolSamplingRelativeTolerance

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ICalculationToolSamplingMethod`

   Relative tolerance definition includes parameters that determine how scalar data should be sampled based on limits on difference between actual changes between samples and changes predicted by dead reckoning.

.. py:currentmodule:: CalculationToolSamplingRelativeTolerance

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolSamplingRelativeTolerance.absolute_tolerance`
              - Get the absolute tolerance which determines acceptable difference between predicted and actual changes in values of sampled data over a step.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolSamplingRelativeTolerance.maximum_time_step`
              - Get the maximum allowed time step.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolSamplingRelativeTolerance.minimum_time_step`
              - Get the minimum allowed time step.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolSamplingRelativeTolerance.relative_tolerance`
              - Get the relative tolerance which determines acceptable difference between predicted and actual changes in values of sampled data over a step relative to the sampled values.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolSamplingRelativeTolerance.step_at_boundaries`
              - Get the step taken at boundaries of discontinuity or availability.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import CalculationToolSamplingRelativeTolerance


Property detail
---------------

.. py:property:: absolute_tolerance
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolSamplingRelativeTolerance.absolute_tolerance
    :type: float

    Get the absolute tolerance which determines acceptable difference between predicted and actual changes in values of sampled data over a step.

.. py:property:: maximum_time_step
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolSamplingRelativeTolerance.maximum_time_step
    :type: float

    Get the maximum allowed time step.

.. py:property:: minimum_time_step
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolSamplingRelativeTolerance.minimum_time_step
    :type: float

    Get the minimum allowed time step.

.. py:property:: relative_tolerance
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolSamplingRelativeTolerance.relative_tolerance
    :type: float

    Get the relative tolerance which determines acceptable difference between predicted and actual changes in values of sampled data over a step relative to the sampled values.

.. py:property:: step_at_boundaries
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolSamplingRelativeTolerance.step_at_boundaries
    :type: float

    Get the step taken at boundaries of discontinuity or availability.


