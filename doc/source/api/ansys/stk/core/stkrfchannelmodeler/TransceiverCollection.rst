TransceiverCollection
=====================

.. py:class:: ansys.stk.core.stkrfchannelmodeler.TransceiverCollection

   A collection of transceiver objects.

.. py:currentmodule:: TransceiverCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.TransceiverCollection.add`
              - Add the supplied transceiver to the collection.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.TransceiverCollection.add_new`
              - Add and returns a new transceiver.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.TransceiverCollection.find_by_identifier`
              - Return the transceiver in the collection with the supplied identifier or Null if not found or invalid.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.TransceiverCollection.item`
              - Given an index, returns the element in the collection.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.TransceiverCollection.remove`
              - Remove the supplied transceiver from the collection.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.TransceiverCollection.remove_all`
              - Remove all transceivers from the collection.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.TransceiverCollection.remove_at`
              - Remove the transceiver with the supplied index.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.TransceiverCollection._new_enum`
              - Return an enumerator for the collection.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.TransceiverCollection.count`
              - Return the number of elements in the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkrfchannelmodeler import TransceiverCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkrfchannelmodeler.TransceiverCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator for the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkrfchannelmodeler.TransceiverCollection.count
    :type: int

    Return the number of elements in the collection.


Method detail
-------------

.. py:method:: add(self, value: Transceiver) -> None
    :canonical: ansys.stk.core.stkrfchannelmodeler.TransceiverCollection.add

    Add the supplied transceiver to the collection.

    :Parameters:

        **value** : :obj:`~Transceiver`


    :Returns:

        :obj:`~None`

.. py:method:: add_new(self, type: TransceiverModelType, name: str, parent_object_path: str) -> Transceiver
    :canonical: ansys.stk.core.stkrfchannelmodeler.TransceiverCollection.add_new

    Add and returns a new transceiver.

    :Parameters:

        **type** : :obj:`~TransceiverModelType`

        **name** : :obj:`~str`

        **parent_object_path** : :obj:`~str`


    :Returns:

        :obj:`~Transceiver`


.. py:method:: find_by_identifier(self, identifier: str) -> Transceiver
    :canonical: ansys.stk.core.stkrfchannelmodeler.TransceiverCollection.find_by_identifier

    Return the transceiver in the collection with the supplied identifier or Null if not found or invalid.

    :Parameters:

        **identifier** : :obj:`~str`


    :Returns:

        :obj:`~Transceiver`

.. py:method:: item(self, index: int) -> Transceiver
    :canonical: ansys.stk.core.stkrfchannelmodeler.TransceiverCollection.item

    Given an index, returns the element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~Transceiver`

.. py:method:: remove(self, transceiver: Transceiver) -> None
    :canonical: ansys.stk.core.stkrfchannelmodeler.TransceiverCollection.remove

    Remove the supplied transceiver from the collection.

    :Parameters:

        **transceiver** : :obj:`~Transceiver`


    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkrfchannelmodeler.TransceiverCollection.remove_all

    Remove all transceivers from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkrfchannelmodeler.TransceiverCollection.remove_at

    Remove the transceiver with the supplied index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`


