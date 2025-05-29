TransferFunctionInputBackOffVsCOverImTable
==========================================

.. py:class:: ansys.stk.core.stkobjects.TransferFunctionInputBackOffVsCOverImTable

   Class defining an input back off vs C/Im table.

.. py:currentmodule:: TransferFunctionInputBackOffVsCOverImTable

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.TransferFunctionInputBackOffVsCOverImTable.item`
              - Given an index, returns the element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransferFunctionInputBackOffVsCOverImTable.remove_at`
              - Remove the row with the supplied index.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransferFunctionInputBackOffVsCOverImTable.add`
              - Add and returns a new row.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransferFunctionInputBackOffVsCOverImTable.insert_at`
              - Insert and returns a new row at the supplied index.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.TransferFunctionInputBackOffVsCOverImTable.count`
              - Return the number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransferFunctionInputBackOffVsCOverImTable._new_enum`
              - Return an enumerator for the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import TransferFunctionInputBackOffVsCOverImTable


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.TransferFunctionInputBackOffVsCOverImTable.count
    :type: int

    Return the number of elements in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.TransferFunctionInputBackOffVsCOverImTable._new_enum
    :type: EnumeratorProxy

    Return an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> TransferFunctionInputBackOffVsCOverImTableRow
    :canonical: ansys.stk.core.stkobjects.TransferFunctionInputBackOffVsCOverImTable.item

    Given an index, returns the element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~TransferFunctionInputBackOffVsCOverImTableRow`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.TransferFunctionInputBackOffVsCOverImTable.remove_at

    Remove the row with the supplied index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`

.. py:method:: add(self, input_back_off: float, c_over_im: float) -> TransferFunctionInputBackOffVsCOverImTableRow
    :canonical: ansys.stk.core.stkobjects.TransferFunctionInputBackOffVsCOverImTable.add

    Add and returns a new row.

    :Parameters:

        **input_back_off** : :obj:`~float`

        **c_over_im** : :obj:`~float`


    :Returns:

        :obj:`~TransferFunctionInputBackOffVsCOverImTableRow`

.. py:method:: insert_at(self, index: int, input_back_off: float, c_over_im: float) -> TransferFunctionInputBackOffVsCOverImTableRow
    :canonical: ansys.stk.core.stkobjects.TransferFunctionInputBackOffVsCOverImTable.insert_at

    Insert and returns a new row at the supplied index.

    :Parameters:

        **index** : :obj:`~int`

        **input_back_off** : :obj:`~float`

        **c_over_im** : :obj:`~float`


    :Returns:

        :obj:`~TransferFunctionInputBackOffVsCOverImTableRow`

