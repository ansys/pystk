IRadarActivityTimeComponentListCollection
=========================================

.. py:class:: ansys.stk.core.stkobjects.IRadarActivityTimeComponentListCollection

   object
   
   Represents a collection of time component activity elements.

.. py:currentmodule:: IRadarActivityTimeComponentListCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarActivityTimeComponentListCollection.item`
              - Given an index, returns the time component element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarActivityTimeComponentListCollection.remove_at`
              - Remove the time component element with the specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarActivityTimeComponentListCollection.insert_at`
              - Insert a new time component element at the supplied index, configured with a component with the supplied identifier.  An example of a valid component identifier would be \"Facility/MFR_Facility/Radar/MFR LightingIntervals.Umbra EventIntervalList\".
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarActivityTimeComponentListCollection.add`
              - Add a new time component element to the collection, configured with a component with the supplied identifier.  An example of a valid component identifier would be \"Facility/MFR_Facility/Radar/MFR LightingIntervals.Umbra EventIntervalList\".
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarActivityTimeComponentListCollection.clear`
              - Clear all time component elements from the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarActivityTimeComponentListCollection.count`
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarActivityTimeComponentListCollection._NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarActivityTimeComponentListCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IRadarActivityTimeComponentListCollection.count
    :type: int

    Returns the number of time component elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IRadarActivityTimeComponentListCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> IRadarActivityTimeComponentListElement
    :canonical: ansys.stk.core.stkobjects.IRadarActivityTimeComponentListCollection.item

    Given an index, returns the time component element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IRadarActivityTimeComponentListElement`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.IRadarActivityTimeComponentListCollection.remove_at

    Remove the time component element with the specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: insert_at(self, index: int, componentIdentifier: str) -> IRadarActivityTimeComponentListElement
    :canonical: ansys.stk.core.stkobjects.IRadarActivityTimeComponentListCollection.insert_at

    Insert a new time component element at the supplied index, configured with a component with the supplied identifier.  An example of a valid component identifier would be \"Facility/MFR_Facility/Radar/MFR LightingIntervals.Umbra EventIntervalList\".

    :Parameters:

    **index** : :obj:`~int`
    **componentIdentifier** : :obj:`~str`

    :Returns:

        :obj:`~IRadarActivityTimeComponentListElement`

.. py:method:: add(self, componentIdentifier: str) -> IRadarActivityTimeComponentListElement
    :canonical: ansys.stk.core.stkobjects.IRadarActivityTimeComponentListCollection.add

    Add a new time component element to the collection, configured with a component with the supplied identifier.  An example of a valid component identifier would be \"Facility/MFR_Facility/Radar/MFR LightingIntervals.Umbra EventIntervalList\".

    :Parameters:

    **componentIdentifier** : :obj:`~str`

    :Returns:

        :obj:`~IRadarActivityTimeComponentListElement`

.. py:method:: clear(self) -> None
    :canonical: ansys.stk.core.stkobjects.IRadarActivityTimeComponentListCollection.clear

    Clear all time component elements from the collection.

    :Returns:

        :obj:`~None`

