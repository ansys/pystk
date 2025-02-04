StkRfcmCommunicationsTransceiverConfiguration
=============================================

.. py:class:: ansys.stk.core.rfcm.StkRfcmCommunicationsTransceiverConfiguration

   The transceiver configuration for a communications transceiver.

.. py:currentmodule:: StkRfcmCommunicationsTransceiverConfiguration

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.rfcm.StkRfcmCommunicationsTransceiverConfiguration.supported_transceivers`
              - Gets an array of available transceiver instances.
            * - :py:attr:`~ansys.stk.core.rfcm.StkRfcmCommunicationsTransceiverConfiguration.transceiver`
              - Gets or sets the transceiver.
            * - :py:attr:`~ansys.stk.core.rfcm.StkRfcmCommunicationsTransceiverConfiguration.mode`
              - Gets or sets the transceiver mode.
            * - :py:attr:`~ansys.stk.core.rfcm.StkRfcmCommunicationsTransceiverConfiguration.include_parent_object_facets`
              - Gets or sets an indicator of whether or not to include the parent object facets.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.rfcm import StkRfcmCommunicationsTransceiverConfiguration


Property detail
---------------

.. py:property:: supported_transceivers
    :canonical: ansys.stk.core.rfcm.StkRfcmCommunicationsTransceiverConfiguration.supported_transceivers
    :type: list

    Gets an array of available transceiver instances.

.. py:property:: transceiver
    :canonical: ansys.stk.core.rfcm.StkRfcmCommunicationsTransceiverConfiguration.transceiver
    :type: StkRfcmTransceiver

    Gets or sets the transceiver.

.. py:property:: mode
    :canonical: ansys.stk.core.rfcm.StkRfcmCommunicationsTransceiverConfiguration.mode
    :type: RfcmTransceiverMode

    Gets or sets the transceiver mode.

.. py:property:: include_parent_object_facets
    :canonical: ansys.stk.core.rfcm.StkRfcmCommunicationsTransceiverConfiguration.include_parent_object_facets
    :type: bool

    Gets or sets an indicator of whether or not to include the parent object facets.


