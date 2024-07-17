SpatialAnalysisToolVolumeGridSpherical
======================================

.. py:class:: ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridSpherical

   Bases: :py:class:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGrid`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   A volume grid spherical interface.

.. py:currentmodule:: SpatialAnalysisToolVolumeGridSpherical

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridSpherical.reference_system`
              - Get the reference system in which spherical parameters are computed.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridSpherical.azimuth_coordinates`
              - Returns azimuth coordinates parameters for the spherical volume grid.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridSpherical.elevation_coordinates`
              - Returns elevation coordinates parameters for the spherical volume grid.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridSpherical.range_coordinates`
              - Returns range coordinates parameters for the spherical volume grid.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import SpatialAnalysisToolVolumeGridSpherical


Property detail
---------------

.. py:property:: reference_system
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridSpherical.reference_system
    :type: IVectorGeometryToolSystem

    Get the reference system in which spherical parameters are computed.

.. py:property:: azimuth_coordinates
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridSpherical.azimuth_coordinates
    :type: ISpatialAnalysisToolGridCoordinateDefinition

    Returns azimuth coordinates parameters for the spherical volume grid.

.. py:property:: elevation_coordinates
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridSpherical.elevation_coordinates
    :type: ISpatialAnalysisToolGridCoordinateDefinition

    Returns elevation coordinates parameters for the spherical volume grid.

.. py:property:: range_coordinates
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridSpherical.range_coordinates
    :type: ISpatialAnalysisToolGridCoordinateDefinition

    Returns range coordinates parameters for the spherical volume grid.


