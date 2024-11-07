TimeToolTimeIntervalGroup
=========================

.. py:class:: ansys.stk.core.vgt.TimeToolTimeIntervalGroup

   Access or create VGT event intervals associated with an object.

.. py:currentmodule:: TimeToolTimeIntervalGroup

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalGroup.remove`
              - Remove an element by name.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalGroup.contains`
              - Search for a an element with a given name. Returns false if the specified element does not exist.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalGroup.item`
              - Return an element by name or at a specified position.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalGroup.get_item_by_index`
              - Retrieve an event interval from the collection by index.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalGroup.get_item_by_name`
              - Retrieve an event interval from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalGroup.context`
              - Returns a context object. The context can be used to find out which central body or STK object this instance is associated with.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalGroup.count`
              - Returns a number of elements in the group.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalGroup.factory`
              - Returns a Factory object used to create custom event intervals.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalGroup._NewEnum`
              - Returns a COM enumerator.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import TimeToolTimeIntervalGroup


Property detail
---------------

.. py:property:: context
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalGroup.context
    :type: IAnalysisWorkbenchComponentContext

    Returns a context object. The context can be used to find out which central body or STK object this instance is associated with.

.. py:property:: count
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalGroup.count
    :type: int

    Returns a number of elements in the group.

.. py:property:: factory
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalGroup.factory
    :type: TimeToolTimeIntervalFactory

    Returns a Factory object used to create custom event intervals.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalGroup._NewEnum
    :type: EnumeratorProxy

    Returns a COM enumerator.


Method detail
-------------

.. py:method:: remove(self, event_interval_name: str) -> None
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalGroup.remove

    Remove an element by name.

    :Parameters:

    **event_interval_name** : :obj:`~str`

    :Returns:

        :obj:`~None`


.. py:method:: contains(self, name: str) -> bool
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalGroup.contains

    Search for a an element with a given name. Returns false if the specified element does not exist.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~bool`



.. py:method:: item(self, index_or_name: typing.Any) -> ITimeToolTimeInterval
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalGroup.item

    Return an element by name or at a specified position.

    :Parameters:

    **index_or_name** : :obj:`~typing.Any`

    :Returns:

        :obj:`~ITimeToolTimeInterval`


.. py:method:: get_item_by_index(self, index: int) -> ITimeToolTimeInterval
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalGroup.get_item_by_index

    Retrieve an event interval from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~ITimeToolTimeInterval`

.. py:method:: get_item_by_name(self, name: str) -> ITimeToolTimeInterval
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalGroup.get_item_by_name

    Retrieve an event interval from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolTimeInterval`

