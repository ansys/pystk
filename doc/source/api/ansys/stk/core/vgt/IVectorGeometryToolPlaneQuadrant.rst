IVectorGeometryToolPlaneQuadrant
================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolPlaneQuadrant

   object
   
   A plane based on a selected Quadrant of a reference system.

.. py:currentmodule:: IVectorGeometryToolPlaneQuadrant

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPlaneQuadrant.reference_system`
              - Specify a reference system.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPlaneQuadrant.quadrant`
              - Specify a quadrant.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolPlaneQuadrant


Property detail
---------------

.. py:property:: reference_system
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneQuadrant.reference_system
    :type: IVectorGeometryToolSystemRefTo

    Specify a reference system.

.. py:property:: quadrant
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneQuadrant.quadrant
    :type: CRDN_QUADRANT_TYPE

    Specify a quadrant.


