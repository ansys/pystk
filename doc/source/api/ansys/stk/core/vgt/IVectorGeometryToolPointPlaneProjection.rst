IVectorGeometryToolPointPlaneProjection
=======================================

.. py:class:: IVectorGeometryToolPointPlaneProjection

   object
   
   The projection of a point onto a reference plane. Specify the Source Point and Reference Plane.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~source_point`
            * - :py:meth:`~reference_plane`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolPointPlaneProjection


Property detail
---------------

.. py:property:: source_point
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointPlaneProjection.source_point
    :type: IAgCrdnPointRefTo

    Specify a source point.

.. py:property:: reference_plane
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointPlaneProjection.reference_plane
    :type: IAgCrdnPlaneRefTo

    Specify a reference plane.


