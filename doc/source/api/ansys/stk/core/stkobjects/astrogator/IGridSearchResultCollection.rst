IGridSearchResultCollection
===========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IGridSearchResultCollection

   object
   
   Properties for the list of Grid Search result parameters.

.. py:currentmodule:: IGridSearchResultCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IGridSearchResultCollection.item`
              - Allow you to iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IGridSearchResultCollection.get_result_by_paths`
              - Return the result specified by the object/result path.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IGridSearchResultCollection._NewEnum`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IGridSearchResultCollection.count`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IGridSearchResultCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.IGridSearchResultCollection._NewEnum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.IGridSearchResultCollection.count
    :type: int

    Returns the size of the collection.


Method detail
-------------

.. py:method:: item(self, index: int) -> IGridSearchResult
    :canonical: ansys.stk.core.stkobjects.astrogator.IGridSearchResultCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IGridSearchResult`



.. py:method:: get_result_by_paths(self, objectPath: str, resultPath: str) -> IGridSearchResult
    :canonical: ansys.stk.core.stkobjects.astrogator.IGridSearchResultCollection.get_result_by_paths

    Return the result specified by the object/result path.

    :Parameters:

    **objectPath** : :obj:`~str`
    **resultPath** : :obj:`~str`

    :Returns:

        :obj:`~IGridSearchResult`

