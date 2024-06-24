IVectorGeometryToolPlaneFindInSystemResult
==========================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolPlaneFindInSystemResult

   object
   
   Contains the results returned with IAgCrdnPlane.FindInSystem method.

.. py:currentmodule:: IVectorGeometryToolPlaneFindInSystemResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPlaneFindInSystemResult.is_valid`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPlaneFindInSystemResult.origin_position`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPlaneFindInSystemResult.x_axis`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPlaneFindInSystemResult.y_axis`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolPlaneFindInSystemResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneFindInSystemResult.is_valid
    :type: bool

    True indicates the method call was successful.

.. py:property:: origin_position
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneFindInSystemResult.origin_position
    :type: ICartesian3Vector

    The position of the plane's center point in the specified coordinate system.

.. py:property:: x_axis
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneFindInSystemResult.x_axis
    :type: ICartesian3Vector

    X-axis vector in the specified reference system.

.. py:property:: y_axis
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneFindInSystemResult.y_axis
    :type: ICartesian3Vector

    Y-axis vector in the specified reference system.


