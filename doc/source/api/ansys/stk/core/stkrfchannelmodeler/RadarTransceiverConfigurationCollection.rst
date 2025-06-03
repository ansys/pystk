RadarTransceiverConfigurationCollection
=======================================

.. py:class:: ansys.stk.core.stkrfchannelmodeler.RadarTransceiverConfigurationCollection

   A collection of radar transceivers.

.. py:currentmodule:: RadarTransceiverConfigurationCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.RadarTransceiverConfigurationCollection.item`
              - Given an index, returns the element in the collection.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.RadarTransceiverConfigurationCollection.remove_at`
              - Remove the configuration with the supplied index.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.RadarTransceiverConfigurationCollection.remove`
              - Remove the supplied transceiver from the collection.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.RadarTransceiverConfigurationCollection.add_new`
              - Add and returns a new configuration.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.RadarTransceiverConfigurationCollection.remove_all`
              - Clear all configurations from the collection.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.RadarTransceiverConfigurationCollection.contains`
              - Check to see if a given configuration exists in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.RadarTransceiverConfigurationCollection.count`
              - Return the number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.RadarTransceiverConfigurationCollection._new_enum`
              - Return an enumerator for the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkrfchannelmodeler import RadarTransceiverConfigurationCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkrfchannelmodeler.RadarTransceiverConfigurationCollection.count
    :type: int

    Return the number of elements in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkrfchannelmodeler.RadarTransceiverConfigurationCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> RadarTransceiverConfiguration
    :canonical: ansys.stk.core.stkrfchannelmodeler.RadarTransceiverConfigurationCollection.item

    Given an index, returns the element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~RadarTransceiverConfiguration`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkrfchannelmodeler.RadarTransceiverConfigurationCollection.remove_at

    Remove the configuration with the supplied index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`

.. py:method:: remove(self, transceiver: Transceiver) -> None
    :canonical: ansys.stk.core.stkrfchannelmodeler.RadarTransceiverConfigurationCollection.remove

    Remove the supplied transceiver from the collection.

    :Parameters:

        **transceiver** : :obj:`~Transceiver`


    :Returns:

        :obj:`~None`

.. py:method:: add_new(self) -> RadarTransceiverConfiguration
    :canonical: ansys.stk.core.stkrfchannelmodeler.RadarTransceiverConfigurationCollection.add_new

    Add and returns a new configuration.

    :Returns:

        :obj:`~RadarTransceiverConfiguration`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkrfchannelmodeler.RadarTransceiverConfigurationCollection.remove_all

    Clear all configurations from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: contains(self, transceiver: Transceiver) -> bool
    :canonical: ansys.stk.core.stkrfchannelmodeler.RadarTransceiverConfigurationCollection.contains

    Check to see if a given configuration exists in the collection.

    :Parameters:

        **transceiver** : :obj:`~Transceiver`


    :Returns:

        :obj:`~bool`

