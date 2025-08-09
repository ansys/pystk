PropagatorSGP4SegmentCollection
===============================

.. py:class:: ansys.stk.core.stkobjects.PropagatorSGP4SegmentCollection

   Set of Trajectories.

.. py:currentmodule:: PropagatorSGP4SegmentCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4SegmentCollection.add_segment`
              - Add a default segment.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4SegmentCollection.item`
              - Get the item for the specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4SegmentCollection.remove_all_segments`
              - Remove all the segments in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4SegmentCollection.remove_segment`
              - Remove a Segment given an index.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4SegmentCollection._new_enum`
              - Enumerates the elements of the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4SegmentCollection.available_routines`
              - An array of strings returning all available routine types.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4SegmentCollection.count`
              - Get the size of the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4SegmentCollection.load_method`
              - File Load Data.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4SegmentCollection.load_method_type`
              - File Load Type.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4SegmentCollection.maximum_number_of_elements`
              - Max number of elements. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4SegmentCollection.routine_type`
              - Get or set whether a routine type being used.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4SegmentCollection.ssc_number`
              - Catalog number of the spacecraft. Note that any changes to the SSCNumber will reset the element set collection. Importing elements from file or online storage will also reset the SSCNumber.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import PropagatorSGP4SegmentCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4SegmentCollection._new_enum
    :type: EnumeratorProxy

    Enumerates the elements of the collection.

.. py:property:: available_routines
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4SegmentCollection.available_routines
    :type: list

    An array of strings returning all available routine types.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4SegmentCollection.count
    :type: int

    Get the size of the collection.

.. py:property:: load_method
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4SegmentCollection.load_method
    :type: IPropagatorSGP4LoadData

    File Load Data.

.. py:property:: load_method_type
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4SegmentCollection.load_method_type
    :type: LoadMethod

    File Load Type.

.. py:property:: maximum_number_of_elements
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4SegmentCollection.maximum_number_of_elements
    :type: int

    Max number of elements. Dimensionless.

.. py:property:: routine_type
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4SegmentCollection.routine_type
    :type: str

    Get or set whether a routine type being used.

.. py:property:: ssc_number
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4SegmentCollection.ssc_number
    :type: str

    Catalog number of the spacecraft. Note that any changes to the SSCNumber will reset the element set collection. Importing elements from file or online storage will also reset the SSCNumber.


Method detail
-------------

.. py:method:: add_segment(self) -> PropagatorSGP4Segment
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4SegmentCollection.add_segment

    Add a default segment.

    :Returns:

        :obj:`~PropagatorSGP4Segment`



.. py:method:: item(self, index: int) -> PropagatorSGP4Segment
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4SegmentCollection.item

    Get the item for the specified index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~PropagatorSGP4Segment`






.. py:method:: remove_all_segments(self) -> None
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4SegmentCollection.remove_all_segments

    Remove all the segments in the collection.

    :Returns:

        :obj:`~None`

.. py:method:: remove_segment(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4SegmentCollection.remove_segment

    Remove a Segment given an index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`






