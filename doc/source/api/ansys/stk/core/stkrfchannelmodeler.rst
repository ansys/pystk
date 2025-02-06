
The ``stkrfchannelmodeler`` module
==================================


.. py:module:: ansys.stk.core.stkrfchannelmodeler


Summary
-------

.. tab-set::

 
    .. tab-item:: Interfaces

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.IStkRfcmProgressTrackCancel`
              - Control for progress tracker.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.IStkRfcmAntenna`
              - Base interface for a transceiver antenna model.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.IStkRfcmTransceiverModel`
              - Base interface which defines common properties for a transceiver model.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.IStkRfcmSceneContributorCollection`
              - Represents a collection of scene contributors.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.IStkRfcmResponse`
              - Properties and data for a channel characaterization response.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisLink`
              - Properties for a transceiver link for an analysis.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisConfigurationModel`
              - Base interface for all analysis configuration models.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.IStkRfcmRadarAnalysisConfigurationModel`
              - Properties for an analysis configuration model for a radar analysis. This contains a collection of the transceiver configurations belonging to the radar analysis.

    
    .. tab-item:: Classes

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProduct`
              - Imaging data product that facilitates the generation of range doppler radar images.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmMaterial`
              - A material for scene contributors.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmFacetTileset`
              - The facet tileset information.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmValidationResponse`
              - The response from validating an analysis configuration.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmExtent`
              - The extent in which the channel characterizations will be computed.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmCommunicationsWaveform`
              - The waveform settings of a communications transceiver.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarWaveform`
              - The waveform settings of a radar transceiver.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmParametricBeamAntenna`
              - The antenna settings for a parametric beam antenna.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmElementExportPatternAntenna`
              - The antenna settings for an element export pattern antenna.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmFarFieldDataPatternAntenna`
              - The antenna settings for a far field data pattern antenna.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmTransceiver`
              - The transceiver object and its settings.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmCommunicationsTransceiverConfiguration`
              - The transceiver configuration for a communications transceiver.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarTransceiverConfiguration`
              - The transceiver configuration for a radar transceiver.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarImagingDataProductCollection`
              - A collection of radar transceivers.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarTransceiverConfigurationCollection`
              - A collection of radar transceivers.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmAnalysisConfiguration`
              - The configuration for an analysis.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmCommunicationsAnalysisConfigurationModel`
              - The analysis configuration model for a communications analysis. This contains a collection of the transceiver configurations belonging to the communications analysis.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarISarAnalysisConfigurationModel`
              - The analysis configuration model for an ISar analysis. This contains a collection of the transceiver configurations belonging to the ISar analysis.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarSarAnalysisConfigurationModel`
              - The analysis configuration model for a Sar analysis. This contains a collection of the transceiver configurations belonging to the Sar analysis.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmTransceiverCollection`
              - A collection of transceiver objects.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmFacetTilesetCollection`
              - A collection of facet tilesets.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmSceneContributor`
              - A scene contributor object.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmSceneContributorCollection`
              - A collection of scene contributor objects.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarTargetCollection`
              - A collection of radar target objects.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarSarImageLocation`
              - The image location information for use by a range doppler Sar analysis.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarSarImageLocationCollection`
              - A collection of image location information.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmCommunicationsTransceiverConfigurationCollection`
              - A collection of communication transceivers.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmAnalysisConfigurationCollection`
              - A collection of analysis configurations.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmComputeOptions`
              - The options for computing RF Channel Modeler.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.StkRFChannelModeler`
              - The main RF Channel Modeler object.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmCommunicationsTransceiverModel`
              - The model for a communications transceiver.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarTransceiverModel`
              - The model for a radar transceiver.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmRangeDopplerResponse`
              - The response data and properties for a range doppler channel characterization.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmFrequencyPulseResponse`
              - The response data and properties for a frequency pulse channel characterization.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmAnalysisLink`
              - A transceiver link for an analysis.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarSarAnalysisLink`
              - A transceiver link for a Sar analysis.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmRadarISarAnalysisLink`
              - A transceiver link for an ISar analysis.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmAnalysisLinkCollection`
              - A collection of links between transceivers.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmAnalysis`
              - An RF Channel Modeler analysis.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmGpuProperties`
              - The properties of a GPU pertaining to RF Channel Modeler.


    .. tab-item:: Enums

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.RfcmChannelResponseType`
              - Channel Response Type

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.RfcmAnalysisConfigurationModelType`
              - Analysis Configuration Model Type

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.RfcmTransceiverMode`
              - Transceiver Mode

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.RfcmAnalysisConfigurationComputeStepMode`
              - Analysis configuration compute step mode.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.RfcmAnalysisResultsFileMode`
              - Analysis results file mode.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.RfcmAnalysisSolverBoundingBoxMode`
              - Analysis solver bounding box mode.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.RfcmTransceiverModelType`
              - Transceiver Model Type

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.RfcmPolarizationType`
              - Polarization Type

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.RfcmImageWindowType`
              - Polarization Type



Description
-----------

Object Model components specifically designed to support STK RF Channel Modeler.


.. py:currentmodule:: ansys.stk.core.stkrfchannelmodeler


.. TABLE OF CONTENTS

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     IStkRfcmProgressTrackCancel<stkrfchannelmodeler/IStkRfcmProgressTrackCancel>
     IStkRfcmAntenna<stkrfchannelmodeler/IStkRfcmAntenna>
     IStkRfcmTransceiverModel<stkrfchannelmodeler/IStkRfcmTransceiverModel>
     IStkRfcmSceneContributorCollection<stkrfchannelmodeler/IStkRfcmSceneContributorCollection>
     IStkRfcmResponse<stkrfchannelmodeler/IStkRfcmResponse>
     IStkRfcmAnalysisLink<stkrfchannelmodeler/IStkRfcmAnalysisLink>
     IStkRfcmAnalysisConfigurationModel<stkrfchannelmodeler/IStkRfcmAnalysisConfigurationModel>
     IStkRfcmRadarAnalysisConfigurationModel<stkrfchannelmodeler/IStkRfcmRadarAnalysisConfigurationModel>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     StkRfcmRadarImagingDataProduct<stkrfchannelmodeler/StkRfcmRadarImagingDataProduct>
     StkRfcmMaterial<stkrfchannelmodeler/StkRfcmMaterial>
     StkRfcmFacetTileset<stkrfchannelmodeler/StkRfcmFacetTileset>
     StkRfcmValidationResponse<stkrfchannelmodeler/StkRfcmValidationResponse>
     StkRfcmExtent<stkrfchannelmodeler/StkRfcmExtent>
     StkRfcmCommunicationsWaveform<stkrfchannelmodeler/StkRfcmCommunicationsWaveform>
     StkRfcmRadarWaveform<stkrfchannelmodeler/StkRfcmRadarWaveform>
     StkRfcmParametricBeamAntenna<stkrfchannelmodeler/StkRfcmParametricBeamAntenna>
     StkRfcmElementExportPatternAntenna<stkrfchannelmodeler/StkRfcmElementExportPatternAntenna>
     StkRfcmFarFieldDataPatternAntenna<stkrfchannelmodeler/StkRfcmFarFieldDataPatternAntenna>
     StkRfcmTransceiver<stkrfchannelmodeler/StkRfcmTransceiver>
     StkRfcmCommunicationsTransceiverConfiguration<stkrfchannelmodeler/StkRfcmCommunicationsTransceiverConfiguration>
     StkRfcmRadarTransceiverConfiguration<stkrfchannelmodeler/StkRfcmRadarTransceiverConfiguration>
     StkRfcmRadarImagingDataProductCollection<stkrfchannelmodeler/StkRfcmRadarImagingDataProductCollection>
     StkRfcmRadarTransceiverConfigurationCollection<stkrfchannelmodeler/StkRfcmRadarTransceiverConfigurationCollection>
     StkRfcmAnalysisConfiguration<stkrfchannelmodeler/StkRfcmAnalysisConfiguration>
     StkRfcmCommunicationsAnalysisConfigurationModel<stkrfchannelmodeler/StkRfcmCommunicationsAnalysisConfigurationModel>
     StkRfcmRadarISarAnalysisConfigurationModel<stkrfchannelmodeler/StkRfcmRadarISarAnalysisConfigurationModel>
     StkRfcmRadarSarAnalysisConfigurationModel<stkrfchannelmodeler/StkRfcmRadarSarAnalysisConfigurationModel>
     StkRfcmTransceiverCollection<stkrfchannelmodeler/StkRfcmTransceiverCollection>
     StkRfcmFacetTilesetCollection<stkrfchannelmodeler/StkRfcmFacetTilesetCollection>
     StkRfcmSceneContributor<stkrfchannelmodeler/StkRfcmSceneContributor>
     StkRfcmSceneContributorCollection<stkrfchannelmodeler/StkRfcmSceneContributorCollection>
     StkRfcmRadarTargetCollection<stkrfchannelmodeler/StkRfcmRadarTargetCollection>
     StkRfcmRadarSarImageLocation<stkrfchannelmodeler/StkRfcmRadarSarImageLocation>
     StkRfcmRadarSarImageLocationCollection<stkrfchannelmodeler/StkRfcmRadarSarImageLocationCollection>
     StkRfcmCommunicationsTransceiverConfigurationCollection<stkrfchannelmodeler/StkRfcmCommunicationsTransceiverConfigurationCollection>
     StkRfcmAnalysisConfigurationCollection<stkrfchannelmodeler/StkRfcmAnalysisConfigurationCollection>
     StkRfcmComputeOptions<stkrfchannelmodeler/StkRfcmComputeOptions>
     StkRFChannelModeler<stkrfchannelmodeler/StkRFChannelModeler>
     StkRfcmCommunicationsTransceiverModel<stkrfchannelmodeler/StkRfcmCommunicationsTransceiverModel>
     StkRfcmRadarTransceiverModel<stkrfchannelmodeler/StkRfcmRadarTransceiverModel>
     StkRfcmRangeDopplerResponse<stkrfchannelmodeler/StkRfcmRangeDopplerResponse>
     StkRfcmFrequencyPulseResponse<stkrfchannelmodeler/StkRfcmFrequencyPulseResponse>
     StkRfcmAnalysisLink<stkrfchannelmodeler/StkRfcmAnalysisLink>
     StkRfcmRadarSarAnalysisLink<stkrfchannelmodeler/StkRfcmRadarSarAnalysisLink>
     StkRfcmRadarISarAnalysisLink<stkrfchannelmodeler/StkRfcmRadarISarAnalysisLink>
     StkRfcmAnalysisLinkCollection<stkrfchannelmodeler/StkRfcmAnalysisLinkCollection>
     StkRfcmAnalysis<stkrfchannelmodeler/StkRfcmAnalysis>
     StkRfcmGpuProperties<stkrfchannelmodeler/StkRfcmGpuProperties>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    ≔ RfcmChannelResponseType<stkrfchannelmodeler/RfcmChannelResponseType>
    ≔ RfcmAnalysisConfigurationModelType<stkrfchannelmodeler/RfcmAnalysisConfigurationModelType>
    ≔ RfcmTransceiverMode<stkrfchannelmodeler/RfcmTransceiverMode>
    ≔ RfcmAnalysisConfigurationComputeStepMode<stkrfchannelmodeler/RfcmAnalysisConfigurationComputeStepMode>
    ≔ RfcmAnalysisResultsFileMode<stkrfchannelmodeler/RfcmAnalysisResultsFileMode>
    ≔ RfcmAnalysisSolverBoundingBoxMode<stkrfchannelmodeler/RfcmAnalysisSolverBoundingBoxMode>
    ≔ RfcmTransceiverModelType<stkrfchannelmodeler/RfcmTransceiverModelType>
    ≔ RfcmPolarizationType<stkrfchannelmodeler/RfcmPolarizationType>
    ≔ RfcmImageWindowType<stkrfchannelmodeler/RfcmImageWindowType>

