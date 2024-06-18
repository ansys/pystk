IDrawElemCollection
===================

.. py:class:: IDrawElemCollection

   object
   
   Collection of elements to draw on the control.

.. py:currentmodule:: ansys.stk.core.stkx

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Get the element at the specified index (0-based).
            * - :py:meth:`~clear`
              - Clear the contents of the collection and updates the display.
            * - :py:meth:`~add`
              - Create and add a new element to the end of the sequence.
            * - :py:meth:`~remove`
              - Remove the specified element.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`
            * - :py:meth:`~visible`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkx import IDrawElemCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkx.IDrawElemCollection.count
    :type: int

    Number of elements contained in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkx.IDrawElemCollection._NewEnum
    :type: EnumeratorProxy

    Returns an object that can be used to iterate through all the strings in the collection.

.. py:property:: visible
    :canonical: ansys.stk.core.stkx.IDrawElemCollection.visible
    :type: bool

    Show or hide all the elements.


Method detail
-------------


.. py:method:: item(self, index:int) -> "IDrawElem"

    Get the element at the specified index (0-based).

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~"IDrawElem"`


.. py:method:: clear(self) -> None

    Clear the contents of the collection and updates the display.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, elemType:str) -> "IDrawElem"

    Create and add a new element to the end of the sequence.

    :Parameters:

    **elemType** : :obj:`~str`

    :Returns:

        :obj:`~"IDrawElem"`

.. py:method:: remove(self, drawElem:"IDrawElem") -> None

    Remove the specified element.

    :Parameters:

    **drawElem** : :obj:`~"IDrawElem"`

    :Returns:

        :obj:`~None`



