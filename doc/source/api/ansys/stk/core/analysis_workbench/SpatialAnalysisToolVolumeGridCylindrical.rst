SpatialAnalysisToolVolumeGridCylindrical
========================================

.. py:class:: ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridCylindrical

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ISpatialAnalysisToolVolumeGrid`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   A volume grid cylindrical interface.

.. py:currentmodule:: SpatialAnalysisToolVolumeGridCylindrical

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridCylindrical.height_coordinates`
              - Return height Coordinates parameters for the Height system.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridCylindrical.radius_coordinates`
              - Return radius Coordinates parameters for the Radius system.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridCylindrical.reference_system`
              - Get the reference system in which cylindrical parameters are computed.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridCylindrical.theta_coordinates`
              - Return theta Coordinates parameters for the Theta system.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import SpatialAnalysisToolVolumeGridCylindrical


Property detail
---------------

.. py:property:: height_coordinates
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridCylindrical.height_coordinates
    :type: SpatialAnalysisToolGridCoordinateDefinition

    Return height Coordinates parameters for the Height system.

.. py:property:: radius_coordinates
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridCylindrical.radius_coordinates
    :type: SpatialAnalysisToolGridCoordinateDefinition

    Return radius Coordinates parameters for the Radius system.

.. py:property:: reference_system
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridCylindrical.reference_system
    :type: IVectorGeometryToolSystem

    Get the reference system in which cylindrical parameters are computed.

.. py:property:: theta_coordinates
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridCylindrical.theta_coordinates
    :type: SpatialAnalysisToolGridCoordinateDefinition

    Return theta Coordinates parameters for the Theta system.


