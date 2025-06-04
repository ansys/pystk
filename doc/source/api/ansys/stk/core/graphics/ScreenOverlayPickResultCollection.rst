ScreenOverlayPickResultCollection
=================================

.. py:class:: ansys.stk.core.graphics.ScreenOverlayPickResultCollection

   A collection of pick results.

.. py:currentmodule:: ScreenOverlayPickResultCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ScreenOverlayPickResultCollection.item`
              - Get an element at the specified position in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ScreenOverlayPickResultCollection.count`
              - A total number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.graphics.ScreenOverlayPickResultCollection._new_enum`
              - Return an enumerator that iterates through the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ScreenOverlayPickResultCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.graphics.ScreenOverlayPickResultCollection.count
    :type: int

    A total number of elements in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.graphics.ScreenOverlayPickResultCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that iterates through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> ScreenOverlayPickResult
    :canonical: ansys.stk.core.graphics.ScreenOverlayPickResultCollection.item

    Get an element at the specified position in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~ScreenOverlayPickResult`


