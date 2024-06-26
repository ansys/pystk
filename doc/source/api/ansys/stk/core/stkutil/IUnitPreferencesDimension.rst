IUnitPreferencesDimension
=========================

.. py:class:: ansys.stk.core.stkutil.IUnitPreferencesDimension

   object
   
   Provide info on a Dimension from the global unit table.

.. py:currentmodule:: IUnitPreferencesDimension

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.IUnitPreferencesDimension.set_current_unit`
              - Set the Unit for this simple dimension.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.IUnitPreferencesDimension.id`
              - Returns the ID of the dimension.
            * - :py:attr:`~ansys.stk.core.stkutil.IUnitPreferencesDimension.name`
              - Returns the current Dimension's full name.
            * - :py:attr:`~ansys.stk.core.stkutil.IUnitPreferencesDimension.available_units`
              - Returns collection of Units.
            * - :py:attr:`~ansys.stk.core.stkutil.IUnitPreferencesDimension.current_unit`
              - Returns the current unit for this dimension.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkutil import IUnitPreferencesDimension


Property detail
---------------

.. py:property:: id
    :canonical: ansys.stk.core.stkutil.IUnitPreferencesDimension.id
    :type: int

    Returns the ID of the dimension.

.. py:property:: name
    :canonical: ansys.stk.core.stkutil.IUnitPreferencesDimension.name
    :type: str

    Returns the current Dimension's full name.

.. py:property:: available_units
    :canonical: ansys.stk.core.stkutil.IUnitPreferencesDimension.available_units
    :type: IUnitPreferencesUnitCollection

    Returns collection of Units.

.. py:property:: current_unit
    :canonical: ansys.stk.core.stkutil.IUnitPreferencesDimension.current_unit
    :type: IUnitPreferencesUnit

    Returns the current unit for this dimension.


Method detail
-------------





.. py:method:: set_current_unit(self, unitAbbrv: str) -> None
    :canonical: ansys.stk.core.stkutil.IUnitPreferencesDimension.set_current_unit

    Set the Unit for this simple dimension.

    :Parameters:

    **unitAbbrv** : :obj:`~str`

    :Returns:

        :obj:`~None`

