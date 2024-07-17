SpatialAnalysisToolVolumeGridBearingAlt
=======================================

.. py:class:: ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridBearingAlt

   Bases: :py:class:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGrid`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   A volume grid bearing alt (Surface Bearing) interface.

.. py:currentmodule:: SpatialAnalysisToolVolumeGridBearingAlt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridBearingAlt.reference_central_body`
              - Get the central body for the volume grid. Both the central body reference shape and its CBF (central body centered fixed) system are used by this volume grid.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridBearingAlt.along_bearing_coordinates`
              - Returns AlongBearing Coordinates parameters for the surface bearing.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridBearingAlt.cross_bearing_coordinates`
              - Returns CrossBearing Coordinates parameters for the surface bearing.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridBearingAlt.altitude_coordinates`
              - Returns altitude Coordinates parameters for the surface bearing.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridBearingAlt.auto_fit_bounds`
              - Specify whether to use the auto fit bounds. Set to true to use the auto fit bounds..
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridBearingAlt.bearing_angle`
              - Specify the Bearing Angle.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridBearingAlt.reference_location`
              - Get lat/lon for reference location.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import SpatialAnalysisToolVolumeGridBearingAlt


Property detail
---------------

.. py:property:: reference_central_body
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridBearingAlt.reference_central_body
    :type: str

    Get the central body for the volume grid. Both the central body reference shape and its CBF (central body centered fixed) system are used by this volume grid.

.. py:property:: along_bearing_coordinates
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridBearingAlt.along_bearing_coordinates
    :type: ISpatialAnalysisToolGridCoordinateDefinition

    Returns AlongBearing Coordinates parameters for the surface bearing.

.. py:property:: cross_bearing_coordinates
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridBearingAlt.cross_bearing_coordinates
    :type: ISpatialAnalysisToolGridCoordinateDefinition

    Returns CrossBearing Coordinates parameters for the surface bearing.

.. py:property:: altitude_coordinates
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridBearingAlt.altitude_coordinates
    :type: ISpatialAnalysisToolGridCoordinateDefinition

    Returns altitude Coordinates parameters for the surface bearing.

.. py:property:: auto_fit_bounds
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridBearingAlt.auto_fit_bounds
    :type: bool

    Specify whether to use the auto fit bounds. Set to true to use the auto fit bounds..

.. py:property:: bearing_angle
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridBearingAlt.bearing_angle
    :type: float

    Specify the Bearing Angle.

.. py:property:: reference_location
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridBearingAlt.reference_location
    :type: list

    Get lat/lon for reference location.


