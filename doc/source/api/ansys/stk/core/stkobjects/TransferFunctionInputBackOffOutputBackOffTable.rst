TransferFunctionInputBackOffOutputBackOffTable
==============================================

.. py:class:: ansys.stk.core.stkobjects.TransferFunctionInputBackOffOutputBackOffTable

   Class defining an input back off vs output back off table.

.. py:currentmodule:: TransferFunctionInputBackOffOutputBackOffTable

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.TransferFunctionInputBackOffOutputBackOffTable.item`
              - Given an index, returns the element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransferFunctionInputBackOffOutputBackOffTable.remove_at`
              - Remove the row with the supplied index.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransferFunctionInputBackOffOutputBackOffTable.add`
              - Add and returns a new row.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransferFunctionInputBackOffOutputBackOffTable.insert_at`
              - Insert and returns a new row at the supplied index.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.TransferFunctionInputBackOffOutputBackOffTable.count`
              - Returns the number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransferFunctionInputBackOffOutputBackOffTable._NewEnum`
              - Returns an enumerator for the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import TransferFunctionInputBackOffOutputBackOffTable


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.TransferFunctionInputBackOffOutputBackOffTable.count
    :type: int

    Returns the number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.TransferFunctionInputBackOffOutputBackOffTable._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> TransferFunctionInputBackOffOutputBackOffTableRow
    :canonical: ansys.stk.core.stkobjects.TransferFunctionInputBackOffOutputBackOffTable.item

    Given an index, returns the element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~TransferFunctionInputBackOffOutputBackOffTableRow`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.TransferFunctionInputBackOffOutputBackOffTable.remove_at

    Remove the row with the supplied index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: add(self, input_back_off: float, output_back_off: float) -> TransferFunctionInputBackOffOutputBackOffTableRow
    :canonical: ansys.stk.core.stkobjects.TransferFunctionInputBackOffOutputBackOffTable.add

    Add and returns a new row.

    :Parameters:

    **input_back_off** : :obj:`~float`
    **output_back_off** : :obj:`~float`

    :Returns:

        :obj:`~TransferFunctionInputBackOffOutputBackOffTableRow`

.. py:method:: insert_at(self, index: int, input_back_off: float, output_back_off: float) -> TransferFunctionInputBackOffOutputBackOffTableRow
    :canonical: ansys.stk.core.stkobjects.TransferFunctionInputBackOffOutputBackOffTable.insert_at

    Insert and returns a new row at the supplied index.

    :Parameters:

    **index** : :obj:`~int`
    **input_back_off** : :obj:`~float`
    **output_back_off** : :obj:`~float`

    :Returns:

        :obj:`~TransferFunctionInputBackOffOutputBackOffTableRow`

