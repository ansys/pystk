TimeIntervalCollectionReadOnly
==============================

.. py:class:: ansys.stk.core.stkobjects.TimeIntervalCollectionReadOnly

   Read-only collection of intervals.

.. py:currentmodule:: TimeIntervalCollectionReadOnly

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.TimeIntervalCollectionReadOnly.get_interval`
              - Return start and stop times of the interval at a given index. Start/Stop use DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.TimeIntervalCollectionReadOnly.to_array`
              - Return a two-dimensional array of intervals.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.TimeIntervalCollectionReadOnly.count`
              - Number of items in the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import TimeIntervalCollectionReadOnly


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.TimeIntervalCollectionReadOnly.count
    :type: int

    Number of items in the collection.


Method detail
-------------


.. py:method:: get_interval(self, index: int) -> typing.Tuple[typing.Any, typing.Any]
    :canonical: ansys.stk.core.stkobjects.TimeIntervalCollectionReadOnly.get_interval

    Return start and stop times of the interval at a given index. Start/Stop use DateFormat Dimension.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~typing.Tuple[typing.Any, typing.Any]`

.. py:method:: to_array(self) -> list
    :canonical: ansys.stk.core.stkobjects.TimeIntervalCollectionReadOnly.to_array

    Return a two-dimensional array of intervals.

    :Returns:

        :obj:`~list`

