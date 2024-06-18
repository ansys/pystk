ISpatialAnalysisToolVolumeGridSpherical
=======================================

.. py:class:: ISpatialAnalysisToolVolumeGridSpherical

   object
   
   A volume grid spherical interface.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~reference_system`
            * - :py:meth:`~azimuth_coordinates`
            * - :py:meth:`~elevation_coordinates`
            * - :py:meth:`~range_coordinates`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ISpatialAnalysisToolVolumeGridSpherical


Property detail
---------------

.. py:property:: reference_system
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridSpherical.reference_system
    :type: "IAgCrdnSystem"

    Get the reference system in which spherical parameters are computed.

.. py:property:: azimuth_coordinates
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridSpherical.azimuth_coordinates
    :type: "IAgCrdnGridCoordinateDefinition"

    Returns azimuth coordinates parameters for the spherical volume grid.

.. py:property:: elevation_coordinates
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridSpherical.elevation_coordinates
    :type: "IAgCrdnGridCoordinateDefinition"

    Returns elevation coordinates parameters for the spherical volume grid.

.. py:property:: range_coordinates
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridSpherical.range_coordinates
    :type: "IAgCrdnGridCoordinateDefinition"

    Returns range coordinates parameters for the spherical volume grid.


