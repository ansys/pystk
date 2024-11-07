AccessConstraintExclZonesCollection
===================================

.. py:class:: ansys.stk.core.stkobjects.AccessConstraintExclZonesCollection

   Bases: :py:class:`~ansys.stk.core.stkobjects.IAccessConstraint`

   Collection of Exclusion Zones used in Exclusion Zone constraint.

.. py:currentmodule:: AccessConstraintExclZonesCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintExclZonesCollection.remove_index`
              - Remove an item given an index.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintExclZonesCollection.remove_all`
              - Remove all items from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintExclZonesCollection.remove_exclusion_zone`
              - Remove an Exclusion Zone using the min and max lat/lon values. Lat/Lon Values use Latitude and Longitude Dimensions respectively.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintExclZonesCollection.change_exclusion_zone`
              - Update Exclusion Zone data at a given index. Lat/Lon Values use Latitude and Longitude Dimensions respectively.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintExclZonesCollection.get_exclusion_zone`
              - Return min and max lat/lon values at a given index. Lat/Lon Values use Latitude and Longitude Dimensions respectively.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintExclZonesCollection.to_array`
              - Return a four-dimensional array of min/max lat/lon values beginning at a given position and having specified number of rows.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintExclZonesCollection.item`
              - Get an IAgAccessCnstrZone interface using an index.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintExclZonesCollection.count`
              - Number of items in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintExclZonesCollection.constraint_name`
              - Gets the constraint name.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintExclZonesCollection.is_plugin`
              - Returns true if the access constraint is a plugin.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintExclZonesCollection.exclusion_interval`
              - Gets or sets the ExclInterval.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintExclZonesCollection.constraint_type`
              - Gets the constraint type.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintExclZonesCollection._NewEnum`
              - Enumerate the IAgAccessCnstrZone interfaces.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintExclZonesCollection.maximum_time_step`
              - Maximum time step used in adaptive sampling.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintExclZonesCollection.maximum_relative_motion`
              - Maximum relative motion used in adaptive sampling.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AccessConstraintExclZonesCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.AccessConstraintExclZonesCollection.count
    :type: int

    Number of items in the collection.

.. py:property:: constraint_name
    :canonical: ansys.stk.core.stkobjects.AccessConstraintExclZonesCollection.constraint_name
    :type: str

    Gets the constraint name.

.. py:property:: is_plugin
    :canonical: ansys.stk.core.stkobjects.AccessConstraintExclZonesCollection.is_plugin
    :type: bool

    Returns true if the access constraint is a plugin.

.. py:property:: exclusion_interval
    :canonical: ansys.stk.core.stkobjects.AccessConstraintExclZonesCollection.exclusion_interval
    :type: bool

    Gets or sets the ExclInterval.

.. py:property:: constraint_type
    :canonical: ansys.stk.core.stkobjects.AccessConstraintExclZonesCollection.constraint_type
    :type: ACCESS_CONSTRAINT_TYPE

    Gets the constraint type.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.AccessConstraintExclZonesCollection._NewEnum
    :type: EnumeratorProxy

    Enumerate the IAgAccessCnstrZone interfaces.

.. py:property:: maximum_time_step
    :canonical: ansys.stk.core.stkobjects.AccessConstraintExclZonesCollection.maximum_time_step
    :type: float

    Maximum time step used in adaptive sampling.

.. py:property:: maximum_relative_motion
    :canonical: ansys.stk.core.stkobjects.AccessConstraintExclZonesCollection.maximum_relative_motion
    :type: float

    Maximum relative motion used in adaptive sampling.


Method detail
-------------


.. py:method:: remove_index(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.AccessConstraintExclZonesCollection.remove_index

    Remove an item given an index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.AccessConstraintExclZonesCollection.remove_all

    Remove all items from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: remove_exclusion_zone(self, min_lat: typing.Any, min_lon: typing.Any, max_lat: typing.Any, max_lon: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.AccessConstraintExclZonesCollection.remove_exclusion_zone

    Remove an Exclusion Zone using the min and max lat/lon values. Lat/Lon Values use Latitude and Longitude Dimensions respectively.

    :Parameters:

    **min_lat** : :obj:`~typing.Any`
    **min_lon** : :obj:`~typing.Any`
    **max_lat** : :obj:`~typing.Any`
    **max_lon** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: change_exclusion_zone(self, index: int, min_lat: typing.Any, min_lon: typing.Any, max_lat: typing.Any, max_lon: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.AccessConstraintExclZonesCollection.change_exclusion_zone

    Update Exclusion Zone data at a given index. Lat/Lon Values use Latitude and Longitude Dimensions respectively.

    :Parameters:

    **index** : :obj:`~int`
    **min_lat** : :obj:`~typing.Any`
    **min_lon** : :obj:`~typing.Any`
    **max_lat** : :obj:`~typing.Any`
    **max_lon** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: get_exclusion_zone(self, index: int) -> typing.Tuple[typing.Any, typing.Any, typing.Any, typing.Any]
    :canonical: ansys.stk.core.stkobjects.AccessConstraintExclZonesCollection.get_exclusion_zone

    Return min and max lat/lon values at a given index. Lat/Lon Values use Latitude and Longitude Dimensions respectively.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~typing.Tuple[typing.Any, typing.Any, typing.Any, typing.Any]`

.. py:method:: to_array(self, index: int, length: int) -> list
    :canonical: ansys.stk.core.stkobjects.AccessConstraintExclZonesCollection.to_array

    Return a four-dimensional array of min/max lat/lon values beginning at a given position and having specified number of rows.

    :Parameters:

    **index** : :obj:`~int`
    **length** : :obj:`~int`

    :Returns:

        :obj:`~list`






.. py:method:: item(self, index: int) -> AccessConstraintLatitudeLongitudeZone
    :canonical: ansys.stk.core.stkobjects.AccessConstraintExclZonesCollection.item

    Get an IAgAccessCnstrZone interface using an index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~AccessConstraintLatitudeLongitudeZone`






