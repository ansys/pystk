BeerBouguerLambertLawLayerCollection
====================================

.. py:class:: ansys.stk.core.stkobjects.BeerBouguerLambertLawLayerCollection

   Class defining collection of Beer-Bouguer-Lamber Law atmosphere layers.

.. py:currentmodule:: BeerBouguerLambertLawLayerCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.BeerBouguerLambertLawLayerCollection.item`
              - Given an index, returns the element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.BeerBouguerLambertLawLayerCollection.remove_at`
              - Remove the layer with the specified index.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.BeerBouguerLambertLawLayerCollection.count`
              - Return the number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.BeerBouguerLambertLawLayerCollection._new_enum`
              - Return an enumerator for the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import BeerBouguerLambertLawLayerCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.BeerBouguerLambertLawLayerCollection.count
    :type: int

    Return the number of elements in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.BeerBouguerLambertLawLayerCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> BeerBouguerLambertLawLayer
    :canonical: ansys.stk.core.stkobjects.BeerBouguerLambertLawLayerCollection.item

    Given an index, returns the element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~BeerBouguerLambertLawLayer`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.BeerBouguerLambertLawLayerCollection.remove_at

    Remove the layer with the specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

