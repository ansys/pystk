IRotorcraftProp
===============

.. py:class:: IRotorcraftProp

   object
   
   Interface used to access the Propulsion options for a rotorcraft.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~powerplant_type`
            * - :py:meth:`~max_sl_power`
            * - :py:meth:`~max_sl_fuel_flow`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IRotorcraftProp


Property detail
---------------

.. py:property:: powerplant_type
    :canonical: ansys.stk.core.stkobjects.aviator.IRotorcraftProp.powerplant_type
    :type: ROTORCRAFT_POWERPLANT_TYPE

    Gets or sets the rotorcraft's powerplant type.

.. py:property:: max_sl_power
    :canonical: ansys.stk.core.stkobjects.aviator.IRotorcraftProp.max_sl_power
    :type: float

    Gets or sets the maximum power at sea level.

.. py:property:: max_sl_fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.IRotorcraftProp.max_sl_fuel_flow
    :type: float

    Gets or sets the maximum fuel flow at sea level.


