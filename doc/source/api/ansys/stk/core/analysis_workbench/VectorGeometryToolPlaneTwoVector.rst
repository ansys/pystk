VectorGeometryToolPlaneTwoVector
================================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolPlaneTwoVector

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolPlane`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   A plane normal to a vector at a given point.

.. py:currentmodule:: VectorGeometryToolPlaneTwoVector

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPlaneTwoVector.reference_vector`
              - Specify a reference vector.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPlaneTwoVector.vector_2`
              - Specify a Normal vector.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPlaneTwoVector.reference_point`
              - Specify a reference point.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolPlaneTwoVector


Property detail
---------------

.. py:property:: reference_vector
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPlaneTwoVector.reference_vector
    :type: VectorGeometryToolVectorReference

    Specify a reference vector.

.. py:property:: vector_2
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPlaneTwoVector.vector_2
    :type: VectorGeometryToolVectorReference

    Specify a Normal vector.

.. py:property:: reference_point
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPlaneTwoVector.reference_point
    :type: VectorGeometryToolPointReference

    Specify a reference point.


