IStkRfcmAnalysisConfigurationModel
==================================

.. py:class:: ansys.stk.core.rfcm.IStkRfcmAnalysisConfigurationModel

   Base interface for all analysis configuration models.

.. py:currentmodule:: IStkRfcmAnalysisConfigurationModel

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.rfcm.IStkRfcmAnalysisConfigurationModel.type`
              - Gets the analysis configuration model type.
            * - :py:attr:`~ansys.stk.core.rfcm.IStkRfcmAnalysisConfigurationModel.scene_contributor_collection`
              - Gets the collection of scene contributors.
            * - :py:attr:`~ansys.stk.core.rfcm.IStkRfcmAnalysisConfigurationModel.link_count`
              - Gets the link count.
            * - :py:attr:`~ansys.stk.core.rfcm.IStkRfcmAnalysisConfigurationModel.validate_configuration`
              - Validates whether or not the configuration is ready to run.
            * - :py:attr:`~ansys.stk.core.rfcm.IStkRfcmAnalysisConfigurationModel.validate_platform_facets`
              - Validates the configuration platforms which provide facets are configured properly.
            * - :py:attr:`~ansys.stk.core.rfcm.IStkRfcmAnalysisConfigurationModel.interval_start`
              - Gets or sets the interval start time.
            * - :py:attr:`~ansys.stk.core.rfcm.IStkRfcmAnalysisConfigurationModel.interval_stop`
              - Gets or sets the interval stop time.
            * - :py:attr:`~ansys.stk.core.rfcm.IStkRfcmAnalysisConfigurationModel.compute_step_mode`
              - Gets or sets the compute step mode.
            * - :py:attr:`~ansys.stk.core.rfcm.IStkRfcmAnalysisConfigurationModel.fixed_step_count`
              - Gets or sets the step count.
            * - :py:attr:`~ansys.stk.core.rfcm.IStkRfcmAnalysisConfigurationModel.fixed_step_size`
              - Gets or sets the step size.
            * - :py:attr:`~ansys.stk.core.rfcm.IStkRfcmAnalysisConfigurationModel.results_file_mode`
              - Gets or sets the results file mode.
            * - :py:attr:`~ansys.stk.core.rfcm.IStkRfcmAnalysisConfigurationModel.use_scenario_analysis_interval`
              - Gets or sets whether or not to use the scenario analysis interval.
            * - :py:attr:`~ansys.stk.core.rfcm.IStkRfcmAnalysisConfigurationModel.hide_incompatible_tilesets`
              - Gets or sets the show all tilesets indicator.
            * - :py:attr:`~ansys.stk.core.rfcm.IStkRfcmAnalysisConfigurationModel.supported_facet_tilesets`
              - Gets an array of available facet tilesets.
            * - :py:attr:`~ansys.stk.core.rfcm.IStkRfcmAnalysisConfigurationModel.facet_tileset_collection`
              - Gets the collection of facet tilesets.
            * - :py:attr:`~ansys.stk.core.rfcm.IStkRfcmAnalysisConfigurationModel.analysis_extent`
              - Gets the facet tileset extent.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.rfcm import IStkRfcmAnalysisConfigurationModel


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.rfcm.IStkRfcmAnalysisConfigurationModel.type
    :type: RfcmAnalysisConfigurationModelType

    Gets the analysis configuration model type.

.. py:property:: scene_contributor_collection
    :canonical: ansys.stk.core.rfcm.IStkRfcmAnalysisConfigurationModel.scene_contributor_collection
    :type: IStkRfcmSceneContributorCollection

    Gets the collection of scene contributors.

.. py:property:: link_count
    :canonical: ansys.stk.core.rfcm.IStkRfcmAnalysisConfigurationModel.link_count
    :type: int

    Gets the link count.

.. py:property:: validate_configuration
    :canonical: ansys.stk.core.rfcm.IStkRfcmAnalysisConfigurationModel.validate_configuration
    :type: StkRfcmValidationResponse

    Validates whether or not the configuration is ready to run.

.. py:property:: validate_platform_facets
    :canonical: ansys.stk.core.rfcm.IStkRfcmAnalysisConfigurationModel.validate_platform_facets
    :type: StkRfcmValidationResponse

    Validates the configuration platforms which provide facets are configured properly.

.. py:property:: interval_start
    :canonical: ansys.stk.core.rfcm.IStkRfcmAnalysisConfigurationModel.interval_start
    :type: float

    Gets or sets the interval start time.

.. py:property:: interval_stop
    :canonical: ansys.stk.core.rfcm.IStkRfcmAnalysisConfigurationModel.interval_stop
    :type: float

    Gets or sets the interval stop time.

.. py:property:: compute_step_mode
    :canonical: ansys.stk.core.rfcm.IStkRfcmAnalysisConfigurationModel.compute_step_mode
    :type: RfcmAnalysisConfigurationComputeStepMode

    Gets or sets the compute step mode.

.. py:property:: fixed_step_count
    :canonical: ansys.stk.core.rfcm.IStkRfcmAnalysisConfigurationModel.fixed_step_count
    :type: int

    Gets or sets the step count.

.. py:property:: fixed_step_size
    :canonical: ansys.stk.core.rfcm.IStkRfcmAnalysisConfigurationModel.fixed_step_size
    :type: float

    Gets or sets the step size.

.. py:property:: results_file_mode
    :canonical: ansys.stk.core.rfcm.IStkRfcmAnalysisConfigurationModel.results_file_mode
    :type: RfcmAnalysisResultsFileMode

    Gets or sets the results file mode.

.. py:property:: use_scenario_analysis_interval
    :canonical: ansys.stk.core.rfcm.IStkRfcmAnalysisConfigurationModel.use_scenario_analysis_interval
    :type: bool

    Gets or sets whether or not to use the scenario analysis interval.

.. py:property:: hide_incompatible_tilesets
    :canonical: ansys.stk.core.rfcm.IStkRfcmAnalysisConfigurationModel.hide_incompatible_tilesets
    :type: bool

    Gets or sets the show all tilesets indicator.

.. py:property:: supported_facet_tilesets
    :canonical: ansys.stk.core.rfcm.IStkRfcmAnalysisConfigurationModel.supported_facet_tilesets
    :type: list

    Gets an array of available facet tilesets.

.. py:property:: facet_tileset_collection
    :canonical: ansys.stk.core.rfcm.IStkRfcmAnalysisConfigurationModel.facet_tileset_collection
    :type: StkRfcmFacetTilesetCollection

    Gets the collection of facet tilesets.

.. py:property:: analysis_extent
    :canonical: ansys.stk.core.rfcm.IStkRfcmAnalysisConfigurationModel.analysis_extent
    :type: StkRfcmExtent

    Gets the facet tileset extent.


