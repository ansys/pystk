AnalysisWorkbenchComponentCollection
====================================

.. py:class:: ansys.stk.core.analysis_workbench.AnalysisWorkbenchComponentCollection

   A collection of VGT objects.

.. py:currentmodule:: AnalysisWorkbenchComponentCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchComponentCollection.contains`
              - Search for a an element with a given name. Returns false if the specified element does not exist.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchComponentCollection.item`
              - Retrieve an element of the collection using the name of the element or a position in the collection.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchComponentCollection.get_item_by_index`
              - Retrieve an item from the crdn collection by index.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchComponentCollection.get_item_by_name`
              - Retrieve an item from the crdn collection by name.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchComponentCollection.count`
              - Return a number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchComponentCollection._new_enum`
              - Return a COM enumerator.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import AnalysisWorkbenchComponentCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchComponentCollection.count
    :type: int

    Return a number of elements in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchComponentCollection._new_enum
    :type: EnumeratorProxy

    Return a COM enumerator.


Method detail
-------------

.. py:method:: contains(self, name: str) -> bool
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchComponentCollection.contains

    Search for a an element with a given name. Returns false if the specified element does not exist.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~bool`


.. py:method:: item(self, index_or_name: typing.Any) -> IAnalysisWorkbenchComponent
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchComponentCollection.item

    Retrieve an element of the collection using the name of the element or a position in the collection.

    :Parameters:

        **index_or_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~IAnalysisWorkbenchComponent`


.. py:method:: get_item_by_index(self, index: int) -> IAnalysisWorkbenchComponent
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchComponentCollection.get_item_by_index

    Retrieve an item from the crdn collection by index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~IAnalysisWorkbenchComponent`

.. py:method:: get_item_by_name(self, name: str) -> IAnalysisWorkbenchComponent
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchComponentCollection.get_item_by_name

    Retrieve an item from the crdn collection by name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~IAnalysisWorkbenchComponent`

