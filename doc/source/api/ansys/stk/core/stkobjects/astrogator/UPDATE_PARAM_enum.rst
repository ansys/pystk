UPDATE_PARAM
============

.. py:class:: ansys.stk.core.stkobjects.astrogator.UPDATE_PARAM

   IntEnum


.. py:currentmodule:: UPDATE_PARAM

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~DRAG_AREA`
              - Drag Area - the cross-sectional area of the spacecraft assumed perpendicular to the direction of motion, used for atmospheric drag calculations.

            * - :py:attr:`~SRP_AREA`
              - Solar Radiation Pressure (Spherical) Area - the cross-sectional area of the spacecraft assumed perpendicular to the direction of solar radiation, used for solar radiation calculations.

            * - :py:attr:`~DRY_MASS`
              - Dry Mass - the mass of the spacecraft exclusive of propellant.

            * - :py:attr:`~FUEL_MASS`
              - The mass of the spacecraft propellant.

            * - :py:attr:`~FUEL_DENSITY`
              - The density of the fuel tank.

            * - :py:attr:`~TANK_PRESSURE`
              - The fuel tank pressure.

            * - :py:attr:`~TANK_TEMPERATURE`
              - The temperature of the fuel tank.

            * - :py:attr:`~CR`
              - Solar Radiation Pressure (Spherical) Coefficient (Cr) - the reflectivity of the spacecraft used for solar radiation pressure calculations, where 2.0 is fully reflective and 1.0 is not reflective at all.

            * - :py:attr:`~CD`
              - Drag Coefficient (Cd) - the dimensionless drag coefficient associated with the drag area.

            * - :py:attr:`~CK`
              - Radiation Pressure (Albedo/Thermal) Coefficient (Ck) - the reflectivity of the spacecraft used for central body radiation pressure (albedo / thermal pressure) calculations, where 2.0 is fully reflective and 1.0 is not reflective at all.

            * - :py:attr:`~RADIATION_PRESSURE_AREA`
              - Radiation Pressure (Albedo/Thermal) Area - the cross-sectional area of the spacecraft assumed perpendicular to the direction of central body radiation, used for central body radiation (albedo / thermal pressure) calculations.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import UPDATE_PARAM


