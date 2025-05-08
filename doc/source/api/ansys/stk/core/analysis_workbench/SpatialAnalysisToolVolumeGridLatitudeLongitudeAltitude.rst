SpatialAnalysisToolVolumeGridLatitudeLongitudeAltitude
======================================================

.. py:class:: ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridLatitudeLongitudeAltitude

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ISpatialAnalysisToolVolumeGrid`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   A volume grid lat lon alt (Cartogrographic) interface.

.. py:currentmodule:: SpatialAnalysisToolVolumeGridLatitudeLongitudeAltitude

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridLatitudeLongitudeAltitude.reference_central_body`
              - Get the central body for the volume grid. Both the central body reference shape and its CBF (central body centered fixed) system are used by this volume grid.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridLatitudeLongitudeAltitude.latitude_coordinates`
              - Return latitude Coordinates parameters for the Theta system.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridLatitudeLongitudeAltitude.longitude_coordinates`
              - Return longtitude Coordinates parameters for the Radius system.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridLatitudeLongitudeAltitude.altitude_grid_parameters`
              - Return altitude parameters for the Height system.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridLatitudeLongitudeAltitude.auto_fit_bounds`
              - Specify whether to use the auto fit bounds. Set to true to use the auto fit bounds..



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import SpatialAnalysisToolVolumeGridLatitudeLongitudeAltitude


Property detail
---------------

.. py:property:: reference_central_body
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridLatitudeLongitudeAltitude.reference_central_body
    :type: str

    Get the central body for the volume grid. Both the central body reference shape and its CBF (central body centered fixed) system are used by this volume grid.

.. py:property:: latitude_coordinates
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridLatitudeLongitudeAltitude.latitude_coordinates
    :type: SpatialAnalysisToolGridCoordinateDefinition

    Return latitude Coordinates parameters for the Theta system.

.. py:property:: longitude_coordinates
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridLatitudeLongitudeAltitude.longitude_coordinates
    :type: SpatialAnalysisToolGridCoordinateDefinition

    Return longtitude Coordinates parameters for the Radius system.

.. py:property:: altitude_grid_parameters
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridLatitudeLongitudeAltitude.altitude_grid_parameters
    :type: SpatialAnalysisToolGridCoordinateDefinition

    Return altitude parameters for the Height system.

.. py:property:: auto_fit_bounds
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridLatitudeLongitudeAltitude.auto_fit_bounds
    :type: bool

    Specify whether to use the auto fit bounds. Set to true to use the auto fit bounds..


