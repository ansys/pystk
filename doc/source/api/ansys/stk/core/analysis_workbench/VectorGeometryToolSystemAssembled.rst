VectorGeometryToolSystemAssembled
=================================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolSystemAssembled

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolSystem`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   A system assembled from an origin point and a set of reference axes.

.. py:currentmodule:: VectorGeometryToolSystemAssembled

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolSystemAssembled.origin_point`
              - Specify a point of origin.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolSystemAssembled.reference_axes`
              - Specify a reference axes.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolSystemAssembled


Property detail
---------------

.. py:property:: origin_point
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolSystemAssembled.origin_point
    :type: VectorGeometryToolPointReference

    Specify a point of origin.

.. py:property:: reference_axes
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolSystemAssembled.reference_axes
    :type: VectorGeometryToolAxesReference

    Specify a reference axes.


