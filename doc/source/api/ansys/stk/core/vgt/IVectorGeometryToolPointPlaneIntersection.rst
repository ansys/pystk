IVectorGeometryToolPointPlaneIntersection
=========================================

.. py:class:: IVectorGeometryToolPointPlaneIntersection

   object
   
   Point on a plane located along a given direction looking from a given origin.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~direction_vector`
            * - :py:meth:`~reference_plane`
            * - :py:meth:`~origin_point`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolPointPlaneIntersection


Property detail
---------------

.. py:property:: direction_vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointPlaneIntersection.direction_vector
    :type: IAgCrdnVectorRefTo

    Specify a direction vector.

.. py:property:: reference_plane
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointPlaneIntersection.reference_plane
    :type: IAgCrdnPlaneRefTo

    Specify a reference plane.

.. py:property:: origin_point
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointPlaneIntersection.origin_point
    :type: IAgCrdnPointRefTo

    Specify the origin point.


