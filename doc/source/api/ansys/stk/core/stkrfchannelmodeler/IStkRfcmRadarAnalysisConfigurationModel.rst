IStkRfcmRadarAnalysisConfigurationModel
=======================================

.. py:class:: ansys.stk.core.stkrfchannelmodeler.IStkRfcmRadarAnalysisConfigurationModel

   Properties for an analysis configuration model for a radar analysis. This contains a collection of the transceiver configurations belonging to the radar analysis.

.. py:currentmodule:: IStkRfcmRadarAnalysisConfigurationModel

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IStkRfcmRadarAnalysisConfigurationModel.transceiver_configuration_collection`
              - Gets the collection of transceiver configurations.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IStkRfcmRadarAnalysisConfigurationModel.imaging_data_product_list`
              - Gets the imaging product list.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkrfchannelmodeler import IStkRfcmRadarAnalysisConfigurationModel


Property detail
---------------

.. py:property:: transceiver_configuration_collection
    :canonical: ansys.stk.core.stkrfchannelmodeler.IStkRfcmRadarAnalysisConfigurationModel.transceiver_configuration_collection
    :type: StkRfcmRadarTransceiverConfigurationCollection

    Gets the collection of transceiver configurations.

.. py:property:: imaging_data_product_list
    :canonical: ansys.stk.core.stkrfchannelmodeler.IStkRfcmRadarAnalysisConfigurationModel.imaging_data_product_list
    :type: StkRfcmRadarImagingDataProductCollection

    Gets the imaging product list.


