CommunicationsTransceiverConfigurationCollection
================================================

.. py:class:: ansys.stk.core.stkrfchannelmodeler.CommunicationsTransceiverConfigurationCollection

   A collection of communication transceivers.

.. py:currentmodule:: CommunicationsTransceiverConfigurationCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.CommunicationsTransceiverConfigurationCollection.add_new`
              - Add and returns a new configuration.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.CommunicationsTransceiverConfigurationCollection.contains`
              - Check to see if a given configuration exists in the collection.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.CommunicationsTransceiverConfigurationCollection.item`
              - Given an index, returns the element in the collection.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.CommunicationsTransceiverConfigurationCollection.remove`
              - Remove the supplied configuration from the collection.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.CommunicationsTransceiverConfigurationCollection.remove_all`
              - Clear all configurations from the collection.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.CommunicationsTransceiverConfigurationCollection.remove_at`
              - Remove the configuration with the supplied index.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.CommunicationsTransceiverConfigurationCollection._new_enum`
              - Return an enumerator for the collection.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.CommunicationsTransceiverConfigurationCollection.count`
              - Return the number of elements in the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkrfchannelmodeler import CommunicationsTransceiverConfigurationCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkrfchannelmodeler.CommunicationsTransceiverConfigurationCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator for the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkrfchannelmodeler.CommunicationsTransceiverConfigurationCollection.count
    :type: int

    Return the number of elements in the collection.


Method detail
-------------

.. py:method:: add_new(self) -> CommunicationsTransceiverConfiguration
    :canonical: ansys.stk.core.stkrfchannelmodeler.CommunicationsTransceiverConfigurationCollection.add_new

    Add and returns a new configuration.

    :Returns:

        :obj:`~CommunicationsTransceiverConfiguration`

.. py:method:: contains(self, transceiver: Transceiver) -> bool
    :canonical: ansys.stk.core.stkrfchannelmodeler.CommunicationsTransceiverConfigurationCollection.contains

    Check to see if a given configuration exists in the collection.

    :Parameters:

        **transceiver** : :obj:`~Transceiver`


    :Returns:

        :obj:`~bool`


.. py:method:: item(self, index: int) -> CommunicationsTransceiverConfiguration
    :canonical: ansys.stk.core.stkrfchannelmodeler.CommunicationsTransceiverConfigurationCollection.item

    Given an index, returns the element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~CommunicationsTransceiverConfiguration`

.. py:method:: remove(self, transceiver: Transceiver) -> None
    :canonical: ansys.stk.core.stkrfchannelmodeler.CommunicationsTransceiverConfigurationCollection.remove

    Remove the supplied configuration from the collection.

    :Parameters:

        **transceiver** : :obj:`~Transceiver`


    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkrfchannelmodeler.CommunicationsTransceiverConfigurationCollection.remove_all

    Clear all configurations from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkrfchannelmodeler.CommunicationsTransceiverConfigurationCollection.remove_at

    Remove the configuration with the supplied index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`


