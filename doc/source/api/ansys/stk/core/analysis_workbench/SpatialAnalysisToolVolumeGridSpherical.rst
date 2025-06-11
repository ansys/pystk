SpatialAnalysisToolVolumeGridSpherical
======================================

.. py:class:: ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridSpherical

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ISpatialAnalysisToolVolumeGrid`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   A volume grid spherical interface.

.. py:currentmodule:: SpatialAnalysisToolVolumeGridSpherical

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridSpherical.reference_system`
              - Get the reference system in which spherical parameters are computed.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridSpherical.azimuth_grid_parameters`
              - Return azimuth coordinates parameters for the spherical volume grid.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridSpherical.elevation_grid_parameters`
              - Return elevation coordinates parameters for the spherical volume grid.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridSpherical.range_coordinates`
              - Return range coordinates parameters for the spherical volume grid.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import SpatialAnalysisToolVolumeGridSpherical


Property detail
---------------

.. py:property:: reference_system
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridSpherical.reference_system
    :type: IVectorGeometryToolSystem

    Get the reference system in which spherical parameters are computed.

.. py:property:: azimuth_grid_parameters
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridSpherical.azimuth_grid_parameters
    :type: SpatialAnalysisToolGridCoordinateDefinition

    Return azimuth coordinates parameters for the spherical volume grid.

.. py:property:: elevation_grid_parameters
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridSpherical.elevation_grid_parameters
    :type: SpatialAnalysisToolGridCoordinateDefinition

    Return elevation coordinates parameters for the spherical volume grid.

.. py:property:: range_coordinates
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridSpherical.range_coordinates
    :type: SpatialAnalysisToolGridCoordinateDefinition

    Return range coordinates parameters for the spherical volume grid.


