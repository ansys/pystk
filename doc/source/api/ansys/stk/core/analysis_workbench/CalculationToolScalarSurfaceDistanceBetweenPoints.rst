CalculationToolScalarSurfaceDistanceBetweenPoints
=================================================

.. py:class:: ansys.stk.core.analysis_workbench.CalculationToolScalarSurfaceDistanceBetweenPoints

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ICalculationToolScalar`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Surface distance along the specified central body ellipsoid between two points (or their respective projections if specified at altitude).

.. py:currentmodule:: CalculationToolScalarSurfaceDistanceBetweenPoints

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarSurfaceDistanceBetweenPoints.point_1`
              - Starting point on the central body ellipsoid (or projection of point at altitude onto the ellipsoid).
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarSurfaceDistanceBetweenPoints.point_2`
              - Terminating point on the central body ellipsoid (or projection of point at altitude onto the ellipsoid).
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarSurfaceDistanceBetweenPoints.surface_central_body`
              - Central body on which the surface distance between points is to be calculated.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarSurfaceDistanceBetweenPoints.differencing_time_step`
              - Time step used in numerical evaluation of scalar calculation time rate of change (derivatives using central differencing).



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import (
        CalculationToolScalarSurfaceDistanceBetweenPoints,
    )


Property detail
---------------

.. py:property:: point_1
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarSurfaceDistanceBetweenPoints.point_1
    :type: IVectorGeometryToolPoint

    Starting point on the central body ellipsoid (or projection of point at altitude onto the ellipsoid).

.. py:property:: point_2
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarSurfaceDistanceBetweenPoints.point_2
    :type: IVectorGeometryToolPoint

    Terminating point on the central body ellipsoid (or projection of point at altitude onto the ellipsoid).

.. py:property:: surface_central_body
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarSurfaceDistanceBetweenPoints.surface_central_body
    :type: str

    Central body on which the surface distance between points is to be calculated.

.. py:property:: differencing_time_step
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarSurfaceDistanceBetweenPoints.differencing_time_step
    :type: float

    Time step used in numerical evaluation of scalar calculation time rate of change (derivatives using central differencing).


