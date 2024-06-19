ISpatialAnalysisToolVolumeGridFactory
=====================================

.. py:class:: ISpatialAnalysisToolVolumeGridFactory

   object
   
   The factory is used to create instances of volume grids.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~create`
              - Create and registers a volume grid using specified name and description.
            * - :py:meth:`~create_volume_grid_cartesian`
              - Create and registers a cartesian volume grid type using specified name and description.
            * - :py:meth:`~is_type_supported`
              - Return whether the specified type is supported.
            * - :py:meth:`~create_volume_grid_cylindrical`
              - Create and registers a cylindrical volume grid type using specified name and description.
            * - :py:meth:`~create_volume_grid_spherical`
              - Create and registers a spherical volume grid type using specified name and description.
            * - :py:meth:`~create_volume_grid_constrained`
              - Create and registers a volume grid of type that can be constrained by conditions using specified name and description.
            * - :py:meth:`~create_volume_grid_lat_lon_altitude`
              - Create and registers cartographic volume grid type using specified name and description.
            * - :py:meth:`~create_volume_grid_bearing_altitude`
              - Create and registers a volume grid of type surface bearing using specified name and description.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ISpatialAnalysisToolVolumeGridFactory



Method detail
-------------

.. py:method:: create(self, name: str, description: str, type: CRDN_VOLUME_GRID_TYPE) -> ISpatialAnalysisToolVolumeGrid
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridFactory.create

    Create and registers a volume grid using specified name and description.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`
    **type** : :obj:`~CRDN_VOLUME_GRID_TYPE`

    :Returns:

        :obj:`~ISpatialAnalysisToolVolumeGrid`

.. py:method:: create_volume_grid_cartesian(self, name: str, description: str) -> ISpatialAnalysisToolVolumeGrid
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridFactory.create_volume_grid_cartesian

    Create and registers a cartesian volume grid type using specified name and description.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ISpatialAnalysisToolVolumeGrid`

.. py:method:: is_type_supported(self, eType: CRDN_VOLUME_GRID_TYPE) -> bool
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridFactory.is_type_supported

    Return whether the specified type is supported.

    :Parameters:

    **eType** : :obj:`~CRDN_VOLUME_GRID_TYPE`

    :Returns:

        :obj:`~bool`

.. py:method:: create_volume_grid_cylindrical(self, name: str, description: str) -> ISpatialAnalysisToolVolumeGrid
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridFactory.create_volume_grid_cylindrical

    Create and registers a cylindrical volume grid type using specified name and description.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ISpatialAnalysisToolVolumeGrid`

.. py:method:: create_volume_grid_spherical(self, name: str, description: str) -> ISpatialAnalysisToolVolumeGrid
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridFactory.create_volume_grid_spherical

    Create and registers a spherical volume grid type using specified name and description.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ISpatialAnalysisToolVolumeGrid`

.. py:method:: create_volume_grid_constrained(self, name: str, description: str) -> ISpatialAnalysisToolVolumeGrid
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridFactory.create_volume_grid_constrained

    Create and registers a volume grid of type that can be constrained by conditions using specified name and description.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ISpatialAnalysisToolVolumeGrid`

.. py:method:: create_volume_grid_lat_lon_altitude(self, name: str, description: str) -> ISpatialAnalysisToolVolumeGrid
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridFactory.create_volume_grid_lat_lon_altitude

    Create and registers cartographic volume grid type using specified name and description.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ISpatialAnalysisToolVolumeGrid`

.. py:method:: create_volume_grid_bearing_altitude(self, name: str, description: str) -> ISpatialAnalysisToolVolumeGrid
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGridFactory.create_volume_grid_bearing_altitude

    Create and registers a volume grid of type surface bearing using specified name and description.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ISpatialAnalysisToolVolumeGrid`

