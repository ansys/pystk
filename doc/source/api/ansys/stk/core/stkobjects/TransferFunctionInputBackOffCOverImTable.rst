TransferFunctionInputBackOffCOverImTable
========================================

.. py:class:: ansys.stk.core.stkobjects.TransferFunctionInputBackOffCOverImTable

   Class defining an input back off vs C/Im table.

.. py:currentmodule:: TransferFunctionInputBackOffCOverImTable

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.TransferFunctionInputBackOffCOverImTable.item`
              - Given an index, returns the element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransferFunctionInputBackOffCOverImTable.remove_at`
              - Remove the row with the supplied index.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransferFunctionInputBackOffCOverImTable.add`
              - Add and returns a new row.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransferFunctionInputBackOffCOverImTable.insert_at`
              - Insert and returns a new row at the supplied index.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.TransferFunctionInputBackOffCOverImTable.count`
              - Returns the number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransferFunctionInputBackOffCOverImTable._NewEnum`
              - Returns an enumerator for the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import TransferFunctionInputBackOffCOverImTable


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.TransferFunctionInputBackOffCOverImTable.count
    :type: int

    Returns the number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.TransferFunctionInputBackOffCOverImTable._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> TransferFunctionInputBackOffCOverImTableRow
    :canonical: ansys.stk.core.stkobjects.TransferFunctionInputBackOffCOverImTable.item

    Given an index, returns the element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~TransferFunctionInputBackOffCOverImTableRow`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.TransferFunctionInputBackOffCOverImTable.remove_at

    Remove the row with the supplied index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: add(self, inputBackOff: float, cOverIm: float) -> TransferFunctionInputBackOffCOverImTableRow
    :canonical: ansys.stk.core.stkobjects.TransferFunctionInputBackOffCOverImTable.add

    Add and returns a new row.

    :Parameters:

    **inputBackOff** : :obj:`~float`
    **cOverIm** : :obj:`~float`

    :Returns:

        :obj:`~TransferFunctionInputBackOffCOverImTableRow`

.. py:method:: insert_at(self, index: int, inputBackOff: float, cOverIm: float) -> TransferFunctionInputBackOffCOverImTableRow
    :canonical: ansys.stk.core.stkobjects.TransferFunctionInputBackOffCOverImTable.insert_at

    Insert and returns a new row at the supplied index.

    :Parameters:

    **index** : :obj:`~int`
    **inputBackOff** : :obj:`~float`
    **cOverIm** : :obj:`~float`

    :Returns:

        :obj:`~TransferFunctionInputBackOffCOverImTableRow`

