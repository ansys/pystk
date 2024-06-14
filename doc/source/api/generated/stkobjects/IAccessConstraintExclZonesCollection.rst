IAccessConstraintExclZonesCollection
====================================

.. py:class:: IAccessConstraintExclZonesCollection

   object
   
   AgAccessCnstrExclZonesCollection used to access the Exclusion Zones List interface.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~remove_index`
              - Remove an item given an index.
            * - :py:meth:`~remove_all`
              - Remove all items from the collection.
            * - :py:meth:`~remove_excl_zone`
              - Remove an Exclusion Zone using the min and max lat/lon values. Lat/Lon Values use Latitude and Longitude Dimensions respectively.
            * - :py:meth:`~change_excl_zone`
              - Update Exclusion Zone data at a given index. Lat/Lon Values use Latitude and Longitude Dimensions respectively.
            * - :py:meth:`~get_excl_zone`
              - Return min and max lat/lon values at a given index. Lat/Lon Values use Latitude and Longitude Dimensions respectively.
            * - :py:meth:`~to_array`
              - Return a four-dimensional array of min/max lat/lon values beginning at a given position and having specified number of rows.
            * - :py:meth:`~item`
              - Get an IAgAccessCnstrZone interface using an index.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~constraint_name`
            * - :py:meth:`~is_plugin`
            * - :py:meth:`~excl_intvl`
            * - :py:meth:`~constraint_type`
            * - :py:meth:`~_NewEnum`
            * - :py:meth:`~max_time_step`
            * - :py:meth:`~max_rel_motion`
            * - :py:meth:`~enabled`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAccessConstraintExclZonesCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintExclZonesCollection.count
    :type: int

    Number of items in the collection.

.. py:property:: constraint_name
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintExclZonesCollection.constraint_name
    :type: str

    Gets the constraint name.

.. py:property:: is_plugin
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintExclZonesCollection.is_plugin
    :type: bool

    Returns true if the access constraint is a plugin.

.. py:property:: excl_intvl
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintExclZonesCollection.excl_intvl
    :type: bool

    Gets or sets the ExclInterval.

.. py:property:: constraint_type
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintExclZonesCollection.constraint_type
    :type: "ACCESS_CONSTRAINTS"

    Gets the constraint type.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintExclZonesCollection._NewEnum
    :type: EnumeratorProxy

    Enumerate the IAgAccessCnstrZone interfaces.

.. py:property:: max_time_step
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintExclZonesCollection.max_time_step
    :type: float

    Maximum time step used in adaptive sampling.

.. py:property:: max_rel_motion
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintExclZonesCollection.max_rel_motion
    :type: float

    Maximum relative motion used in adaptive sampling.

.. py:property:: enabled
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintExclZonesCollection.enabled
    :type: bool

    Indicates whether the constraint should be considered (true) or ignored (false) in access computations.


Method detail
-------------


.. py:method:: remove_index(self, index:int) -> None

    Remove an item given an index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None

    Remove all items from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: remove_excl_zone(self, minLat:typing.Any, minLon:typing.Any, maxLat:typing.Any, maxLon:typing.Any) -> None

    Remove an Exclusion Zone using the min and max lat/lon values. Lat/Lon Values use Latitude and Longitude Dimensions respectively.

    :Parameters:

    **minLat** : :obj:`~typing.Any`
    **minLon** : :obj:`~typing.Any`
    **maxLat** : :obj:`~typing.Any`
    **maxLon** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: change_excl_zone(self, index:int, minLat:typing.Any, minLon:typing.Any, maxLat:typing.Any, maxLon:typing.Any) -> None

    Update Exclusion Zone data at a given index. Lat/Lon Values use Latitude and Longitude Dimensions respectively.

    :Parameters:

    **index** : :obj:`~int`
    **minLat** : :obj:`~typing.Any`
    **minLon** : :obj:`~typing.Any`
    **maxLat** : :obj:`~typing.Any`
    **maxLon** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: get_excl_zone(self, index:int) -> typing.Tuple[typing.Any, typing.Any, typing.Any, typing.Any]

    Return min and max lat/lon values at a given index. Lat/Lon Values use Latitude and Longitude Dimensions respectively.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~typing.Tuple[typing.Any, typing.Any, typing.Any, typing.Any]`

.. py:method:: to_array(self, index:int, length:int) -> list

    Return a four-dimensional array of min/max lat/lon values beginning at a given position and having specified number of rows.

    :Parameters:

    **index** : :obj:`~int`
    **length** : :obj:`~int`

    :Returns:

        :obj:`~list`






.. py:method:: item(self, index:int) -> "IAccessConstraintZone"

    Get an IAgAccessCnstrZone interface using an index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~"IAccessConstraintZone"`








