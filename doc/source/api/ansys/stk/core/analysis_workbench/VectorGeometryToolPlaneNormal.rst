VectorGeometryToolPlaneNormal
=============================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolPlaneNormal

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolPlane`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   A plane normal to a vector at a given point.

.. py:currentmodule:: VectorGeometryToolPlaneNormal

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPlaneNormal.normal_vector`
              - Specify a Normal vector.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPlaneNormal.reference_vector`
              - Specify a reference vector.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPlaneNormal.reference_point`
              - Specify a reference point.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolPlaneNormal


Property detail
---------------

.. py:property:: normal_vector
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPlaneNormal.normal_vector
    :type: VectorGeometryToolVectorReference

    Specify a Normal vector.

.. py:property:: reference_vector
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPlaneNormal.reference_vector
    :type: VectorGeometryToolVectorReference

    Specify a reference vector.

.. py:property:: reference_point
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPlaneNormal.reference_point
    :type: VectorGeometryToolPointReference

    Specify a reference point.


