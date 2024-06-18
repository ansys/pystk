IVectorGeometryToolSystemFindInSystemResult
===========================================

.. py:class:: IVectorGeometryToolSystemFindInSystemResult

   object
   
   Contains the results returned with IAgCrdnSystem.FindInSystem method.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_valid`
            * - :py:meth:`~position`
            * - :py:meth:`~velocity`
            * - :py:meth:`~rate`
            * - :py:meth:`~orientation`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolSystemFindInSystemResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolSystemFindInSystemResult.is_valid
    :type: bool

    True indicates the method call was successful.

.. py:property:: position
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolSystemFindInSystemResult.position
    :type: "IAgCartesian3Vector"

    A position vector.

.. py:property:: velocity
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolSystemFindInSystemResult.velocity
    :type: "IAgCartesian3Vector"

    A velocity vector.

.. py:property:: rate
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolSystemFindInSystemResult.rate
    :type: "IAgCartesian3Vector"

    Rate of change.

.. py:property:: orientation
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolSystemFindInSystemResult.orientation
    :type: "IAgOrientation"

    Orientation.


