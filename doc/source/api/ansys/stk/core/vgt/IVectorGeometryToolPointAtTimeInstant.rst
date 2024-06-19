IVectorGeometryToolPointAtTimeInstant
=====================================

.. py:class:: IVectorGeometryToolPointAtTimeInstant

   object
   
   Point fixed relative to reference system based on another point evaluated at specified time instant.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~reference_time_instant`
            * - :py:meth:`~source_point`
            * - :py:meth:`~reference_system`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolPointAtTimeInstant


Property detail
---------------

.. py:property:: reference_time_instant
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointAtTimeInstant.reference_time_instant
    :type: IAgCrdnEvent

    A reference time instant. Can be any Time event.

.. py:property:: source_point
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointAtTimeInstant.source_point
    :type: IAgCrdnPoint

    A source point. Can be any VGT point.

.. py:property:: reference_system
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointAtTimeInstant.reference_system
    :type: IAgCrdnSystem

    A reference system. Can be any VGT system.


