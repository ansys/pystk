IRadarActivityTimeIntervalListCollection
========================================

.. py:class:: IRadarActivityTimeIntervalListCollection

   object
   
   Represents a collection of time interval activity elements.

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
            * - :py:meth:`~remove_at`
              - Remove the element with the specified index.
            * - :py:meth:`~insert_at`
              - Insert a new element at the supplied index.
            * - :py:meth:`~add`
              - Add a new element to the collection.
            * - :py:meth:`~import_from_component`
              - Import time intervals from specified time component.
            * - :py:meth:`~load_from_file`
              - Load time intervals from file.
            * - :py:meth:`~clear`
              - Clear all elements from the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarActivityTimeIntervalListCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IRadarActivityTimeIntervalListCollection.count
    :type: int

    Returns the number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IRadarActivityTimeIntervalListCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index:int) -> "IRadarActivityTimeIntervalListElement"

    Given an index, returns the element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~"IRadarActivityTimeIntervalListElement"`


.. py:method:: remove_at(self, index:int) -> None

    Remove the element with the specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: insert_at(self, index:int) -> "IRadarActivityTimeIntervalListElement"

    Insert a new element at the supplied index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~"IRadarActivityTimeIntervalListElement"`

.. py:method:: add(self) -> "IRadarActivityTimeIntervalListElement"

    Add a new element to the collection.

    :Returns:

        :obj:`~"IRadarActivityTimeIntervalListElement"`

.. py:method:: import_from_component(self, identifier:str) -> None

    Import time intervals from specified time component.

    :Parameters:

    **identifier** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: load_from_file(self, path:str) -> None

    Load time intervals from file.

    :Parameters:

    **path** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: clear(self) -> None

    Clear all elements from the collection.

    :Returns:

        :obj:`~None`

