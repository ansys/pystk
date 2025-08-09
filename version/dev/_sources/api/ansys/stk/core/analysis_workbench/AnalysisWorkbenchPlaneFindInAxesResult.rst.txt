AnalysisWorkbenchPlaneFindInAxesResult
======================================

.. py:class:: ansys.stk.core.analysis_workbench.AnalysisWorkbenchPlaneFindInAxesResult

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchMethodCallResult`

   Contains the results returned with IVectorGeometryToolPlane.FindInAxes method.

.. py:currentmodule:: AnalysisWorkbenchPlaneFindInAxesResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchPlaneFindInAxesResult.is_valid`
              - True indicates the method call was successful.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchPlaneFindInAxesResult.x_axis`
              - X-axis vector in the specified reference axes.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchPlaneFindInAxesResult.y_axis`
              - Y-axis vector in the specified reference axes.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import AnalysisWorkbenchPlaneFindInAxesResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchPlaneFindInAxesResult.is_valid
    :type: bool

    True indicates the method call was successful.

.. py:property:: x_axis
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchPlaneFindInAxesResult.x_axis
    :type: ICartesian3Vector

    X-axis vector in the specified reference axes.

.. py:property:: y_axis
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchPlaneFindInAxesResult.y_axis
    :type: ICartesian3Vector

    Y-axis vector in the specified reference axes.


