ICalculationToolSamplingRelativeTolerance
=========================================

.. py:class:: ansys.stk.core.vgt.ICalculationToolSamplingRelativeTolerance

   object
   
   Relative tolerance definition includes parameters that determine how scalar data should be sampled based on limits on difference between actual changes between samples and changes predicted by dead reckoning.

.. py:currentmodule:: ICalculationToolSamplingRelativeTolerance

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolSamplingRelativeTolerance.minimum_time_step`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolSamplingRelativeTolerance.maximum_time_step`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolSamplingRelativeTolerance.step_at_boundaries`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolSamplingRelativeTolerance.relative_tolerance`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolSamplingRelativeTolerance.absolute_tolerance`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolSamplingRelativeTolerance


Property detail
---------------

.. py:property:: minimum_time_step
    :canonical: ansys.stk.core.vgt.ICalculationToolSamplingRelativeTolerance.minimum_time_step
    :type: float

    Get the minimum allowed time step.

.. py:property:: maximum_time_step
    :canonical: ansys.stk.core.vgt.ICalculationToolSamplingRelativeTolerance.maximum_time_step
    :type: float

    Get the maximum allowed time step.

.. py:property:: step_at_boundaries
    :canonical: ansys.stk.core.vgt.ICalculationToolSamplingRelativeTolerance.step_at_boundaries
    :type: float

    Get the step taken at boundaries of discontinuity or availability.

.. py:property:: relative_tolerance
    :canonical: ansys.stk.core.vgt.ICalculationToolSamplingRelativeTolerance.relative_tolerance
    :type: float

    Get the relative tolerance which determines acceptable difference between predicted and actual changes in values of sampled data over a step relative to the sampled values.

.. py:property:: absolute_tolerance
    :canonical: ansys.stk.core.vgt.ICalculationToolSamplingRelativeTolerance.absolute_tolerance
    :type: float

    Get the absolute tolerance which determines acceptable difference between predicted and actual changes in values of sampled data over a step.


