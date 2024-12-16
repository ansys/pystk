ControlUpdate
=============

.. py:class:: ansys.stk.core.stkobjects.astrogator.ControlUpdate

   IntEnum


.. py:currentmodule:: ControlUpdate

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~CD`
              - Drag Coefficient (Cd) - the dimensionless drag coefficient associated with the drag area.

            * - :py:attr:`~CR`
              - Solar Radiation Pressure (Spherical) Coefficient (Cr) - the reflectivity of the spacecraft used for solar radiation pressure calculations, where 2.0 is fully reflective and 1.0 is not reflective at all.

            * - :py:attr:`~DRAG_AREA`
              - Drag Area - the cross-sectional area of the spacecraft assumed perpendicular to the direction of motion, used for atmospheric drag calculations. Enter a value in the selected distance unit squared.

            * - :py:attr:`~DRY_MASS`
              - Dry Mass - the mass of the spacecraft exclusive of propellant. Enter a value in the selected mass unit (e.g. kg).

            * - :py:attr:`~FUEL_DENSITY`
              - Fuel Density - the density of the fuel tank. Enter a value in the selected mass unit per the selected distance unit cubed (e.g. kg/m^3).

            * - :py:attr:`~FUEL_MASS`
              - Fuel Mass - the mass of the spacecraft propellant. Enter a value in the selected mass unit (e.g. kg).

            * - :py:attr:`~RADIATION_PRESSURE_AREA`
              - The cross-sectional area of the spacecraft assumed perpendicular to the direction of central body radiation, used for central body radiation (albedo / thermal pressure) calculations. Enter a value in the selected distance unit squared.

            * - :py:attr:`~RADIATION_PRESSURE_COEFFICIENT`
              - Radiation Pressure (Albedo/Thermal) Coefficient (Ck) - the reflectivity of the spacecraft used for central body radiation pressure (albedo / thermal pressure) calculations, where 2.0 is fully reflective and 1.0 is not reflective at all.

            * - :py:attr:`~SRP_AREA`
              - Solar Radiation Pressure (Spherical) Area - the cross-sectional area of the spacecraft assumed perpendicular to the direction of solar radiation, used for solar radiation calculations. Enter a value in the selected distance unit squared.

            * - :py:attr:`~TANK_PRESSURE`
              - Tank Pressure - the fuel tank pressure. Enter a value in the selected pressure unit (e.g. Pa).

            * - :py:attr:`~TANK_TEMPERATURE`
              - Tank Temperature - the temperature of the fuel tank. Enter a value in the selected temperature unit.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ControlUpdate


