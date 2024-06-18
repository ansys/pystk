IUnitPreferencesDimension
=========================

.. py:class:: IUnitPreferencesDimension

   object
   
   Provide info on a Dimension from the global unit table.

.. py:currentmodule:: ansys.stk.core.stkutil

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_current_unit`
              - Set the Unit for this simple dimension.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~id`
            * - :py:meth:`~name`
            * - :py:meth:`~available_units`
            * - :py:meth:`~current_unit`


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
    :type: "IAgUnitPrefsUnitCollection"

    Returns collection of Units.

.. py:property:: current_unit
    :canonical: ansys.stk.core.stkutil.IUnitPreferencesDimension.current_unit
    :type: "IAgUnitPrefsUnit"

    Returns the current unit for this dimension.


Method detail
-------------





.. py:method:: set_current_unit(self, unitAbbrv:str) -> None

    Set the Unit for this simple dimension.

    :Parameters:

    **unitAbbrv** : :obj:`~str`

    :Returns:

        :obj:`~None`

