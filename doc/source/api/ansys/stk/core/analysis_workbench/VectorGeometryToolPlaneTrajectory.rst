VectorGeometryToolPlaneTrajectory
=================================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolPlaneTrajectory

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolPlane`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   The plane is defined on the basis of a trajectory of a Point with respect to a ReferenceSystem.

.. py:currentmodule:: VectorGeometryToolPlaneTrajectory

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPlaneTrajectory.point`
              - Specify a trajectory point.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPlaneTrajectory.reference_system`
              - Specify a reference system.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPlaneTrajectory.rotation_offset`
              - Specify an angle measured from X (Axis 1) away from Y (Axis 2).



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolPlaneTrajectory


Property detail
---------------

.. py:property:: point
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPlaneTrajectory.point
    :type: VectorGeometryToolPointReference

    Specify a trajectory point.

.. py:property:: reference_system
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPlaneTrajectory.reference_system
    :type: VectorGeometryToolSystemReference

    Specify a reference system.

.. py:property:: rotation_offset
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPlaneTrajectory.rotation_offset
    :type: float

    Specify an angle measured from X (Axis 1) away from Y (Axis 2).


