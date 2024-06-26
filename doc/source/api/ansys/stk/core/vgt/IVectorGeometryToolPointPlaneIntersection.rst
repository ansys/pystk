IVectorGeometryToolPointPlaneIntersection
=========================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolPointPlaneIntersection

   object
   
   Point on a plane located along a given direction looking from a given origin.

.. py:currentmodule:: IVectorGeometryToolPointPlaneIntersection

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPointPlaneIntersection.direction_vector`
              - Specify a direction vector.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPointPlaneIntersection.reference_plane`
              - Specify a reference plane.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPointPlaneIntersection.origin_point`
              - Specify the origin point.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolPointPlaneIntersection


Property detail
---------------

.. py:property:: direction_vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointPlaneIntersection.direction_vector
    :type: IVectorGeometryToolVectorRefTo

    Specify a direction vector.

.. py:property:: reference_plane
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointPlaneIntersection.reference_plane
    :type: IVectorGeometryToolPlaneRefTo

    Specify a reference plane.

.. py:property:: origin_point
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointPlaneIntersection.origin_point
    :type: IVectorGeometryToolPointRefTo

    Specify the origin point.


