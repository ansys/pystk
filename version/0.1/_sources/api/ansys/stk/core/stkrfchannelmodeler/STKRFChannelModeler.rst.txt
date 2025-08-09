STKRFChannelModeler
===================

.. py:class:: ansys.stk.core.stkrfchannelmodeler.STKRFChannelModeler

   The main RF Channel Modeler object.

.. py:currentmodule:: STKRFChannelModeler

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.STKRFChannelModeler.duplicate_transceiver`
              - Duplicates a transceiver instance.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.STKRFChannelModeler.duplicate_analysis_configuration`
              - Duplicates an analysis configuration instance.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.STKRFChannelModeler.set_gpu_devices`
              - Set the desired GPU device IDs
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.STKRFChannelModeler.construct_analysis`
              - Construct an Analysis for an analysis configuration.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.STKRFChannelModeler.validate_analysis`
              - Validate an analysis configuration.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.STKRFChannelModeler.transceiver_collection`
              - Get the collection of transceiver objects.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.STKRFChannelModeler.analysis_configuration_collection`
              - Get the collection of analysis configurations.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.STKRFChannelModeler.supported_materials`
              - Get the supported tileset materials
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.STKRFChannelModeler.default_materials`
              - Get the default tileset materials
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.STKRFChannelModeler.compute_options`
              - Get the compute options.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.STKRFChannelModeler.supported_gpu_properties_list`
              - Get the GPU properties list.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkrfchannelmodeler import STKRFChannelModeler


Property detail
---------------

.. py:property:: transceiver_collection
    :canonical: ansys.stk.core.stkrfchannelmodeler.STKRFChannelModeler.transceiver_collection
    :type: TransceiverCollection

    Get the collection of transceiver objects.

.. py:property:: analysis_configuration_collection
    :canonical: ansys.stk.core.stkrfchannelmodeler.STKRFChannelModeler.analysis_configuration_collection
    :type: AnalysisConfigurationCollection

    Get the collection of analysis configurations.

.. py:property:: supported_materials
    :canonical: ansys.stk.core.stkrfchannelmodeler.STKRFChannelModeler.supported_materials
    :type: list

    Get the supported tileset materials

.. py:property:: default_materials
    :canonical: ansys.stk.core.stkrfchannelmodeler.STKRFChannelModeler.default_materials
    :type: list

    Get the default tileset materials

.. py:property:: compute_options
    :canonical: ansys.stk.core.stkrfchannelmodeler.STKRFChannelModeler.compute_options
    :type: ComputeOptions

    Get the compute options.

.. py:property:: supported_gpu_properties_list
    :canonical: ansys.stk.core.stkrfchannelmodeler.STKRFChannelModeler.supported_gpu_properties_list
    :type: list

    Get the GPU properties list.


Method detail
-------------



.. py:method:: duplicate_transceiver(self, transceiver: Transceiver) -> Transceiver
    :canonical: ansys.stk.core.stkrfchannelmodeler.STKRFChannelModeler.duplicate_transceiver

    Duplicates a transceiver instance.

    :Parameters:

        **transceiver** : :obj:`~Transceiver`


    :Returns:

        :obj:`~Transceiver`

.. py:method:: duplicate_analysis_configuration(self, analysis_configuration: AnalysisConfiguration) -> AnalysisConfiguration
    :canonical: ansys.stk.core.stkrfchannelmodeler.STKRFChannelModeler.duplicate_analysis_configuration

    Duplicates an analysis configuration instance.

    :Parameters:

        **analysis_configuration** : :obj:`~AnalysisConfiguration`


    :Returns:

        :obj:`~AnalysisConfiguration`





.. py:method:: set_gpu_devices(self, gpu_device_ids: list) -> None
    :canonical: ansys.stk.core.stkrfchannelmodeler.STKRFChannelModeler.set_gpu_devices

    Set the desired GPU device IDs

    :Parameters:

        **gpu_device_ids** : :obj:`~list`


    :Returns:

        :obj:`~None`

.. py:method:: construct_analysis(self, analysis_configuration_name: str) -> Analysis
    :canonical: ansys.stk.core.stkrfchannelmodeler.STKRFChannelModeler.construct_analysis

    Construct an Analysis for an analysis configuration.

    :Parameters:

        **analysis_configuration_name** : :obj:`~str`


    :Returns:

        :obj:`~Analysis`

.. py:method:: validate_analysis(self, analysis_configuration_name: str) -> ValidationResponse
    :canonical: ansys.stk.core.stkrfchannelmodeler.STKRFChannelModeler.validate_analysis

    Validate an analysis configuration.

    :Parameters:

        **analysis_configuration_name** : :obj:`~str`


    :Returns:

        :obj:`~ValidationResponse`

