
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


            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.IAnalysisConfigurationModel`
              - Base interface for all analysis configuration models.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.IAnalysisLink`
              - Properties for a transceiver link for an analysis.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.IAntenna`
              - Base interface for a transceiver antenna model.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.IProgressTrackCancel`
              - Control for progress tracker.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.IRadarAnalysisConfigurationModel`
              - Properties for an analysis configuration model for a radar analysis. This contains a collection of the transceiver configurations belonging to the radar analysis.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.IResponse`
              - Properties and data for a channel characaterization response.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.ISceneContributorCollection`
              - Represents a collection of scene contributors.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.ITransceiverModel`
              - Base interface which defines common properties for a transceiver model.


    .. tab-item:: Classes

        .. list-table::
            :header-rows: 0
            :widths: auto


            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.Analysis`
              - An RF Channel Modeler analysis.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.AnalysisConfiguration`
              - The configuration for an analysis.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.AnalysisConfigurationCollection`
              - A collection of analysis configurations.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.AnalysisLink`
              - A transceiver link for an analysis.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.AnalysisLinkCollection`
              - A collection of links between transceivers.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.CommunicationsAnalysisConfigurationModel`
              - The analysis configuration model for a communications analysis. This contains a collection of the transceiver configurations belonging to the communications analysis.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.CommunicationsTransceiverConfiguration`
              - The transceiver configuration for a communications transceiver.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.CommunicationsTransceiverConfigurationCollection`
              - A collection of communication transceivers.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.CommunicationsTransceiverModel`
              - The model for a communications transceiver.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.CommunicationsWaveform`
              - The waveform settings of a communications transceiver.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.ComputeOptions`
              - The options for computing RF Channel Modeler.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.ElementExportPatternAntenna`
              - The antenna settings for an element export pattern antenna.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.Extent`
              - The extent in which the channel characterizations will be computed.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.FacetTileset`
              - The facet tileset information.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.FacetTilesetCollection`
              - A collection of facet tilesets.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.FarFieldDataPatternAntenna`
              - The antenna settings for a far field data pattern antenna.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.FrequencyPulseResponse`
              - The response data and properties for a frequency pulse channel characterization.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.GpuProperties`
              - The properties of a GPU pertaining to RF Channel Modeler.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.Material`
              - A material for scene contributors.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.ParametricBeamAntenna`
              - The antenna settings for a parametric beam antenna.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProduct`
              - Imaging data product that facilitates the generation of range doppler radar images.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.RadarImagingDataProductCollection`
              - A collection of radar transceivers.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.RadarISarAnalysisConfigurationModel`
              - The analysis configuration model for an ISar analysis. This contains a collection of the transceiver configurations belonging to the ISar analysis.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.RadarISarAnalysisLink`
              - A transceiver link for an ISar analysis.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.RadarSarAnalysisConfigurationModel`
              - The analysis configuration model for a Sar analysis. This contains a collection of the transceiver configurations belonging to the Sar analysis.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.RadarSarAnalysisLink`
              - A transceiver link for a Sar analysis.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.RadarSarImageLocation`
              - The image location information for use by a range doppler Sar analysis.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.RadarSarImageLocationCollection`
              - A collection of image location information.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.RadarTargetCollection`
              - A collection of radar target objects.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.RadarTransceiverConfiguration`
              - The transceiver configuration for a radar transceiver.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.RadarTransceiverConfigurationCollection`
              - A collection of radar transceivers.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.RadarTransceiverModel`
              - The model for a radar transceiver.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.RadarWaveform`
              - The waveform settings of a radar transceiver.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.RangeDopplerResponse`
              - The response data and properties for a range doppler channel characterization.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.SceneContributor`
              - A scene contributor object.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.SceneContributorCollection`
              - A collection of scene contributor objects.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.STKRFChannelModeler`
              - The main RF Channel Modeler object.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.Transceiver`
              - The transceiver object and its settings.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.TransceiverCollection`
              - A collection of transceiver objects.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.ValidationResponse`
              - The response from validating an analysis configuration.


    .. tab-item:: Enums

        .. list-table::
            :header-rows: 0
            :widths: auto


            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.AnalysisConfigurationComputeStepMode`
              - Analysis configuration compute step mode.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.AnalysisConfigurationModelType`
              - Analysis Configuration Model Type

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.AnalysisResultsFileMode`
              - Analysis results file mode.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.AnalysisSolverBoundingBoxMode`
              - Analysis solver bounding box mode.

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.ChannelResponseType`
              - Channel Response Type

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.ImageWindowType`
              - Polarization Type

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.PolarizationType`
              - Polarization Type

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.TransceiverMode`
              - Transceiver Mode

            * - :py:class:`~ansys.stk.core.stkrfchannelmodeler.TransceiverModelType`
              - Transceiver Model Type



Description
-----------

Object Model components specifically designed to support STK RF Channel Modeler.


.. py:currentmodule:: ansys.stk.core.stkrfchannelmodeler


