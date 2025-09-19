SpatialAnalysisToolVolumeGridCartesian
======================================

.. py:class:: ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridCartesian

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ISpatialAnalysisToolVolumeGrid`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   A volume grid Cartesian interface.

.. py:currentmodule:: SpatialAnalysisToolVolumeGridCartesian

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridCartesian.reference_system`
              - Get the reference system in which Cartesian parameters are computed.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridCartesian.x_grid_parameters`
              - Return X Coordinates parameters for the Cartesian system.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridCartesian.y_grid_parameters`
              - Return Y Coordinates parameters for the Cartesian system.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridCartesian.z_grid_parameters`
              - Return Z Coordinates parameters for the Cartesian system.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import SpatialAnalysisToolVolumeGridCartesian


Property detail
---------------

.. py:property:: reference_system
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridCartesian.reference_system
    :type: IVectorGeometryToolSystem

    Get the reference system in which Cartesian parameters are computed.

.. py:property:: x_grid_parameters
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridCartesian.x_grid_parameters
    :type: SpatialAnalysisToolGridCoordinateDefinition

    Return X Coordinates parameters for the Cartesian system.

.. py:property:: y_grid_parameters
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridCartesian.y_grid_parameters
    :type: SpatialAnalysisToolGridCoordinateDefinition

    Return Y Coordinates parameters for the Cartesian system.

.. py:property:: z_grid_parameters
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridCartesian.z_grid_parameters
    :type: SpatialAnalysisToolGridCoordinateDefinition

    Return Z Coordinates parameters for the Cartesian system.


