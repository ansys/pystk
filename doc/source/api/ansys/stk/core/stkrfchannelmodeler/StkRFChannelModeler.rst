StkRFChannelModeler
===================

.. py:class:: ansys.stk.core.stkrfcm.StkRFChannelModeler

   The main RF Channel Modeler object.

.. py:currentmodule:: StkRFChannelModeler

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfcm.StkRFChannelModeler.duplicate_transceiver`
              - Duplicates a transceiver instance.
            * - :py:attr:`~ansys.stk.core.stkrfcm.StkRFChannelModeler.duplicate_analysis_configuration`
              - Duplicates an analysis configuration instance.
            * - :py:attr:`~ansys.stk.core.stkrfcm.StkRFChannelModeler.set_gpu_devices`
              - Set the desired GPU device IDs
            * - :py:attr:`~ansys.stk.core.stkrfcm.StkRFChannelModeler.construct_analysis`
              - Construct an Analysis for an analysis configuration.
            * - :py:attr:`~ansys.stk.core.stkrfcm.StkRFChannelModeler.validate_analysis`
              - Validate an analysis configuration.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfcm.StkRFChannelModeler.transceiver_collection`
              - Gets the collection of transceiver objects.
            * - :py:attr:`~ansys.stk.core.stkrfcm.StkRFChannelModeler.analysis_configuration_collection`
              - Gets the collection of analysis configurations.
            * - :py:attr:`~ansys.stk.core.stkrfcm.StkRFChannelModeler.supported_materials`
              - Gets the supported tileset materials
            * - :py:attr:`~ansys.stk.core.stkrfcm.StkRFChannelModeler.default_materials`
              - Gets the default tileset materials
            * - :py:attr:`~ansys.stk.core.stkrfcm.StkRFChannelModeler.compute_options`
              - Gets the compute options.
            * - :py:attr:`~ansys.stk.core.stkrfcm.StkRFChannelModeler.supported_gpu_properties_list`
              - Gets the GPU properties list.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkrfcm import StkRFChannelModeler


Property detail
---------------

.. py:property:: transceiver_collection
    :canonical: ansys.stk.core.stkrfcm.StkRFChannelModeler.transceiver_collection
    :type: StkRfcmTransceiverCollection

    Gets the collection of transceiver objects.

.. py:property:: analysis_configuration_collection
    :canonical: ansys.stk.core.stkrfcm.StkRFChannelModeler.analysis_configuration_collection
    :type: StkRfcmAnalysisConfigurationCollection

    Gets the collection of analysis configurations.

.. py:property:: supported_materials
    :canonical: ansys.stk.core.stkrfcm.StkRFChannelModeler.supported_materials
    :type: list

    Gets the supported tileset materials

.. py:property:: default_materials
    :canonical: ansys.stk.core.stkrfcm.StkRFChannelModeler.default_materials
    :type: list

    Gets the default tileset materials

.. py:property:: compute_options
    :canonical: ansys.stk.core.stkrfcm.StkRFChannelModeler.compute_options
    :type: StkRfcmComputeOptions

    Gets the compute options.

.. py:property:: supported_gpu_properties_list
    :canonical: ansys.stk.core.stkrfcm.StkRFChannelModeler.supported_gpu_properties_list
    :type: list

    Gets the GPU properties list.


Method detail
-------------



.. py:method:: duplicate_transceiver(self, transceiver: StkRfcmTransceiver) -> StkRfcmTransceiver
    :canonical: ansys.stk.core.stkrfcm.StkRFChannelModeler.duplicate_transceiver

    Duplicates a transceiver instance.

    :Parameters:

    **transceiver** : :obj:`~StkRfcmTransceiver`

    :Returns:

        :obj:`~StkRfcmTransceiver`

.. py:method:: duplicate_analysis_configuration(self, analysis_configuration: StkRfcmAnalysisConfiguration) -> StkRfcmAnalysisConfiguration
    :canonical: ansys.stk.core.stkrfcm.StkRFChannelModeler.duplicate_analysis_configuration

    Duplicates an analysis configuration instance.

    :Parameters:

    **analysis_configuration** : :obj:`~StkRfcmAnalysisConfiguration`

    :Returns:

        :obj:`~StkRfcmAnalysisConfiguration`





.. py:method:: set_gpu_devices(self, gpu_device_ids: list) -> None
    :canonical: ansys.stk.core.stkrfcm.StkRFChannelModeler.set_gpu_devices

    Set the desired GPU device IDs

    :Parameters:

    **gpu_device_ids** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: construct_analysis(self, analysis_configuration_name: str) -> StkRfcmAnalysis
    :canonical: ansys.stk.core.stkrfcm.StkRFChannelModeler.construct_analysis

    Construct an Analysis for an analysis configuration.

    :Parameters:

    **analysis_configuration_name** : :obj:`~str`

    :Returns:

        :obj:`~StkRfcmAnalysis`

.. py:method:: validate_analysis(self, analysis_configuration_name: str) -> StkRfcmValidationResponse
    :canonical: ansys.stk.core.stkrfcm.StkRFChannelModeler.validate_analysis

    Validate an analysis configuration.

    :Parameters:

    **analysis_configuration_name** : :obj:`~str`

    :Returns:

        :obj:`~StkRfcmValidationResponse`

