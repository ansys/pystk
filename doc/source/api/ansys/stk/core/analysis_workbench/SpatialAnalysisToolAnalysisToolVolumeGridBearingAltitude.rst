SpatialAnalysisToolAnalysisToolVolumeGridBearingAltitude
========================================================

.. py:class:: ansys.stk.core.analysis_workbench.SpatialAnalysisToolAnalysisToolVolumeGridBearingAltitude

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ISpatialAnalysisToolVolumeGrid`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   A volume grid bearing alt (Surface Bearing) interface.

.. py:currentmodule:: SpatialAnalysisToolAnalysisToolVolumeGridBearingAltitude

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolAnalysisToolVolumeGridBearingAltitude.reference_central_body`
              - Get the central body for the volume grid. Both the central body reference shape and its CBF (central body centered fixed) system are used by this volume grid.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolAnalysisToolVolumeGridBearingAltitude.along_bearing_grid_parameters`
              - Return AlongBearing Coordinates parameters for the surface bearing.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolAnalysisToolVolumeGridBearingAltitude.cross_bearing_grid_parameters`
              - Return CrossBearing Coordinates parameters for the surface bearing.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolAnalysisToolVolumeGridBearingAltitude.altitude_grid_parameters`
              - Return altitude Coordinates parameters for the surface bearing.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolAnalysisToolVolumeGridBearingAltitude.auto_fit_bounds`
              - Specify whether to use the auto fit bounds. Set to true to use the auto fit bounds..
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolAnalysisToolVolumeGridBearingAltitude.bearing_angle`
              - Specify the Bearing Angle.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolAnalysisToolVolumeGridBearingAltitude.reference_location`
              - Get lat/lon for reference location.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import (
        SpatialAnalysisToolAnalysisToolVolumeGridBearingAltitude,
    )


Property detail
---------------

.. py:property:: reference_central_body
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolAnalysisToolVolumeGridBearingAltitude.reference_central_body
    :type: str

    Get the central body for the volume grid. Both the central body reference shape and its CBF (central body centered fixed) system are used by this volume grid.

.. py:property:: along_bearing_grid_parameters
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolAnalysisToolVolumeGridBearingAltitude.along_bearing_grid_parameters
    :type: SpatialAnalysisToolGridCoordinateDefinition

    Return AlongBearing Coordinates parameters for the surface bearing.

.. py:property:: cross_bearing_grid_parameters
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolAnalysisToolVolumeGridBearingAltitude.cross_bearing_grid_parameters
    :type: SpatialAnalysisToolGridCoordinateDefinition

    Return CrossBearing Coordinates parameters for the surface bearing.

.. py:property:: altitude_grid_parameters
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolAnalysisToolVolumeGridBearingAltitude.altitude_grid_parameters
    :type: SpatialAnalysisToolGridCoordinateDefinition

    Return altitude Coordinates parameters for the surface bearing.

.. py:property:: auto_fit_bounds
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolAnalysisToolVolumeGridBearingAltitude.auto_fit_bounds
    :type: bool

    Specify whether to use the auto fit bounds. Set to true to use the auto fit bounds..

.. py:property:: bearing_angle
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolAnalysisToolVolumeGridBearingAltitude.bearing_angle
    :type: float

    Specify the Bearing Angle.

.. py:property:: reference_location
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolAnalysisToolVolumeGridBearingAltitude.reference_location
    :type: list

    Get lat/lon for reference location.


