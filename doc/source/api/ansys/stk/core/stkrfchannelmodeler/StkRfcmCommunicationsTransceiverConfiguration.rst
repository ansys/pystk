StkRfcmCommunicationsTransceiverConfiguration
=============================================

.. py:class:: ansys.stk.core.stkrfcm.StkRfcmCommunicationsTransceiverConfiguration

   The transceiver configuration for a communications transceiver.

.. py:currentmodule:: StkRfcmCommunicationsTransceiverConfiguration

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfcm.StkRfcmCommunicationsTransceiverConfiguration.supported_transceivers`
              - Gets an array of available transceiver instances.
            * - :py:attr:`~ansys.stk.core.stkrfcm.StkRfcmCommunicationsTransceiverConfiguration.transceiver`
              - Gets or sets the transceiver.
            * - :py:attr:`~ansys.stk.core.stkrfcm.StkRfcmCommunicationsTransceiverConfiguration.mode`
              - Gets or sets the tranceiver mode.
            * - :py:attr:`~ansys.stk.core.stkrfcm.StkRfcmCommunicationsTransceiverConfiguration.include_parent_object_facets`
              - Gets or sets an indicator of whether or not to include the parent object facets.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkrfcm import StkRfcmCommunicationsTransceiverConfiguration


Property detail
---------------

.. py:property:: supported_transceivers
    :canonical: ansys.stk.core.stkrfcm.StkRfcmCommunicationsTransceiverConfiguration.supported_transceivers
    :type: list

    Gets an array of available transceiver instances.

.. py:property:: transceiver
    :canonical: ansys.stk.core.stkrfcm.StkRfcmCommunicationsTransceiverConfiguration.transceiver
    :type: StkRfcmTransceiver

    Gets or sets the transceiver.

.. py:property:: mode
    :canonical: ansys.stk.core.stkrfcm.StkRfcmCommunicationsTransceiverConfiguration.mode
    :type: RFCM_TRANSCEIVER_MODE

    Gets or sets the tranceiver mode.

.. py:property:: include_parent_object_facets
    :canonical: ansys.stk.core.stkrfcm.StkRfcmCommunicationsTransceiverConfiguration.include_parent_object_facets
    :type: bool

    Gets or sets an indicator of whether or not to include the parent object facets.


