IDrawElementCollection
======================

.. py:class:: ansys.stk.core.stkx.IDrawElementCollection

   Collection of elements to draw on the control.

.. py:currentmodule:: IDrawElementCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkx.IDrawElementCollection.item`
              - Get the element at the specified index (0-based).
            * - :py:attr:`~ansys.stk.core.stkx.IDrawElementCollection.clear`
              - Clear the contents of the collection and updates the display.
            * - :py:attr:`~ansys.stk.core.stkx.IDrawElementCollection.add`
              - Create and add a new element to the end of the sequence.
            * - :py:attr:`~ansys.stk.core.stkx.IDrawElementCollection.remove`
              - Remove the specified element.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkx.IDrawElementCollection.count`
              - Number of elements contained in the collection.
            * - :py:attr:`~ansys.stk.core.stkx.IDrawElementCollection._new_enum`
              - Return an object that can be used to iterate through all the strings in the collection.
            * - :py:attr:`~ansys.stk.core.stkx.IDrawElementCollection.visible`
              - Show or hide all the elements.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkx import IDrawElementCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkx.IDrawElementCollection.count
    :type: int

    Number of elements contained in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkx.IDrawElementCollection._new_enum
    :type: EnumeratorProxy

    Return an object that can be used to iterate through all the strings in the collection.

.. py:property:: visible
    :canonical: ansys.stk.core.stkx.IDrawElementCollection.visible
    :type: bool

    Show or hide all the elements.


Method detail
-------------


.. py:method:: item(self, index: int) -> IDrawElement
    :canonical: ansys.stk.core.stkx.IDrawElementCollection.item

    Get the element at the specified index (0-based).

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IDrawElement`


.. py:method:: clear(self) -> None
    :canonical: ansys.stk.core.stkx.IDrawElementCollection.clear

    Clear the contents of the collection and updates the display.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, elem_type: str) -> IDrawElement
    :canonical: ansys.stk.core.stkx.IDrawElementCollection.add

    Create and add a new element to the end of the sequence.

    :Parameters:

    **elem_type** : :obj:`~str`

    :Returns:

        :obj:`~IDrawElement`

.. py:method:: remove(self, draw_elem: IDrawElement) -> None
    :canonical: ansys.stk.core.stkx.IDrawElementCollection.remove

    Remove the specified element.

    :Parameters:

    **draw_elem** : :obj:`~IDrawElement`

    :Returns:

        :obj:`~None`



