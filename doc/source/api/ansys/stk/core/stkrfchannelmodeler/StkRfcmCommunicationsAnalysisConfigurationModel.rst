StkRfcmCommunicationsAnalysisConfigurationModel
===============================================

.. py:class:: ansys.stk.core.stkrfcm.StkRfcmCommunicationsAnalysisConfigurationModel

   Bases: :py:class:`~ansys.stk.core.stkrfcm.IStkRfcmAnalysisConfigurationModel`

   The analysis configuration model for a communications analysis. This contains a collection of the transceiver configurations belonging to the communications analysis.

.. py:currentmodule:: StkRfcmCommunicationsAnalysisConfigurationModel

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfcm.StkRfcmCommunicationsAnalysisConfigurationModel.duplicate_transceiver_configuration`
              - Duplicates a transceiver configuration instance.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfcm.StkRfcmCommunicationsAnalysisConfigurationModel.transceiver_configuration_collection`
              - Gets the collection of transceiver configurations.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkrfcm import StkRfcmCommunicationsAnalysisConfigurationModel


Property detail
---------------

.. py:property:: transceiver_configuration_collection
    :canonical: ansys.stk.core.stkrfcm.StkRfcmCommunicationsAnalysisConfigurationModel.transceiver_configuration_collection
    :type: StkRfcmCommunicationsTransceiverConfigurationCollection

    Gets the collection of transceiver configurations.


Method detail
-------------

.. py:method:: duplicate_transceiver_configuration(self, transceiver_configuration: StkRfcmCommunicationsTransceiverConfiguration) -> StkRfcmCommunicationsTransceiverConfiguration
    :canonical: ansys.stk.core.stkrfcm.StkRfcmCommunicationsAnalysisConfigurationModel.duplicate_transceiver_configuration

    Duplicates a transceiver configuration instance.

    :Parameters:

    **transceiver_configuration** : :obj:`~StkRfcmCommunicationsTransceiverConfiguration`

    :Returns:

        :obj:`~StkRfcmCommunicationsTransceiverConfiguration`


