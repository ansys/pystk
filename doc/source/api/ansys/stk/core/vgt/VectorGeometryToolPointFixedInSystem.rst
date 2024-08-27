VectorGeometryToolPointFixedInSystem
====================================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolPointFixedInSystem

   Bases: :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolPoint`, :py:class:`~ansys.stk.core.vgt.ITimeToolTimeProperties`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Point fixed in a reference coordinate system using the selected coordinate type.

.. py:currentmodule:: VectorGeometryToolPointFixedInSystem

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointFixedInSystem.reference`
              - Specify a reference system.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointFixedInSystem.fixed_point`
              - Specify the point's position. The position is relative with respect to the specified reference system.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolPointFixedInSystem


Property detail
---------------

.. py:property:: reference
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointFixedInSystem.reference
    :type: VectorGeometryToolSystemRefTo

    Specify a reference system.

.. py:property:: fixed_point
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointFixedInSystem.fixed_point
    :type: IPosition

    Specify the point's position. The position is relative with respect to the specified reference system.


