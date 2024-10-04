AnalysisWorkbenchPlaneFindInSystemWithRateResult
================================================

.. py:class:: ansys.stk.core.vgt.AnalysisWorkbenchPlaneFindInSystemWithRateResult

   Bases: :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchMethodCallResult`

   Contains the results returned with IAgCrdnPlane.FindInSystemWithRate method.

.. py:currentmodule:: AnalysisWorkbenchPlaneFindInSystemWithRateResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchPlaneFindInSystemWithRateResult.is_valid`
              - True indicates the method call was successful.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchPlaneFindInSystemWithRateResult.origin_position`
              - The position of the plane's center point in the specified coordinate system.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchPlaneFindInSystemWithRateResult.origin_velocity`
              - The rate of change of the position of the plane's center point in the specified coordinate system.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchPlaneFindInSystemWithRateResult.x_axis`
              - X-axis vector in the specified reference system.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchPlaneFindInSystemWithRateResult.x_axis_rate`
              - A rate of change of the X-axis vector in the specified reference system.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchPlaneFindInSystemWithRateResult.y_axis`
              - Y-axis vector in the specified reference system.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchPlaneFindInSystemWithRateResult.y_axis_rate`
              - A rate of change of the Y-axis vector in the specified reference system.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import AnalysisWorkbenchPlaneFindInSystemWithRateResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchPlaneFindInSystemWithRateResult.is_valid
    :type: bool

    True indicates the method call was successful.

.. py:property:: origin_position
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchPlaneFindInSystemWithRateResult.origin_position
    :type: ICartesian3Vector

    The position of the plane's center point in the specified coordinate system.

.. py:property:: origin_velocity
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchPlaneFindInSystemWithRateResult.origin_velocity
    :type: ICartesian3Vector

    The rate of change of the position of the plane's center point in the specified coordinate system.

.. py:property:: x_axis
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchPlaneFindInSystemWithRateResult.x_axis
    :type: ICartesian3Vector

    X-axis vector in the specified reference system.

.. py:property:: x_axis_rate
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchPlaneFindInSystemWithRateResult.x_axis_rate
    :type: ICartesian3Vector

    A rate of change of the X-axis vector in the specified reference system.

.. py:property:: y_axis
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchPlaneFindInSystemWithRateResult.y_axis
    :type: ICartesian3Vector

    Y-axis vector in the specified reference system.

.. py:property:: y_axis_rate
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchPlaneFindInSystemWithRateResult.y_axis_rate
    :type: ICartesian3Vector

    A rate of change of the Y-axis vector in the specified reference system.


