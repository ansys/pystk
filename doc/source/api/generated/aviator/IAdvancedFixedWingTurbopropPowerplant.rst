IAdvancedFixedWingTurbopropPowerplant
=====================================

.. py:class:: IAdvancedFixedWingTurbopropPowerplant

   object
   
   Interface used to access the options for the Turboprop powerplant strategy in the advanced fixed wing tool.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~max_sea_level_static_power`
            * - :py:meth:`~propeller_count`
            * - :py:meth:`~propeller_diameter`
            * - :py:meth:`~fuel_flow`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAdvancedFixedWingTurbopropPowerplant


Property detail
---------------

.. py:property:: max_sea_level_static_power
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTurbopropPowerplant.max_sea_level_static_power
    :type: float

    Gets or sets the maximum static power of the engine at sea level.

.. py:property:: propeller_count
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTurbopropPowerplant.propeller_count
    :type: int

    Gets or sets the number of propellers.

.. py:property:: propeller_diameter
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTurbopropPowerplant.propeller_diameter
    :type: float

    Gets or sets the propeller diameter.

.. py:property:: fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTurbopropPowerplant.fuel_flow
    :type: float

    Gets or sets the engine's fuel flow at max power.


