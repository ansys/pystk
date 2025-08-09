TimeToolTimeIntervalGroup
=========================

.. py:class:: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalGroup

   Access or create VGT event intervals associated with an object.

.. py:currentmodule:: TimeToolTimeIntervalGroup

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalGroup.remove`
              - Remove an element by name.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalGroup.contains`
              - Search for a an element with a given name. Returns false if the specified element does not exist.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalGroup.item`
              - Return an element by name or at a specified position.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalGroup.get_item_by_index`
              - Retrieve an event interval from the collection by index.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalGroup.get_item_by_name`
              - Retrieve an event interval from the collection by name.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalGroup.context`
              - Return a context object. The context can be used to find out which central body or STK object this instance is associated with.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalGroup.count`
              - Return a number of elements in the group.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalGroup.factory`
              - Return a Factory object used to create custom event intervals.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalGroup._new_enum`
              - Return a COM enumerator.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import TimeToolTimeIntervalGroup


Property detail
---------------

.. py:property:: context
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalGroup.context
    :type: IAnalysisWorkbenchComponentContext

    Return a context object. The context can be used to find out which central body or STK object this instance is associated with.

.. py:property:: count
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalGroup.count
    :type: int

    Return a number of elements in the group.

.. py:property:: factory
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalGroup.factory
    :type: TimeToolTimeIntervalFactory

    Return a Factory object used to create custom event intervals.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalGroup._new_enum
    :type: EnumeratorProxy

    Return a COM enumerator.


Method detail
-------------

.. py:method:: remove(self, event_interval_name: str) -> None
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalGroup.remove

    Remove an element by name.

    :Parameters:

        **event_interval_name** : :obj:`~str`


    :Returns:

        :obj:`~None`


.. py:method:: contains(self, name: str) -> bool
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalGroup.contains

    Search for a an element with a given name. Returns false if the specified element does not exist.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~bool`



.. py:method:: item(self, index_or_name: typing.Any) -> ITimeToolTimeInterval
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalGroup.item

    Return an element by name or at a specified position.

    :Parameters:

        **index_or_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~ITimeToolTimeInterval`


.. py:method:: get_item_by_index(self, index: int) -> ITimeToolTimeInterval
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalGroup.get_item_by_index

    Retrieve an event interval from the collection by index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~ITimeToolTimeInterval`

.. py:method:: get_item_by_name(self, name: str) -> ITimeToolTimeInterval
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalGroup.get_item_by_name

    Retrieve an event interval from the collection by name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~ITimeToolTimeInterval`

