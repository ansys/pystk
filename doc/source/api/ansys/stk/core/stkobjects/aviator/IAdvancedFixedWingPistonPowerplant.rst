IAdvancedFixedWingPistonPowerplant
==================================

.. py:class:: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingPistonPowerplant

   object
   
   Interface used to access the options for the Piston powerplant strategy in the advanced fixed wing tool.

.. py:currentmodule:: IAdvancedFixedWingPistonPowerplant

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingPistonPowerplant.max_sea_level_static_power`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingPistonPowerplant.critical_altitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingPistonPowerplant.propeller_count`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingPistonPowerplant.propeller_diameter`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingPistonPowerplant.fuel_flow`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAdvancedFixedWingPistonPowerplant


Property detail
---------------

.. py:property:: max_sea_level_static_power
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingPistonPowerplant.max_sea_level_static_power
    :type: float

    Gets or sets the maximum static power of the engine at sea level.

.. py:property:: critical_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingPistonPowerplant.critical_altitude
    :type: float

    Gets or sets the engine's critical altitude.

.. py:property:: propeller_count
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingPistonPowerplant.propeller_count
    :type: int

    Gets or sets the number of propellers.

.. py:property:: propeller_diameter
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingPistonPowerplant.propeller_diameter
    :type: float

    Gets or sets the propeller diameter.

.. py:property:: fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingPistonPowerplant.fuel_flow
    :type: float

    Gets or sets the engine's fuel flow at max power.


