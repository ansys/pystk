ITransferFunctionPolynomialCollection
=====================================

.. py:class:: ITransferFunctionPolynomialCollection

   object
   
   Represents a transfer function polynomial collection.

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
              - Remove the complex value with the supplied index.
            * - :py:meth:`~add`
              - Add a new coefficient.
            * - :py:meth:`~insert_at`
              - Insert a new coefficient at the supplied index.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ITransferFunctionPolynomialCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.ITransferFunctionPolynomialCollection.count
    :type: int

    Returns the number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.ITransferFunctionPolynomialCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index:int) -> float

    Given an index, returns the element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~float`


.. py:method:: remove_at(self, index:int) -> None

    Remove the complex value with the supplied index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: add(self, coefficient:float) -> None

    Add a new coefficient.

    :Parameters:

    **coefficient** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: insert_at(self, index:int, coefficient:float) -> None

    Insert a new coefficient at the supplied index.

    :Parameters:

    **index** : :obj:`~int`
    **coefficient** : :obj:`~float`

    :Returns:

        :obj:`~None`

