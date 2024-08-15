IVectorGeometryToolPlaneFindInAxesWithRateResult
================================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolPlaneFindInAxesWithRateResult

   Contains the results returned with IAgCrdnPlane.FindInAxesWithRate method.

.. py:currentmodule:: IVectorGeometryToolPlaneFindInAxesWithRateResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPlaneFindInAxesWithRateResult.is_valid`
              - True indicates the method call was successful.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPlaneFindInAxesWithRateResult.x_axis`
              - X-axis vector in the specified reference axes.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPlaneFindInAxesWithRateResult.x_axis_rate`
              - The rate of change of X-axis vector in the specified reference axes.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPlaneFindInAxesWithRateResult.y_axis`
              - Y-axis vector in the specified reference axes.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPlaneFindInAxesWithRateResult.y_axis_rate`
              - The rate of change of Y-axis vector in the specified reference axes.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolPlaneFindInAxesWithRateResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneFindInAxesWithRateResult.is_valid
    :type: bool

    True indicates the method call was successful.

.. py:property:: x_axis
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneFindInAxesWithRateResult.x_axis
    :type: ICartesian3Vector

    X-axis vector in the specified reference axes.

.. py:property:: x_axis_rate
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneFindInAxesWithRateResult.x_axis_rate
    :type: ICartesian3Vector

    The rate of change of X-axis vector in the specified reference axes.

.. py:property:: y_axis
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneFindInAxesWithRateResult.y_axis
    :type: ICartesian3Vector

    Y-axis vector in the specified reference axes.

.. py:property:: y_axis_rate
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneFindInAxesWithRateResult.y_axis_rate
    :type: ICartesian3Vector

    The rate of change of Y-axis vector in the specified reference axes.


