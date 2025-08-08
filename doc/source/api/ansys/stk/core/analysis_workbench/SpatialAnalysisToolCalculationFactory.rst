SpatialAnalysisToolCalculationFactory
=====================================

.. py:class:: ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationFactory

   The factory is used to create instances of volume calcs.

.. py:currentmodule:: SpatialAnalysisToolCalculationFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationFactory.create`
              - Create and registers a volume calc using specified name and description.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationFactory.create_altitude`
              - Create and registers a altitude to location volume calc type using specified name and description.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationFactory.create_angle_to_location`
              - Create and registers a angle to location volume calc type using specified name and description.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationFactory.create_propagation_delay_to_location`
              - Create and registers a distance to location volume calc type using specified name and description.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationFactory.create_from_file`
              - Create and registers a file volume calc type using specified name and description.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationFactory.create_from_calculation_scalar`
              - Create and registers a scalar to location volume calc type using specified name and description.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationFactory.create_distance_to_location`
              - Create and registers a distance to location volume calc type using specified name and description.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationFactory.create_solar_intensity`
              - Create and registers a solar intensity volume calc type using specified name and description.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationFactory.create_spatial_condition_satisfaction_metrics`
              - Create and registers a spatial condition satisfaction metric volume calc type using specified name and description.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationFactory.is_type_supported`
              - Return whether the specified type is supported.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import SpatialAnalysisToolCalculationFactory



Method detail
-------------

.. py:method:: create(self, name: str, description: str, type: SpatialCalculationType) -> ISpatialAnalysisToolSpatialCalculation
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationFactory.create

    Create and registers a volume calc using specified name and description.

    :Parameters:

        **name** : :obj:`~str`

        **description** : :obj:`~str`

        **type** : :obj:`~SpatialCalculationType`


    :Returns:

        :obj:`~ISpatialAnalysisToolSpatialCalculation`

.. py:method:: create_altitude(self, name: str, description: str) -> ISpatialAnalysisToolSpatialCalculation
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationFactory.create_altitude

    Create and registers a altitude to location volume calc type using specified name and description.

    :Parameters:

        **name** : :obj:`~str`

        **description** : :obj:`~str`


    :Returns:

        :obj:`~ISpatialAnalysisToolSpatialCalculation`

.. py:method:: create_angle_to_location(self, name: str, description: str) -> ISpatialAnalysisToolSpatialCalculation
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationFactory.create_angle_to_location

    Create and registers a angle to location volume calc type using specified name and description.

    :Parameters:

        **name** : :obj:`~str`

        **description** : :obj:`~str`


    :Returns:

        :obj:`~ISpatialAnalysisToolSpatialCalculation`

.. py:method:: create_propagation_delay_to_location(self, name: str, description: str) -> ISpatialAnalysisToolSpatialCalculation
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationFactory.create_propagation_delay_to_location

    Create and registers a distance to location volume calc type using specified name and description.

    :Parameters:

        **name** : :obj:`~str`

        **description** : :obj:`~str`


    :Returns:

        :obj:`~ISpatialAnalysisToolSpatialCalculation`

.. py:method:: create_from_file(self, name: str, description: str) -> ISpatialAnalysisToolSpatialCalculation
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationFactory.create_from_file

    Create and registers a file volume calc type using specified name and description.

    :Parameters:

        **name** : :obj:`~str`

        **description** : :obj:`~str`


    :Returns:

        :obj:`~ISpatialAnalysisToolSpatialCalculation`

.. py:method:: create_from_calculation_scalar(self, name: str, description: str) -> ISpatialAnalysisToolSpatialCalculation
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationFactory.create_from_calculation_scalar

    Create and registers a scalar to location volume calc type using specified name and description.

    :Parameters:

        **name** : :obj:`~str`

        **description** : :obj:`~str`


    :Returns:

        :obj:`~ISpatialAnalysisToolSpatialCalculation`

.. py:method:: create_distance_to_location(self, name: str, description: str) -> ISpatialAnalysisToolSpatialCalculation
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationFactory.create_distance_to_location

    Create and registers a distance to location volume calc type using specified name and description.

    :Parameters:

        **name** : :obj:`~str`

        **description** : :obj:`~str`


    :Returns:

        :obj:`~ISpatialAnalysisToolSpatialCalculation`

.. py:method:: create_solar_intensity(self, name: str, description: str) -> ISpatialAnalysisToolSpatialCalculation
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationFactory.create_solar_intensity

    Create and registers a solar intensity volume calc type using specified name and description.

    :Parameters:

        **name** : :obj:`~str`

        **description** : :obj:`~str`


    :Returns:

        :obj:`~ISpatialAnalysisToolSpatialCalculation`

.. py:method:: create_spatial_condition_satisfaction_metrics(self, name: str, description: str) -> ISpatialAnalysisToolSpatialCalculation
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationFactory.create_spatial_condition_satisfaction_metrics

    Create and registers a spatial condition satisfaction metric volume calc type using specified name and description.

    :Parameters:

        **name** : :obj:`~str`

        **description** : :obj:`~str`


    :Returns:

        :obj:`~ISpatialAnalysisToolSpatialCalculation`

.. py:method:: is_type_supported(self, type: SpatialCalculationType) -> bool
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationFactory.is_type_supported

    Return whether the specified type is supported.

    :Parameters:

        **type** : :obj:`~SpatialCalculationType`


    :Returns:

        :obj:`~bool`

