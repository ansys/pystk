SpatialAnalysisToolVolumeGridCartesian
======================================

.. py:class:: ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridCartesian

   Bases: :py:class:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGrid`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   A volume grid Cartesian interface.

.. py:currentmodule:: SpatialAnalysisToolVolumeGridCartesian

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridCartesian.reference_system`
              - Get the reference system in which Cartesian parameters are computed.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridCartesian.x_grid_parameters`
              - Returns X Coordinates parameters for the Cartesian system.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridCartesian.y_grid_parameters`
              - Returns Y Coordinates parameters for the Cartesian system.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridCartesian.z_grid_parameters`
              - Returns Z Coordinates parameters for the Cartesian system.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import SpatialAnalysisToolVolumeGridCartesian


Property detail
---------------

.. py:property:: reference_system
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridCartesian.reference_system
    :type: IVectorGeometryToolSystem

    Get the reference system in which Cartesian parameters are computed.

.. py:property:: x_grid_parameters
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridCartesian.x_grid_parameters
    :type: SpatialAnalysisToolGridCoordinateDefinition

    Returns X Coordinates parameters for the Cartesian system.

.. py:property:: y_grid_parameters
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridCartesian.y_grid_parameters
    :type: SpatialAnalysisToolGridCoordinateDefinition

    Returns Y Coordinates parameters for the Cartesian system.

.. py:property:: z_grid_parameters
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeGridCartesian.z_grid_parameters
    :type: SpatialAnalysisToolGridCoordinateDefinition

    Returns Z Coordinates parameters for the Cartesian system.


