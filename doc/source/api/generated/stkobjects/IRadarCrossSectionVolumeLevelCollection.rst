IRadarCrossSectionVolumeLevelCollection
=======================================

.. py:class:: IRadarCrossSectionVolumeLevelCollection

   object
   
   Represents a collection of radar cross section volume levels.

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
            * - :py:meth:`~contains`
              - Check whether the collection contains an object with the given value.
            * - :py:meth:`~remove`
              - Remove the level with the corresponding value.
            * - :py:meth:`~remove_at`
              - Remove the level with the supplied index.
            * - :py:meth:`~add`
              - Add and returns a new level with the corresponding value.
            * - :py:meth:`~clear`
              - Clear all contour levels from the collection.
            * - :py:meth:`~get_level`
              - Get the level with the specified value.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarCrossSectionVolumeLevelCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionVolumeLevelCollection.count
    :type: int

    Returns the number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionVolumeLevelCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index:int) -> "IRadarCrossSectionVolumeLevel"

    Given an index, returns the element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~"IRadarCrossSectionVolumeLevel"`


.. py:method:: contains(self, value:float) -> bool

    Check whether the collection contains an object with the given value.

    :Parameters:

    **value** : :obj:`~float`

    :Returns:

        :obj:`~bool`

.. py:method:: remove(self, value:float) -> None

    Remove the level with the corresponding value.

    :Parameters:

    **value** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: remove_at(self, index:int) -> None

    Remove the level with the supplied index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: add(self, value:float) -> "IRadarCrossSectionVolumeLevel"

    Add and returns a new level with the corresponding value.

    :Parameters:

    **value** : :obj:`~float`

    :Returns:

        :obj:`~"IRadarCrossSectionVolumeLevel"`

.. py:method:: clear(self) -> None

    Clear all contour levels from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: get_level(self, value:float) -> "IRadarCrossSectionVolumeLevel"

    Get the level with the specified value.

    :Parameters:

    **value** : :obj:`~float`

    :Returns:

        :obj:`~"IRadarCrossSectionVolumeLevel"`

