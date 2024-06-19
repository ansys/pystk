IUnitPreferencesDimensionCollection
===================================

.. py:class:: IUnitPreferencesDimensionCollection

   object
   
   Provide accesses to the global unit table.

.. py:currentmodule:: ansys.stk.core.stkutil

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Return an IAgUnitPrefsDim given a Dimension name or an index.
            * - :py:meth:`~set_current_unit`
              - Return the Current unit for a Dimension.
            * - :py:meth:`~get_current_unit_abbrv`
              - Return the Current Unit for a Dimension.
            * - :py:meth:`~reset_units`
              - Reset the unitpreferences to the Default units.
            * - :py:meth:`~get_item_by_index`
              - Retrieve a dimension from the collection by index.
            * - :py:meth:`~get_item_by_name`
              - Retrieve a dimension from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~mission_elapsed_time`
            * - :py:meth:`~julian_date_offset`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkutil import IUnitPreferencesDimensionCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkutil.IUnitPreferencesDimensionCollection.count
    :type: int

    Returns the number of items in the collection.

.. py:property:: mission_elapsed_time
    :canonical: ansys.stk.core.stkutil.IUnitPreferencesDimensionCollection.mission_elapsed_time
    :type: typing.Any

    The MissionElapsedTime.

.. py:property:: julian_date_offset
    :canonical: ansys.stk.core.stkutil.IUnitPreferencesDimensionCollection.julian_date_offset
    :type: float

    The JulianDateOffset.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkutil.IUnitPreferencesDimensionCollection._NewEnum
    :type: EnumeratorProxy

    Returns a collection of IAgUnitPrefsDim.


Method detail
-------------

.. py:method:: item(self, indexOrName: typing.Any) -> IUnitPreferencesDimension
    :canonical: ansys.stk.core.stkutil.IUnitPreferencesDimensionCollection.item

    Return an IAgUnitPrefsDim given a Dimension name or an index.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IUnitPreferencesDimension`


.. py:method:: set_current_unit(self, dimension: str, unitAbbrv: str) -> None
    :canonical: ansys.stk.core.stkutil.IUnitPreferencesDimensionCollection.set_current_unit

    Return the Current unit for a Dimension.

    :Parameters:

    **dimension** : :obj:`~str`
    **unitAbbrv** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: get_current_unit_abbrv(self, indexOrDimName: typing.Any) -> str
    :canonical: ansys.stk.core.stkutil.IUnitPreferencesDimensionCollection.get_current_unit_abbrv

    Return the Current Unit for a Dimension.

    :Parameters:

    **indexOrDimName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~str`






.. py:method:: reset_units(self) -> None
    :canonical: ansys.stk.core.stkutil.IUnitPreferencesDimensionCollection.reset_units

    Reset the unitpreferences to the Default units.

    :Returns:

        :obj:`~None`

.. py:method:: get_item_by_index(self, index: int) -> IUnitPreferencesDimension
    :canonical: ansys.stk.core.stkutil.IUnitPreferencesDimensionCollection.get_item_by_index

    Retrieve a dimension from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IUnitPreferencesDimension`

.. py:method:: get_item_by_name(self, name: str) -> IUnitPreferencesDimension
    :canonical: ansys.stk.core.stkutil.IUnitPreferencesDimensionCollection.get_item_by_name

    Retrieve a dimension from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IUnitPreferencesDimension`

