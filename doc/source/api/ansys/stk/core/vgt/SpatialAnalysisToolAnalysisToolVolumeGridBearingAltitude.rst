SpatialAnalysisToolAnalysisToolVolumeGridBearingAltitude
========================================================

.. py:class:: ansys.stk.core.vgt.SpatialAnalysisToolAnalysisToolVolumeGridBearingAltitude

   Bases: :py:class:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGrid`, :py:class:`~ansys.stk.core.vgt.IComponent`

   A volume grid bearing alt (Surface Bearing) interface.

.. py:currentmodule:: SpatialAnalysisToolAnalysisToolVolumeGridBearingAltitude

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolAnalysisToolVolumeGridBearingAltitude.reference_central_body`
              - Get the central body for the volume grid. Both the central body reference shape and its CBF (central body centered fixed) system are used by this volume grid.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolAnalysisToolVolumeGridBearingAltitude.along_bearing_grid_parameters`
              - Returns AlongBearing Coordinates parameters for the surface bearing.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolAnalysisToolVolumeGridBearingAltitude.cross_bearing_grid_parameters`
              - Returns CrossBearing Coordinates parameters for the surface bearing.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolAnalysisToolVolumeGridBearingAltitude.altitude_grid_parameters`
              - Returns altitude Coordinates parameters for the surface bearing.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolAnalysisToolVolumeGridBearingAltitude.auto_fit_bounds`
              - Specify whether to use the auto fit bounds. Set to true to use the auto fit bounds..
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolAnalysisToolVolumeGridBearingAltitude.bearing_angle`
              - Specify the Bearing Angle.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolAnalysisToolVolumeGridBearingAltitude.reference_location`
              - Get lat/lon for reference location.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import SpatialAnalysisToolAnalysisToolVolumeGridBearingAltitude


Property detail
---------------

.. py:property:: reference_central_body
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolAnalysisToolVolumeGridBearingAltitude.reference_central_body
    :type: str

    Get the central body for the volume grid. Both the central body reference shape and its CBF (central body centered fixed) system are used by this volume grid.

.. py:property:: along_bearing_grid_parameters
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolAnalysisToolVolumeGridBearingAltitude.along_bearing_grid_parameters
    :type: SpatialAnalysisToolGridCoordinateDefinition

    Returns AlongBearing Coordinates parameters for the surface bearing.

.. py:property:: cross_bearing_grid_parameters
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolAnalysisToolVolumeGridBearingAltitude.cross_bearing_grid_parameters
    :type: SpatialAnalysisToolGridCoordinateDefinition

    Returns CrossBearing Coordinates parameters for the surface bearing.

.. py:property:: altitude_grid_parameters
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolAnalysisToolVolumeGridBearingAltitude.altitude_grid_parameters
    :type: SpatialAnalysisToolGridCoordinateDefinition

    Returns altitude Coordinates parameters for the surface bearing.

.. py:property:: auto_fit_bounds
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolAnalysisToolVolumeGridBearingAltitude.auto_fit_bounds
    :type: bool

    Specify whether to use the auto fit bounds. Set to true to use the auto fit bounds..

.. py:property:: bearing_angle
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolAnalysisToolVolumeGridBearingAltitude.bearing_angle
    :type: float

    Specify the Bearing Angle.

.. py:property:: reference_location
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolAnalysisToolVolumeGridBearingAltitude.reference_location
    :type: list

    Get lat/lon for reference location.


