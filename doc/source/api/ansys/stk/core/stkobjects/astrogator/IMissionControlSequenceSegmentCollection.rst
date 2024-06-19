IMissionControlSequenceSegmentCollection
========================================

.. py:class:: IMissionControlSequenceSegmentCollection

   object
   
   Properties for a collection of segments.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Return the specified segment(using segment name or index number).
            * - :py:meth:`~insert`
              - Add a segment to the segment collection.
            * - :py:meth:`~remove`
              - Remove a segment; the End segment cannot be deleted.
            * - :py:meth:`~remove_all`
              - Remove all segments; the End segment cannot be deleted.
            * - :py:meth:`~cut`
              - Copy the segment into the clipboard and removes the segment from the sequence.
            * - :py:meth:`~paste`
              - Pastes the segment from the clipboard and inserts in before the given segment name.
            * - :py:meth:`~insert_copy`
              - Copy the segment pointer and inserts the copy before the given segment name.
            * - :py:meth:`~insert_by_name`
              - Insert a segment by name to the segment collection.
            * - :py:meth:`~get_item_by_index`
              - Retrieve the specified segment(using segment index number).
            * - :py:meth:`~get_item_by_name`
              - Retrieve the specified segment(using segment name).

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~_NewEnum`
            * - :py:meth:`~count`
            * - :py:meth:`~provide_runtime_type_info`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IMissionControlSequenceSegmentCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegmentCollection._NewEnum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegmentCollection.count
    :type: int

    Returns the size of the collection.

.. py:property:: provide_runtime_type_info
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegmentCollection.provide_runtime_type_info
    :type: IAgRuntimeTypeInfo

    Returns the IAgRuntimeTypeInfo interface to access properties at runtime.


Method detail
-------------

.. py:method:: item(self, indexOrName: typing.Any) -> IMissionControlSequenceSegment
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegmentCollection.item

    Return the specified segment(using segment name or index number).

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IMissionControlSequenceSegment`

.. py:method:: insert(self, segmentType: SEGMENT_TYPE, segmentName: str, segmentToInsertBefore: str) -> IMissionControlSequenceSegment
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegmentCollection.insert

    Add a segment to the segment collection.

    :Parameters:

    **segmentType** : :obj:`~SEGMENT_TYPE`
    **segmentName** : :obj:`~str`
    **segmentToInsertBefore** : :obj:`~str`

    :Returns:

        :obj:`~IMissionControlSequenceSegment`

.. py:method:: remove(self, segmentNameToRemove: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegmentCollection.remove

    Remove a segment; the End segment cannot be deleted.

    :Parameters:

    **segmentNameToRemove** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegmentCollection.remove_all

    Remove all segments; the End segment cannot be deleted.

    :Returns:

        :obj:`~None`



.. py:method:: cut(self, segmentNameToCut: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegmentCollection.cut

    Copy the segment into the clipboard and removes the segment from the sequence.

    :Parameters:

    **segmentNameToCut** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: paste(self, segmentToPasteBefore: str) -> IMissionControlSequenceSegment
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegmentCollection.paste

    Pastes the segment from the clipboard and inserts in before the given segment name.

    :Parameters:

    **segmentToPasteBefore** : :obj:`~str`

    :Returns:

        :obj:`~IMissionControlSequenceSegment`

.. py:method:: insert_copy(self, segment: IMissionControlSequenceSegment, segmentToInsertBefore: str) -> IMissionControlSequenceSegment
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegmentCollection.insert_copy

    Copy the segment pointer and inserts the copy before the given segment name.

    :Parameters:

    **segment** : :obj:`~IMissionControlSequenceSegment`
    **segmentToInsertBefore** : :obj:`~str`

    :Returns:

        :obj:`~IMissionControlSequenceSegment`

.. py:method:: insert_by_name(self, segmentName: str, segmentToInsertBefore: str) -> IMissionControlSequenceSegment
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegmentCollection.insert_by_name

    Insert a segment by name to the segment collection.

    :Parameters:

    **segmentName** : :obj:`~str`
    **segmentToInsertBefore** : :obj:`~str`

    :Returns:

        :obj:`~IMissionControlSequenceSegment`


.. py:method:: get_item_by_index(self, index: int) -> IMissionControlSequenceSegment
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegmentCollection.get_item_by_index

    Retrieve the specified segment(using segment index number).

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IMissionControlSequenceSegment`

.. py:method:: get_item_by_name(self, name: str) -> IMissionControlSequenceSegment
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegmentCollection.get_item_by_name

    Retrieve the specified segment(using segment name).

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IMissionControlSequenceSegment`