.. TABLE OF CONTENTS

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     IAnalysisConfigurationModel<stkrfchannelmodeler/IAnalysisConfigurationModel>
     IAnalysisLink<stkrfchannelmodeler/IAnalysisLink>
     IAntenna<stkrfchannelmodeler/IAntenna>
     IProgressTrackCancel<stkrfchannelmodeler/IProgressTrackCancel>
     IRadarAnalysisConfigurationModel<stkrfchannelmodeler/IRadarAnalysisConfigurationModel>
     IResponse<stkrfchannelmodeler/IResponse>
     ISceneContributorCollection<stkrfchannelmodeler/ISceneContributorCollection>
     ITransceiverModel<stkrfchannelmodeler/ITransceiverModel>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     Analysis<stkrfchannelmodeler/Analysis>
     AnalysisConfiguration<stkrfchannelmodeler/AnalysisConfiguration>
     AnalysisConfigurationCollection<stkrfchannelmodeler/AnalysisConfigurationCollection>
     AnalysisLink<stkrfchannelmodeler/AnalysisLink>
     AnalysisLinkCollection<stkrfchannelmodeler/AnalysisLinkCollection>
     CommunicationsAnalysisConfigurationModel<stkrfchannelmodeler/CommunicationsAnalysisConfigurationModel>
     CommunicationsTransceiverConfiguration<stkrfchannelmodeler/CommunicationsTransceiverConfiguration>
     CommunicationsTransceiverConfigurationCollection<stkrfchannelmodeler/CommunicationsTransceiverConfigurationCollection>
     CommunicationsTransceiverModel<stkrfchannelmodeler/CommunicationsTransceiverModel>
     CommunicationsWaveform<stkrfchannelmodeler/CommunicationsWaveform>
     ComputeOptions<stkrfchannelmodeler/ComputeOptions>
     ElementExportPatternAntenna<stkrfchannelmodeler/ElementExportPatternAntenna>
     Extent<stkrfchannelmodeler/Extent>
     FacetTileset<stkrfchannelmodeler/FacetTileset>
     FacetTilesetCollection<stkrfchannelmodeler/FacetTilesetCollection>
     FarFieldDataPatternAntenna<stkrfchannelmodeler/FarFieldDataPatternAntenna>
     FrequencyPulseResponse<stkrfchannelmodeler/FrequencyPulseResponse>
     GpuProperties<stkrfchannelmodeler/GpuProperties>
     Material<stkrfchannelmodeler/Material>
     ParametricBeamAntenna<stkrfchannelmodeler/ParametricBeamAntenna>
     RadarImagingDataProduct<stkrfchannelmodeler/RadarImagingDataProduct>
     RadarImagingDataProductCollection<stkrfchannelmodeler/RadarImagingDataProductCollection>
     RadarISarAnalysisConfigurationModel<stkrfchannelmodeler/RadarISarAnalysisConfigurationModel>
     RadarISarAnalysisLink<stkrfchannelmodeler/RadarISarAnalysisLink>
     RadarSarAnalysisConfigurationModel<stkrfchannelmodeler/RadarSarAnalysisConfigurationModel>
     RadarSarAnalysisLink<stkrfchannelmodeler/RadarSarAnalysisLink>
     RadarSarImageLocation<stkrfchannelmodeler/RadarSarImageLocation>
     RadarSarImageLocationCollection<stkrfchannelmodeler/RadarSarImageLocationCollection>
     RadarTargetCollection<stkrfchannelmodeler/RadarTargetCollection>
     RadarTransceiverConfiguration<stkrfchannelmodeler/RadarTransceiverConfiguration>
     RadarTransceiverConfigurationCollection<stkrfchannelmodeler/RadarTransceiverConfigurationCollection>
     RadarTransceiverModel<stkrfchannelmodeler/RadarTransceiverModel>
     RadarWaveform<stkrfchannelmodeler/RadarWaveform>
     RangeDopplerResponse<stkrfchannelmodeler/RangeDopplerResponse>
     SceneContributor<stkrfchannelmodeler/SceneContributor>
     SceneContributorCollection<stkrfchannelmodeler/SceneContributorCollection>
     STKRFChannelModeler<stkrfchannelmodeler/STKRFChannelModeler>
     Transceiver<stkrfchannelmodeler/Transceiver>
     TransceiverCollection<stkrfchannelmodeler/TransceiverCollection>
     ValidationResponse<stkrfchannelmodeler/ValidationResponse>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    ≔ AnalysisConfigurationComputeStepMode<stkrfchannelmodeler/AnalysisConfigurationComputeStepMode>
    ≔ AnalysisConfigurationModelType<stkrfchannelmodeler/AnalysisConfigurationModelType>
    ≔ AnalysisResultsFileMode<stkrfchannelmodeler/AnalysisResultsFileMode>
    ≔ AnalysisSolverBoundingBoxMode<stkrfchannelmodeler/AnalysisSolverBoundingBoxMode>
    ≔ ChannelResponseType<stkrfchannelmodeler/ChannelResponseType>
    ≔ ImageWindowType<stkrfchannelmodeler/ImageWindowType>
    ≔ PolarizationType<stkrfchannelmodeler/PolarizationType>
    ≔ TransceiverMode<stkrfchannelmodeler/TransceiverMode>
    ≔ TransceiverModelType<stkrfchannelmodeler/TransceiverModelType>

