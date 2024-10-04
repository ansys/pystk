VectorGeometryToolPointAtTimeInstant
====================================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolPointAtTimeInstant

   Bases: :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolPoint`

   Point fixed relative to reference system based on another point evaluated at specified time instant.

.. py:currentmodule:: VectorGeometryToolPointAtTimeInstant

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointAtTimeInstant.reference_time_instant`
              - A reference time instant. Can be any Time event.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointAtTimeInstant.source_point`
              - A source point. Can be any VGT point.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointAtTimeInstant.reference_system`
              - A reference system. Can be any VGT system.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolPointAtTimeInstant


Property detail
---------------

.. py:property:: reference_time_instant
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointAtTimeInstant.reference_time_instant
    :type: ITimeToolInstant

    A reference time instant. Can be any Time event.

.. py:property:: source_point
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointAtTimeInstant.source_point
    :type: IVectorGeometryToolPoint

    A source point. Can be any VGT point.

.. py:property:: reference_system
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointAtTimeInstant.reference_system
    :type: IVectorGeometryToolSystem

    A reference system. Can be any VGT system.


