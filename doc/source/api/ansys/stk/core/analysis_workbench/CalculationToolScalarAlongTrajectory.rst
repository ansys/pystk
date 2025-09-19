CalculationToolScalarAlongTrajectory
====================================

.. py:class:: ansys.stk.core.analysis_workbench.CalculationToolScalarAlongTrajectory

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ICalculationToolScalar`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Scalar value of spatial calculation evaluated along trajectory of point.

.. py:currentmodule:: CalculationToolScalarAlongTrajectory

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarAlongTrajectory.spatial_calculation`
              - Spatial Calculation.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarAlongTrajectory.trajectory_point`
              - Trajectory point.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import CalculationToolScalarAlongTrajectory


Property detail
---------------

.. py:property:: spatial_calculation
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarAlongTrajectory.spatial_calculation
    :type: ISpatialAnalysisToolSpatialCalculation

    Spatial Calculation.

.. py:property:: trajectory_point
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarAlongTrajectory.trajectory_point
    :type: IVectorGeometryToolPoint

    Trajectory point.


