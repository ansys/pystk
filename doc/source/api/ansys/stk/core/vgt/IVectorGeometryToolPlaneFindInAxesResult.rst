IVectorGeometryToolPlaneFindInAxesResult
========================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolPlaneFindInAxesResult

   object
   
   Contains the results returned with IAgCrdnPlane.FindInAxes method.

.. py:currentmodule:: IVectorGeometryToolPlaneFindInAxesResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPlaneFindInAxesResult.is_valid`
              - True indicates the method call was successful.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPlaneFindInAxesResult.x_axis`
              - X-axis vector in the specified reference axes.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPlaneFindInAxesResult.y_axis`
              - Y-axis vector in the specified reference axes.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolPlaneFindInAxesResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneFindInAxesResult.is_valid
    :type: bool

    True indicates the method call was successful.

.. py:property:: x_axis
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneFindInAxesResult.x_axis
    :type: ICartesian3Vector

    X-axis vector in the specified reference axes.

.. py:property:: y_axis
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneFindInAxesResult.y_axis
    :type: ICartesian3Vector

    Y-axis vector in the specified reference axes.


