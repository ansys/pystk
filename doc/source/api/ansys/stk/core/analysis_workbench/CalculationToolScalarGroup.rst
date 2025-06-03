CalculationToolScalarGroup
==========================

.. py:class:: ansys.stk.core.analysis_workbench.CalculationToolScalarGroup

   Access or create VGT calculation scalars associated with an object or a central body.

.. py:currentmodule:: CalculationToolScalarGroup

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarGroup.remove`
              - Remove a specified element.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarGroup.contains`
              - Search for a an element with a given name. Returns false if the specified element does not exist.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarGroup.item`
              - Return an element by name or at a specified position.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarGroup.get_item_by_index`
              - Retrieve an element from the collection by index.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarGroup.get_item_by_name`
              - Retrieve an element from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarGroup.context`
              - Return a context object. The context can be used to find out which central body or STK object this instance is associated with.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarGroup.count`
              - Return a number of elements in the group.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarGroup.factory`
              - Return a factory object used to create calc scalar components.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolScalarGroup._new_enum`
              - Return a COM enumerator.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import CalculationToolScalarGroup


Property detail
---------------

.. py:property:: context
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarGroup.context
    :type: IAnalysisWorkbenchComponentContext

    Return a context object. The context can be used to find out which central body or STK object this instance is associated with.

.. py:property:: count
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarGroup.count
    :type: int

    Return a number of elements in the group.

.. py:property:: factory
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarGroup.factory
    :type: CalculationToolScalarFactory

    Return a factory object used to create calc scalar components.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarGroup._new_enum
    :type: EnumeratorProxy

    Return a COM enumerator.


Method detail
-------------

.. py:method:: remove(self, event_name: str) -> None
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarGroup.remove

    Remove a specified element.

    :Parameters:

        **event_name** : :obj:`~str`


    :Returns:

        :obj:`~None`


.. py:method:: contains(self, name: str) -> bool
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarGroup.contains

    Search for a an element with a given name. Returns false if the specified element does not exist.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~bool`



.. py:method:: item(self, index_or_name: typing.Any) -> ICalculationToolScalar
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarGroup.item

    Return an element by name or at a specified position.

    :Parameters:

        **index_or_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~ICalculationToolScalar`


.. py:method:: get_item_by_index(self, index: int) -> ICalculationToolScalar
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarGroup.get_item_by_index

    Retrieve an element from the collection by index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~ICalculationToolScalar`

.. py:method:: get_item_by_name(self, name: str) -> ICalculationToolScalar
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolScalarGroup.get_item_by_name

    Retrieve an element from the collection by name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~ICalculationToolScalar`

