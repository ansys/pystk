AdditionalGainLossCollection
============================

.. py:class:: ansys.stk.core.stkobjects.AdditionalGainLossCollection

   Class defining a collection of additional gains and losses.

.. py:currentmodule:: AdditionalGainLossCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AdditionalGainLossCollection.item`
              - Given an index, returns the element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.AdditionalGainLossCollection.remove_at`
              - Remove the gain with the supplied index.
            * - :py:attr:`~ansys.stk.core.stkobjects.AdditionalGainLossCollection.add`
              - Add and returns a new gain with the corresponding value.
            * - :py:attr:`~ansys.stk.core.stkobjects.AdditionalGainLossCollection.clear`
              - Clear all gain values from the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AdditionalGainLossCollection.count`
              - Return the number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.AdditionalGainLossCollection._new_enum`
              - Return an enumerator for the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AdditionalGainLossCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.AdditionalGainLossCollection.count
    :type: int

    Return the number of elements in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.AdditionalGainLossCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> AdditionalGainLoss
    :canonical: ansys.stk.core.stkobjects.AdditionalGainLossCollection.item

    Given an index, returns the element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~AdditionalGainLoss`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.AdditionalGainLossCollection.remove_at

    Remove the gain with the supplied index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: add(self, value: float) -> AdditionalGainLoss
    :canonical: ansys.stk.core.stkobjects.AdditionalGainLossCollection.add

    Add and returns a new gain with the corresponding value.

    :Parameters:

    **value** : :obj:`~float`

    :Returns:

        :obj:`~AdditionalGainLoss`

.. py:method:: clear(self) -> None
    :canonical: ansys.stk.core.stkobjects.AdditionalGainLossCollection.clear

    Clear all gain values from the collection.

    :Returns:

        :obj:`~None`

