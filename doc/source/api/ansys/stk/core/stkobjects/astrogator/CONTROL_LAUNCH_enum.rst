CONTROL_LAUNCH
==============

.. py:class:: ansys.stk.core.stkobjects.astrogator.CONTROL_LAUNCH

   IntEnum


.. py:currentmodule:: CONTROL_LAUNCH

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~EPOCH`
              - The date and time of the launch.

            * - :py:attr:`~GEODETIC_LATITUDE`
              - The geodetic latitude of the launch location.

            * - :py:attr:`~GEODETIC_LONGITUDE`
              - The geodetic longitude of the launch location.

            * - :py:attr:`~GEODETIC_ALTITUDE`
              - The geodetic altitude of the launch location.

            * - :py:attr:`~GEOCENTRIC_LATITUDE`
              - The geocentric latitude of the launch location.

            * - :py:attr:`~GEOCENTRIC_LONGITUDE`
              - The geocentric longitude of the launch location.

            * - :py:attr:`~GEOCENTRIC_RADIUS`
              - The geocentric radius of the launch location.

            * - :py:attr:`~TIME_OF_FLIGHT`
              - The time of flight, from launch until burnout.

            * - :py:attr:`~BURNOUT_GEOCENTRIC_LATITUDE`
              - The geocentric latitude of the burnout point.

            * - :py:attr:`~BURNOUT_GEOCENTRIC_LONGITUDE`
              - The geocentric longitude of the burnout point.

            * - :py:attr:`~BURNOUT_GEOCENTRIC_RADIUS`
              - The geocentric radius of the burnout point.

            * - :py:attr:`~BURNOUT_GEODETIC_LATITUDE`
              - The geodetic latitude of the burnout point.

            * - :py:attr:`~BURNOUT_GEODETIC_LONGITUDE`
              - The geodetic longitude of the burnout point.

            * - :py:attr:`~BURNOUT_GEODETIC_ALTITUDE`
              - The geodetic altitude of the burnout point.

            * - :py:attr:`~BURNOUT_AZIMUTH_ALTITUDE_AZIMUTH`
              - The geodetic azimuth of the launch trajectory.

            * - :py:attr:`~BURNOUT_AZIMUTH_ALTITUDE_DOWNRANGE_DIST`
              - The geodetic downrange distance of the burnout point.

            * - :py:attr:`~BURNOUT_AZIMUTH_ALTITUDE_ALTITUDE`
              - The geodetic altitude of the burnout point.

            * - :py:attr:`~BURNOUT_AZIMUTH_RADIUS_AZIMUTH`
              - The geocentric azimuth of the launch trajectory.

            * - :py:attr:`~BURNOUT_AZIMUTH_RADIUS_DOWNRANGE_DIST`
              - The geocentric downrange distance of the burnout point.

            * - :py:attr:`~BURNOUT_AZIMUTH_RADIUS_RADIUS`
              - The geocentric radius of the burnout point.

            * - :py:attr:`~BURNOUT_FIXED_VELOCITY`
              - The burnout velocity in the fixed frame.

            * - :py:attr:`~BURNOUT_INERTIAL_VELOCITY`
              - The burnout velocity in the inertial frame.

            * - :py:attr:`~BURNOUT_INERTIAL_VELOCITY_AZIMUTH`
              - Inertial Velocity Azimuth - the angle from the projection of north in the local horizontal plane to the inertial velocity vector, right handed.

            * - :py:attr:`~BURNOUT_INERTIAL_HORIZONTAL_FLIGHT_PATH_ANGLE`
              - Inertial Horizontal FPA - the angle from the local horizontal to the inertial velocity vector, positive towards radius. It is also 90 degrees minus vertical flight path angle.

            * - :py:attr:`~DRY_MASS`
              - Dry Mass - the mass of the spacecraft exclusive of propellant.

            * - :py:attr:`~CD`
              - Drag Coefficient (Cd) - the dimensionless drag coefficient associated with the drag area.

            * - :py:attr:`~DRAG_AREA`
              - Drag Area - the cross-sectional area of the spacecraft assumed perpendicular to the direction of motion, used for atmospheric drag calculations.

            * - :py:attr:`~CR`
              - Solar Radiation Pressure (Spherical) Coefficient (Cr) - the reflectivity of the spacecraft used for solar radiation pressure calculations, where 2.0 is fully reflective and 1.0 is not reflective at all.

            * - :py:attr:`~SRP_AREA`
              - Solar Radiation Pressure (Spherical) Area - the cross-sectional area of the spacecraft assumed perpendicular to the direction of solar radiation, used for solar radiation calculations.

            * - :py:attr:`~CK`
              - Radiation Pressure (Albedo/Thermal) Coefficient (Ck) - the reflectivity of the spacecraft used for central body radiation pressure (albedo / thermal pressure) calculations, where 2.0 is fully reflective and 1.0 is not reflective at all.

            * - :py:attr:`~RADIATION_PRESSURE_AREA`
              - Radiation Pressure (Albedo/Thermal) Area - the cross-sectional area of the spacecraft assumed perpendicular to the direction of central body radiation, used for central body radiation (albedo / thermal pressure) calculations.

            * - :py:attr:`~K1`
              - GPS Solar Radiation Pressure K1 - if you are using a non-spherical SRP model, this field defines the model's K1 (scale) value.

            * - :py:attr:`~K2`
              - GPS Solar Radiation Pressure K2 - if you are using a non-spherical SRP model, this field defines the model's K2 (scale) value.

            * - :py:attr:`~TANK_PRESSURE`
              - The fuel tank pressure.

            * - :py:attr:`~TANK_VOLUME`
              - The volume of the fuel tank.

            * - :py:attr:`~TANK_TEMP`
              - The fuel tank temperature.

            * - :py:attr:`~FUEL_DENSITY`
              - The density of the fuel tank.

            * - :py:attr:`~FUEL_MASS`
              - The mass of the spacecraft propellant.

            * - :py:attr:`~MAX_FUEL_MASS`
              - Maximum Fuel Mass - the maximum fuel mass of the spacecraft; this parameter specifically applies to Finite Maneuver segments that are being executed in Backward Sequences.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import CONTROL_LAUNCH


