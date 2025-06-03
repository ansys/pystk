ScheduleTimeCollection
======================

.. py:class:: ansys.stk.core.stkobjects.ScheduleTimeCollection

   Collection of user-scheduled access times.

.. py:currentmodule:: ScheduleTimeCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ScheduleTimeCollection.add`
              - Add a schedule time item to the collection. Start/Stop use DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScheduleTimeCollection.remove_index`
              - Remove an item given an index.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScheduleTimeCollection.remove_all`
              - Remove all items in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScheduleTimeCollection.remove_schedule`
              - Remove an interval using the interval interface. Start/Stop use DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScheduleTimeCollection.item`
              - Retrieve and ScheduleTime interface given an index.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScheduleTimeCollection.deconflict`
              - Deconflicts the schedule time intervals.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ScheduleTimeCollection.count`
              - The number of items in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScheduleTimeCollection._new_enum`
              - Enumerates through the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ScheduleTimeCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.ScheduleTimeCollection.count
    :type: int

    The number of items in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.ScheduleTimeCollection._new_enum
    :type: EnumeratorProxy

    Enumerates through the collection.


Method detail
-------------


.. py:method:: add(self, start: typing.Any, stop: typing.Any, name: str) -> ScheduleTime
    :canonical: ansys.stk.core.stkobjects.ScheduleTimeCollection.add

    Add a schedule time item to the collection. Start/Stop use DateFormat Dimension.

    :Parameters:

        **start** : :obj:`~typing.Any`

        **stop** : :obj:`~typing.Any`

        **name** : :obj:`~str`


    :Returns:

        :obj:`~ScheduleTime`

.. py:method:: remove_index(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.ScheduleTimeCollection.remove_index

    Remove an item given an index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.ScheduleTimeCollection.remove_all

    Remove all items in the collection.

    :Returns:

        :obj:`~None`

.. py:method:: remove_schedule(self, start: typing.Any, stop: typing.Any, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.ScheduleTimeCollection.remove_schedule

    Remove an interval using the interval interface. Start/Stop use DateFormat Dimension.

    :Parameters:

        **start** : :obj:`~typing.Any`

        **stop** : :obj:`~typing.Any`

        **name** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: item(self, index: int) -> ScheduleTime
    :canonical: ansys.stk.core.stkobjects.ScheduleTimeCollection.item

    Retrieve and ScheduleTime interface given an index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~ScheduleTime`


.. py:method:: deconflict(self) -> None
    :canonical: ansys.stk.core.stkobjects.ScheduleTimeCollection.deconflict

    Deconflicts the schedule time intervals.

    :Returns:

        :obj:`~None`

