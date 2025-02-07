StkRfcmCommunicationsTransceiverConfigurationCollection
=======================================================

.. py:class:: ansys.stk.core.stkrfchannelmodeler.StkRfcmCommunicationsTransceiverConfigurationCollection

   A collection of communication transceivers.

.. py:currentmodule:: StkRfcmCommunicationsTransceiverConfigurationCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmCommunicationsTransceiverConfigurationCollection.item`
              - Given an index, returns the element in the collection.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmCommunicationsTransceiverConfigurationCollection.remove_at`
              - Remove the configuration with the supplied index.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmCommunicationsTransceiverConfigurationCollection.remove`
              - Remove the supplied configuration from the collection.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmCommunicationsTransceiverConfigurationCollection.add_new`
              - Add and returns a new configuration.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmCommunicationsTransceiverConfigurationCollection.remove_all`
              - Clear all configurations from the collection.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmCommunicationsTransceiverConfigurationCollection.contains`
              - Check to see if a given configuration exists in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmCommunicationsTransceiverConfigurationCollection.count`
              - Return the number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmCommunicationsTransceiverConfigurationCollection._new_enum`
              - Return an enumerator for the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkrfchannelmodeler import StkRfcmCommunicationsTransceiverConfigurationCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmCommunicationsTransceiverConfigurationCollection.count
    :type: int

    Return the number of elements in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmCommunicationsTransceiverConfigurationCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> StkRfcmCommunicationsTransceiverConfiguration
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmCommunicationsTransceiverConfigurationCollection.item

    Given an index, returns the element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~StkRfcmCommunicationsTransceiverConfiguration`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmCommunicationsTransceiverConfigurationCollection.remove_at

    Remove the configuration with the supplied index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove(self, transceiver: StkRfcmTransceiver) -> None
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmCommunicationsTransceiverConfigurationCollection.remove

    Remove the supplied configuration from the collection.

    :Parameters:

    **transceiver** : :obj:`~StkRfcmTransceiver`

    :Returns:

        :obj:`~None`

.. py:method:: add_new(self) -> StkRfcmCommunicationsTransceiverConfiguration
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmCommunicationsTransceiverConfigurationCollection.add_new

    Add and returns a new configuration.

    :Returns:

        :obj:`~StkRfcmCommunicationsTransceiverConfiguration`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmCommunicationsTransceiverConfigurationCollection.remove_all

    Clear all configurations from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: contains(self, transceiver: StkRfcmTransceiver) -> bool
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmCommunicationsTransceiverConfigurationCollection.contains

    Check to see if a given configuration exists in the collection.

    :Parameters:

    **transceiver** : :obj:`~StkRfcmTransceiver`

    :Returns:

        :obj:`~bool`

