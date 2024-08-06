FigureOfMeritAssetListCollection
================================

.. py:class:: ansys.stk.core.stkobjects.FigureOfMeritAssetListCollection

   List of assets available for specifying range uncertainty (for Navigation Accuracy FOM).

.. py:currentmodule:: FigureOfMeritAssetListCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritAssetListCollection.item`
              - Given an index, returns an element in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritAssetListCollection.count`
              - Returns the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritAssetListCollection._NewEnum`
              - Returns an enumerator that can iterate through the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import FigureOfMeritAssetListCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritAssetListCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritAssetListCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> FigureOfMeritAssetListElement
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritAssetListCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~FigureOfMeritAssetListElement`


