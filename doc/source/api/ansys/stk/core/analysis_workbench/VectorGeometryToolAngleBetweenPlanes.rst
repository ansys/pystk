VectorGeometryToolAngleBetweenPlanes
====================================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolAngleBetweenPlanes

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolAngle`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   An angle between two planes.

.. py:currentmodule:: VectorGeometryToolAngleBetweenPlanes

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAngleBetweenPlanes.from_plane`
              - Specify the first of the two planes the angle is measured.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAngleBetweenPlanes.to_plane`
              - Specify the second of the two planes the angle is measured.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolAngleBetweenPlanes


Property detail
---------------

.. py:property:: from_plane
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAngleBetweenPlanes.from_plane
    :type: VectorGeometryToolPlaneReference

    Specify the first of the two planes the angle is measured.

.. py:property:: to_plane
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAngleBetweenPlanes.to_plane
    :type: VectorGeometryToolPlaneReference

    Specify the second of the two planes the angle is measured.


