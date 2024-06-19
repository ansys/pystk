IFigureOfMeritGraphics2DLevelAttributesCollection
=================================================

.. py:class:: IFigureOfMeritGraphics2DLevelAttributesCollection

   object
   
   Level Attributes.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Given an index, returns an element in the collection.
            * - :py:meth:`~remove_at`
              - Remove an element from the collection using specified index.
            * - :py:meth:`~remove_all`
              - Remove all elements from the collection.
            * - :py:meth:`~add_level_range`
              - Add a new element to the collection.
            * - :py:meth:`~add_level`
              - Add a new element to the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IFigureOfMeritGraphics2DLevelAttributesCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DLevelAttributesCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DLevelAttributesCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> IFigureOfMeritGraphics2DLevelAttributesElement
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DLevelAttributesCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IFigureOfMeritGraphics2DLevelAttributesElement`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DLevelAttributesCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DLevelAttributesCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add_level_range(self, start: typing.Any, stop: typing.Any, step: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DLevelAttributesCollection.add_level_range

    Add a new element to the collection.

    :Parameters:

    **start** : :obj:`~typing.Any`
    **stop** : :obj:`~typing.Any`
    **step** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: add_level(self, level: typing.Any) -> IFigureOfMeritGraphics2DLevelAttributesElement
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DLevelAttributesCollection.add_level

    Add a new element to the collection.

    :Parameters:

    **level** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IFigureOfMeritGraphics2DLevelAttributesElement`

