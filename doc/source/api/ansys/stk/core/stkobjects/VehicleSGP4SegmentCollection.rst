VehicleSGP4SegmentCollection
============================

.. py:class:: ansys.stk.core.stkobjects.VehicleSGP4SegmentCollection

   Set of Trajectories.

.. py:currentmodule:: VehicleSGP4SegmentCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSGP4SegmentCollection.item`
              - Get the item for the specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSGP4SegmentCollection.add_seg`
              - Add a default segment.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSGP4SegmentCollection.remove_seg`
              - Remove a Segment given an index.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSGP4SegmentCollection.remove_all_segs`
              - Remove all the segments in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSGP4SegmentCollection.count`
              - Gets the size of the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSGP4SegmentCollection._NewEnum`
              - Enumerates the elements of the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSGP4SegmentCollection.load_method_type`
              - File Load Type.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSGP4SegmentCollection.load_method`
              - File Load Data.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSGP4SegmentCollection.routine_type`
              - Gets or sets whether a routine type being used.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSGP4SegmentCollection.available_routines`
              - An array of strings returning all available routine types.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSGP4SegmentCollection.max_tle_limit`
              - Max number of elements. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSGP4SegmentCollection.ssc_number`
              - Catalog number of the spacecraft. Note that any changes to the SSCNumber will reset the element set collection. Importing elements from file or online storage will also reset the SSCNumber.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleSGP4SegmentCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.VehicleSGP4SegmentCollection.count
    :type: int

    Gets the size of the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.VehicleSGP4SegmentCollection._NewEnum
    :type: EnumeratorProxy

    Enumerates the elements of the collection.

.. py:property:: load_method_type
    :canonical: ansys.stk.core.stkobjects.VehicleSGP4SegmentCollection.load_method_type
    :type: LOAD_METHOD_TYPE

    File Load Type.

.. py:property:: load_method
    :canonical: ansys.stk.core.stkobjects.VehicleSGP4SegmentCollection.load_method
    :type: IVehicleSGP4LoadData

    File Load Data.

.. py:property:: routine_type
    :canonical: ansys.stk.core.stkobjects.VehicleSGP4SegmentCollection.routine_type
    :type: str

    Gets or sets whether a routine type being used.

.. py:property:: available_routines
    :canonical: ansys.stk.core.stkobjects.VehicleSGP4SegmentCollection.available_routines
    :type: list

    An array of strings returning all available routine types.

.. py:property:: max_tle_limit
    :canonical: ansys.stk.core.stkobjects.VehicleSGP4SegmentCollection.max_tle_limit
    :type: int

    Max number of elements. Dimensionless.

.. py:property:: ssc_number
    :canonical: ansys.stk.core.stkobjects.VehicleSGP4SegmentCollection.ssc_number
    :type: str

    Catalog number of the spacecraft. Note that any changes to the SSCNumber will reset the element set collection. Importing elements from file or online storage will also reset the SSCNumber.


Method detail
-------------


.. py:method:: item(self, index: int) -> VehicleSGP4Segment
    :canonical: ansys.stk.core.stkobjects.VehicleSGP4SegmentCollection.item

    Get the item for the specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~VehicleSGP4Segment`


.. py:method:: add_seg(self) -> VehicleSGP4Segment
    :canonical: ansys.stk.core.stkobjects.VehicleSGP4SegmentCollection.add_seg

    Add a default segment.

    :Returns:

        :obj:`~VehicleSGP4Segment`






.. py:method:: remove_seg(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleSGP4SegmentCollection.remove_seg

    Remove a Segment given an index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all_segs(self) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleSGP4SegmentCollection.remove_all_segs

    Remove all the segments in the collection.

    :Returns:

        :obj:`~None`






