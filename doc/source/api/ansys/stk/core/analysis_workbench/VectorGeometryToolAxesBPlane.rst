VectorGeometryToolAxesBPlane
============================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesBPlane

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolAxes`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   B-Plane axes using the selected target body and reference vector.

.. py:currentmodule:: VectorGeometryToolAxesBPlane

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesBPlane.direction`
              - Specify a direction (incoming or outgoing).
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesBPlane.reference_vector`
              - Specify a reference vector.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesBPlane.target_body`
              - Specify a target central body.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesBPlane.trajectory`
              - Specify a trajectory point.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolAxesBPlane


Property detail
---------------

.. py:property:: direction
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesBPlane.direction
    :type: AsymptoteDirectionType

    Specify a direction (incoming or outgoing).

.. py:property:: reference_vector
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesBPlane.reference_vector
    :type: VectorGeometryToolVectorReference

    Specify a reference vector.

.. py:property:: target_body
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesBPlane.target_body
    :type: AnalysisWorkbenchCentralBodyReference

    Specify a target central body.

.. py:property:: trajectory
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesBPlane.trajectory
    :type: VectorGeometryToolPointReference

    Specify a trajectory point.


