ITransferFunctionInputBackOffOutputBackOffTable
===============================================

.. py:class:: ITransferFunctionInputBackOffOutputBackOffTable

   object
   
   Represents a collection of input back off vs output back off values.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Given an index, returns the element in the collection.
            * - :py:meth:`~remove_at`
              - Remove the row with the supplied index.
            * - :py:meth:`~add`
              - Add and returns a new row.
            * - :py:meth:`~insert_at`
              - Insert and returns a new row at the supplied index.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ITransferFunctionInputBackOffOutputBackOffTable


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.ITransferFunctionInputBackOffOutputBackOffTable.count
    :type: int

    Returns the number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.ITransferFunctionInputBackOffOutputBackOffTable._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index:int) -> "ITransferFunctionInputBackOffOutputBackOffTableRow"

    Given an index, returns the element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~"ITransferFunctionInputBackOffOutputBackOffTableRow"`


.. py:method:: remove_at(self, index:int) -> None

    Remove the row with the supplied index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: add(self, inputBackOff:float, outputBackOff:float) -> "ITransferFunctionInputBackOffOutputBackOffTableRow"

    Add and returns a new row.

    :Parameters:

    **inputBackOff** : :obj:`~float`
    **outputBackOff** : :obj:`~float`

    :Returns:

        :obj:`~"ITransferFunctionInputBackOffOutputBackOffTableRow"`

.. py:method:: insert_at(self, index:int, inputBackOff:float, outputBackOff:float) -> "ITransferFunctionInputBackOffOutputBackOffTableRow"

    Insert and returns a new row at the supplied index.

    :Parameters:

    **index** : :obj:`~int`
    **inputBackOff** : :obj:`~float`
    **outputBackOff** : :obj:`~float`

    :Returns:

        :obj:`~"ITransferFunctionInputBackOffOutputBackOffTableRow"`

