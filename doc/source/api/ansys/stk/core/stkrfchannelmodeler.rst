
The ``stkrfcm`` module
======================


.. py:module:: ansys.stk.core.stkrfcm


Summary
-------

.. tab-set::

 
    .. tab-item:: Interfaces

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~ansys.stk.core.stkrfcm.IStkRfcmProgressTrackCancel`
              - Control for progress tracker.

            * - :py:class:`~ansys.stk.core.stkrfcm.IStkRfcmAntenna`
              - Base interface for a transceiver antenna model.

            * - :py:class:`~ansys.stk.core.stkrfcm.IStkRfcmTransceiverModel`
              - Base interface which defines common properties for a transceiver model.

            * - :py:class:`~ansys.stk.core.stkrfcm.IStkRfcmSceneContributor`
              - Properties for a scene contributor object.

            * - :py:class:`~ansys.stk.core.stkrfcm.IStkRfcmResponse`
              - Properties and data for a channel characaterization response.

            * - :py:class:`~ansys.stk.core.stkrfcm.IStkRfcmAnalysisLink`
              - Properties for a transceiver link for an analysis.

            * - :py:class:`~ansys.stk.core.stkrfcm.IStkRfcmAnalysisConfigurationModel`
              - Base interface for all analysis configuration models.

            * - :py:class:`~ansys.stk.core.stkrfcm.IStkRfcmRadarAnalysisConfigurationModel`
              - Properties for an analysis configuration model for a radar analysis. This contains a collection of the transceiver configurations belonging to the radar analysis.

    
    .. tab-item:: Classes

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~ansys.stk.core.stkrfcm.StkRfcmRadarImagingDataProduct`
              - Imaging data product that facilitates the generation of range doppler radar images.

            * - :py:class:`~ansys.stk.core.stkrfcm.StkRfcmMaterial`
              - A material for scene contributors.

            * - :py:class:`~ansys.stk.core.stkrfcm.StkRfcmFacetTileset`
              - The facet tileset information.

            * - :py:class:`~ansys.stk.core.stkrfcm.StkRfcmValidationResponse`
              - The response from validating an analysis configuration.

            * - :py:class:`~ansys.stk.core.stkrfcm.StkRfcmExtent`
              - The extent in which the channel characterizations will be computed.

            * - :py:class:`~ansys.stk.core.stkrfcm.StkRfcmCommunicationsWaveform`
              - The waveform settings of a communications transceiver.

            * - :py:class:`~ansys.stk.core.stkrfcm.StkRfcmRadarWaveform`
              - The waveform settings of a radar transceiver.

            * - :py:class:`~ansys.stk.core.stkrfcm.StkRfcmParametricBeamAntenna`
              - The antenna settings for a parametric beam antenna.

            * - :py:class:`~ansys.stk.core.stkrfcm.StkRfcmElementExportPatternAntenna`
              - The antenna settings for an element export pattern antenna.

            * - :py:class:`~ansys.stk.core.stkrfcm.StkRfcmFarFieldDataPatternAntenna`
              - The antenna settings for a far field data pattern antenna.

            * - :py:class:`~ansys.stk.core.stkrfcm.StkRfcmTransceiver`
              - The transceiver object and its settings.

            * - :py:class:`~ansys.stk.core.stkrfcm.StkRfcmCommunicationsTransceiverConfiguration`
              - The transceiver configuration for a communications transceiver.

            * - :py:class:`~ansys.stk.core.stkrfcm.StkRfcmRadarTransceiverConfiguration`
              - The transceiver configuration for a radar transceiver.

            * - :py:class:`~ansys.stk.core.stkrfcm.StkRfcmRadarTransceiverConfigurationCollection`
              - A collection of radar transceivers.

            * - :py:class:`~ansys.stk.core.stkrfcm.StkRfcmAnalysisConfiguration`
              - The configuration for an analysis.

            * - :py:class:`~ansys.stk.core.stkrfcm.StkRfcmCommunicationsAnalysisConfigurationModel`
              - The analysis configuration model for a communications analysis. This contains a collection of the transceiver configurations belonging to the communications analysis.

            * - :py:class:`~ansys.stk.core.stkrfcm.StkRfcmRadarISarAnalysisConfigurationModel`
              - The analysis configuration model for an ISar analysis. This contains a collection of the transceiver configurations belonging to the ISar analysis.

            * - :py:class:`~ansys.stk.core.stkrfcm.StkRfcmRadarSarAnalysisConfigurationModel`
              - The analysis configuration model for a Sar analysis. This contains a collection of the transceiver configurations belonging to the Sar analysis.

            * - :py:class:`~ansys.stk.core.stkrfcm.StkRfcmTransceiverCollection`
              - A collection of transceiver objects.

            * - :py:class:`~ansys.stk.core.stkrfcm.StkRfcmFacetTilesetCollection`
              - A collection of facet tilesets.

            * - :py:class:`~ansys.stk.core.stkrfcm.StkRfcmSceneContributor`
              - A scene contributor object.

            * - :py:class:`~ansys.stk.core.stkrfcm.StkRfcmRadarTarget`
              - A radar target object, to be utilized by a radar analysis as a scene contributor.

            * - :py:class:`~ansys.stk.core.stkrfcm.StkRfcmSceneContributorCollection`
              - A collection of scene contributor objects.

            * - :py:class:`~ansys.stk.core.stkrfcm.StkRfcmRadarTargetCollection`
              - A collection of radar target objects.

            * - :py:class:`~ansys.stk.core.stkrfcm.StkRfcmRadarSarImageLocation`
              - The image location information for use by a range doppler Sar analysis.

            * - :py:class:`~ansys.stk.core.stkrfcm.StkRfcmRadarSarImageLocationCollection`
              - A collection of image location information.

            * - :py:class:`~ansys.stk.core.stkrfcm.StkRfcmCommunicationsTransceiverConfigurationCollection`
              - A collection of communication transceivers.

            * - :py:class:`~ansys.stk.core.stkrfcm.StkRfcmAnalysisConfigurationCollection`
              - A collection of analysis configurations.

            * - :py:class:`~ansys.stk.core.stkrfcm.StkRfcmComputeOptions`
              - The options for computing RF Channel Modeler.

            * - :py:class:`~ansys.stk.core.stkrfcm.StkRFChannelModeler`
              - The main RF Channel Modeler object.

            * - :py:class:`~ansys.stk.core.stkrfcm.StkRfcmCommunicationsTransceiverModel`
              - The model for a communications transceiver.

            * - :py:class:`~ansys.stk.core.stkrfcm.StkRfcmRadarTransceiverModel`
              - The model for a radar transceiver.

            * - :py:class:`~ansys.stk.core.stkrfcm.StkRfcmRangeDopplerResponse`
              - The response data and properties for a range doppler channel characterization.

            * - :py:class:`~ansys.stk.core.stkrfcm.StkRfcmFrequencyPulseResponse`
              - The response data and properties for a frequency pulse channel characterization.

            * - :py:class:`~ansys.stk.core.stkrfcm.StkRfcmAnalysisLink`
              - A transceiver link for an analysis.

            * - :py:class:`~ansys.stk.core.stkrfcm.StkRfcmRadarSarAnalysisLink`
              - A transceiver link for a Sar analysis.

            * - :py:class:`~ansys.stk.core.stkrfcm.StkRfcmRadarISarAnalysisLink`
              - A transceiver link for an ISar analysis.

            * - :py:class:`~ansys.stk.core.stkrfcm.StkRfcmAnalysisLinkCollection`
              - A collection of links between transceivers.

            * - :py:class:`~ansys.stk.core.stkrfcm.StkRfcmAnalysis`
              - An RF Channel Modeler analysis.

            * - :py:class:`~ansys.stk.core.stkrfcm.StkRfcmGpuProperties`
              - The properties of a GPU pertaining to RF Channel Modeler.


    .. tab-item:: Enums

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~ansys.stk.core.stkrfcm.RFCM_ANALYSIS_TYPE`
              - Analysis Type

            * - :py:class:`~ansys.stk.core.stkrfcm.RFCM_ANALYSIS_SUBTYPE`
              - Analysis Subtype

            * - :py:class:`~ansys.stk.core.stkrfcm.RFCM_CHANNEL_RESPONSE_TYPE`
              - Channel Response Type

            * - :py:class:`~ansys.stk.core.stkrfcm.RFCM_ANALYSIS_CONFIGURATION_MODEL_TYPE`
              - Analysis Configuration Model Type

            * - :py:class:`~ansys.stk.core.stkrfcm.RFCM_TRANSCEIVER_MODE`
              - Transceiver Mode

            * - :py:class:`~ansys.stk.core.stkrfcm.RFCM_ANALYSIS_CONFIGURATION_COMPUTE_STEP_MODE`
              - Analysis configuration compute step mode.

            * - :py:class:`~ansys.stk.core.stkrfcm.RFCM_ANALYSIS_RESULTS_FILE_MODE`
              - Analysis results file mode.

            * - :py:class:`~ansys.stk.core.stkrfcm.RFCM_ANALYSIS_SOLVER_BOUNDING_BOX_MODE`
              - Analysis solver bounding box mode.

            * - :py:class:`~ansys.stk.core.stkrfcm.RFCM_TRANSCEIVER_MODEL_TYPE`
              - Transceiver Model Type

            * - :py:class:`~ansys.stk.core.stkrfcm.RFCM_POLARIZATION_TYPE`
              - Polarization Type

            * - :py:class:`~ansys.stk.core.stkrfcm.RFCM_IMAGE_WINDOW_TYPE`
              - Polarization Type



Description
-----------

Object Model components specifically designed to support STK RF Channel Modeler.


.. py:currentmodule:: ansys.stk.core.stkrfcm


.. TABLE OF CONTENTS

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     IStkRfcmProgressTrackCancel<stkrfcm/IStkRfcmProgressTrackCancel>
     IStkRfcmAntenna<stkrfcm/IStkRfcmAntenna>
     IStkRfcmTransceiverModel<stkrfcm/IStkRfcmTransceiverModel>
     IStkRfcmSceneContributor<stkrfcm/IStkRfcmSceneContributor>
     IStkRfcmResponse<stkrfcm/IStkRfcmResponse>
     IStkRfcmAnalysisLink<stkrfcm/IStkRfcmAnalysisLink>
     IStkRfcmAnalysisConfigurationModel<stkrfcm/IStkRfcmAnalysisConfigurationModel>
     IStkRfcmRadarAnalysisConfigurationModel<stkrfcm/IStkRfcmRadarAnalysisConfigurationModel>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     StkRfcmRadarImagingDataProduct<stkrfcm/StkRfcmRadarImagingDataProduct>
     StkRfcmMaterial<stkrfcm/StkRfcmMaterial>
     StkRfcmFacetTileset<stkrfcm/StkRfcmFacetTileset>
     StkRfcmValidationResponse<stkrfcm/StkRfcmValidationResponse>
     StkRfcmExtent<stkrfcm/StkRfcmExtent>
     StkRfcmCommunicationsWaveform<stkrfcm/StkRfcmCommunicationsWaveform>
     StkRfcmRadarWaveform<stkrfcm/StkRfcmRadarWaveform>
     StkRfcmParametricBeamAntenna<stkrfcm/StkRfcmParametricBeamAntenna>
     StkRfcmElementExportPatternAntenna<stkrfcm/StkRfcmElementExportPatternAntenna>
     StkRfcmFarFieldDataPatternAntenna<stkrfcm/StkRfcmFarFieldDataPatternAntenna>
     StkRfcmTransceiver<stkrfcm/StkRfcmTransceiver>
     StkRfcmCommunicationsTransceiverConfiguration<stkrfcm/StkRfcmCommunicationsTransceiverConfiguration>
     StkRfcmRadarTransceiverConfiguration<stkrfcm/StkRfcmRadarTransceiverConfiguration>
     StkRfcmRadarTransceiverConfigurationCollection<stkrfcm/StkRfcmRadarTransceiverConfigurationCollection>
     StkRfcmAnalysisConfiguration<stkrfcm/StkRfcmAnalysisConfiguration>
     StkRfcmCommunicationsAnalysisConfigurationModel<stkrfcm/StkRfcmCommunicationsAnalysisConfigurationModel>
     StkRfcmRadarISarAnalysisConfigurationModel<stkrfcm/StkRfcmRadarISarAnalysisConfigurationModel>
     StkRfcmRadarSarAnalysisConfigurationModel<stkrfcm/StkRfcmRadarSarAnalysisConfigurationModel>
     StkRfcmTransceiverCollection<stkrfcm/StkRfcmTransceiverCollection>
     StkRfcmFacetTilesetCollection<stkrfcm/StkRfcmFacetTilesetCollection>
     StkRfcmSceneContributor<stkrfcm/StkRfcmSceneContributor>
     StkRfcmRadarTarget<stkrfcm/StkRfcmRadarTarget>
     StkRfcmSceneContributorCollection<stkrfcm/StkRfcmSceneContributorCollection>
     StkRfcmRadarTargetCollection<stkrfcm/StkRfcmRadarTargetCollection>
     StkRfcmRadarSarImageLocation<stkrfcm/StkRfcmRadarSarImageLocation>
     StkRfcmRadarSarImageLocationCollection<stkrfcm/StkRfcmRadarSarImageLocationCollection>
     StkRfcmCommunicationsTransceiverConfigurationCollection<stkrfcm/StkRfcmCommunicationsTransceiverConfigurationCollection>
     StkRfcmAnalysisConfigurationCollection<stkrfcm/StkRfcmAnalysisConfigurationCollection>
     StkRfcmComputeOptions<stkrfcm/StkRfcmComputeOptions>
     StkRFChannelModeler<stkrfcm/StkRFChannelModeler>
     StkRfcmCommunicationsTransceiverModel<stkrfcm/StkRfcmCommunicationsTransceiverModel>
     StkRfcmRadarTransceiverModel<stkrfcm/StkRfcmRadarTransceiverModel>
     StkRfcmRangeDopplerResponse<stkrfcm/StkRfcmRangeDopplerResponse>
     StkRfcmFrequencyPulseResponse<stkrfcm/StkRfcmFrequencyPulseResponse>
     StkRfcmAnalysisLink<stkrfcm/StkRfcmAnalysisLink>
     StkRfcmRadarSarAnalysisLink<stkrfcm/StkRfcmRadarSarAnalysisLink>
     StkRfcmRadarISarAnalysisLink<stkrfcm/StkRfcmRadarISarAnalysisLink>
     StkRfcmAnalysisLinkCollection<stkrfcm/StkRfcmAnalysisLinkCollection>
     StkRfcmAnalysis<stkrfcm/StkRfcmAnalysis>
     StkRfcmGpuProperties<stkrfcm/StkRfcmGpuProperties>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    ≔ RFCM_ANALYSIS_TYPE<stkrfcm/RFCM_ANALYSIS_TYPE_enum>
    ≔ RFCM_ANALYSIS_SUBTYPE<stkrfcm/RFCM_ANALYSIS_SUBTYPE_enum>
    ≔ RFCM_CHANNEL_RESPONSE_TYPE<stkrfcm/RFCM_CHANNEL_RESPONSE_TYPE_enum>
    ≔ RFCM_ANALYSIS_CONFIGURATION_MODEL_TYPE<stkrfcm/RFCM_ANALYSIS_CONFIGURATION_MODEL_TYPE_enum>
    ≔ RFCM_TRANSCEIVER_MODE<stkrfcm/RFCM_TRANSCEIVER_MODE_enum>
    ≔ RFCM_ANALYSIS_CONFIGURATION_COMPUTE_STEP_MODE<stkrfcm/RFCM_ANALYSIS_CONFIGURATION_COMPUTE_STEP_MODE_enum>
    ≔ RFCM_ANALYSIS_RESULTS_FILE_MODE<stkrfcm/RFCM_ANALYSIS_RESULTS_FILE_MODE_enum>
    ≔ RFCM_ANALYSIS_SOLVER_BOUNDING_BOX_MODE<stkrfcm/RFCM_ANALYSIS_SOLVER_BOUNDING_BOX_MODE_enum>
    ≔ RFCM_TRANSCEIVER_MODEL_TYPE<stkrfcm/RFCM_TRANSCEIVER_MODEL_TYPE_enum>
    ≔ RFCM_POLARIZATION_TYPE<stkrfcm/RFCM_POLARIZATION_TYPE_enum>
    ≔ RFCM_IMAGE_WINDOW_TYPE<stkrfcm/RFCM_IMAGE_WINDOW_TYPE_enum>

