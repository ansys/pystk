IVehicleGraphics3DSystemsCollection
===================================

.. py:class:: ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsCollection

   object
   
   List of Systems.

.. py:currentmodule:: IVehicleGraphics3DSystemsCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsCollection.remove_at`
              - Remove an element from the collection using specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsCollection.remove_all`
              - Remove all elements from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsCollection.add`
              - Add a new element to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsCollection.contains`
              - Check whether the given frame is already in the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsCollection.remove`
              - Remove a system by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsCollection.count`
              - Returns the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsCollection._NewEnum`
              - Returns an enumerator that can iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsCollection.supported_systems`
              - Returns a list of element types that can be added to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsCollection.inertial_by_window`
              - Gets the Inertial By Window System.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsCollection.fixed_by_window`
              - Gets the Fixed By Window System.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics3DSystemsCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.

.. py:property:: supported_systems
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsCollection.supported_systems
    :type: list

    Returns a list of element types that can be added to the collection.

.. py:property:: inertial_by_window
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsCollection.inertial_by_window
    :type: IVehicleGraphics3DSystemsSpecialElement

    Gets the Inertial By Window System.

.. py:property:: fixed_by_window
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsCollection.fixed_by_window
    :type: IVehicleGraphics3DSystemsSpecialElement

    Gets the Fixed By Window System.


Method detail
-------------


.. py:method:: item(self, index: int) -> IVehicleGraphics3DSystemsElement
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IVehicleGraphics3DSystemsElement`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, systemName: str) -> IVehicleGraphics3DSystemsElement
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsCollection.add

    Add a new element to the collection.

    :Parameters:

    **systemName** : :obj:`~str`

    :Returns:

        :obj:`~IVehicleGraphics3DSystemsElement`


.. py:method:: contains(self, systemName: str) -> bool
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsCollection.contains

    Check whether the given frame is already in the list.

    :Parameters:

    **systemName** : :obj:`~str`

    :Returns:

        :obj:`~bool`



.. py:method:: remove(self, systemName: str) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsCollection.remove

    Remove a system by name.

    :Parameters:

    **systemName** : :obj:`~str`

    :Returns:

        :obj:`~None`

