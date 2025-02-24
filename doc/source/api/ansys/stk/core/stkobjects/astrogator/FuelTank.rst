FuelTank
========

.. py:class:: ansys.stk.core.stkobjects.astrogator.FuelTank

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   Fuel Tank parameters.

.. py:currentmodule:: FuelTank

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.FuelTank.tank_pressure`
              - Get or set the fuel tank pressure. Uses Pressure Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.FuelTank.tank_volume`
              - Get or set the volume of the fuel tank. Uses SmallVolume Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.FuelTank.tank_temperature`
              - Get or set the temperature of the fuel tank. Uses Temperature Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.FuelTank.fuel_density`
              - Get or set the density of the fuel. Uses SmallDensity Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.FuelTank.fuel_mass`
              - Get or set the mass of the spacecraft propellant. Uses Mass Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.FuelTank.maximum_fuel_mass`
              - Get or set the maximum fuel mass of the spacecraft; this parameter specifically applies to Finite Maneuver segments that are being executed in Backward Sequences. Uses Mass Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import FuelTank


Property detail
---------------

.. py:property:: tank_pressure
    :canonical: ansys.stk.core.stkobjects.astrogator.FuelTank.tank_pressure
    :type: float

    Get or set the fuel tank pressure. Uses Pressure Dimension.

.. py:property:: tank_volume
    :canonical: ansys.stk.core.stkobjects.astrogator.FuelTank.tank_volume
    :type: float

    Get or set the volume of the fuel tank. Uses SmallVolume Dimension.

.. py:property:: tank_temperature
    :canonical: ansys.stk.core.stkobjects.astrogator.FuelTank.tank_temperature
    :type: float

    Get or set the temperature of the fuel tank. Uses Temperature Dimension.

.. py:property:: fuel_density
    :canonical: ansys.stk.core.stkobjects.astrogator.FuelTank.fuel_density
    :type: float

    Get or set the density of the fuel. Uses SmallDensity Dimension.

.. py:property:: fuel_mass
    :canonical: ansys.stk.core.stkobjects.astrogator.FuelTank.fuel_mass
    :type: float

    Get or set the mass of the spacecraft propellant. Uses Mass Dimension.

.. py:property:: maximum_fuel_mass
    :canonical: ansys.stk.core.stkobjects.astrogator.FuelTank.maximum_fuel_mass
    :type: float

    Get or set the maximum fuel mass of the spacecraft; this parameter specifically applies to Finite Maneuver segments that are being executed in Backward Sequences. Uses Mass Dimension.


