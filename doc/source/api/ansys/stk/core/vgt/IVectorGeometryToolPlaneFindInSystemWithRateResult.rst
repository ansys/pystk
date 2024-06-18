IVectorGeometryToolPlaneFindInSystemWithRateResult
==================================================

.. py:class:: IVectorGeometryToolPlaneFindInSystemWithRateResult

   object
   
   Contains the results returned with IAgCrdnPlane.FindInSystemWithRate method.

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
            * - :py:meth:`~origin_velocity`
            * - :py:meth:`~x_axis`
            * - :py:meth:`~x_axis_rate`
            * - :py:meth:`~y_axis`
            * - :py:meth:`~y_axis_rate`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolPlaneFindInSystemWithRateResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneFindInSystemWithRateResult.is_valid
    :type: bool

    True indicates the method call was successful.

.. py:property:: origin_position
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneFindInSystemWithRateResult.origin_position
    :type: "IAgCartesian3Vector"

    The position of the plane's center point in the specified coordinate system.

.. py:property:: origin_velocity
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneFindInSystemWithRateResult.origin_velocity
    :type: "IAgCartesian3Vector"

    The rate of change of the position of the plane's center point in the specified coordinate system.

.. py:property:: x_axis
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneFindInSystemWithRateResult.x_axis
    :type: "IAgCartesian3Vector"

    X-axis vector in the specified reference system.

.. py:property:: x_axis_rate
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneFindInSystemWithRateResult.x_axis_rate
    :type: "IAgCartesian3Vector"

    A rate of change of the X-axis vector in the specified reference system.

.. py:property:: y_axis
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneFindInSystemWithRateResult.y_axis
    :type: "IAgCartesian3Vector"

    Y-axis vector in the specified reference system.

.. py:property:: y_axis_rate
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneFindInSystemWithRateResult.y_axis_rate
    :type: "IAgCartesian3Vector"

    A rate of change of the Y-axis vector in the specified reference system.


