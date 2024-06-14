ISpatialAnalysisToolVolumeGridLatLonAlt
=======================================

.. py:class:: ISpatialAnalysisToolVolumeGridLatLonAlt

   object
   
   A volume grid lat lon alt (Cartogrographic) interface.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~reference_central_body`
            * - :py:meth:`~latitude_coordinates`
            * - :py:meth:`~longitude_coordinates`
            * - :py:meth:`~altitude_coordinates`
            * - :py:meth:`~auto_fit_bounds`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ISpatialAnalysisToolVolumeGridLatLonAlt


Property detail
---------------

.. py:property:: reference_central_body
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridLatLonAlt.reference_central_body
    :type: str

    Get the central body for the volume grid. Both the central body reference shape and its CBF (central body centered fixed) system are used by this volume grid.

.. py:property:: latitude_coordinates
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridLatLonAlt.latitude_coordinates
    :type: "IAgCrdnGridCoordinateDefinition"

    Returns latitude Coordinates parameters for the Theta system.

.. py:property:: longitude_coordinates
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridLatLonAlt.longitude_coordinates
    :type: "IAgCrdnGridCoordinateDefinition"

    Returns longtitude Coordinates parameters for the Radius system.

.. py:property:: altitude_coordinates
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridLatLonAlt.altitude_coordinates
    :type: "IAgCrdnGridCoordinateDefinition"

    Returns altitude parameters for the Height system.

.. py:property:: auto_fit_bounds
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridLatLonAlt.auto_fit_bounds
    :type: bool

    Specify whether to use the auto fit bounds. Set to true to use the auto fit bounds..


