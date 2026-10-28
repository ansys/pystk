NPlateStochasticParametersCollection
====================================

.. py:class:: ansys.stk.core.stkobjects.astrogator.NPlateStochasticParametersCollection

   NPlate Stochastic Parameter Collection.

.. py:currentmodule:: NPlateStochasticParametersCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.NPlateStochasticParametersCollection.get_item_by_index`
              - Retrieve an associated object from the collection by index.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.NPlateStochasticParametersCollection.get_item_by_name`
              - Retrieve an associated object from the collection by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.NPlateStochasticParametersCollection.item`
              - Iterate through the collection.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.NPlateStochasticParametersCollection._new_enum`
              - A property that allows you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.NPlateStochasticParametersCollection.count`
              - Get the number of associated objects in the set.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import NPlateStochasticParametersCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.astrogator.NPlateStochasticParametersCollection._new_enum
    :type: EnumeratorProxy

    A property that allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.NPlateStochasticParametersCollection.count
    :type: int

    Get the number of associated objects in the set.


Method detail
-------------


.. py:method:: get_item_by_index(self, index: int) -> NPlateStochasticParameter
    :canonical: ansys.stk.core.stkobjects.astrogator.NPlateStochasticParametersCollection.get_item_by_index

    Retrieve an associated object from the collection by index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~NPlateStochasticParameter`

.. py:method:: get_item_by_name(self, name: str) -> NPlateStochasticParameter
    :canonical: ansys.stk.core.stkobjects.astrogator.NPlateStochasticParametersCollection.get_item_by_name

    Retrieve an associated object from the collection by name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~NPlateStochasticParameter`

.. py:method:: item(self, index_or_name: typing.Any) -> NPlateStochasticParameter
    :canonical: ansys.stk.core.stkobjects.astrogator.NPlateStochasticParametersCollection.item

    Iterate through the collection.

    :Parameters:

        **index_or_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~NPlateStochasticParameter`


