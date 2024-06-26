IAntennaContourLevelCollection
==============================

.. py:class:: ansys.stk.core.stkobjects.IAntennaContourLevelCollection

   object
   
   Represents a collection of antenna contour levels.

.. py:currentmodule:: IAntennaContourLevelCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContourLevelCollection.item`
              - Given an index, returns the element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContourLevelCollection.contains`
              - Check whether the collection contains an object with the given value.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContourLevelCollection.remove`
              - Remove the level with the corresponding value.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContourLevelCollection.remove_at`
              - Remove the level with the supplied index.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContourLevelCollection.add`
              - Add and returns a new level with the corresponding value.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContourLevelCollection.clear`
              - Clear all contour levels from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContourLevelCollection.get_level`
              - Get the level with the specified value.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContourLevelCollection.count`
              - Returns the number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContourLevelCollection._NewEnum`
              - Returns an enumerator for the collection.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAntennaContourLevelCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IAntennaContourLevelCollection.count
    :type: int

    Returns the number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IAntennaContourLevelCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> IAntennaContourLevel
    :canonical: ansys.stk.core.stkobjects.IAntennaContourLevelCollection.item

    Given an index, returns the element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IAntennaContourLevel`


.. py:method:: contains(self, value: float) -> bool
    :canonical: ansys.stk.core.stkobjects.IAntennaContourLevelCollection.contains

    Check whether the collection contains an object with the given value.

    :Parameters:

    **value** : :obj:`~float`

    :Returns:

        :obj:`~bool`

.. py:method:: remove(self, value: float) -> None
    :canonical: ansys.stk.core.stkobjects.IAntennaContourLevelCollection.remove

    Remove the level with the corresponding value.

    :Parameters:

    **value** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.IAntennaContourLevelCollection.remove_at

    Remove the level with the supplied index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: add(self, value: float) -> IAntennaContourLevel
    :canonical: ansys.stk.core.stkobjects.IAntennaContourLevelCollection.add

    Add and returns a new level with the corresponding value.

    :Parameters:

    **value** : :obj:`~float`

    :Returns:

        :obj:`~IAntennaContourLevel`

.. py:method:: clear(self) -> None
    :canonical: ansys.stk.core.stkobjects.IAntennaContourLevelCollection.clear

    Clear all contour levels from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: get_level(self, value: float) -> IAntennaContourLevel
    :canonical: ansys.stk.core.stkobjects.IAntennaContourLevelCollection.get_level

    Get the level with the specified value.

    :Parameters:

    **value** : :obj:`~float`

    :Returns:

        :obj:`~IAntennaContourLevel`

