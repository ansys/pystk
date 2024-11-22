IStkRfcmRadarAnalysisConfigurationModel
=======================================

.. py:class:: ansys.stk.core.stkrfcm.IStkRfcmRadarAnalysisConfigurationModel

   Properties for an analysis configuration model for a radar analysis. This contains a collection of the transceiver configurations belonging to the radar analysis.

.. py:currentmodule:: IStkRfcmRadarAnalysisConfigurationModel

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfcm.IStkRfcmRadarAnalysisConfigurationModel.duplicate_transceiver_configuration`
              - Duplicates a transceiver configuration instance.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfcm.IStkRfcmRadarAnalysisConfigurationModel.transceiver_configuration_collection`
              - Gets the collection of transceiver configurations.
            * - :py:attr:`~ansys.stk.core.stkrfcm.IStkRfcmRadarAnalysisConfigurationModel.imaging_data_product_list`
              - Gets the imaging product list.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkrfcm import IStkRfcmRadarAnalysisConfigurationModel


Property detail
---------------

.. py:property:: transceiver_configuration_collection
    :canonical: ansys.stk.core.stkrfcm.IStkRfcmRadarAnalysisConfigurationModel.transceiver_configuration_collection
    :type: StkRfcmRadarTransceiverConfigurationCollection

    Gets the collection of transceiver configurations.

.. py:property:: imaging_data_product_list
    :canonical: ansys.stk.core.stkrfcm.IStkRfcmRadarAnalysisConfigurationModel.imaging_data_product_list
    :type: list

    Gets the imaging product list.


Method detail
-------------

.. py:method:: duplicate_transceiver_configuration(self, transceiver_configuration: StkRfcmRadarTransceiverConfiguration) -> StkRfcmRadarTransceiverConfiguration
    :canonical: ansys.stk.core.stkrfcm.IStkRfcmRadarAnalysisConfigurationModel.duplicate_transceiver_configuration

    Duplicates a transceiver configuration instance.

    :Parameters:

    **transceiver_configuration** : :obj:`~StkRfcmRadarTransceiverConfiguration`

    :Returns:

        :obj:`~StkRfcmRadarTransceiverConfiguration`



