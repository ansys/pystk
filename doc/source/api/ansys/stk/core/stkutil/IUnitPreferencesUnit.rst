IUnitPreferencesUnit
====================

.. py:class:: ansys.stk.core.stkutil.IUnitPreferencesUnit

   object
   
   Provide info about a unit.

.. py:currentmodule:: IUnitPreferencesUnit

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.IUnitPreferencesUnit.full_name`
              - Returns the fullname of the unit.
            * - :py:attr:`~ansys.stk.core.stkutil.IUnitPreferencesUnit.abbrv`
              - Returns the abbreviation of the unit.
            * - :py:attr:`~ansys.stk.core.stkutil.IUnitPreferencesUnit.id`
              - Returns the ID of the unit.
            * - :py:attr:`~ansys.stk.core.stkutil.IUnitPreferencesUnit.dimension`
              - Returns the Dimension for this unit.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkutil import IUnitPreferencesUnit


Property detail
---------------

.. py:property:: full_name
    :canonical: ansys.stk.core.stkutil.IUnitPreferencesUnit.full_name
    :type: str

    Returns the fullname of the unit.

.. py:property:: abbrv
    :canonical: ansys.stk.core.stkutil.IUnitPreferencesUnit.abbrv
    :type: str

    Returns the abbreviation of the unit.

.. py:property:: id
    :canonical: ansys.stk.core.stkutil.IUnitPreferencesUnit.id
    :type: int

    Returns the ID of the unit.

.. py:property:: dimension
    :canonical: ansys.stk.core.stkutil.IUnitPreferencesUnit.dimension
    :type: IUnitPreferencesDimension

    Returns the Dimension for this unit.


