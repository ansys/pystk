RadarActivityTimeIntervalListCollection
=======================================

.. py:class:: ansys.stk.core.stkobjects.RadarActivityTimeIntervalListCollection

   Class defining an radar antenna beam collection.

.. py:currentmodule:: RadarActivityTimeIntervalListCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarActivityTimeIntervalListCollection.item`
              - Given an index, returns the element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarActivityTimeIntervalListCollection.remove_at`
              - Remove the element with the specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarActivityTimeIntervalListCollection.insert_at`
              - Insert a new element at the supplied index.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarActivityTimeIntervalListCollection.add`
              - Add a new element to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarActivityTimeIntervalListCollection.import_from_component`
              - Import time intervals from specified time component.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarActivityTimeIntervalListCollection.load_from_file`
              - Load time intervals from file.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarActivityTimeIntervalListCollection.clear`
              - Clear all elements from the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarActivityTimeIntervalListCollection.count`
              - Return the number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarActivityTimeIntervalListCollection._new_enum`
              - Return an enumerator for the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RadarActivityTimeIntervalListCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.RadarActivityTimeIntervalListCollection.count
    :type: int

    Return the number of elements in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.RadarActivityTimeIntervalListCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> RadarActivityTimeIntervalListElement
    :canonical: ansys.stk.core.stkobjects.RadarActivityTimeIntervalListCollection.item

    Given an index, returns the element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~RadarActivityTimeIntervalListElement`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.RadarActivityTimeIntervalListCollection.remove_at

    Remove the element with the specified index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`

.. py:method:: insert_at(self, index: int) -> RadarActivityTimeIntervalListElement
    :canonical: ansys.stk.core.stkobjects.RadarActivityTimeIntervalListCollection.insert_at

    Insert a new element at the supplied index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~RadarActivityTimeIntervalListElement`

.. py:method:: add(self) -> RadarActivityTimeIntervalListElement
    :canonical: ansys.stk.core.stkobjects.RadarActivityTimeIntervalListCollection.add

    Add a new element to the collection.

    :Returns:

        :obj:`~RadarActivityTimeIntervalListElement`

.. py:method:: import_from_component(self, identifier: str) -> None
    :canonical: ansys.stk.core.stkobjects.RadarActivityTimeIntervalListCollection.import_from_component

    Import time intervals from specified time component.

    :Parameters:

        **identifier** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: load_from_file(self, path: str) -> None
    :canonical: ansys.stk.core.stkobjects.RadarActivityTimeIntervalListCollection.load_from_file

    Load time intervals from file.

    :Parameters:

        **path** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: clear(self) -> None
    :canonical: ansys.stk.core.stkobjects.RadarActivityTimeIntervalListCollection.clear

    Clear all elements from the collection.

    :Returns:

        :obj:`~None`

