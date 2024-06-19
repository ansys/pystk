IVehicleTargetPointingCollection
================================

.. py:class:: IVehicleTargetPointingCollection

   object
   
   Attitude Targets.

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
            * - :py:meth:`~add`
              - Add a new element to the collection.
            * - :py:meth:`~contains`
              - Return true if the collection contains the specified target.
            * - :py:meth:`~remove`
              - Remove the element using the object path.
            * - :py:meth:`~add_position_as_target`
              - Add the specified LLA position to the collection of targets. Latitude param uses Latitude Dimension, Longitude param uses Longitude Dimension. Alt param uses Distance Dimension.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`
            * - :py:meth:`~available_targets`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleTargetPointingCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IVehicleTargetPointingCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IVehicleTargetPointingCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.

.. py:property:: available_targets
    :canonical: ansys.stk.core.stkobjects.IVehicleTargetPointingCollection.available_targets
    :type: list

    Returns an array of available targets.


Method detail
-------------


.. py:method:: item(self, index: int) -> IVehicleTargetPointingElement
    :canonical: ansys.stk.core.stkobjects.IVehicleTargetPointingCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IVehicleTargetPointingElement`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleTargetPointingCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleTargetPointingCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, shortPath: str) -> IVehicleTargetPointingElement
    :canonical: ansys.stk.core.stkobjects.IVehicleTargetPointingCollection.add

    Add a new element to the collection.

    :Parameters:

    **shortPath** : :obj:`~str`

    :Returns:

        :obj:`~IVehicleTargetPointingElement`


.. py:method:: contains(self, path: str) -> bool
    :canonical: ansys.stk.core.stkobjects.IVehicleTargetPointingCollection.contains

    Return true if the collection contains the specified target.

    :Parameters:

    **path** : :obj:`~str`

    :Returns:

        :obj:`~bool`

.. py:method:: remove(self, path: str) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleTargetPointingCollection.remove

    Remove the element using the object path.

    :Parameters:

    **path** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: add_position_as_target(self, latitude: float, longitude: float, altitude: float) -> IVehicleTargetPointingElement
    :canonical: ansys.stk.core.stkobjects.IVehicleTargetPointingCollection.add_position_as_target

    Add the specified LLA position to the collection of targets. Latitude param uses Latitude Dimension, Longitude param uses Longitude Dimension. Alt param uses Distance Dimension.

    :Parameters:

    **latitude** : :obj:`~float`
    **longitude** : :obj:`~float`
    **altitude** : :obj:`~float`

    :Returns:

        :obj:`~IVehicleTargetPointingElement`

