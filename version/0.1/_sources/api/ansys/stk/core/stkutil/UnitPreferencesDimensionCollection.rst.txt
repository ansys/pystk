UnitPreferencesDimensionCollection
==================================

.. py:class:: ansys.stk.core.stkutil.UnitPreferencesDimensionCollection

   Object that contains a collection of dimensions.

.. py:currentmodule:: UnitPreferencesDimensionCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.UnitPreferencesDimensionCollection.item`
              - Return an UnitPreferencesDimension given a Dimension name or an index.
            * - :py:attr:`~ansys.stk.core.stkutil.UnitPreferencesDimensionCollection.set_current_unit`
              - Return the Current unit for a Dimension.
            * - :py:attr:`~ansys.stk.core.stkutil.UnitPreferencesDimensionCollection.get_current_unit_abbrv`
              - Return the Current Unit for a Dimension.
            * - :py:attr:`~ansys.stk.core.stkutil.UnitPreferencesDimensionCollection.reset_units`
              - Reset the unitpreferences to the Default units.
            * - :py:attr:`~ansys.stk.core.stkutil.UnitPreferencesDimensionCollection.get_item_by_index`
              - Retrieve a dimension from the collection by index.
            * - :py:attr:`~ansys.stk.core.stkutil.UnitPreferencesDimensionCollection.get_item_by_name`
              - Retrieve a dimension from the collection by name.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.UnitPreferencesDimensionCollection.count`
              - Return the number of items in the collection.
            * - :py:attr:`~ansys.stk.core.stkutil.UnitPreferencesDimensionCollection.mission_elapsed_time`
              - The MissionElapsedTime.
            * - :py:attr:`~ansys.stk.core.stkutil.UnitPreferencesDimensionCollection.julian_date_offset`
              - The JulianDateOffset.
            * - :py:attr:`~ansys.stk.core.stkutil.UnitPreferencesDimensionCollection._new_enum`
              - Return a collection of UnitPreferencesDimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkutil import UnitPreferencesDimensionCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkutil.UnitPreferencesDimensionCollection.count
    :type: int

    Return the number of items in the collection.

.. py:property:: mission_elapsed_time
    :canonical: ansys.stk.core.stkutil.UnitPreferencesDimensionCollection.mission_elapsed_time
    :type: typing.Any

    The MissionElapsedTime.

.. py:property:: julian_date_offset
    :canonical: ansys.stk.core.stkutil.UnitPreferencesDimensionCollection.julian_date_offset
    :type: float

    The JulianDateOffset.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkutil.UnitPreferencesDimensionCollection._new_enum
    :type: EnumeratorProxy

    Return a collection of UnitPreferencesDimension.


Method detail
-------------

.. py:method:: item(self, index_or_name: typing.Any) -> UnitPreferencesDimension
    :canonical: ansys.stk.core.stkutil.UnitPreferencesDimensionCollection.item

    Return an UnitPreferencesDimension given a Dimension name or an index.

    :Parameters:

        **index_or_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~UnitPreferencesDimension`


.. py:method:: set_current_unit(self, dimension: str, unit_abbrv: str) -> None
    :canonical: ansys.stk.core.stkutil.UnitPreferencesDimensionCollection.set_current_unit

    Return the Current unit for a Dimension.

    :Parameters:

        **dimension** : :obj:`~str`

        **unit_abbrv** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: get_current_unit_abbrv(self, index_or_dim_name: typing.Any) -> str
    :canonical: ansys.stk.core.stkutil.UnitPreferencesDimensionCollection.get_current_unit_abbrv

    Return the Current Unit for a Dimension.

    :Parameters:

        **index_or_dim_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~str`






.. py:method:: reset_units(self) -> None
    :canonical: ansys.stk.core.stkutil.UnitPreferencesDimensionCollection.reset_units

    Reset the unitpreferences to the Default units.

    :Returns:

        :obj:`~None`

.. py:method:: get_item_by_index(self, index: int) -> UnitPreferencesDimension
    :canonical: ansys.stk.core.stkutil.UnitPreferencesDimensionCollection.get_item_by_index

    Retrieve a dimension from the collection by index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~UnitPreferencesDimension`

.. py:method:: get_item_by_name(self, name: str) -> UnitPreferencesDimension
    :canonical: ansys.stk.core.stkutil.UnitPreferencesDimensionCollection.get_item_by_name

    Retrieve a dimension from the collection by name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~UnitPreferencesDimension`

