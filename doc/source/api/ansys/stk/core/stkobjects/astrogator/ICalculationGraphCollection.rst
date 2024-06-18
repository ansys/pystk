ICalculationGraphCollection
===========================

.. py:class:: ICalculationGraphCollection

   object
   
   The list of Calculations Graphs to display.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Allow you to iterate through the collection.
            * - :py:meth:`~add`
              - Add a calculation graph.
            * - :py:meth:`~remove`
              - Remove a parameter.
            * - :py:meth:`~remove_all`
              - Remove all parameters.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~_NewEnum`
            * - :py:meth:`~count`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ICalculationGraphCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.ICalculationGraphCollection._NewEnum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.ICalculationGraphCollection.count
    :type: int

    Returns the size of the collection.


Method detail
-------------

.. py:method:: item(self, index:int) -> str

    Allow you to iterate through the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~str`


.. py:method:: add(self, graphName:str) -> None

    Add a calculation graph.

    :Parameters:

    **graphName** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: remove(self, graphName:str) -> None

    Remove a parameter.

    :Parameters:

    **graphName** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None

    Remove all parameters.

    :Returns:

        :obj:`~None`


