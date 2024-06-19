IScheduleTimeCollection
=======================

.. py:class:: IScheduleTimeCollection

   object
   
   You can modify the scheduled times by disabling Use Access Times.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~add`
              - Add a schedule time item to the collection. Start/Stop use DateFormat Dimension.
            * - :py:meth:`~remove_index`
              - Remove an item given an index.
            * - :py:meth:`~remove_all`
              - Remove all items in the collection.
            * - :py:meth:`~remove_schedule`
              - Remove an interval using the interval interface. Start/Stop use DateFormat Dimension.
            * - :py:meth:`~item`
              - Retrieve and IAgScheduleTime interface given an index.
            * - :py:meth:`~deconflict`
              - Deconflicts the schedule time intervals.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IScheduleTimeCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IScheduleTimeCollection.count
    :type: int

    The number of items in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IScheduleTimeCollection._NewEnum
    :type: EnumeratorProxy

    Enumerates through the collection.


Method detail
-------------


.. py:method:: add(self, start: typing.Any, stop: typing.Any, name: str) -> IScheduleTime
    :canonical: ansys.stk.core.stkobjects.IScheduleTimeCollection.add

    Add a schedule time item to the collection. Start/Stop use DateFormat Dimension.

    :Parameters:

    **start** : :obj:`~typing.Any`
    **stop** : :obj:`~typing.Any`
    **name** : :obj:`~str`

    :Returns:

        :obj:`~IScheduleTime`

.. py:method:: remove_index(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.IScheduleTimeCollection.remove_index

    Remove an item given an index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.IScheduleTimeCollection.remove_all

    Remove all items in the collection.

    :Returns:

        :obj:`~None`

.. py:method:: remove_schedule(self, start: typing.Any, stop: typing.Any, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.IScheduleTimeCollection.remove_schedule

    Remove an interval using the interval interface. Start/Stop use DateFormat Dimension.

    :Parameters:

    **start** : :obj:`~typing.Any`
    **stop** : :obj:`~typing.Any`
    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: item(self, index: int) -> IScheduleTime
    :canonical: ansys.stk.core.stkobjects.IScheduleTimeCollection.item

    Retrieve and IAgScheduleTime interface given an index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IScheduleTime`


.. py:method:: deconflict(self) -> None
    :canonical: ansys.stk.core.stkobjects.IScheduleTimeCollection.deconflict

    Deconflicts the schedule time intervals.

    :Returns:

        :obj:`~None`

