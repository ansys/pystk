ISpatialAnalysisToolVolumeGridCylindrical
=========================================

.. py:class:: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridCylindrical

   object
   
   A volume grid cylindrical interface.

.. py:currentmodule:: ISpatialAnalysisToolVolumeGridCylindrical

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridCylindrical.reference_system`
            * - :py:attr:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridCylindrical.theta_coordinates`
            * - :py:attr:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridCylindrical.radius_coordinates`
            * - :py:attr:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridCylindrical.height_coordinates`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ISpatialAnalysisToolVolumeGridCylindrical


Property detail
---------------

.. py:property:: reference_system
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridCylindrical.reference_system
    :type: IVectorGeometryToolSystem

    Get the reference system in which cylindrical parameters are computed.

.. py:property:: theta_coordinates
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridCylindrical.theta_coordinates
    :type: ISpatialAnalysisToolGridCoordinateDefinition

    Returns theta Coordinates parameters for the Theta system.

.. py:property:: radius_coordinates
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridCylindrical.radius_coordinates
    :type: ISpatialAnalysisToolGridCoordinateDefinition

    Returns radius Coordinates parameters for the Radius system.

.. py:property:: height_coordinates
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridCylindrical.height_coordinates
    :type: ISpatialAnalysisToolGridCoordinateDefinition

    Returns height Coordinates parameters for the Height system.


