IVectorGeometryToolSystemFindInSystemResult
===========================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolSystemFindInSystemResult

   object
   
   Contains the results returned with IAgCrdnSystem.FindInSystem method.

.. py:currentmodule:: IVectorGeometryToolSystemFindInSystemResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolSystemFindInSystemResult.is_valid`
              - True indicates the method call was successful.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolSystemFindInSystemResult.position`
              - A position vector.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolSystemFindInSystemResult.velocity`
              - A velocity vector.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolSystemFindInSystemResult.rate`
              - Rate of change.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolSystemFindInSystemResult.orientation`
              - Orientation.


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
    :type: ICartesian3Vector

    A position vector.

.. py:property:: velocity
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolSystemFindInSystemResult.velocity
    :type: ICartesian3Vector

    A velocity vector.

.. py:property:: rate
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolSystemFindInSystemResult.rate
    :type: ICartesian3Vector

    Rate of change.

.. py:property:: orientation
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolSystemFindInSystemResult.orientation
    :type: IOrientation

    Orientation.


