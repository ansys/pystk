TimeToolTimeIntervalListGroup
=============================

.. py:class:: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListGroup

   Access or create VGT event interval lists associated with an object.

.. py:currentmodule:: TimeToolTimeIntervalListGroup

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListGroup.remove`
              - Remove a specified element.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListGroup.contains`
              - Search for a an element with a given name. Returns false if the specified element does not exist.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListGroup.item`
              - Return an element by name or at a specified position.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListGroup.get_item_by_index`
              - Retrieve an event interval list from the collection by index.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListGroup.get_item_by_name`
              - Retrieve an event interval list from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListGroup.context`
              - Return a context object. The context can be used to find out which central body or STK object this instance is associated with.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListGroup.count`
              - Return a number of elements in the group.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListGroup.factory`
              - Return a factory object used to create custom event interval lists.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListGroup._new_enum`
              - Return a COM enumerator.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import TimeToolTimeIntervalListGroup


Property detail
---------------

.. py:property:: context
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListGroup.context
    :type: IAnalysisWorkbenchComponentContext

    Return a context object. The context can be used to find out which central body or STK object this instance is associated with.

.. py:property:: count
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListGroup.count
    :type: int

    Return a number of elements in the group.

.. py:property:: factory
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListGroup.factory
    :type: TimeToolTimeIntervalListFactory

    Return a factory object used to create custom event interval lists.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListGroup._new_enum
    :type: EnumeratorProxy

    Return a COM enumerator.


Method detail
-------------

.. py:method:: remove(self, event_name: str) -> None
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListGroup.remove

    Remove a specified element.

    :Parameters:

        **event_name** : :obj:`~str`


    :Returns:

        :obj:`~None`


.. py:method:: contains(self, name: str) -> bool
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListGroup.contains

    Search for a an element with a given name. Returns false if the specified element does not exist.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~bool`



.. py:method:: item(self, index_or_name: typing.Any) -> ITimeToolTimeIntervalList
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListGroup.item

    Return an element by name or at a specified position.

    :Parameters:

        **index_or_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~ITimeToolTimeIntervalList`


.. py:method:: get_item_by_index(self, index: int) -> ITimeToolTimeIntervalList
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListGroup.get_item_by_index

    Retrieve an event interval list from the collection by index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~ITimeToolTimeIntervalList`

.. py:method:: get_item_by_name(self, name: str) -> ITimeToolTimeIntervalList
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListGroup.get_item_by_name

    Retrieve an event interval list from the collection by name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~ITimeToolTimeIntervalList`

