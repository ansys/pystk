IVectorGeometryToolPointAtTimeInstant
=====================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolPointAtTimeInstant

   object
   
   Point fixed relative to reference system based on another point evaluated at specified time instant.

.. py:currentmodule:: IVectorGeometryToolPointAtTimeInstant

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPointAtTimeInstant.reference_time_instant`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPointAtTimeInstant.source_point`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPointAtTimeInstant.reference_system`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolPointAtTimeInstant


Property detail
---------------

.. py:property:: reference_time_instant
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointAtTimeInstant.reference_time_instant
    :type: ITimeToolEvent

    A reference time instant. Can be any Time event.

.. py:property:: source_point
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointAtTimeInstant.source_point
    :type: IVectorGeometryToolPoint

    A source point. Can be any VGT point.

.. py:property:: reference_system
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointAtTimeInstant.reference_system
    :type: IVectorGeometryToolSystem

    A reference system. Can be any VGT system.


