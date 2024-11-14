LevelAttributeCollection
========================

.. py:class:: ansys.stk.core.stkobjects.LevelAttributeCollection

   Collection of properties defining display of contour levels.

.. py:currentmodule:: LevelAttributeCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.LevelAttributeCollection.item`
              - Return an IAgLevelAttribute given an index number.
            * - :py:attr:`~ansys.stk.core.stkobjects.LevelAttributeCollection.remove`
              - Remove an IAgLevelAttribute Item with given index.
            * - :py:attr:`~ansys.stk.core.stkobjects.LevelAttributeCollection.remove_all`
              - Remove all IAgLevelAttribute.
            * - :py:attr:`~ansys.stk.core.stkobjects.LevelAttributeCollection.add_level`
              - Add a level.
            * - :py:attr:`~ansys.stk.core.stkobjects.LevelAttributeCollection.add_level_range`
              - Add a level range.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.LevelAttributeCollection.count`
              - Returns the size of the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.LevelAttributeCollection._new_enum`
              - Enumerates through IAgLevelAttributeCollection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import LevelAttributeCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.LevelAttributeCollection.count
    :type: int

    Returns the size of the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.LevelAttributeCollection._new_enum
    :type: EnumeratorProxy

    Enumerates through IAgLevelAttributeCollection.


Method detail
-------------


.. py:method:: item(self, index: int) -> LevelAttribute
    :canonical: ansys.stk.core.stkobjects.LevelAttributeCollection.item

    Return an IAgLevelAttribute given an index number.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~LevelAttribute`


.. py:method:: remove(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.LevelAttributeCollection.remove

    Remove an IAgLevelAttribute Item with given index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.LevelAttributeCollection.remove_all

    Remove all IAgLevelAttribute.

    :Returns:

        :obj:`~None`

.. py:method:: add_level(self, level: typing.Any) -> LevelAttribute
    :canonical: ansys.stk.core.stkobjects.LevelAttributeCollection.add_level

    Add a level.

    :Parameters:

    **level** : :obj:`~typing.Any`

    :Returns:

        :obj:`~LevelAttribute`

.. py:method:: add_level_range(self, start: typing.Any, stop: typing.Any, step: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.LevelAttributeCollection.add_level_range

    Add a level range.

    :Parameters:

    **start** : :obj:`~typing.Any`
    **stop** : :obj:`~typing.Any`
    **step** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

