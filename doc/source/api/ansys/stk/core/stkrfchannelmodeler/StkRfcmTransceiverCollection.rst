StkRfcmTransceiverCollection
============================

.. py:class:: ansys.stk.core.rfcm.StkRfcmTransceiverCollection

   A collection of transceiver objects.

.. py:currentmodule:: StkRfcmTransceiverCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.rfcm.StkRfcmTransceiverCollection.item`
              - Given an index, returns the element in the collection.
            * - :py:attr:`~ansys.stk.core.rfcm.StkRfcmTransceiverCollection.remove_at`
              - Remove the transceiver with the supplied index.
            * - :py:attr:`~ansys.stk.core.rfcm.StkRfcmTransceiverCollection.remove`
              - Remove the supplied transceiver from the collection.
            * - :py:attr:`~ansys.stk.core.rfcm.StkRfcmTransceiverCollection.add_new`
              - Add and returns a new transceiver.
            * - :py:attr:`~ansys.stk.core.rfcm.StkRfcmTransceiverCollection.add`
              - Add the supplied transceiver to the collection.
            * - :py:attr:`~ansys.stk.core.rfcm.StkRfcmTransceiverCollection.remove_all`
              - Remove all transceivers from the collection.
            * - :py:attr:`~ansys.stk.core.rfcm.StkRfcmTransceiverCollection.find_by_identifier`
              - Return the transceiver in the collection with the supplied identifier or Null if not found or invalid.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.rfcm.StkRfcmTransceiverCollection.count`
              - Returns the number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.rfcm.StkRfcmTransceiverCollection._new_enum`
              - Returns an enumerator for the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.rfcm import StkRfcmTransceiverCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.rfcm.StkRfcmTransceiverCollection.count
    :type: int

    Returns the number of elements in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.rfcm.StkRfcmTransceiverCollection._new_enum
    :type: EnumeratorProxy

    Returns an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> StkRfcmTransceiver
    :canonical: ansys.stk.core.rfcm.StkRfcmTransceiverCollection.item

    Given an index, returns the element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~StkRfcmTransceiver`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.rfcm.StkRfcmTransceiverCollection.remove_at

    Remove the transceiver with the supplied index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove(self, transceiver: StkRfcmTransceiver) -> None
    :canonical: ansys.stk.core.rfcm.StkRfcmTransceiverCollection.remove

    Remove the supplied transceiver from the collection.

    :Parameters:

    **transceiver** : :obj:`~StkRfcmTransceiver`

    :Returns:

        :obj:`~None`

.. py:method:: add_new(self, type: RfcmTransceiverModelType, name: str, parent_object_path: str) -> StkRfcmTransceiver
    :canonical: ansys.stk.core.rfcm.StkRfcmTransceiverCollection.add_new

    Add and returns a new transceiver.

    :Parameters:

    **type** : :obj:`~RfcmTransceiverModelType`
    **name** : :obj:`~str`
    **parent_object_path** : :obj:`~str`

    :Returns:

        :obj:`~StkRfcmTransceiver`

.. py:method:: add(self, value: StkRfcmTransceiver) -> None
    :canonical: ansys.stk.core.rfcm.StkRfcmTransceiverCollection.add

    Add the supplied transceiver to the collection.

    :Parameters:

    **value** : :obj:`~StkRfcmTransceiver`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.rfcm.StkRfcmTransceiverCollection.remove_all

    Remove all transceivers from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: find_by_identifier(self, identifier: str) -> StkRfcmTransceiver
    :canonical: ansys.stk.core.rfcm.StkRfcmTransceiverCollection.find_by_identifier

    Return the transceiver in the collection with the supplied identifier or Null if not found or invalid.

    :Parameters:

    **identifier** : :obj:`~str`

    :Returns:

        :obj:`~StkRfcmTransceiver`

