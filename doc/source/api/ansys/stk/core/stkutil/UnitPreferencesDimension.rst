UnitPreferencesDimension
========================

.. py:class:: ansys.stk.core.stkutil.UnitPreferencesDimension

   Object that contains info on the Dimension.

.. py:currentmodule:: UnitPreferencesDimension

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.UnitPreferencesDimension.set_current_unit`
              - Set the Unit for this simple dimension.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.UnitPreferencesDimension.available_units`
              - Return collection of Units.
            * - :py:attr:`~ansys.stk.core.stkutil.UnitPreferencesDimension.current_unit`
              - Return the current unit for this dimension.
            * - :py:attr:`~ansys.stk.core.stkutil.UnitPreferencesDimension.identifier`
              - Return the ID of the dimension.
            * - :py:attr:`~ansys.stk.core.stkutil.UnitPreferencesDimension.name`
              - Return the current Dimension's full name.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkutil import UnitPreferencesDimension


Property detail
---------------

.. py:property:: available_units
    :canonical: ansys.stk.core.stkutil.UnitPreferencesDimension.available_units
    :type: UnitPreferencesUnitCollection

    Return collection of Units.

.. py:property:: current_unit
    :canonical: ansys.stk.core.stkutil.UnitPreferencesDimension.current_unit
    :type: UnitPreferencesUnit

    Return the current unit for this dimension.

.. py:property:: identifier
    :canonical: ansys.stk.core.stkutil.UnitPreferencesDimension.identifier
    :type: int

    Return the ID of the dimension.

.. py:property:: name
    :canonical: ansys.stk.core.stkutil.UnitPreferencesDimension.name
    :type: str

    Return the current Dimension's full name.


Method detail
-------------





.. py:method:: set_current_unit(self, unit_abbrv: str) -> None
    :canonical: ansys.stk.core.stkutil.UnitPreferencesDimension.set_current_unit

    Set the Unit for this simple dimension.

    :Parameters:

        **unit_abbrv** : :obj:`~str`


    :Returns:

        :obj:`~None`

