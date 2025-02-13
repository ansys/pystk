SpatialAnalysisToolConditionGroup
=================================

.. py:class:: ansys.stk.core.vgt.SpatialAnalysisToolConditionGroup

   Access or create spatial conditions associated with a volume grid.

.. py:currentmodule:: SpatialAnalysisToolConditionGroup

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolConditionGroup.remove`
              - Remove a specified element.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolConditionGroup.contains`
              - Search for a an element with a given name. Returns false if the specified element does not exist.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolConditionGroup.item`
              - Return an element by name or at a specified position.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolConditionGroup.get_item_by_index`
              - Retrieve an volume from the collection by index.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolConditionGroup.get_item_by_name`
              - Retrieve volume from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolConditionGroup.context`
              - Return a context object. The context can be used to find out which central body or STK object this instance is associated with.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolConditionGroup.count`
              - Return a number of elements in the group.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolConditionGroup.factory`
              - Return a factory object used to create spatial condition components.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolConditionGroup._new_enum`
              - Return a COM enumerator.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import SpatialAnalysisToolConditionGroup


Property detail
---------------

.. py:property:: context
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolConditionGroup.context
    :type: IAnalysisWorkbenchComponentContext

    Return a context object. The context can be used to find out which central body or STK object this instance is associated with.

.. py:property:: count
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolConditionGroup.count
    :type: int

    Return a number of elements in the group.

.. py:property:: factory
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolConditionGroup.factory
    :type: SpatialAnalysisToolConditionFactory

    Return a factory object used to create spatial condition components.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolConditionGroup._new_enum
    :type: EnumeratorProxy

    Return a COM enumerator.


Method detail
-------------

.. py:method:: remove(self, event_name: str) -> None
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolConditionGroup.remove

    Remove a specified element.

    :Parameters:

    **event_name** : :obj:`~str`

    :Returns:

        :obj:`~None`


.. py:method:: contains(self, name: str) -> bool
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolConditionGroup.contains

    Search for a an element with a given name. Returns false if the specified element does not exist.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~bool`



.. py:method:: item(self, index_or_name: typing.Any) -> ISpatialAnalysisToolVolume
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolConditionGroup.item

    Return an element by name or at a specified position.

    :Parameters:

    **index_or_name** : :obj:`~typing.Any`

    :Returns:

        :obj:`~ISpatialAnalysisToolVolume`


.. py:method:: get_item_by_index(self, index: int) -> ISpatialAnalysisToolVolume
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolConditionGroup.get_item_by_index

    Retrieve an volume from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~ISpatialAnalysisToolVolume`

.. py:method:: get_item_by_name(self, name: str) -> ISpatialAnalysisToolVolume
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolConditionGroup.get_item_by_name

    Retrieve volume from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~ISpatialAnalysisToolVolume`

