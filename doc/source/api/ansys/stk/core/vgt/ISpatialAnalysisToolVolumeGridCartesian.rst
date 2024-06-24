ISpatialAnalysisToolVolumeGridCartesian
=======================================

.. py:class:: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridCartesian

   object
   
   A volume grid Cartesian interface.

.. py:currentmodule:: ISpatialAnalysisToolVolumeGridCartesian

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridCartesian.reference_system`
            * - :py:attr:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridCartesian.x_coordinates`
            * - :py:attr:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridCartesian.y_coordinates`
            * - :py:attr:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridCartesian.z_coordinates`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ISpatialAnalysisToolVolumeGridCartesian


Property detail
---------------

.. py:property:: reference_system
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridCartesian.reference_system
    :type: IVectorGeometryToolSystem

    Get the reference system in which Cartesian parameters are computed.

.. py:property:: x_coordinates
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridCartesian.x_coordinates
    :type: ISpatialAnalysisToolGridCoordinateDefinition

    Returns X Coordinates parameters for the Cartesian system.

.. py:property:: y_coordinates
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridCartesian.y_coordinates
    :type: ISpatialAnalysisToolGridCoordinateDefinition

    Returns Y Coordinates parameters for the Cartesian system.

.. py:property:: z_coordinates
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridCartesian.z_coordinates
    :type: ISpatialAnalysisToolGridCoordinateDefinition

    Returns Z Coordinates parameters for the Cartesian system.


