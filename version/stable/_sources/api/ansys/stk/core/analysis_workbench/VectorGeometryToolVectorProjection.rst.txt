VectorGeometryToolVectorProjection
==================================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorProjection

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolVector`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   A projection of a vector computed with respect to a reference plane.

.. py:currentmodule:: VectorGeometryToolVectorProjection

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorProjection.source`
              - Specify a source vector.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorProjection.reference_plane`
              - Specify a reference plane.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolVectorProjection


Property detail
---------------

.. py:property:: source
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorProjection.source
    :type: VectorGeometryToolVectorReference

    Specify a source vector.

.. py:property:: reference_plane
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorProjection.reference_plane
    :type: VectorGeometryToolPlaneReference

    Specify a reference plane.


