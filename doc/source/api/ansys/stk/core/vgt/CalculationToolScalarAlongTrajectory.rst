CalculationToolScalarAlongTrajectory
====================================

.. py:class:: ansys.stk.core.vgt.CalculationToolScalarAlongTrajectory

   Bases: :py:class:`~ansys.stk.core.vgt.ICalculationToolScalar`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Scalar value of spatial calculation evaluated along trajectory of point.

.. py:currentmodule:: CalculationToolScalarAlongTrajectory

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolScalarAlongTrajectory.trajectory_point`
              - Trajectory point.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolScalarAlongTrajectory.spatial_calculation`
              - Spatial Calculation.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import CalculationToolScalarAlongTrajectory


Property detail
---------------

.. py:property:: trajectory_point
    :canonical: ansys.stk.core.vgt.CalculationToolScalarAlongTrajectory.trajectory_point
    :type: IVectorGeometryToolPoint

    Trajectory point.

.. py:property:: spatial_calculation
    :canonical: ansys.stk.core.vgt.CalculationToolScalarAlongTrajectory.spatial_calculation
    :type: ISpatialAnalysisToolSpatialCalculation

    Spatial Calculation.


