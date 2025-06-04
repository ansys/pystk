AntennaVolumeLevelCollection
============================

.. py:class:: ansys.stk.core.stkobjects.AntennaVolumeLevelCollection

   Class defining a collection of antenna volume levels.

.. py:currentmodule:: AntennaVolumeLevelCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaVolumeLevelCollection.item`
              - Given an index, returns the element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaVolumeLevelCollection.contains`
              - Check whether the collection contains an object with the given value.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaVolumeLevelCollection.remove`
              - Remove the level with the corresponding value.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaVolumeLevelCollection.remove_at`
              - Remove the level with the supplied index.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaVolumeLevelCollection.add`
              - Add and returns a new level with the corresponding value.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaVolumeLevelCollection.clear`
              - Clear all contour levels from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaVolumeLevelCollection.get_level`
              - Get the level with the specified value.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaVolumeLevelCollection.count`
              - Return the number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaVolumeLevelCollection._new_enum`
              - Return an enumerator for the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AntennaVolumeLevelCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.AntennaVolumeLevelCollection.count
    :type: int

    Return the number of elements in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.AntennaVolumeLevelCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> AntennaVolumeLevel
    :canonical: ansys.stk.core.stkobjects.AntennaVolumeLevelCollection.item

    Given an index, returns the element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~AntennaVolumeLevel`


.. py:method:: contains(self, value: float) -> bool
    :canonical: ansys.stk.core.stkobjects.AntennaVolumeLevelCollection.contains

    Check whether the collection contains an object with the given value.

    :Parameters:

        **value** : :obj:`~float`


    :Returns:

        :obj:`~bool`

.. py:method:: remove(self, value: float) -> None
    :canonical: ansys.stk.core.stkobjects.AntennaVolumeLevelCollection.remove

    Remove the level with the corresponding value.

    :Parameters:

        **value** : :obj:`~float`


    :Returns:

        :obj:`~None`

.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.AntennaVolumeLevelCollection.remove_at

    Remove the level with the supplied index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`

.. py:method:: add(self, value: float) -> AntennaVolumeLevel
    :canonical: ansys.stk.core.stkobjects.AntennaVolumeLevelCollection.add

    Add and returns a new level with the corresponding value.

    :Parameters:

        **value** : :obj:`~float`


    :Returns:

        :obj:`~AntennaVolumeLevel`

.. py:method:: clear(self) -> None
    :canonical: ansys.stk.core.stkobjects.AntennaVolumeLevelCollection.clear

    Clear all contour levels from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: get_level(self, value: float) -> AntennaVolumeLevel
    :canonical: ansys.stk.core.stkobjects.AntennaVolumeLevelCollection.get_level

    Get the level with the specified value.

    :Parameters:

        **value** : :obj:`~float`


    :Returns:

        :obj:`~AntennaVolumeLevel`

