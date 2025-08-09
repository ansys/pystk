IRadarAnalysisConfigurationModel
================================

.. py:class:: ansys.stk.core.stkrfchannelmodeler.IRadarAnalysisConfigurationModel

   Properties for an analysis configuration model for a radar analysis. This contains a collection of the transceiver configurations belonging to the radar analysis.

.. py:currentmodule:: IRadarAnalysisConfigurationModel

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IRadarAnalysisConfigurationModel.transceiver_configuration_collection`
              - Get the collection of transceiver configurations.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IRadarAnalysisConfigurationModel.imaging_data_product_list`
              - Get the imaging product list.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkrfchannelmodeler import IRadarAnalysisConfigurationModel


Property detail
---------------

.. py:property:: transceiver_configuration_collection
    :canonical: ansys.stk.core.stkrfchannelmodeler.IRadarAnalysisConfigurationModel.transceiver_configuration_collection
    :type: RadarTransceiverConfigurationCollection

    Get the collection of transceiver configurations.

.. py:property:: imaging_data_product_list
    :canonical: ansys.stk.core.stkrfchannelmodeler.IRadarAnalysisConfigurationModel.imaging_data_product_list
    :type: RadarImagingDataProductCollection

    Get the imaging product list.


