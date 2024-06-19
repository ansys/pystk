IVectorGeometryToolPlaneFindInAxesWithRateResult
================================================

.. py:class:: IVectorGeometryToolPlaneFindInAxesWithRateResult

   object
   
   Contains the results returned with IAgCrdnPlane.FindInAxesWithRate method.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_valid`
            * - :py:meth:`~x_axis`
            * - :py:meth:`~x_axis_rate`
            * - :py:meth:`~y_axis`
            * - :py:meth:`~y_axis_rate`


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
    :type: IAgCartesian3Vector

    X-axis vector in the specified reference axes.

.. py:property:: x_axis_rate
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneFindInAxesWithRateResult.x_axis_rate
    :type: IAgCartesian3Vector

    The rate of change of X-axis vector in the specified reference axes.

.. py:property:: y_axis
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneFindInAxesWithRateResult.y_axis
    :type: IAgCartesian3Vector

    Y-axis vector in the specified reference axes.

.. py:property:: y_axis_rate
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneFindInAxesWithRateResult.y_axis_rate
    :type: IAgCartesian3Vector

    The rate of change of Y-axis vector in the specified reference axes.


