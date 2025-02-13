VectorGeometryToolVectorProjection
==================================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolVectorProjection

   Bases: :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolVector`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   A projection of a vector computed with respect to a reference plane.

.. py:currentmodule:: VectorGeometryToolVectorProjection

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorProjection.source`
              - Specify a source vector.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorProjection.reference_plane`
              - Specify a reference plane.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolVectorProjection


Property detail
---------------

.. py:property:: source
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorProjection.source
    :type: VectorGeometryToolVectorReference

    Specify a source vector.

.. py:property:: reference_plane
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorProjection.reference_plane
    :type: VectorGeometryToolPlaneReference

    Specify a reference plane.


