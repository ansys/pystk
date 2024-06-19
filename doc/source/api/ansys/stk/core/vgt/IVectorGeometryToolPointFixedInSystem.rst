IVectorGeometryToolPointFixedInSystem
=====================================

.. py:class:: IVectorGeometryToolPointFixedInSystem

   object
   
   Point fixed in a reference coordinate system using the selected coordinate type.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~reference`
            * - :py:meth:`~fixed_point`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolPointFixedInSystem


Property detail
---------------

.. py:property:: reference
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointFixedInSystem.reference
    :type: IAgCrdnSystemRefTo

    Specify a reference system.

.. py:property:: fixed_point
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointFixedInSystem.fixed_point
    :type: IAgPosition

    Specify the point's position. The position is relative with respect to the specified reference system.


