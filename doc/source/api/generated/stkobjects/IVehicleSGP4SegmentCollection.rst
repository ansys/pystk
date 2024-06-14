IVehicleSGP4SegmentCollection
=============================

.. py:class:: IVehicleSGP4SegmentCollection

   object
   
   Set of Trajectories.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Get the item for the specified index.
            * - :py:meth:`~add_seg`
              - Add a default segment.
            * - :py:meth:`~remove_seg`
              - Remove a Segment given an index.
            * - :py:meth:`~remove_all_segs`
              - Remove all the segments in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`
            * - :py:meth:`~load_method_type`
            * - :py:meth:`~load_method`
            * - :py:meth:`~routine_type`
            * - :py:meth:`~available_routines`
            * - :py:meth:`~max_tle_limit`
            * - :py:meth:`~ssc_number`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleSGP4SegmentCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IVehicleSGP4SegmentCollection.count
    :type: int

    Gets the size of the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IVehicleSGP4SegmentCollection._NewEnum
    :type: EnumeratorProxy

    Enumerates the elements of the collection.

.. py:property:: load_method_type
    :canonical: ansys.stk.core.stkobjects.IVehicleSGP4SegmentCollection.load_method_type
    :type: "LOAD_METHOD_TYPE"

    File Load Type.

.. py:property:: load_method
    :canonical: ansys.stk.core.stkobjects.IVehicleSGP4SegmentCollection.load_method
    :type: "IAgVeSGP4LoadData"

    File Load Data.

.. py:property:: routine_type
    :canonical: ansys.stk.core.stkobjects.IVehicleSGP4SegmentCollection.routine_type
    :type: str

    Gets or sets whether a routine type being used.

.. py:property:: available_routines
    :canonical: ansys.stk.core.stkobjects.IVehicleSGP4SegmentCollection.available_routines
    :type: list

    An array of strings returning all available routine types.

.. py:property:: max_tle_limit
    :canonical: ansys.stk.core.stkobjects.IVehicleSGP4SegmentCollection.max_tle_limit
    :type: int

    Max number of elements. Dimensionless.

.. py:property:: ssc_number
    :canonical: ansys.stk.core.stkobjects.IVehicleSGP4SegmentCollection.ssc_number
    :type: str

    Catalog number of the spacecraft. Note that any changes to the SSCNumber will reset the element set collection. Importing elements from file or online storage will also reset the SSCNumber.


Method detail
-------------


.. py:method:: item(self, index:int) -> "IVehicleSGP4Segment"

    Get the item for the specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~"IVehicleSGP4Segment"`


.. py:method:: add_seg(self) -> "IVehicleSGP4Segment"

    Add a default segment.

    :Returns:

        :obj:`~"IVehicleSGP4Segment"`






.. py:method:: remove_seg(self, index:int) -> None

    Remove a Segment given an index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all_segs(self) -> None

    Remove all the segments in the collection.

    :Returns:

        :obj:`~None`






