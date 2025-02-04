
The ``rfcm`` module
===================


.. py:module:: ansys.stk.core.rfcm


Summary
-------

.. tab-set::

 
    .. tab-item:: Interfaces

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~ansys.stk.core.rfcm.IStkRfcmProgressTrackCancel`
              - Control for progress tracker.

            * - :py:class:`~ansys.stk.core.rfcm.IStkRfcmAntenna`
              - Base interface for a transceiver antenna model.

            * - :py:class:`~ansys.stk.core.rfcm.IStkRfcmTransceiverModel`
              - Base interface which defines common properties for a transceiver model.

            * - :py:class:`~ansys.stk.core.rfcm.IStkRfcmSceneContributorCollection`
              - Represents a collection of scene contributors.

            * - :py:class:`~ansys.stk.core.rfcm.IStkRfcmResponse`
              - Properties and data for a channel characaterization response.

            * - :py:class:`~ansys.stk.core.rfcm.IStkRfcmAnalysisLink`
              - Properties for a transceiver link for an analysis.

            * - :py:class:`~ansys.stk.core.rfcm.IStkRfcmAnalysisConfigurationModel`
              - Base interface for all analysis configuration models.

            * - :py:class:`~ansys.stk.core.rfcm.IStkRfcmRadarAnalysisConfigurationModel`
              - Properties for an analysis configuration model for a radar analysis. This contains a collection of the transceiver configurations belonging to the radar analysis.

    
    .. tab-item:: Classes

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~ansys.stk.core.rfcm.StkRfcmRadarImagingDataProduct`
              - Imaging data product that facilitates the generation of range doppler radar images.

            * - :py:class:`~ansys.stk.core.rfcm.StkRfcmMaterial`
              - A material for scene contributors.

            * - :py:class:`~ansys.stk.core.rfcm.StkRfcmFacetTileset`
              - The facet tileset information.

            * - :py:class:`~ansys.stk.core.rfcm.StkRfcmValidationResponse`
              - The response from validating an analysis configuration.

            * - :py:class:`~ansys.stk.core.rfcm.StkRfcmExtent`
              - The extent in which the channel characterizations will be computed.

            * - :py:class:`~ansys.stk.core.rfcm.StkRfcmCommunicationsWaveform`
              - The waveform settings of a communications transceiver.

            * - :py:class:`~ansys.stk.core.rfcm.StkRfcmRadarWaveform`
              - The waveform settings of a radar transceiver.

            * - :py:class:`~ansys.stk.core.rfcm.StkRfcmParametricBeamAntenna`
              - The antenna settings for a parametric beam antenna.

            * - :py:class:`~ansys.stk.core.rfcm.StkRfcmElementExportPatternAntenna`
              - The antenna settings for an element export pattern antenna.

            * - :py:class:`~ansys.stk.core.rfcm.StkRfcmFarFieldDataPatternAntenna`
              - The antenna settings for a far field data pattern antenna.

            * - :py:class:`~ansys.stk.core.rfcm.StkRfcmTransceiver`
              - The transceiver object and its settings.

            * - :py:class:`~ansys.stk.core.rfcm.StkRfcmCommunicationsTransceiverConfiguration`
              - The transceiver configuration for a communications transceiver.

            * - :py:class:`~ansys.stk.core.rfcm.StkRfcmRadarTransceiverConfiguration`
              - The transceiver configuration for a radar transceiver.

            * - :py:class:`~ansys.stk.core.rfcm.StkRfcmRadarImagingDataProductCollection`
              - A collection of radar transceivers.

            * - :py:class:`~ansys.stk.core.rfcm.StkRfcmRadarTransceiverConfigurationCollection`
              - A collection of radar transceivers.

            * - :py:class:`~ansys.stk.core.rfcm.StkRfcmAnalysisConfiguration`
              - The configuration for an analysis.

            * - :py:class:`~ansys.stk.core.rfcm.StkRfcmCommunicationsAnalysisConfigurationModel`
              - The analysis configuration model for a communications analysis. This contains a collection of the transceiver configurations belonging to the communications analysis.

            * - :py:class:`~ansys.stk.core.rfcm.StkRfcmRadarISarAnalysisConfigurationModel`
              - The analysis configuration model for an ISar analysis. This contains a collection of the transceiver configurations belonging to the ISar analysis.

            * - :py:class:`~ansys.stk.core.rfcm.StkRfcmRadarSarAnalysisConfigurationModel`
              - The analysis configuration model for a Sar analysis. This contains a collection of the transceiver configurations belonging to the Sar analysis.

            * - :py:class:`~ansys.stk.core.rfcm.StkRfcmTransceiverCollection`
              - A collection of transceiver objects.

            * - :py:class:`~ansys.stk.core.rfcm.StkRfcmFacetTilesetCollection`
              - A collection of facet tilesets.

            * - :py:class:`~ansys.stk.core.rfcm.StkRfcmSceneContributor`
              - A scene contributor object.

            * - :py:class:`~ansys.stk.core.rfcm.StkRfcmSceneContributorCollection`
              - A collection of scene contributor objects.

            * - :py:class:`~ansys.stk.core.rfcm.StkRfcmRadarTargetCollection`
              - A collection of radar target objects.

            * - :py:class:`~ansys.stk.core.rfcm.StkRfcmRadarSarImageLocation`
              - The image location information for use by a range doppler Sar analysis.

            * - :py:class:`~ansys.stk.core.rfcm.StkRfcmRadarSarImageLocationCollection`
              - A collection of image location information.

            * - :py:class:`~ansys.stk.core.rfcm.StkRfcmCommunicationsTransceiverConfigurationCollection`
              - A collection of communication transceivers.

            * - :py:class:`~ansys.stk.core.rfcm.StkRfcmAnalysisConfigurationCollection`
              - A collection of analysis configurations.

            * - :py:class:`~ansys.stk.core.rfcm.StkRfcmComputeOptions`
              - The options for computing RF Channel Modeler.

            * - :py:class:`~ansys.stk.core.rfcm.StkRFChannelModeler`
              - The main RF Channel Modeler object.

            * - :py:class:`~ansys.stk.core.rfcm.StkRfcmCommunicationsTransceiverModel`
              - The model for a communications transceiver.

            * - :py:class:`~ansys.stk.core.rfcm.StkRfcmRadarTransceiverModel`
              - The model for a radar transceiver.

            * - :py:class:`~ansys.stk.core.rfcm.StkRfcmRangeDopplerResponse`
              - The response data and properties for a range doppler channel characterization.

            * - :py:class:`~ansys.stk.core.rfcm.StkRfcmFrequencyPulseResponse`
              - The response data and properties for a frequency pulse channel characterization.

            * - :py:class:`~ansys.stk.core.rfcm.StkRfcmAnalysisLink`
              - A transceiver link for an analysis.

            * - :py:class:`~ansys.stk.core.rfcm.StkRfcmRadarSarAnalysisLink`
              - A transceiver link for a Sar analysis.

            * - :py:class:`~ansys.stk.core.rfcm.StkRfcmRadarISarAnalysisLink`
              - A transceiver link for an ISar analysis.

            * - :py:class:`~ansys.stk.core.rfcm.StkRfcmAnalysisLinkCollection`
              - A collection of links between transceivers.

            * - :py:class:`~ansys.stk.core.rfcm.StkRfcmAnalysis`
              - An RF Channel Modeler analysis.

            * - :py:class:`~ansys.stk.core.rfcm.StkRfcmGpuProperties`
              - The properties of a GPU pertaining to RF Channel Modeler.


    .. tab-item:: Enums

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~ansys.stk.core.rfcm.RfcmChannelResponseType`
              - Channel Response Type

            * - :py:class:`~ansys.stk.core.rfcm.RfcmAnalysisConfigurationModelType`
              - Analysis Configuration Model Type

            * - :py:class:`~ansys.stk.core.rfcm.RfcmTransceiverMode`
              - Transceiver Mode

            * - :py:class:`~ansys.stk.core.rfcm.RfcmAnalysisConfigurationComputeStepMode`
              - Analysis configuration compute step mode.

            * - :py:class:`~ansys.stk.core.rfcm.RfcmAnalysisResultsFileMode`
              - Analysis results file mode.

            * - :py:class:`~ansys.stk.core.rfcm.RfcmAnalysisSolverBoundingBoxMode`
              - Analysis solver bounding box mode.

            * - :py:class:`~ansys.stk.core.rfcm.RfcmTransceiverModelType`
              - Transceiver Model Type

            * - :py:class:`~ansys.stk.core.rfcm.RfcmPolarizationType`
              - Polarization Type

            * - :py:class:`~ansys.stk.core.rfcm.RfcmImageWindowType`
              - Polarization Type



Description
-----------

Object Model components specifically designed to support STK RF Channel Modeler.


.. py:currentmodule:: ansys.stk.core.rfcm


.. TABLE OF CONTENTS

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     IStkRfcmProgressTrackCancel<rfcm/IStkRfcmProgressTrackCancel>
     IStkRfcmAntenna<rfcm/IStkRfcmAntenna>
     IStkRfcmTransceiverModel<rfcm/IStkRfcmTransceiverModel>
     IStkRfcmSceneContributorCollection<rfcm/IStkRfcmSceneContributorCollection>
     IStkRfcmResponse<rfcm/IStkRfcmResponse>
     IStkRfcmAnalysisLink<rfcm/IStkRfcmAnalysisLink>
     IStkRfcmAnalysisConfigurationModel<rfcm/IStkRfcmAnalysisConfigurationModel>
     IStkRfcmRadarAnalysisConfigurationModel<rfcm/IStkRfcmRadarAnalysisConfigurationModel>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     StkRfcmRadarImagingDataProduct<rfcm/StkRfcmRadarImagingDataProduct>
     StkRfcmMaterial<rfcm/StkRfcmMaterial>
     StkRfcmFacetTileset<rfcm/StkRfcmFacetTileset>
     StkRfcmValidationResponse<rfcm/StkRfcmValidationResponse>
     StkRfcmExtent<rfcm/StkRfcmExtent>
     StkRfcmCommunicationsWaveform<rfcm/StkRfcmCommunicationsWaveform>
     StkRfcmRadarWaveform<rfcm/StkRfcmRadarWaveform>
     StkRfcmParametricBeamAntenna<rfcm/StkRfcmParametricBeamAntenna>
     StkRfcmElementExportPatternAntenna<rfcm/StkRfcmElementExportPatternAntenna>
     StkRfcmFarFieldDataPatternAntenna<rfcm/StkRfcmFarFieldDataPatternAntenna>
     StkRfcmTransceiver<rfcm/StkRfcmTransceiver>
     StkRfcmCommunicationsTransceiverConfiguration<rfcm/StkRfcmCommunicationsTransceiverConfiguration>
     StkRfcmRadarTransceiverConfiguration<rfcm/StkRfcmRadarTransceiverConfiguration>
     StkRfcmRadarImagingDataProductCollection<rfcm/StkRfcmRadarImagingDataProductCollection>
     StkRfcmRadarTransceiverConfigurationCollection<rfcm/StkRfcmRadarTransceiverConfigurationCollection>
     StkRfcmAnalysisConfiguration<rfcm/StkRfcmAnalysisConfiguration>
     StkRfcmCommunicationsAnalysisConfigurationModel<rfcm/StkRfcmCommunicationsAnalysisConfigurationModel>
     StkRfcmRadarISarAnalysisConfigurationModel<rfcm/StkRfcmRadarISarAnalysisConfigurationModel>
     StkRfcmRadarSarAnalysisConfigurationModel<rfcm/StkRfcmRadarSarAnalysisConfigurationModel>
     StkRfcmTransceiverCollection<rfcm/StkRfcmTransceiverCollection>
     StkRfcmFacetTilesetCollection<rfcm/StkRfcmFacetTilesetCollection>
     StkRfcmSceneContributor<rfcm/StkRfcmSceneContributor>
     StkRfcmSceneContributorCollection<rfcm/StkRfcmSceneContributorCollection>
     StkRfcmRadarTargetCollection<rfcm/StkRfcmRadarTargetCollection>
     StkRfcmRadarSarImageLocation<rfcm/StkRfcmRadarSarImageLocation>
     StkRfcmRadarSarImageLocationCollection<rfcm/StkRfcmRadarSarImageLocationCollection>
     StkRfcmCommunicationsTransceiverConfigurationCollection<rfcm/StkRfcmCommunicationsTransceiverConfigurationCollection>
     StkRfcmAnalysisConfigurationCollection<rfcm/StkRfcmAnalysisConfigurationCollection>
     StkRfcmComputeOptions<rfcm/StkRfcmComputeOptions>
     StkRFChannelModeler<rfcm/StkRFChannelModeler>
     StkRfcmCommunicationsTransceiverModel<rfcm/StkRfcmCommunicationsTransceiverModel>
     StkRfcmRadarTransceiverModel<rfcm/StkRfcmRadarTransceiverModel>
     StkRfcmRangeDopplerResponse<rfcm/StkRfcmRangeDopplerResponse>
     StkRfcmFrequencyPulseResponse<rfcm/StkRfcmFrequencyPulseResponse>
     StkRfcmAnalysisLink<rfcm/StkRfcmAnalysisLink>
     StkRfcmRadarSarAnalysisLink<rfcm/StkRfcmRadarSarAnalysisLink>
     StkRfcmRadarISarAnalysisLink<rfcm/StkRfcmRadarISarAnalysisLink>
     StkRfcmAnalysisLinkCollection<rfcm/StkRfcmAnalysisLinkCollection>
     StkRfcmAnalysis<rfcm/StkRfcmAnalysis>
     StkRfcmGpuProperties<rfcm/StkRfcmGpuProperties>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    ≔ RfcmChannelResponseType<rfcm/RfcmChannelResponseType>
    ≔ RfcmAnalysisConfigurationModelType<rfcm/RfcmAnalysisConfigurationModelType>
    ≔ RfcmTransceiverMode<rfcm/RfcmTransceiverMode>
    ≔ RfcmAnalysisConfigurationComputeStepMode<rfcm/RfcmAnalysisConfigurationComputeStepMode>
    ≔ RfcmAnalysisResultsFileMode<rfcm/RfcmAnalysisResultsFileMode>
    ≔ RfcmAnalysisSolverBoundingBoxMode<rfcm/RfcmAnalysisSolverBoundingBoxMode>
    ≔ RfcmTransceiverModelType<rfcm/RfcmTransceiverModelType>
    ≔ RfcmPolarizationType<rfcm/RfcmPolarizationType>
    ≔ RfcmImageWindowType<rfcm/RfcmImageWindowType>

