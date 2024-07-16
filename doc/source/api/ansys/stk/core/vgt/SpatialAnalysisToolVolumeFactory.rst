SpatialAnalysisToolVolumeFactory
================================

.. py:class:: ansys.stk.core.vgt.SpatialAnalysisToolVolumeFactory

   Bases: 

   The factory is used to create instances of volumes.

.. py:currentmodule:: SpatialAnalysisToolVolumeFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeFactory.create`
              - Create and registers a volume using specified name and description.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeFactory.is_type_supported`
              - Return whether the specified type is supported.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeFactory.create_volume_combined`
              - Create a volume type combined.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeFactory.create_volume_lighting`
              - Create a volume type lighting.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeFactory.create_volume_over_time`
              - Create a volume type over time.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeFactory.create_volume_from_grid`
              - Create a volume type from grid.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeFactory.create_volume_from_calc`
              - Create a volume type from calc.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeFactory.create_volume_from_time_satisfaction`
              - Create a volume type from time satisfaction.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeFactory.create_volume_from_condition`
              - Create a volume type condition.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeFactory.create_volume_inview`
              - Create a volume type Inview.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import SpatialAnalysisToolVolumeFactory



Method detail
-------------

.. py:method:: create(self, name: str, description: str, type: CRDN_VOLUME_TYPE) -> ISpatialAnalysisToolVolume
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeFactory.create

    Create and registers a volume using specified name and description.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`
    **type** : :obj:`~CRDN_VOLUME_TYPE`

    :Returns:

        :obj:`~ISpatialAnalysisToolVolume`

.. py:method:: is_type_supported(self, eType: CRDN_VOLUME_TYPE) -> bool
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeFactory.is_type_supported

    Return whether the specified type is supported.

    :Parameters:

    **eType** : :obj:`~CRDN_VOLUME_TYPE`

    :Returns:

        :obj:`~bool`

.. py:method:: create_volume_combined(self, name: str, description: str) -> ISpatialAnalysisToolVolume
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeFactory.create_volume_combined

    Create a volume type combined.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ISpatialAnalysisToolVolume`

.. py:method:: create_volume_lighting(self, name: str, description: str) -> ISpatialAnalysisToolVolume
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeFactory.create_volume_lighting

    Create a volume type lighting.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ISpatialAnalysisToolVolume`

.. py:method:: create_volume_over_time(self, name: str, description: str) -> ISpatialAnalysisToolVolume
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeFactory.create_volume_over_time

    Create a volume type over time.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ISpatialAnalysisToolVolume`

.. py:method:: create_volume_from_grid(self, name: str, description: str) -> ISpatialAnalysisToolVolume
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeFactory.create_volume_from_grid

    Create a volume type from grid.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ISpatialAnalysisToolVolume`

.. py:method:: create_volume_from_calc(self, name: str, description: str) -> ISpatialAnalysisToolVolume
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeFactory.create_volume_from_calc

    Create a volume type from calc.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ISpatialAnalysisToolVolume`

.. py:method:: create_volume_from_time_satisfaction(self, name: str, description: str) -> ISpatialAnalysisToolVolume
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeFactory.create_volume_from_time_satisfaction

    Create a volume type from time satisfaction.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ISpatialAnalysisToolVolume`

.. py:method:: create_volume_from_condition(self, name: str, description: str) -> ISpatialAnalysisToolVolume
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeFactory.create_volume_from_condition

    Create a volume type condition.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ISpatialAnalysisToolVolume`

.. py:method:: create_volume_inview(self, name: str, description: str) -> ISpatialAnalysisToolVolume
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeFactory.create_volume_inview

    Create a volume type Inview.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ISpatialAnalysisToolVolume`

