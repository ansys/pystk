IAdditionalGainLossCollection
=============================

.. py:class:: IAdditionalGainLossCollection

   object
   
   Represents a collection of gains and losses.

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
              - Remove the gain with the supplied index.
            * - :py:meth:`~add`
              - Add and returns a new gain with the corresponding value.
            * - :py:meth:`~clear`
              - Clear all gain values from the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAdditionalGainLossCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IAdditionalGainLossCollection.count
    :type: int

    Returns the number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IAdditionalGainLossCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index:int) -> "IAdditionalGainLoss"

    Given an index, returns the element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~"IAdditionalGainLoss"`


.. py:method:: remove_at(self, index:int) -> None

    Remove the gain with the supplied index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: add(self, value:float) -> "IAdditionalGainLoss"

    Add and returns a new gain with the corresponding value.

    :Parameters:

    **value** : :obj:`~float`

    :Returns:

        :obj:`~"IAdditionalGainLoss"`

.. py:method:: clear(self) -> None

    Clear all gain values from the collection.

    :Returns:

        :obj:`~None`

