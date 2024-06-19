IIntervalCollection
===================

.. py:class:: IIntervalCollection

   object
   
   AgIntervalCollection used to access the Intervals Collection interface.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~add`
              - Add an interval to the collection and returns the index. Start/Stop use DateFormat Dimension.
            * - :py:meth:`~remove_index`
              - Remove an item by the index.
            * - :py:meth:`~remove_all`
              - Remove all items in the collection.
            * - :py:meth:`~remove_interval`
              - Remove an interval using the interval interface. Start/Stop use DateFormat Dimension.
            * - :py:meth:`~deconflict`
              - Deconflict display intervals.
            * - :py:meth:`~load_intervals`
              - Load an interval file.
            * - :py:meth:`~change_interval`
              - Update interval with specified start and stop times at a given index. Start/Stop use DateFormat Dimension.
            * - :py:meth:`~get_interval`
              - Return start and stop times of the interval at a given index. Start/Stop use DateFormat Dimension.
            * - :py:meth:`~to_array`
              - Return a two-dimensional array of intervals beginning at a given position and having specified number of rows.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IIntervalCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IIntervalCollection.count
    :type: int

    Number of items in the collection.


Method detail
-------------


.. py:method:: add(self, start: typing.Any, stop: typing.Any) -> int
    :canonical: ansys.stk.core.stkobjects.IIntervalCollection.add

    Add an interval to the collection and returns the index. Start/Stop use DateFormat Dimension.

    :Parameters:

    **start** : :obj:`~typing.Any`
    **stop** : :obj:`~typing.Any`

    :Returns:

        :obj:`~int`

.. py:method:: remove_index(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.IIntervalCollection.remove_index

    Remove an item by the index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.IIntervalCollection.remove_all

    Remove all items in the collection.

    :Returns:

        :obj:`~None`

.. py:method:: remove_interval(self, start: typing.Any, stop: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.IIntervalCollection.remove_interval

    Remove an interval using the interval interface. Start/Stop use DateFormat Dimension.

    :Parameters:

    **start** : :obj:`~typing.Any`
    **stop** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: deconflict(self) -> None
    :canonical: ansys.stk.core.stkobjects.IIntervalCollection.deconflict

    Deconflict display intervals.

    :Returns:

        :obj:`~None`

.. py:method:: load_intervals(self, filename: str) -> None
    :canonical: ansys.stk.core.stkobjects.IIntervalCollection.load_intervals

    Load an interval file.

    :Parameters:

    **filename** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: change_interval(self, index: int, start: typing.Any, stop: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.IIntervalCollection.change_interval

    Update interval with specified start and stop times at a given index. Start/Stop use DateFormat Dimension.

    :Parameters:

    **index** : :obj:`~int`
    **start** : :obj:`~typing.Any`
    **stop** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: get_interval(self, index: int) -> typing.Tuple[typing.Any, typing.Any]
    :canonical: ansys.stk.core.stkobjects.IIntervalCollection.get_interval

    Return start and stop times of the interval at a given index. Start/Stop use DateFormat Dimension.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~typing.Tuple[typing.Any, typing.Any]`

.. py:method:: to_array(self, index: int, length: int) -> list
    :canonical: ansys.stk.core.stkobjects.IIntervalCollection.to_array

    Return a two-dimensional array of intervals beginning at a given position and having specified number of rows.

    :Parameters:

    **index** : :obj:`~int`
    **length** : :obj:`~int`

    :Returns:

        :obj:`~list`

