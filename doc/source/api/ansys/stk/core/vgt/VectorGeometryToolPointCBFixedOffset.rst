VectorGeometryToolPointCBFixedOffset
====================================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolPointCBFixedOffset

   Bases: :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`, :py:class:`~ansys.stk.core.vgt.ITimeToolTimeProperties`, :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolPoint`

   Point specified by fixed components with respect to central body.

.. py:currentmodule:: VectorGeometryToolPointCBFixedOffset

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointCBFixedOffset.central_body`
              - Get the central body.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointCBFixedOffset.reference_shape`
              - Choose the point height's reference. Available options are central body ellipsoid (WSG84), terrain or Mean Sea Level.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointCBFixedOffset.position`
              - A position of the point fixed on the central body.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolPointCBFixedOffset


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointCBFixedOffset.central_body
    :type: str

    Get the central body.

.. py:property:: reference_shape
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointCBFixedOffset.reference_shape
    :type: CRDN_REFERENCE_SHAPE_TYPE

    Choose the point height's reference. Available options are central body ellipsoid (WSG84), terrain or Mean Sea Level.

.. py:property:: position
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointCBFixedOffset.position
    :type: IPosition

    A position of the point fixed on the central body.


