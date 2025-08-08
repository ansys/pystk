TimeToolInstantGroup
====================

.. py:class:: ansys.stk.core.analysis_workbench.TimeToolInstantGroup

   Access or create VGT events associated with an object.

.. py:currentmodule:: TimeToolInstantGroup

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolInstantGroup.contains`
              - Search for a an element with a given name. Returns false if the specified element does not exist.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolInstantGroup.get_item_by_index`
              - Retrieve an event from the collection by index.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolInstantGroup.get_item_by_name`
              - Retrieve an event from the collection by name.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolInstantGroup.item`
              - Return an element by name or at a specified position.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolInstantGroup.remove`
              - Remove a specified element.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolInstantGroup._new_enum`
              - Return a COM enumerator.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolInstantGroup.context`
              - Return a context object. The context can be used to find out which central body or STK object this instance is associated with.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolInstantGroup.count`
              - Return a number of elements in the group.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolInstantGroup.factory`
              - Return a Factory object used to create custom events.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import TimeToolInstantGroup


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.analysis_workbench.TimeToolInstantGroup._new_enum
    :type: EnumeratorProxy

    Return a COM enumerator.

.. py:property:: context
    :canonical: ansys.stk.core.analysis_workbench.TimeToolInstantGroup.context
    :type: IAnalysisWorkbenchComponentContext

    Return a context object. The context can be used to find out which central body or STK object this instance is associated with.

.. py:property:: count
    :canonical: ansys.stk.core.analysis_workbench.TimeToolInstantGroup.count
    :type: int

    Return a number of elements in the group.

.. py:property:: factory
    :canonical: ansys.stk.core.analysis_workbench.TimeToolInstantGroup.factory
    :type: TimeToolInstantFactory

    Return a Factory object used to create custom events.


Method detail
-------------

.. py:method:: contains(self, name: str) -> bool
    :canonical: ansys.stk.core.analysis_workbench.TimeToolInstantGroup.contains

    Search for a an element with a given name. Returns false if the specified element does not exist.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~bool`




.. py:method:: get_item_by_index(self, index: int) -> ITimeToolInstant
    :canonical: ansys.stk.core.analysis_workbench.TimeToolInstantGroup.get_item_by_index

    Retrieve an event from the collection by index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~ITimeToolInstant`

.. py:method:: get_item_by_name(self, name: str) -> ITimeToolInstant
    :canonical: ansys.stk.core.analysis_workbench.TimeToolInstantGroup.get_item_by_name

    Retrieve an event from the collection by name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~ITimeToolInstant`

.. py:method:: item(self, index_or_name: typing.Any) -> ITimeToolInstant
    :canonical: ansys.stk.core.analysis_workbench.TimeToolInstantGroup.item

    Return an element by name or at a specified position.

    :Parameters:

        **index_or_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~ITimeToolInstant`

.. py:method:: remove(self, event_name: str) -> None
    :canonical: ansys.stk.core.analysis_workbench.TimeToolInstantGroup.remove

    Remove a specified element.

    :Parameters:

        **event_name** : :obj:`~str`


    :Returns:

        :obj:`~None`


