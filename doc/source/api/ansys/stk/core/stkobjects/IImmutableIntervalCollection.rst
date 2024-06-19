IImmutableIntervalCollection
============================

.. py:class:: IImmutableIntervalCollection

   object
   
   IAgImmutableIntervalCollection represents a immutable (read-only) collection of intervals.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~get_interval`
              - Return start and stop times of the interval at a given index. Start/Stop use DateFormat Dimension.
            * - :py:meth:`~to_array`
              - Return a two-dimensional array of intervals.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IImmutableIntervalCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IImmutableIntervalCollection.count
    :type: int

    Number of items in the collection.


Method detail
-------------


.. py:method:: get_interval(self, index: int) -> typing.Tuple[typing.Any, typing.Any]
    :canonical: ansys.stk.core.stkobjects.IImmutableIntervalCollection.get_interval

    Return start and stop times of the interval at a given index. Start/Stop use DateFormat Dimension.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~typing.Tuple[typing.Any, typing.Any]`

.. py:method:: to_array(self) -> list
    :canonical: ansys.stk.core.stkobjects.IImmutableIntervalCollection.to_array

    Return a two-dimensional array of intervals.

    :Returns:

        :obj:`~list`

