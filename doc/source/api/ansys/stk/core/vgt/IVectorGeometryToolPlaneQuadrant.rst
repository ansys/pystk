IVectorGeometryToolPlaneQuadrant
================================

.. py:class:: IVectorGeometryToolPlaneQuadrant

   object
   
   A plane based on a selected Quadrant of a reference system.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~reference_system`
            * - :py:meth:`~quadrant`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolPlaneQuadrant


Property detail
---------------

.. py:property:: reference_system
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneQuadrant.reference_system
    :type: IAgCrdnSystemRefTo

    Specify a reference system.

.. py:property:: quadrant
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneQuadrant.quadrant
    :type: CRDN_QUADRANT_TYPE

    Specify a quadrant.


