IVectorGeometryToolAxesFindInAxesWithRateResult
===============================================

.. py:class:: IVectorGeometryToolAxesFindInAxesWithRateResult

   object
   
   Contains the results returned with IAgCrdnAxes.FindInAxesWithRate method.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_valid`
            * - :py:meth:`~angular_velocity`
            * - :py:meth:`~orientation`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolAxesFindInAxesWithRateResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesFindInAxesWithRateResult.is_valid
    :type: bool

    True indicates the method call was successful.

.. py:property:: angular_velocity
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesFindInAxesWithRateResult.angular_velocity
    :type: "IAgCartesian3Vector"

    Axes' angular velocity.

.. py:property:: orientation
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesFindInAxesWithRateResult.orientation
    :type: "IAgOrientation"

    The axes' orientation.


