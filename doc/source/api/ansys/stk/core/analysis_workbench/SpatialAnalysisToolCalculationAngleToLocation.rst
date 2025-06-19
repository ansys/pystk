SpatialAnalysisToolCalculationAngleToLocation
=============================================

.. py:class:: ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationAngleToLocation

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ISpatialAnalysisToolSpatialCalculation`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   A volume calc angle off vector interface.

.. py:currentmodule:: SpatialAnalysisToolCalculationAngleToLocation

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationAngleToLocation.angle`
              - The Volume Calc Angle Off Vector Type.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationAngleToLocation.reference_plane`
              - The Volume Calc Angle Off Vector reference plane.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationAngleToLocation.reference_point`
              - The Volume Calc Angle Off Vector reference point.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationAngleToLocation.reference_vector`
              - The Volume Calc Angle Off Vector reference vector.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationAngleToLocation.about_vector`
              - The Volume Calc Angle Off Vector reference about vector.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import (
        SpatialAnalysisToolCalculationAngleToLocation,
    )


Property detail
---------------

.. py:property:: angle
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationAngleToLocation.angle
    :type: AngleToLocationType

    The Volume Calc Angle Off Vector Type.

.. py:property:: reference_plane
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationAngleToLocation.reference_plane
    :type: IVectorGeometryToolPlane

    The Volume Calc Angle Off Vector reference plane.

.. py:property:: reference_point
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationAngleToLocation.reference_point
    :type: IVectorGeometryToolPoint

    The Volume Calc Angle Off Vector reference point.

.. py:property:: reference_vector
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationAngleToLocation.reference_vector
    :type: IVectorGeometryToolVector

    The Volume Calc Angle Off Vector reference vector.

.. py:property:: about_vector
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationAngleToLocation.about_vector
    :type: IVectorGeometryToolVector

    The Volume Calc Angle Off Vector reference about vector.


