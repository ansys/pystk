ISpatialAnalysisToolVolumeGridCartesian
=======================================

.. py:class:: ISpatialAnalysisToolVolumeGridCartesian

   object
   
   A volume grid Cartesian interface.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~reference_system`
            * - :py:meth:`~x_coordinates`
            * - :py:meth:`~y_coordinates`
            * - :py:meth:`~z_coordinates`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ISpatialAnalysisToolVolumeGridCartesian


Property detail
---------------

.. py:property:: reference_system
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridCartesian.reference_system
    :type: IAgCrdnSystem

    Get the reference system in which Cartesian parameters are computed.

.. py:property:: x_coordinates
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridCartesian.x_coordinates
    :type: IAgCrdnGridCoordinateDefinition

    Returns X Coordinates parameters for the Cartesian system.

.. py:property:: y_coordinates
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridCartesian.y_coordinates
    :type: IAgCrdnGridCoordinateDefinition

    Returns Y Coordinates parameters for the Cartesian system.

.. py:property:: z_coordinates
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridCartesian.z_coordinates
    :type: IAgCrdnGridCoordinateDefinition

    Returns Z Coordinates parameters for the Cartesian system.


