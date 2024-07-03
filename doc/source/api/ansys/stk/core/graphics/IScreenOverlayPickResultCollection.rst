IScreenOverlayPickResultCollection
==================================

.. py:class:: ansys.stk.core.graphics.IScreenOverlayPickResultCollection

   object
   
   A collection of pick results.

.. py:currentmodule:: IScreenOverlayPickResultCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IScreenOverlayPickResultCollection.item`
              - Get an element at the specified position in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IScreenOverlayPickResultCollection.count`
              - A total number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.graphics.IScreenOverlayPickResultCollection._NewEnum`
              - Return an enumerator that iterates through the collection.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IScreenOverlayPickResultCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.graphics.IScreenOverlayPickResultCollection.count
    :type: int

    A total number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.graphics.IScreenOverlayPickResultCollection._NewEnum
    :type: EnumeratorProxy

    Return an enumerator that iterates through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> IScreenOverlayPickResult
    :canonical: ansys.stk.core.graphics.IScreenOverlayPickResultCollection.item

    Get an element at the specified position in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IScreenOverlayPickResult`


