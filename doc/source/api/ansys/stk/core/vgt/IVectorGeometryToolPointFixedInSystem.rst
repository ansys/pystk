IVectorGeometryToolPointFixedInSystem
=====================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolPointFixedInSystem

   object
   
   Point fixed in a reference coordinate system using the selected coordinate type.

.. py:currentmodule:: IVectorGeometryToolPointFixedInSystem

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPointFixedInSystem.reference`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPointFixedInSystem.fixed_point`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolPointFixedInSystem


Property detail
---------------

.. py:property:: reference
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointFixedInSystem.reference
    :type: IVectorGeometryToolSystemRefTo

    Specify a reference system.

.. py:property:: fixed_point
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointFixedInSystem.fixed_point
    :type: IPosition

    Specify the point's position. The position is relative with respect to the specified reference system.


