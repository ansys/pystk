SpatialAnalysisToolVolumeGridLatLonAlt
======================================

.. py:class:: ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridLatLonAlt

   Bases: :py:class:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGrid`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   A volume grid lat lon alt (Cartogrographic) interface.

.. py:currentmodule:: SpatialAnalysisToolVolumeGridLatLonAlt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridLatLonAlt.reference_central_body`
              - Get the central body for the volume grid. Both the central body reference shape and its CBF (central body centered fixed) system are used by this volume grid.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridLatLonAlt.latitude_coordinates`
              - Returns latitude Coordinates parameters for the Theta system.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridLatLonAlt.longitude_coordinates`
              - Returns longtitude Coordinates parameters for the Radius system.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridLatLonAlt.altitude_coordinates`
              - Returns altitude parameters for the Height system.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridLatLonAlt.auto_fit_bounds`
              - Specify whether to use the auto fit bounds. Set to true to use the auto fit bounds..



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import SpatialAnalysisToolVolumeGridLatLonAlt


Property detail
---------------

.. py:property:: reference_central_body
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridLatLonAlt.reference_central_body
    :type: str

    Get the central body for the volume grid. Both the central body reference shape and its CBF (central body centered fixed) system are used by this volume grid.

.. py:property:: latitude_coordinates
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridLatLonAlt.latitude_coordinates
    :type: ISpatialAnalysisToolGridCoordinateDefinition

    Returns latitude Coordinates parameters for the Theta system.

.. py:property:: longitude_coordinates
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridLatLonAlt.longitude_coordinates
    :type: ISpatialAnalysisToolGridCoordinateDefinition

    Returns longtitude Coordinates parameters for the Radius system.

.. py:property:: altitude_coordinates
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridLatLonAlt.altitude_coordinates
    :type: ISpatialAnalysisToolGridCoordinateDefinition

    Returns altitude parameters for the Height system.

.. py:property:: auto_fit_bounds
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridLatLonAlt.auto_fit_bounds
    :type: bool

    Specify whether to use the auto fit bounds. Set to true to use the auto fit bounds..


