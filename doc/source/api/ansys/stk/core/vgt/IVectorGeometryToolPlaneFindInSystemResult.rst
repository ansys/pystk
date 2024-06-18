IVectorGeometryToolPlaneFindInSystemResult
==========================================

.. py:class:: IVectorGeometryToolPlaneFindInSystemResult

   object
   
   Contains the results returned with IAgCrdnPlane.FindInSystem method.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_valid`
            * - :py:meth:`~origin_position`
            * - :py:meth:`~x_axis`
            * - :py:meth:`~y_axis`


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
    :type: "IAgCartesian3Vector"

    The position of the plane's center point in the specified coordinate system.

.. py:property:: x_axis
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneFindInSystemResult.x_axis
    :type: "IAgCartesian3Vector"

    X-axis vector in the specified reference system.

.. py:property:: y_axis
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneFindInSystemResult.y_axis
    :type: "IAgCartesian3Vector"

    Y-axis vector in the specified reference system.


