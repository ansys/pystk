IVectorGeometryToolVectorProjection
===================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolVectorProjection

   object
   
   A projection of a vector computed with respect to a reference plane.

.. py:currentmodule:: IVectorGeometryToolVectorProjection

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorProjection.source`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorProjection.reference_plane`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolVectorProjection


Property detail
---------------

.. py:property:: source
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorProjection.source
    :type: IVectorGeometryToolVectorRefTo

    Specify a source vector.

.. py:property:: reference_plane
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorProjection.reference_plane
    :type: IVectorGeometryToolPlaneRefTo

    Specify a reference plane.


