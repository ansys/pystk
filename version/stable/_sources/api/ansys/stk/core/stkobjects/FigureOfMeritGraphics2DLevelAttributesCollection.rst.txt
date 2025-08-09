FigureOfMeritGraphics2DLevelAttributesCollection
================================================

.. py:class:: ansys.stk.core.stkobjects.FigureOfMeritGraphics2DLevelAttributesCollection

   Collection of Level Attributes.

.. py:currentmodule:: FigureOfMeritGraphics2DLevelAttributesCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics2DLevelAttributesCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics2DLevelAttributesCollection.remove_at`
              - Remove an element from the collection using specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics2DLevelAttributesCollection.remove_all`
              - Remove all elements from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics2DLevelAttributesCollection.add_level_range`
              - Add a new element to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics2DLevelAttributesCollection.add_level`
              - Add a new element to the collection.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics2DLevelAttributesCollection.count`
              - Return the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics2DLevelAttributesCollection._new_enum`
              - Return an enumerator that can iterate through the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import FigureOfMeritGraphics2DLevelAttributesCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritGraphics2DLevelAttributesCollection.count
    :type: int

    Return the number of elements in a collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritGraphics2DLevelAttributesCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> FigureOfMeritGraphics2DLevelAttributesElement
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritGraphics2DLevelAttributesCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~FigureOfMeritGraphics2DLevelAttributesElement`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritGraphics2DLevelAttributesCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritGraphics2DLevelAttributesCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add_level_range(self, start: typing.Any, stop: typing.Any, step: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritGraphics2DLevelAttributesCollection.add_level_range

    Add a new element to the collection.

    :Parameters:

        **start** : :obj:`~typing.Any`

        **stop** : :obj:`~typing.Any`

        **step** : :obj:`~typing.Any`


    :Returns:

        :obj:`~None`

.. py:method:: add_level(self, level: typing.Any) -> FigureOfMeritGraphics2DLevelAttributesElement
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritGraphics2DLevelAttributesCollection.add_level

    Add a new element to the collection.

    :Parameters:

        **level** : :obj:`~typing.Any`


    :Returns:

        :obj:`~FigureOfMeritGraphics2DLevelAttributesElement`

