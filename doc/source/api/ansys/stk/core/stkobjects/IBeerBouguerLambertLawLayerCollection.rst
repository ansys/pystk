IBeerBouguerLambertLawLayerCollection
=====================================

.. py:class:: IBeerBouguerLambertLawLayerCollection

   object
   
   Represents a collection of complex numbers.

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
              - Remove the layer with the specified index.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IBeerBouguerLambertLawLayerCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IBeerBouguerLambertLawLayerCollection.count
    :type: int

    Returns the number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IBeerBouguerLambertLawLayerCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> IBeerBouguerLambertLawLayer
    :canonical: ansys.stk.core.stkobjects.IBeerBouguerLambertLawLayerCollection.item

    Given an index, returns the element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IBeerBouguerLambertLawLayer`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.IBeerBouguerLambertLawLayerCollection.remove_at

    Remove the layer with the specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

