CalculationToolSamplingCurvatureTolerance
=========================================

.. py:class:: ansys.stk.core.analysis_workbench.CalculationToolSamplingCurvatureTolerance

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ICalculationToolSamplingMethod`

   Curvature tolerance definition includes parameters that determine how scalar data should be sampled based on limits on slope changes between samples.

.. py:currentmodule:: CalculationToolSamplingCurvatureTolerance

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolSamplingCurvatureTolerance.minimum_time_step`
              - Get the minimum allowed time step.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolSamplingCurvatureTolerance.maximum_time_step`
              - Get the maximum allowed time step.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolSamplingCurvatureTolerance.step_at_boundaries`
              - Get the step taken at boundaries of discontinuity or availability.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolSamplingCurvatureTolerance.relative_tolerance`
              - Get the relative tolerance which determines acceptable difference between predicted and actual changes in values of sampled data over a step relative to the sampled values.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolSamplingCurvatureTolerance.absolute_tolerance`
              - Get the absolute tolerance which determines acceptable difference between predicted and actual changes in values of sampled data over a step.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolSamplingCurvatureTolerance.curvature_tolerance`
              - Get the curvature tolerance which determines acceptable angular difference between slopes over consecutive steps.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import CalculationToolSamplingCurvatureTolerance


Property detail
---------------

.. py:property:: minimum_time_step
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolSamplingCurvatureTolerance.minimum_time_step
    :type: float

    Get the minimum allowed time step.

.. py:property:: maximum_time_step
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolSamplingCurvatureTolerance.maximum_time_step
    :type: float

    Get the maximum allowed time step.

.. py:property:: step_at_boundaries
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolSamplingCurvatureTolerance.step_at_boundaries
    :type: float

    Get the step taken at boundaries of discontinuity or availability.

.. py:property:: relative_tolerance
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolSamplingCurvatureTolerance.relative_tolerance
    :type: float

    Get the relative tolerance which determines acceptable difference between predicted and actual changes in values of sampled data over a step relative to the sampled values.

.. py:property:: absolute_tolerance
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolSamplingCurvatureTolerance.absolute_tolerance
    :type: float

    Get the absolute tolerance which determines acceptable difference between predicted and actual changes in values of sampled data over a step.

.. py:property:: curvature_tolerance
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolSamplingCurvatureTolerance.curvature_tolerance
    :type: float

    Get the curvature tolerance which determines acceptable angular difference between slopes over consecutive steps.


