VectorGeometryToolSystemAssembled
=================================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolSystemAssembled

   Bases: :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolSystem`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   A system assembled from an origin point and a set of reference axes.

.. py:currentmodule:: VectorGeometryToolSystemAssembled

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolSystemAssembled.origin_point`
              - Specify a point of origin.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolSystemAssembled.reference_axes`
              - Specify a reference axes.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolSystemAssembled


Property detail
---------------

.. py:property:: origin_point
    :canonical: ansys.stk.core.vgt.VectorGeometryToolSystemAssembled.origin_point
    :type: VectorGeometryToolPointReference

    Specify a point of origin.

.. py:property:: reference_axes
    :canonical: ansys.stk.core.vgt.VectorGeometryToolSystemAssembled.reference_axes
    :type: VectorGeometryToolAxesReference

    Specify a reference axes.


