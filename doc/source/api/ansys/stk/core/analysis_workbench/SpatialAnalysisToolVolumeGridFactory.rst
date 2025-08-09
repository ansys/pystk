SpatialAnalysisToolVolumeGridFactory
====================================

.. py:class:: ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridFactory

   The factory is used to create instances of volume grids.

.. py:currentmodule:: SpatialAnalysisToolVolumeGridFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridFactory.create`
              - Create and registers a volume grid using specified name and description.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridFactory.create_bearing_altitude`
              - Create and registers a volume grid of type surface bearing using specified name and description.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridFactory.create_cartesian`
              - Create and registers a cartesian volume grid type using specified name and description.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridFactory.create_constrained`
              - Create and registers a volume grid of type that can be constrained by conditions using specified name and description.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridFactory.create_cylindrical`
              - Create and registers a cylindrical volume grid type using specified name and description.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridFactory.create_latitude_longitude_altitude`
              - Create and registers cartographic volume grid type using specified name and description.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridFactory.create_spherical`
              - Create and registers a spherical volume grid type using specified name and description.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridFactory.is_type_supported`
              - Return whether the specified type is supported.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import SpatialAnalysisToolVolumeGridFactory



Method detail
-------------

.. py:method:: create(self, name: str, description: str, type: VolumeGridType) -> ISpatialAnalysisToolVolumeGrid
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridFactory.create

    Create and registers a volume grid using specified name and description.

    :Parameters:

        **name** : :obj:`~str`

        **description** : :obj:`~str`

        **type** : :obj:`~VolumeGridType`


    :Returns:

        :obj:`~ISpatialAnalysisToolVolumeGrid`

.. py:method:: create_bearing_altitude(self, name: str, description: str) -> ISpatialAnalysisToolVolumeGrid
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridFactory.create_bearing_altitude

    Create and registers a volume grid of type surface bearing using specified name and description.

    :Parameters:

        **name** : :obj:`~str`

        **description** : :obj:`~str`


    :Returns:

        :obj:`~ISpatialAnalysisToolVolumeGrid`

.. py:method:: create_cartesian(self, name: str, description: str) -> ISpatialAnalysisToolVolumeGrid
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridFactory.create_cartesian

    Create and registers a cartesian volume grid type using specified name and description.

    :Parameters:

        **name** : :obj:`~str`

        **description** : :obj:`~str`


    :Returns:

        :obj:`~ISpatialAnalysisToolVolumeGrid`

.. py:method:: create_constrained(self, name: str, description: str) -> ISpatialAnalysisToolVolumeGrid
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridFactory.create_constrained

    Create and registers a volume grid of type that can be constrained by conditions using specified name and description.

    :Parameters:

        **name** : :obj:`~str`

        **description** : :obj:`~str`


    :Returns:

        :obj:`~ISpatialAnalysisToolVolumeGrid`

.. py:method:: create_cylindrical(self, name: str, description: str) -> ISpatialAnalysisToolVolumeGrid
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridFactory.create_cylindrical

    Create and registers a cylindrical volume grid type using specified name and description.

    :Parameters:

        **name** : :obj:`~str`

        **description** : :obj:`~str`


    :Returns:

        :obj:`~ISpatialAnalysisToolVolumeGrid`

.. py:method:: create_latitude_longitude_altitude(self, name: str, description: str) -> ISpatialAnalysisToolVolumeGrid
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridFactory.create_latitude_longitude_altitude

    Create and registers cartographic volume grid type using specified name and description.

    :Parameters:

        **name** : :obj:`~str`

        **description** : :obj:`~str`


    :Returns:

        :obj:`~ISpatialAnalysisToolVolumeGrid`

.. py:method:: create_spherical(self, name: str, description: str) -> ISpatialAnalysisToolVolumeGrid
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridFactory.create_spherical

    Create and registers a spherical volume grid type using specified name and description.

    :Parameters:

        **name** : :obj:`~str`

        **description** : :obj:`~str`


    :Returns:

        :obj:`~ISpatialAnalysisToolVolumeGrid`

.. py:method:: is_type_supported(self, type: VolumeGridType) -> bool
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolVolumeGridFactory.is_type_supported

    Return whether the specified type is supported.

    :Parameters:

        **type** : :obj:`~VolumeGridType`


    :Returns:

        :obj:`~bool`

