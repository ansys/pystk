SpatialAnalysisToolVolumeGridCylindrical
========================================

.. py:class:: ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridCylindrical

   Bases: :py:class:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGrid`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   A volume grid cylindrical interface.

.. py:currentmodule:: SpatialAnalysisToolVolumeGridCylindrical

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridCylindrical.reference_system`
              - Get the reference system in which cylindrical parameters are computed.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridCylindrical.theta_coordinates`
              - Returns theta Coordinates parameters for the Theta system.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridCylindrical.radius_coordinates`
              - Returns radius Coordinates parameters for the Radius system.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridCylindrical.height_coordinates`
              - Returns height Coordinates parameters for the Height system.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import SpatialAnalysisToolVolumeGridCylindrical


Property detail
---------------

.. py:property:: reference_system
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridCylindrical.reference_system
    :type: IVectorGeometryToolSystem

    Get the reference system in which cylindrical parameters are computed.

.. py:property:: theta_coordinates
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridCylindrical.theta_coordinates
    :type: SpatialAnalysisToolGridCoordinateDefinition

    Returns theta Coordinates parameters for the Theta system.

.. py:property:: radius_coordinates
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridCylindrical.radius_coordinates
    :type: SpatialAnalysisToolGridCoordinateDefinition

    Returns radius Coordinates parameters for the Radius system.

.. py:property:: height_coordinates
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridCylindrical.height_coordinates
    :type: SpatialAnalysisToolGridCoordinateDefinition

    Returns height Coordinates parameters for the Height system.


