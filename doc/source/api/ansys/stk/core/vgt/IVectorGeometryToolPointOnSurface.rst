IVectorGeometryToolPointOnSurface
=================================

.. py:class:: IVectorGeometryToolPointOnSurface

   object
   
   The detic subpoint of the reference point as projected onto the central body.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~central_body`
            * - :py:meth:`~reference_point`
            * - :py:meth:`~reference_shape`
            * - :py:meth:`~surface_type`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolPointOnSurface


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointOnSurface.central_body
    :type: IAgCrdnCentralBodyRefTo

    Specify a central body.

.. py:property:: reference_point
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointOnSurface.reference_point
    :type: IAgCrdnPointRefTo

    Specify a reference point.

.. py:property:: reference_shape
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointOnSurface.reference_shape
    :type: CRDN_REFERENCE_SHAPE_TYPE

    Specify a reference shape.

.. py:property:: surface_type
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointOnSurface.surface_type
    :type: CRDN_SURFACE_TYPE

    Specify a surface type.


