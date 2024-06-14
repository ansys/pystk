ISpatialAnalysisToolVolumeGridBearingAlt
========================================

.. py:class:: ISpatialAnalysisToolVolumeGridBearingAlt

   object
   
   A volume grid bearing alt (Surface Bearing) interface.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~reference_central_body`
            * - :py:meth:`~along_bearing_coordinates`
            * - :py:meth:`~cross_bearing_coordinates`
            * - :py:meth:`~altitude_coordinates`
            * - :py:meth:`~auto_fit_bounds`
            * - :py:meth:`~bearing_angle`
            * - :py:meth:`~reference_location`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ISpatialAnalysisToolVolumeGridBearingAlt


Property detail
---------------

.. py:property:: reference_central_body
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridBearingAlt.reference_central_body
    :type: str

    Get the central body for the volume grid. Both the central body reference shape and its CBF (central body centered fixed) system are used by this volume grid.

.. py:property:: along_bearing_coordinates
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridBearingAlt.along_bearing_coordinates
    :type: "IAgCrdnGridCoordinateDefinition"

    Returns AlongBearing Coordinates parameters for the surface bearing.

.. py:property:: cross_bearing_coordinates
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridBearingAlt.cross_bearing_coordinates
    :type: "IAgCrdnGridCoordinateDefinition"

    Returns CrossBearing Coordinates parameters for the surface bearing.

.. py:property:: altitude_coordinates
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridBearingAlt.altitude_coordinates
    :type: "IAgCrdnGridCoordinateDefinition"

    Returns altitude Coordinates parameters for the surface bearing.

.. py:property:: auto_fit_bounds
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridBearingAlt.auto_fit_bounds
    :type: bool

    Specify whether to use the auto fit bounds. Set to true to use the auto fit bounds..

.. py:property:: bearing_angle
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridBearingAlt.bearing_angle
    :type: float

    Specify the Bearing Angle.

.. py:property:: reference_location
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridBearingAlt.reference_location
    :type: list

    Get lat/lon for reference location.


