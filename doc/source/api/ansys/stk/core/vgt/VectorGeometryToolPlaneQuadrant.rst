VectorGeometryToolPlaneQuadrant
===============================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolPlaneQuadrant

   Bases: :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolPlane`, :py:class:`~ansys.stk.core.vgt.ITimeToolTimeProperties`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   A plane based on a selected Quadrant of a reference system.

.. py:currentmodule:: VectorGeometryToolPlaneQuadrant

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPlaneQuadrant.reference_system`
              - Specify a reference system.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPlaneQuadrant.quadrant`
              - Specify a quadrant.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolPlaneQuadrant


Property detail
---------------

.. py:property:: reference_system
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPlaneQuadrant.reference_system
    :type: VectorGeometryToolSystemRefTo

    Specify a reference system.

.. py:property:: quadrant
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPlaneQuadrant.quadrant
    :type: CRDN_QUADRANT_TYPE

    Specify a quadrant.


