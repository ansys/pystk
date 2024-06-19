IElementCollection
==================

.. py:class:: IElementCollection

   object
   
   Represents a collection of phased array elements.

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

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IElementCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IElementCollection.count
    :type: int

    Returns the number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IElementCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> IElement
    :canonical: ansys.stk.core.stkobjects.IElementCollection.item

    Given an index, returns the element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IElement`


