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

            * - :py:attr:`~ansys.stk.core.stkutil.UnitPreferencesDimension.identifier`
              - Returns the ID of the dimension.
            * - :py:attr:`~ansys.stk.core.stkutil.UnitPreferencesDimension.name`
              - Returns the current Dimension's full name.
            * - :py:attr:`~ansys.stk.core.stkutil.UnitPreferencesDimension.available_units`
              - Returns collection of Units.
            * - :py:attr:`~ansys.stk.core.stkutil.UnitPreferencesDimension.current_unit`
              - Returns the current unit for this dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkutil import UnitPreferencesDimension


Property detail
---------------

.. py:property:: identifier
    :canonical: ansys.stk.core.stkutil.UnitPreferencesDimension.identifier
    :type: int

    Returns the ID of the dimension.

.. py:property:: name
    :canonical: ansys.stk.core.stkutil.UnitPreferencesDimension.name
    :type: str

    Returns the current Dimension's full name.

.. py:property:: available_units
    :canonical: ansys.stk.core.stkutil.UnitPreferencesDimension.available_units
    :type: UnitPreferencesUnitCollection

    Returns collection of Units.

.. py:property:: current_unit
    :canonical: ansys.stk.core.stkutil.UnitPreferencesDimension.current_unit
    :type: UnitPreferencesUnit

    Returns the current unit for this dimension.


Method detail
-------------





.. py:method:: set_current_unit(self, unitAbbrv: str) -> None
    :canonical: ansys.stk.core.stkutil.UnitPreferencesDimension.set_current_unit

    Set the Unit for this simple dimension.

    :Parameters:

    **unitAbbrv** : :obj:`~str`

    :Returns:

        :obj:`~None`

