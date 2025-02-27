VehicleGraphics3DSystemsCollection
==================================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics3DSystemsCollection

   List of Systems.

.. py:currentmodule:: VehicleGraphics3DSystemsCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DSystemsCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DSystemsCollection.remove_at`
              - Remove an element from the collection using specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DSystemsCollection.remove_all`
              - Remove all elements from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DSystemsCollection.add`
              - Add a new element to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DSystemsCollection.contains`
              - Check whether the given frame is already in the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DSystemsCollection.remove`
              - Remove a system by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DSystemsCollection.count`
              - Return the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DSystemsCollection._new_enum`
              - Return an enumerator that can iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DSystemsCollection.supported_systems`
              - Return a list of element types that can be added to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DSystemsCollection.inertial_by_window`
              - Get the Inertial By Window System.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DSystemsCollection.fixed_by_window`
              - Get the Fixed By Window System.



Examples
--------

Add Fixed System Orbit System in 3D Display

.. code-block:: python

    # Satellitesatellite: Satellite object
    orbitsystems = satellite.graphics_3d.orbit_systems
    orbitsystems.fixed_by_window.show_graphics = True
    orbitsystems.fixed_by_window.inherit = False
    orbitsystems.fixed_by_window.color = Colors.Yellow


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics3DSystemsCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DSystemsCollection.count
    :type: int

    Return the number of elements in a collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DSystemsCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that can iterate through the collection.

.. py:property:: supported_systems
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DSystemsCollection.supported_systems
    :type: list

    Return a list of element types that can be added to the collection.

.. py:property:: inertial_by_window
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DSystemsCollection.inertial_by_window
    :type: VehicleGraphics3DSystemsSpecialElement

    Get the Inertial By Window System.

.. py:property:: fixed_by_window
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DSystemsCollection.fixed_by_window
    :type: VehicleGraphics3DSystemsSpecialElement

    Get the Fixed By Window System.


Method detail
-------------


.. py:method:: item(self, index: int) -> VehicleGraphics3DSystemsElement
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DSystemsCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~VehicleGraphics3DSystemsElement`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DSystemsCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DSystemsCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, system_name: str) -> VehicleGraphics3DSystemsElement
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DSystemsCollection.add

    Add a new element to the collection.

    :Parameters:

    **system_name** : :obj:`~str`

    :Returns:

        :obj:`~VehicleGraphics3DSystemsElement`


.. py:method:: contains(self, system_name: str) -> bool
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DSystemsCollection.contains

    Check whether the given frame is already in the list.

    :Parameters:

    **system_name** : :obj:`~str`

    :Returns:

        :obj:`~bool`



.. py:method:: remove(self, system_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DSystemsCollection.remove

    Remove a system by name.

    :Parameters:

    **system_name** : :obj:`~str`

    :Returns:

        :obj:`~None`

