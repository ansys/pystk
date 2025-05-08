CalculationToolConvergeBasic
============================

.. py:class:: ansys.stk.core.analysis_workbench.CalculationToolConvergeBasic

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchConvergence`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Convergence definition includes parameters that determine criteria for accurate detection of extrema or condition crossings for scalar calculations.

.. py:currentmodule:: CalculationToolConvergeBasic

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolConvergeBasic.sense`
              - Get the convergence sense which determines whether the converged value should be limited to just within or just outside of condition boundaries.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolConvergeBasic.time_tolerance`
              - Get the time tolerance which determines the time accuracy of the converged value.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolConvergeBasic.absolute_tolerance`
              - Get the absolute tolerance which determines the distance between the value and the boundaries within which the value is considered converged.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolConvergeBasic.relative_tolerance`
              - Get the relative tolerance which determines the relative distance between the value and the boundaries within which the value is considered converged.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import CalculationToolConvergeBasic


Property detail
---------------

.. py:property:: sense
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolConvergeBasic.sense
    :type: ThresholdConvergenceSenseType

    Get the convergence sense which determines whether the converged value should be limited to just within or just outside of condition boundaries.

.. py:property:: time_tolerance
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolConvergeBasic.time_tolerance
    :type: float

    Get the time tolerance which determines the time accuracy of the converged value.

.. py:property:: absolute_tolerance
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolConvergeBasic.absolute_tolerance
    :type: float

    Get the absolute tolerance which determines the distance between the value and the boundaries within which the value is considered converged.

.. py:property:: relative_tolerance
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolConvergeBasic.relative_tolerance
    :type: float

    Get the relative tolerance which determines the relative distance between the value and the boundaries within which the value is considered converged.


