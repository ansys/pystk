IStkRfcmAnalysisConfigurationModel
==================================

.. py:class:: ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisConfigurationModel

   Base interface for all analysis configuration models.

.. py:currentmodule:: IStkRfcmAnalysisConfigurationModel

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisConfigurationModel.type`
              - Get the analysis configuration model type.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisConfigurationModel.scene_contributor_collection`
              - Get the collection of scene contributors.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisConfigurationModel.link_count`
              - Get the link count.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisConfigurationModel.validate_configuration`
              - Validates whether or not the configuration is ready to run.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisConfigurationModel.validate_platform_facets`
              - Validates the configuration platforms which provide facets are configured properly.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisConfigurationModel.interval_start`
              - Get or set the interval start time.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisConfigurationModel.interval_stop`
              - Get or set the interval stop time.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisConfigurationModel.compute_step_mode`
              - Get or set the compute step mode.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisConfigurationModel.fixed_step_count`
              - Get or set the step count.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisConfigurationModel.fixed_step_size`
              - Get or set the step size.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisConfigurationModel.results_file_mode`
              - Get or set the results file mode.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisConfigurationModel.use_scenario_analysis_interval`
              - Get or set whether or not to use the scenario analysis interval.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisConfigurationModel.hide_incompatible_tilesets`
              - Get or set the show all tilesets indicator.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisConfigurationModel.supported_facet_tilesets`
              - Get an array of available facet tilesets.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisConfigurationModel.facet_tileset_collection`
              - Get the collection of facet tilesets.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisConfigurationModel.analysis_extent`
              - Get the facet tileset extent.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkrfchannelmodeler import IStkRfcmAnalysisConfigurationModel


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisConfigurationModel.type
    :type: RfcmAnalysisConfigurationModelType

    Get the analysis configuration model type.

.. py:property:: scene_contributor_collection
    :canonical: ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisConfigurationModel.scene_contributor_collection
    :type: IStkRfcmSceneContributorCollection

    Get the collection of scene contributors.

.. py:property:: link_count
    :canonical: ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisConfigurationModel.link_count
    :type: int

    Get the link count.

.. py:property:: validate_configuration
    :canonical: ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisConfigurationModel.validate_configuration
    :type: StkRfcmValidationResponse

    Validates whether or not the configuration is ready to run.

.. py:property:: validate_platform_facets
    :canonical: ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisConfigurationModel.validate_platform_facets
    :type: StkRfcmValidationResponse

    Validates the configuration platforms which provide facets are configured properly.

.. py:property:: interval_start
    :canonical: ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisConfigurationModel.interval_start
    :type: float

    Get or set the interval start time.

.. py:property:: interval_stop
    :canonical: ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisConfigurationModel.interval_stop
    :type: float

    Get or set the interval stop time.

.. py:property:: compute_step_mode
    :canonical: ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisConfigurationModel.compute_step_mode
    :type: RfcmAnalysisConfigurationComputeStepMode

    Get or set the compute step mode.

.. py:property:: fixed_step_count
    :canonical: ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisConfigurationModel.fixed_step_count
    :type: int

    Get or set the step count.

.. py:property:: fixed_step_size
    :canonical: ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisConfigurationModel.fixed_step_size
    :type: float

    Get or set the step size.

.. py:property:: results_file_mode
    :canonical: ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisConfigurationModel.results_file_mode
    :type: RfcmAnalysisResultsFileMode

    Get or set the results file mode.

.. py:property:: use_scenario_analysis_interval
    :canonical: ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisConfigurationModel.use_scenario_analysis_interval
    :type: bool

    Get or set whether or not to use the scenario analysis interval.

.. py:property:: hide_incompatible_tilesets
    :canonical: ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisConfigurationModel.hide_incompatible_tilesets
    :type: bool

    Get or set the show all tilesets indicator.

.. py:property:: supported_facet_tilesets
    :canonical: ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisConfigurationModel.supported_facet_tilesets
    :type: list

    Get an array of available facet tilesets.

.. py:property:: facet_tileset_collection
    :canonical: ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisConfigurationModel.facet_tileset_collection
    :type: StkRfcmFacetTilesetCollection

    Get the collection of facet tilesets.

.. py:property:: analysis_extent
    :canonical: ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisConfigurationModel.analysis_extent
    :type: StkRfcmExtent

    Get the facet tileset extent.


