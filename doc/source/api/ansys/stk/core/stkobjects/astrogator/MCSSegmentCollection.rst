MCSSegmentCollection
====================

.. py:class:: ansys.stk.core.stkobjects.astrogator.MCSSegmentCollection

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The Mission Control Sequence.

.. py:currentmodule:: MCSSegmentCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSSegmentCollection.item`
              - Return the specified segment(using segment name or index number).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSSegmentCollection.insert`
              - Add a segment to the segment collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSSegmentCollection.remove`
              - Remove a segment; the End segment cannot be deleted.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSSegmentCollection.remove_all`
              - Remove all segments; the End segment cannot be deleted.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSSegmentCollection.cut`
              - Copy the segment into the clipboard and removes the segment from the sequence.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSSegmentCollection.paste`
              - Pastes the segment from the clipboard and inserts in before the given segment name.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSSegmentCollection.insert_copy`
              - Copy the segment pointer and inserts the copy before the given segment name.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSSegmentCollection.insert_by_name`
              - Insert a segment by name to the segment collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSSegmentCollection.get_item_by_index`
              - Retrieve the specified segment(using segment index number).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSSegmentCollection.get_item_by_name`
              - Retrieve the specified segment(using segment name).

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSSegmentCollection._NewEnum`
              - Allows you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSSegmentCollection.count`
              - Returns the size of the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSSegmentCollection.provide_runtime_type_info`
              - Returns the IAgRuntimeTypeInfo interface to access properties at runtime.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import MCSSegmentCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSSegmentCollection._NewEnum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSSegmentCollection.count
    :type: int

    Returns the size of the collection.

.. py:property:: provide_runtime_type_info
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSSegmentCollection.provide_runtime_type_info
    :type: IRuntimeTypeInfo

    Returns the IAgRuntimeTypeInfo interface to access properties at runtime.


Method detail
-------------

.. py:method:: item(self, indexOrName: typing.Any) -> IMCSSegment
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSSegmentCollection.item

    Return the specified segment(using segment name or index number).

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IMCSSegment`

.. py:method:: insert(self, segmentType: SEGMENT_TYPE, segmentName: str, segmentToInsertBefore: str) -> IMCSSegment
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSSegmentCollection.insert

    Add a segment to the segment collection.

    :Parameters:

    **segmentType** : :obj:`~SEGMENT_TYPE`
    **segmentName** : :obj:`~str`
    **segmentToInsertBefore** : :obj:`~str`

    :Returns:

        :obj:`~IMCSSegment`

.. py:method:: remove(self, segmentNameToRemove: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSSegmentCollection.remove

    Remove a segment; the End segment cannot be deleted.

    :Parameters:

    **segmentNameToRemove** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSSegmentCollection.remove_all

    Remove all segments; the End segment cannot be deleted.

    :Returns:

        :obj:`~None`



.. py:method:: cut(self, segmentNameToCut: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSSegmentCollection.cut

    Copy the segment into the clipboard and removes the segment from the sequence.

    :Parameters:

    **segmentNameToCut** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: paste(self, segmentToPasteBefore: str) -> IMCSSegment
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSSegmentCollection.paste

    Pastes the segment from the clipboard and inserts in before the given segment name.

    :Parameters:

    **segmentToPasteBefore** : :obj:`~str`

    :Returns:

        :obj:`~IMCSSegment`

.. py:method:: insert_copy(self, segment: IMCSSegment, segmentToInsertBefore: str) -> IMCSSegment
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSSegmentCollection.insert_copy

    Copy the segment pointer and inserts the copy before the given segment name.

    :Parameters:

    **segment** : :obj:`~IMCSSegment`
    **segmentToInsertBefore** : :obj:`~str`

    :Returns:

        :obj:`~IMCSSegment`

.. py:method:: insert_by_name(self, segmentName: str, segmentToInsertBefore: str) -> IMCSSegment
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSSegmentCollection.insert_by_name

    Insert a segment by name to the segment collection.

    :Parameters:

    **segmentName** : :obj:`~str`
    **segmentToInsertBefore** : :obj:`~str`

    :Returns:

        :obj:`~IMCSSegment`


.. py:method:: get_item_by_index(self, index: int) -> IMCSSegment
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSSegmentCollection.get_item_by_index

    Retrieve the specified segment(using segment index number).

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IMCSSegment`

.. py:method:: get_item_by_name(self, name: str) -> IMCSSegment
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSSegmentCollection.get_item_by_name

    Retrieve the specified segment(using segment name).

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IMCSSegment`

