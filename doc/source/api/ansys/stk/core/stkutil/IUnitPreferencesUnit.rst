IUnitPreferencesUnit
====================

.. py:class:: IUnitPreferencesUnit

   object
   
   Provide info about a unit.

.. py:currentmodule:: ansys.stk.core.stkutil

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~full_name`
            * - :py:meth:`~abbrv`
            * - :py:meth:`~id`
            * - :py:meth:`~dimension`


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
    :type: IAgUnitPrefsDim

    Returns the Dimension for this unit.


