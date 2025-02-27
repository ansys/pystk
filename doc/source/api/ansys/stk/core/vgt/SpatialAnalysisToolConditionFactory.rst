SpatialAnalysisToolConditionFactory
===================================

.. py:class:: ansys.stk.core.vgt.SpatialAnalysisToolConditionFactory

   The factory is used to create instances of volumes.

.. py:currentmodule:: SpatialAnalysisToolConditionFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolConditionFactory.create`
              - Create and registers a volume using specified name and description.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolConditionFactory.is_type_supported`
              - Return whether the specified type is supported.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolConditionFactory.create_combined`
              - Create a volume type combined.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolConditionFactory.create_lighting`
              - Create a volume type lighting.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolConditionFactory.create_volume_over_time`
              - Create a volume type over time.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolConditionFactory.create_from_grid`
              - Create a volume type from grid.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolConditionFactory.create_from_spatial_calculation`
              - Create a volume type from calc.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolConditionFactory.create_from_time_satisfaction`
              - Create a volume type from time satisfaction.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolConditionFactory.create_from_condition`
              - Create a volume type condition.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolConditionFactory.create_from_access`
              - Create a volume type Inview.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import SpatialAnalysisToolConditionFactory



Method detail
-------------

.. py:method:: create(self, name: str, description: str, type: VolumeType) -> ISpatialAnalysisToolVolume
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolConditionFactory.create

    Create and registers a volume using specified name and description.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`
    **type** : :obj:`~VolumeType`

    :Returns:

        :obj:`~ISpatialAnalysisToolVolume`

.. py:method:: is_type_supported(self, type: VolumeType) -> bool
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolConditionFactory.is_type_supported

    Return whether the specified type is supported.

    :Parameters:

    **type** : :obj:`~VolumeType`

    :Returns:

        :obj:`~bool`

.. py:method:: create_combined(self, name: str, description: str) -> ISpatialAnalysisToolVolume
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolConditionFactory.create_combined

    Create a volume type combined.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ISpatialAnalysisToolVolume`

.. py:method:: create_lighting(self, name: str, description: str) -> ISpatialAnalysisToolVolume
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolConditionFactory.create_lighting

    Create a volume type lighting.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ISpatialAnalysisToolVolume`

.. py:method:: create_volume_over_time(self, name: str, description: str) -> ISpatialAnalysisToolVolume
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolConditionFactory.create_volume_over_time

    Create a volume type over time.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ISpatialAnalysisToolVolume`

.. py:method:: create_from_grid(self, name: str, description: str) -> ISpatialAnalysisToolVolume
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolConditionFactory.create_from_grid

    Create a volume type from grid.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ISpatialAnalysisToolVolume`

.. py:method:: create_from_spatial_calculation(self, name: str, description: str) -> ISpatialAnalysisToolVolume
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolConditionFactory.create_from_spatial_calculation

    Create a volume type from calc.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ISpatialAnalysisToolVolume`

.. py:method:: create_from_time_satisfaction(self, name: str, description: str) -> ISpatialAnalysisToolVolume
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolConditionFactory.create_from_time_satisfaction

    Create a volume type from time satisfaction.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ISpatialAnalysisToolVolume`

.. py:method:: create_from_condition(self, name: str, description: str) -> ISpatialAnalysisToolVolume
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolConditionFactory.create_from_condition

    Create a volume type condition.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ISpatialAnalysisToolVolume`

.. py:method:: create_from_access(self, name: str, description: str) -> ISpatialAnalysisToolVolume
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolConditionFactory.create_from_access

    Create a volume type Inview.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ISpatialAnalysisToolVolume`

