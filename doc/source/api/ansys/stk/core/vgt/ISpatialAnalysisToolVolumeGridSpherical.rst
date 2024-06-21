ISpatialAnalysisToolVolumeGridSpherical
=======================================

.. py:class:: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridSpherical

   object
   
   A volume grid spherical interface.

.. py:currentmodule:: ISpatialAnalysisToolVolumeGridSpherical

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridSpherical.reference_system`
            * - :py:attr:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridSpherical.azimuth_coordinates`
            * - :py:attr:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridSpherical.elevation_coordinates`
            * - :py:attr:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridSpherical.range_coordinates`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ISpatialAnalysisToolVolumeGridSpherical


Property detail
---------------

.. py:property:: reference_system
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridSpherical.reference_system
    :type: IVectorGeometryToolSystem

    Get the reference system in which spherical parameters are computed.

.. py:property:: azimuth_coordinates
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridSpherical.azimuth_coordinates
    :type: ISpatialAnalysisToolGridCoordinateDefinition

    Returns azimuth coordinates parameters for the spherical volume grid.

.. py:property:: elevation_coordinates
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridSpherical.elevation_coordinates
    :type: ISpatialAnalysisToolGridCoordinateDefinition

    Returns elevation coordinates parameters for the spherical volume grid.

.. py:property:: range_coordinates
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridSpherical.range_coordinates
    :type: ISpatialAnalysisToolGridCoordinateDefinition

    Returns range coordinates parameters for the spherical volume grid.


