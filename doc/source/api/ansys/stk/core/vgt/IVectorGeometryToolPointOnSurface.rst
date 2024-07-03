IVectorGeometryToolPointOnSurface
=================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolPointOnSurface

   object
   
   The detic subpoint of the reference point as projected onto the central body.

.. py:currentmodule:: IVectorGeometryToolPointOnSurface

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPointOnSurface.central_body`
              - Specify a central body.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPointOnSurface.reference_point`
              - Specify a reference point.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPointOnSurface.reference_shape`
              - Specify a reference shape.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPointOnSurface.surface_type`
              - Specify a surface type.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolPointOnSurface


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointOnSurface.central_body
    :type: IAnalysisWorkbenchCentralBodyRefTo

    Specify a central body.

.. py:property:: reference_point
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointOnSurface.reference_point
    :type: IVectorGeometryToolPointRefTo

    Specify a reference point.

.. py:property:: reference_shape
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointOnSurface.reference_shape
    :type: CRDN_REFERENCE_SHAPE_TYPE

    Specify a reference shape.

.. py:property:: surface_type
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointOnSurface.surface_type
    :type: CRDN_SURFACE_TYPE

    Specify a surface type.


