IAnalysisConfigurationModel
===========================

.. py:class:: ansys.stk.core.stkrfchannelmodeler.IAnalysisConfigurationModel

   Base interface for all analysis configuration models.

.. py:currentmodule:: IAnalysisConfigurationModel

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IAnalysisConfigurationModel.analysis_extent`
              - Get the facet tileset extent.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IAnalysisConfigurationModel.compute_step_mode`
              - Get or set the compute step mode.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IAnalysisConfigurationModel.facet_tileset_collection`
              - Get the collection of facet tilesets.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IAnalysisConfigurationModel.fixed_step_count`
              - Get or set the step count.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IAnalysisConfigurationModel.fixed_step_size`
              - Get or set the step size.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IAnalysisConfigurationModel.hide_incompatible_tilesets`
              - Get or set the show all tilesets indicator.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IAnalysisConfigurationModel.interval_start`
              - Get or set the interval start time.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IAnalysisConfigurationModel.interval_stop`
              - Get or set the interval stop time.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IAnalysisConfigurationModel.link_count`
              - Get the link count.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IAnalysisConfigurationModel.results_file_mode`
              - Get or set the results file mode.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IAnalysisConfigurationModel.scene_contributor_collection`
              - Get the collection of scene contributors.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IAnalysisConfigurationModel.supported_facet_tilesets`
              - Get an array of available facet tilesets.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IAnalysisConfigurationModel.type`
              - Get the analysis configuration model type.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IAnalysisConfigurationModel.use_scenario_analysis_interval`
              - Get or set whether or not to use the scenario analysis interval.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IAnalysisConfigurationModel.validate_configuration`
              - Validate whether or not the configuration is ready to run.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IAnalysisConfigurationModel.validate_platform_facets`
              - Validate the configuration platforms which provide facets are configured properly.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkrfchannelmodeler import IAnalysisConfigurationModel


Property detail
---------------

.. py:property:: analysis_extent
    :canonical: ansys.stk.core.stkrfchannelmodeler.IAnalysisConfigurationModel.analysis_extent
    :type: Extent

    Get the facet tileset extent.

.. py:property:: compute_step_mode
    :canonical: ansys.stk.core.stkrfchannelmodeler.IAnalysisConfigurationModel.compute_step_mode
    :type: AnalysisConfigurationComputeStepMode

    Get or set the compute step mode.

.. py:property:: facet_tileset_collection
    :canonical: ansys.stk.core.stkrfchannelmodeler.IAnalysisConfigurationModel.facet_tileset_collection
    :type: FacetTilesetCollection

    Get the collection of facet tilesets.

.. py:property:: fixed_step_count
    :canonical: ansys.stk.core.stkrfchannelmodeler.IAnalysisConfigurationModel.fixed_step_count
    :type: int

    Get or set the step count.

.. py:property:: fixed_step_size
    :canonical: ansys.stk.core.stkrfchannelmodeler.IAnalysisConfigurationModel.fixed_step_size
    :type: float

    Get or set the step size.

.. py:property:: hide_incompatible_tilesets
    :canonical: ansys.stk.core.stkrfchannelmodeler.IAnalysisConfigurationModel.hide_incompatible_tilesets
    :type: bool

    Get or set the show all tilesets indicator.

.. py:property:: interval_start
    :canonical: ansys.stk.core.stkrfchannelmodeler.IAnalysisConfigurationModel.interval_start
    :type: float

    Get or set the interval start time.

.. py:property:: interval_stop
    :canonical: ansys.stk.core.stkrfchannelmodeler.IAnalysisConfigurationModel.interval_stop
    :type: float

    Get or set the interval stop time.

.. py:property:: link_count
    :canonical: ansys.stk.core.stkrfchannelmodeler.IAnalysisConfigurationModel.link_count
    :type: int

    Get the link count.

.. py:property:: results_file_mode
    :canonical: ansys.stk.core.stkrfchannelmodeler.IAnalysisConfigurationModel.results_file_mode
    :type: AnalysisResultsFileMode

    Get or set the results file mode.

.. py:property:: scene_contributor_collection
    :canonical: ansys.stk.core.stkrfchannelmodeler.IAnalysisConfigurationModel.scene_contributor_collection
    :type: ISceneContributorCollection

    Get the collection of scene contributors.

.. py:property:: supported_facet_tilesets
    :canonical: ansys.stk.core.stkrfchannelmodeler.IAnalysisConfigurationModel.supported_facet_tilesets
    :type: list

    Get an array of available facet tilesets.

.. py:property:: type
    :canonical: ansys.stk.core.stkrfchannelmodeler.IAnalysisConfigurationModel.type
    :type: AnalysisConfigurationModelType

    Get the analysis configuration model type.

.. py:property:: use_scenario_analysis_interval
    :canonical: ansys.stk.core.stkrfchannelmodeler.IAnalysisConfigurationModel.use_scenario_analysis_interval
    :type: bool

    Get or set whether or not to use the scenario analysis interval.

.. py:property:: validate_configuration
    :canonical: ansys.stk.core.stkrfchannelmodeler.IAnalysisConfigurationModel.validate_configuration
    :type: ValidationResponse

    Validate whether or not the configuration is ready to run.

.. py:property:: validate_platform_facets
    :canonical: ansys.stk.core.stkrfchannelmodeler.IAnalysisConfigurationModel.validate_platform_facets
    :type: ValidationResponse

    Validate the configuration platforms which provide facets are configured properly.


