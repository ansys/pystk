AnalysisWorkbenchComponentCollection
====================================

.. py:class:: ansys.stk.core.vgt.AnalysisWorkbenchComponentCollection

   A collection of VGT objects.

.. py:currentmodule:: AnalysisWorkbenchComponentCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentCollection.contains`
              - Search for a an element with a given name. Returns false if the specified element does not exist.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentCollection.item`
              - Retrieve an element of the collection using the name of the element or a position in the collection.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentCollection.get_item_by_index`
              - Retrieve an item from the crdn collection by index.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentCollection.get_item_by_name`
              - Retrieve an item from the crdn collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentCollection.count`
              - Returns a number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentCollection._NewEnum`
              - Returns a COM enumerator.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import AnalysisWorkbenchComponentCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentCollection.count
    :type: int

    Returns a number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentCollection._NewEnum
    :type: EnumeratorProxy

    Returns a COM enumerator.


Method detail
-------------

.. py:method:: contains(self, name: str) -> bool
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentCollection.contains

    Search for a an element with a given name. Returns false if the specified element does not exist.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~bool`


.. py:method:: item(self, index_or_name: typing.Any) -> IAnalysisWorkbenchComponent
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentCollection.item

    Retrieve an element of the collection using the name of the element or a position in the collection.

    :Parameters:

    **index_or_name** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IAnalysisWorkbenchComponent`


.. py:method:: get_item_by_index(self, index: int) -> IAnalysisWorkbenchComponent
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentCollection.get_item_by_index

    Retrieve an item from the crdn collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IAnalysisWorkbenchComponent`

.. py:method:: get_item_by_name(self, name: str) -> IAnalysisWorkbenchComponent
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentCollection.get_item_by_name

    Retrieve an item from the crdn collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IAnalysisWorkbenchComponent`

