CalculationGraphCollection
==========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.CalculationGraphCollection

   Calculation Graph Collection.

.. py:currentmodule:: CalculationGraphCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CalculationGraphCollection.item`
              - Allow you to iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CalculationGraphCollection.add`
              - Add a calculation graph.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CalculationGraphCollection.remove`
              - Remove a parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CalculationGraphCollection.remove_all`
              - Remove all parameters.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CalculationGraphCollection._new_enum`
              - Allow you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CalculationGraphCollection.count`
              - Return the size of the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import CalculationGraphCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.astrogator.CalculationGraphCollection._new_enum
    :type: EnumeratorProxy

    Allow you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.CalculationGraphCollection.count
    :type: int

    Return the size of the collection.


Method detail
-------------

.. py:method:: item(self, index: int) -> str
    :canonical: ansys.stk.core.stkobjects.astrogator.CalculationGraphCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~str`


.. py:method:: add(self, graph_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.CalculationGraphCollection.add

    Add a calculation graph.

    :Parameters:

    **graph_name** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: remove(self, graph_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.CalculationGraphCollection.remove

    Remove a parameter.

    :Parameters:

    **graph_name** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.CalculationGraphCollection.remove_all

    Remove all parameters.

    :Returns:

        :obj:`~None`


