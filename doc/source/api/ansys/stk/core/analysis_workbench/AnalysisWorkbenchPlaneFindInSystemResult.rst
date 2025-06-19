AnalysisWorkbenchPlaneFindInSystemResult
========================================

.. py:class:: ansys.stk.core.analysis_workbench.AnalysisWorkbenchPlaneFindInSystemResult

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchMethodCallResult`

   Contains the results returned with IVectorGeometryToolPlane.FindInSystem method.

.. py:currentmodule:: AnalysisWorkbenchPlaneFindInSystemResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchPlaneFindInSystemResult.is_valid`
              - True indicates the method call was successful.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchPlaneFindInSystemResult.origin_position`
              - The position of the plane's center point in the specified coordinate system.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchPlaneFindInSystemResult.x_axis`
              - X-axis vector in the specified reference system.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchPlaneFindInSystemResult.y_axis`
              - Y-axis vector in the specified reference system.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import AnalysisWorkbenchPlaneFindInSystemResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchPlaneFindInSystemResult.is_valid
    :type: bool

    True indicates the method call was successful.

.. py:property:: origin_position
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchPlaneFindInSystemResult.origin_position
    :type: ICartesian3Vector

    The position of the plane's center point in the specified coordinate system.

.. py:property:: x_axis
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchPlaneFindInSystemResult.x_axis
    :type: ICartesian3Vector

    X-axis vector in the specified reference system.

.. py:property:: y_axis
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchPlaneFindInSystemResult.y_axis
    :type: ICartesian3Vector

    Y-axis vector in the specified reference system.


