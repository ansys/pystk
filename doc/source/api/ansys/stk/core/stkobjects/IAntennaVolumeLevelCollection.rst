IAntennaVolumeLevelCollection
=============================

.. py:class:: ansys.stk.core.stkobjects.IAntennaVolumeLevelCollection

   object
   
   Represents a collection of antenna volume levels.

.. py:currentmodule:: IAntennaVolumeLevelCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaVolumeLevelCollection.item`
              - Given an index, returns the element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaVolumeLevelCollection.contains`
              - Check whether the collection contains an object with the given value.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaVolumeLevelCollection.remove`
              - Remove the level with the corresponding value.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaVolumeLevelCollection.remove_at`
              - Remove the level with the supplied index.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaVolumeLevelCollection.add`
              - Add and returns a new level with the corresponding value.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaVolumeLevelCollection.clear`
              - Clear all contour levels from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaVolumeLevelCollection.get_level`
              - Get the level with the specified value.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaVolumeLevelCollection.count`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaVolumeLevelCollection._NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAntennaVolumeLevelCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IAntennaVolumeLevelCollection.count
    :type: int

    Returns the number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IAntennaVolumeLevelCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> IAntennaVolumeLevel
    :canonical: ansys.stk.core.stkobjects.IAntennaVolumeLevelCollection.item

    Given an index, returns the element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IAntennaVolumeLevel`


.. py:method:: contains(self, value: float) -> bool
    :canonical: ansys.stk.core.stkobjects.IAntennaVolumeLevelCollection.contains

    Check whether the collection contains an object with the given value.

    :Parameters:

    **value** : :obj:`~float`

    :Returns:

        :obj:`~bool`

.. py:method:: remove(self, value: float) -> None
    :canonical: ansys.stk.core.stkobjects.IAntennaVolumeLevelCollection.remove

    Remove the level with the corresponding value.

    :Parameters:

    **value** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.IAntennaVolumeLevelCollection.remove_at

    Remove the level with the supplied index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: add(self, value: float) -> IAntennaVolumeLevel
    :canonical: ansys.stk.core.stkobjects.IAntennaVolumeLevelCollection.add

    Add and returns a new level with the corresponding value.

    :Parameters:

    **value** : :obj:`~float`

    :Returns:

        :obj:`~IAntennaVolumeLevel`

.. py:method:: clear(self) -> None
    :canonical: ansys.stk.core.stkobjects.IAntennaVolumeLevelCollection.clear

    Clear all contour levels from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: get_level(self, value: float) -> IAntennaVolumeLevel
    :canonical: ansys.stk.core.stkobjects.IAntennaVolumeLevelCollection.get_level

    Get the level with the specified value.

    :Parameters:

    **value** : :obj:`~float`

    :Returns:

        :obj:`~IAntennaVolumeLevel`

