ISpatialAnalysisToolVolumeCalcFactory
=====================================

.. py:class:: ISpatialAnalysisToolVolumeCalcFactory

   object
   
   The factory is used to create instances of volume calcs.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_type_supported`
              - Return whether the specified type is supported.
            * - :py:meth:`~create`
              - Create and registers a volume calc using specified name and description.
            * - :py:meth:`~create_volume_calc_altitude`
              - Create and registers a altitude to location volume calc type using specified name and description.
            * - :py:meth:`~create_volume_calc_angle_off_vector`
              - Create and registers a angle to location volume calc type using specified name and description.
            * - :py:meth:`~create_volume_calc_file`
              - Create and registers a file volume calc type using specified name and description.
            * - :py:meth:`~create_volume_calc_from_scalar`
              - Create and registers a scalar to location volume calc type using specified name and description.
            * - :py:meth:`~create_volume_calc_solar_intensity`
              - Create and registers a solar intensity volume calc type using specified name and description.
            * - :py:meth:`~create_volume_calc_volume_satisfaction_metric`
              - Create and registers a spatial condition satisfaction metric volume calc type using specified name and description.
            * - :py:meth:`~create_volume_calc_range`
              - Create and registers a distance to location volume calc type using specified name and description.
            * - :py:meth:`~create_volume_calc_delay_range`
              - Create and registers a distance to location volume calc type using specified name and description.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ISpatialAnalysisToolVolumeCalcFactory



Method detail
-------------

.. py:method:: is_type_supported(self, eType: CRDN_VOLUME_CALC_TYPE) -> bool
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcFactory.is_type_supported

    Return whether the specified type is supported.

    :Parameters:

    **eType** : :obj:`~CRDN_VOLUME_CALC_TYPE`

    :Returns:

        :obj:`~bool`

.. py:method:: create(self, name: str, description: str, type: CRDN_VOLUME_CALC_TYPE) -> ISpatialAnalysisToolVolumeCalc
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcFactory.create

    Create and registers a volume calc using specified name and description.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`
    **type** : :obj:`~CRDN_VOLUME_CALC_TYPE`

    :Returns:

        :obj:`~ISpatialAnalysisToolVolumeCalc`

.. py:method:: create_volume_calc_altitude(self, name: str, description: str) -> ISpatialAnalysisToolVolumeCalc
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcFactory.create_volume_calc_altitude

    Create and registers a altitude to location volume calc type using specified name and description.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ISpatialAnalysisToolVolumeCalc`

.. py:method:: create_volume_calc_angle_off_vector(self, name: str, description: str) -> ISpatialAnalysisToolVolumeCalc
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcFactory.create_volume_calc_angle_off_vector

    Create and registers a angle to location volume calc type using specified name and description.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ISpatialAnalysisToolVolumeCalc`

.. py:method:: create_volume_calc_file(self, name: str, description: str) -> ISpatialAnalysisToolVolumeCalc
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcFactory.create_volume_calc_file

    Create and registers a file volume calc type using specified name and description.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ISpatialAnalysisToolVolumeCalc`

.. py:method:: create_volume_calc_from_scalar(self, name: str, description: str) -> ISpatialAnalysisToolVolumeCalc
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcFactory.create_volume_calc_from_scalar

    Create and registers a scalar to location volume calc type using specified name and description.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ISpatialAnalysisToolVolumeCalc`

.. py:method:: create_volume_calc_solar_intensity(self, name: str, description: str) -> ISpatialAnalysisToolVolumeCalc
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcFactory.create_volume_calc_solar_intensity

    Create and registers a solar intensity volume calc type using specified name and description.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ISpatialAnalysisToolVolumeCalc`

.. py:method:: create_volume_calc_volume_satisfaction_metric(self, name: str, description: str) -> ISpatialAnalysisToolVolumeCalc
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcFactory.create_volume_calc_volume_satisfaction_metric

    Create and registers a spatial condition satisfaction metric volume calc type using specified name and description.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ISpatialAnalysisToolVolumeCalc`

.. py:method:: create_volume_calc_range(self, name: str, description: str) -> ISpatialAnalysisToolVolumeCalc
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcFactory.create_volume_calc_range

    Create and registers a distance to location volume calc type using specified name and description.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ISpatialAnalysisToolVolumeCalc`

.. py:method:: create_volume_calc_delay_range(self, name: str, description: str) -> ISpatialAnalysisToolVolumeCalc
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcFactory.create_volume_calc_delay_range

    Create and registers a distance to location volume calc type using specified name and description.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ISpatialAnalysisToolVolumeCalc`

