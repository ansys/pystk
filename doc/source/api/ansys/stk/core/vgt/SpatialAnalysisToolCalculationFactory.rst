SpatialAnalysisToolCalculationFactory
=====================================

.. py:class:: ansys.stk.core.vgt.SpatialAnalysisToolCalculationFactory

   The factory is used to create instances of volume calcs.

.. py:currentmodule:: SpatialAnalysisToolCalculationFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolCalculationFactory.is_type_supported`
              - Return whether the specified type is supported.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolCalculationFactory.create`
              - Create and registers a volume calc using specified name and description.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolCalculationFactory.create_altitude`
              - Create and registers a altitude to location volume calc type using specified name and description.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolCalculationFactory.create_angle_to_location`
              - Create and registers a angle to location volume calc type using specified name and description.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolCalculationFactory.create_from_file`
              - Create and registers a file volume calc type using specified name and description.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolCalculationFactory.create_from_calculation_scalar`
              - Create and registers a scalar to location volume calc type using specified name and description.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolCalculationFactory.create_solar_intensity`
              - Create and registers a solar intensity volume calc type using specified name and description.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolCalculationFactory.create_spatial_condition_satisfaction_metrics`
              - Create and registers a spatial condition satisfaction metric volume calc type using specified name and description.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolCalculationFactory.create_distance_to_location`
              - Create and registers a distance to location volume calc type using specified name and description.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolCalculationFactory.create_propagation_delay_to_location`
              - Create and registers a distance to location volume calc type using specified name and description.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import SpatialAnalysisToolCalculationFactory



Method detail
-------------

.. py:method:: is_type_supported(self, eType: SPATIAL_CALCULATION_TYPE) -> bool
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolCalculationFactory.is_type_supported

    Return whether the specified type is supported.

    :Parameters:

    **eType** : :obj:`~SPATIAL_CALCULATION_TYPE`

    :Returns:

        :obj:`~bool`

.. py:method:: create(self, name: str, description: str, type: SPATIAL_CALCULATION_TYPE) -> ISpatialAnalysisToolSpatialCalculation
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolCalculationFactory.create

    Create and registers a volume calc using specified name and description.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`
    **type** : :obj:`~SPATIAL_CALCULATION_TYPE`

    :Returns:

        :obj:`~ISpatialAnalysisToolSpatialCalculation`

.. py:method:: create_altitude(self, name: str, description: str) -> ISpatialAnalysisToolSpatialCalculation
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolCalculationFactory.create_altitude

    Create and registers a altitude to location volume calc type using specified name and description.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ISpatialAnalysisToolSpatialCalculation`

.. py:method:: create_angle_to_location(self, name: str, description: str) -> ISpatialAnalysisToolSpatialCalculation
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolCalculationFactory.create_angle_to_location

    Create and registers a angle to location volume calc type using specified name and description.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ISpatialAnalysisToolSpatialCalculation`

.. py:method:: create_from_file(self, name: str, description: str) -> ISpatialAnalysisToolSpatialCalculation
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolCalculationFactory.create_from_file

    Create and registers a file volume calc type using specified name and description.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ISpatialAnalysisToolSpatialCalculation`

.. py:method:: create_from_calculation_scalar(self, name: str, description: str) -> ISpatialAnalysisToolSpatialCalculation
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolCalculationFactory.create_from_calculation_scalar

    Create and registers a scalar to location volume calc type using specified name and description.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ISpatialAnalysisToolSpatialCalculation`

.. py:method:: create_solar_intensity(self, name: str, description: str) -> ISpatialAnalysisToolSpatialCalculation
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolCalculationFactory.create_solar_intensity

    Create and registers a solar intensity volume calc type using specified name and description.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ISpatialAnalysisToolSpatialCalculation`

.. py:method:: create_spatial_condition_satisfaction_metrics(self, name: str, description: str) -> ISpatialAnalysisToolSpatialCalculation
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolCalculationFactory.create_spatial_condition_satisfaction_metrics

    Create and registers a spatial condition satisfaction metric volume calc type using specified name and description.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ISpatialAnalysisToolSpatialCalculation`

.. py:method:: create_distance_to_location(self, name: str, description: str) -> ISpatialAnalysisToolSpatialCalculation
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolCalculationFactory.create_distance_to_location

    Create and registers a distance to location volume calc type using specified name and description.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ISpatialAnalysisToolSpatialCalculation`

.. py:method:: create_propagation_delay_to_location(self, name: str, description: str) -> ISpatialAnalysisToolSpatialCalculation
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolCalculationFactory.create_propagation_delay_to_location

    Create and registers a distance to location volume calc type using specified name and description.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ISpatialAnalysisToolSpatialCalculation`

