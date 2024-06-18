ISpatialAnalysisToolVolumeGridCylindrical
=========================================

.. py:class:: ISpatialAnalysisToolVolumeGridCylindrical

   object
   
   A volume grid cylindrical interface.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~reference_system`
            * - :py:meth:`~theta_coordinates`
            * - :py:meth:`~radius_coordinates`
            * - :py:meth:`~height_coordinates`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ISpatialAnalysisToolVolumeGridCylindrical


Property detail
---------------

.. py:property:: reference_system
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridCylindrical.reference_system
    :type: "IAgCrdnSystem"

    Get the reference system in which cylindrical parameters are computed.

.. py:property:: theta_coordinates
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridCylindrical.theta_coordinates
    :type: "IAgCrdnGridCoordinateDefinition"

    Returns theta Coordinates parameters for the Theta system.

.. py:property:: radius_coordinates
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridCylindrical.radius_coordinates
    :type: "IAgCrdnGridCoordinateDefinition"

    Returns radius Coordinates parameters for the Radius system.

.. py:property:: height_coordinates
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridCylindrical.height_coordinates
    :type: "IAgCrdnGridCoordinateDefinition"

    Returns height Coordinates parameters for the Height system.


