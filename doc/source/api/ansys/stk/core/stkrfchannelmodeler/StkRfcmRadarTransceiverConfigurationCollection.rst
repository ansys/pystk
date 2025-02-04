StkRfcmRadarTransceiverConfigurationCollection
==============================================

.. py:class:: ansys.stk.core.rfcm.StkRfcmRadarTransceiverConfigurationCollection

   A collection of radar transceivers.

.. py:currentmodule:: StkRfcmRadarTransceiverConfigurationCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.rfcm.StkRfcmRadarTransceiverConfigurationCollection.item`
              - Given an index, returns the element in the collection.
            * - :py:attr:`~ansys.stk.core.rfcm.StkRfcmRadarTransceiverConfigurationCollection.remove_at`
              - Remove the configuration with the supplied index.
            * - :py:attr:`~ansys.stk.core.rfcm.StkRfcmRadarTransceiverConfigurationCollection.remove`
              - Remove the supplied transceiver from the collection.
            * - :py:attr:`~ansys.stk.core.rfcm.StkRfcmRadarTransceiverConfigurationCollection.add_new`
              - Add and returns a new configuration.
            * - :py:attr:`~ansys.stk.core.rfcm.StkRfcmRadarTransceiverConfigurationCollection.remove_all`
              - Clear all configurations from the collection.
            * - :py:attr:`~ansys.stk.core.rfcm.StkRfcmRadarTransceiverConfigurationCollection.contains`
              - Check to see if a given configuration exists in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.rfcm.StkRfcmRadarTransceiverConfigurationCollection.count`
              - Returns the number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.rfcm.StkRfcmRadarTransceiverConfigurationCollection._new_enum`
              - Returns an enumerator for the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.rfcm import StkRfcmRadarTransceiverConfigurationCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.rfcm.StkRfcmRadarTransceiverConfigurationCollection.count
    :type: int

    Returns the number of elements in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.rfcm.StkRfcmRadarTransceiverConfigurationCollection._new_enum
    :type: EnumeratorProxy

    Returns an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> StkRfcmRadarTransceiverConfiguration
    :canonical: ansys.stk.core.rfcm.StkRfcmRadarTransceiverConfigurationCollection.item

    Given an index, returns the element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~StkRfcmRadarTransceiverConfiguration`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.rfcm.StkRfcmRadarTransceiverConfigurationCollection.remove_at

    Remove the configuration with the supplied index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove(self, transceiver: StkRfcmTransceiver) -> None
    :canonical: ansys.stk.core.rfcm.StkRfcmRadarTransceiverConfigurationCollection.remove

    Remove the supplied transceiver from the collection.

    :Parameters:

    **transceiver** : :obj:`~StkRfcmTransceiver`

    :Returns:

        :obj:`~None`

.. py:method:: add_new(self) -> StkRfcmRadarTransceiverConfiguration
    :canonical: ansys.stk.core.rfcm.StkRfcmRadarTransceiverConfigurationCollection.add_new

    Add and returns a new configuration.

    :Returns:

        :obj:`~StkRfcmRadarTransceiverConfiguration`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.rfcm.StkRfcmRadarTransceiverConfigurationCollection.remove_all

    Clear all configurations from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: contains(self, transceiver: StkRfcmTransceiver) -> bool
    :canonical: ansys.stk.core.rfcm.StkRfcmRadarTransceiverConfigurationCollection.contains

    Check to see if a given configuration exists in the collection.

    :Parameters:

    **transceiver** : :obj:`~StkRfcmTransceiver`

    :Returns:

        :obj:`~bool`

