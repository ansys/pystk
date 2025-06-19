SpatialAnalysisToolCalculationDistanceToLocation
================================================

.. py:class:: ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationDistanceToLocation

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ISpatialAnalysisToolSpatialCalculation`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   A volume calc distance to location interface.

.. py:currentmodule:: SpatialAnalysisToolCalculationDistanceToLocation

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationDistanceToLocation.distance`
              - The Volume Calc range distance types.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationDistanceToLocation.reference_point`
              - The Volume Calc Range reference point.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationDistanceToLocation.reference_plane`
              - The Volume Calc Range reference plane.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationDistanceToLocation.along_vector`
              - The Volume Calc Range Along Vector.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import (
        SpatialAnalysisToolCalculationDistanceToLocation,
    )


Property detail
---------------

.. py:property:: distance
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationDistanceToLocation.distance
    :type: DistanceToLocationType

    The Volume Calc range distance types.

.. py:property:: reference_point
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationDistanceToLocation.reference_point
    :type: IVectorGeometryToolPoint

    The Volume Calc Range reference point.

.. py:property:: reference_plane
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationDistanceToLocation.reference_plane
    :type: IVectorGeometryToolPlane

    The Volume Calc Range reference plane.

.. py:property:: along_vector
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationDistanceToLocation.along_vector
    :type: IVectorGeometryToolVector

    The Volume Calc Range Along Vector.


