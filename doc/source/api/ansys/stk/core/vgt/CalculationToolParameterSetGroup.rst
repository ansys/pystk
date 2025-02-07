CalculationToolParameterSetGroup
================================

.. py:class:: ansys.stk.core.vgt.CalculationToolParameterSetGroup

   Access or create VGT parameter sets associated with an object or a central body.

.. py:currentmodule:: CalculationToolParameterSetGroup

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolParameterSetGroup.remove`
              - Remove a specified element.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolParameterSetGroup.contains`
              - Search for a an element with a given name. Returns false if the specified element does not exist.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolParameterSetGroup.item`
              - Return an element by name or at a specified position.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolParameterSetGroup.get_item_by_index`
              - Retrieve an element from the collection by index.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolParameterSetGroup.get_item_by_name`
              - Retrieve an element from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolParameterSetGroup.context`
              - Return a context object. The context can be used to find out which central body or STK object this instance is associated with.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolParameterSetGroup.count`
              - Return a number of elements in the group.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolParameterSetGroup.factory`
              - Return a factory object used to create calc scalar components.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolParameterSetGroup._new_enum`
              - Return a COM enumerator.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import CalculationToolParameterSetGroup


Property detail
---------------

.. py:property:: context
    :canonical: ansys.stk.core.vgt.CalculationToolParameterSetGroup.context
    :type: IAnalysisWorkbenchComponentContext

    Return a context object. The context can be used to find out which central body or STK object this instance is associated with.

.. py:property:: count
    :canonical: ansys.stk.core.vgt.CalculationToolParameterSetGroup.count
    :type: int

    Return a number of elements in the group.

.. py:property:: factory
    :canonical: ansys.stk.core.vgt.CalculationToolParameterSetGroup.factory
    :type: CalculationToolParameterSetFactory

    Return a factory object used to create calc scalar components.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.vgt.CalculationToolParameterSetGroup._new_enum
    :type: EnumeratorProxy

    Return a COM enumerator.


Method detail
-------------

.. py:method:: remove(self, event_name: str) -> None
    :canonical: ansys.stk.core.vgt.CalculationToolParameterSetGroup.remove

    Remove a specified element.

    :Parameters:

    **event_name** : :obj:`~str`

    :Returns:

        :obj:`~None`


.. py:method:: contains(self, name: str) -> bool
    :canonical: ansys.stk.core.vgt.CalculationToolParameterSetGroup.contains

    Search for a an element with a given name. Returns false if the specified element does not exist.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~bool`



.. py:method:: item(self, index_or_name: typing.Any) -> ICalculationToolParameterSet
    :canonical: ansys.stk.core.vgt.CalculationToolParameterSetGroup.item

    Return an element by name or at a specified position.

    :Parameters:

    **index_or_name** : :obj:`~typing.Any`

    :Returns:

        :obj:`~ICalculationToolParameterSet`


.. py:method:: get_item_by_index(self, index: int) -> ICalculationToolParameterSet
    :canonical: ansys.stk.core.vgt.CalculationToolParameterSetGroup.get_item_by_index

    Retrieve an element from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~ICalculationToolParameterSet`

.. py:method:: get_item_by_name(self, name: str) -> ICalculationToolParameterSet
    :canonical: ansys.stk.core.vgt.CalculationToolParameterSetGroup.get_item_by_name

    Retrieve an element from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolParameterSet`

