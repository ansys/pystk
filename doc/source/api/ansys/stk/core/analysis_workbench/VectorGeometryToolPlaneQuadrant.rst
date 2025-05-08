VectorGeometryToolPlaneQuadrant
===============================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolPlaneQuadrant

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolPlane`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   A plane based on a selected Quadrant of a reference system.

.. py:currentmodule:: VectorGeometryToolPlaneQuadrant

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPlaneQuadrant.reference_system`
              - Specify a reference system.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPlaneQuadrant.quadrant`
              - Specify a quadrant.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolPlaneQuadrant


Property detail
---------------

.. py:property:: reference_system
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPlaneQuadrant.reference_system
    :type: VectorGeometryToolSystemReference

    Specify a reference system.

.. py:property:: quadrant
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPlaneQuadrant.quadrant
    :type: PlaneQuadrantType

    Specify a quadrant.


