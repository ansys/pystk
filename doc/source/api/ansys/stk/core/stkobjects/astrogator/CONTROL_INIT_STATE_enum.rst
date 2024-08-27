CONTROL_INIT_STATE
==================

.. py:class:: ansys.stk.core.stkobjects.astrogator.CONTROL_INIT_STATE

   IntEnum


.. py:currentmodule:: CONTROL_INIT_STATE

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~FUEL_MASS`
              - Fuel Mass - the mass of the spacecraft propellant. Enter a value in the selected mass unit (e.g. kg).

            * - :py:attr:`~CARTESIAN_VX`
              - Vx Component - the X component of the spacecraft velocity vector.

            * - :py:attr:`~CARTESIAN_VY`
              - Vy Component - the Y component of the spacecraft velocity vector.

            * - :py:attr:`~CARTESIAN_VZ`
              - Vz Component - the Z component of the spacecraft velocity vector.

            * - :py:attr:`~CARTESIAN_X`
              - X Component - the X component of the spacecraft position vector.

            * - :py:attr:`~CARTESIAN_Y`
              - Y Component - the Y component of the spacecraft position vector.

            * - :py:attr:`~CARTESIAN_Z`
              - Z Component - the Z component of the spacecraft position vector.

            * - :py:attr:`~CD`
              - Drag Coefficient (Cd) - the dimensionless drag coefficient associated with the drag area.

            * - :py:attr:`~CR`
              - Solar Radiation Pressure (Spherical) Coefficient (Cr) - the reflectivity of the spacecraft used for solar radiation pressure calculations, where 2.0 is fully reflective and 1.0 is not reflective at all.

            * - :py:attr:`~DRAG_AREA`
              - Drag Area - the cross-sectional area of the spacecraft assumed perpendicular to the direction of motion, used for atmospheric drag calculations. Enter a value in the selected distance unit squared.

            * - :py:attr:`~DRY_MASS`
              - Dry Mass - the mass of the spacecraft exclusive of propellant. Enter a value in the selected mass unit (e.g. kg).

            * - :py:attr:`~EPOCH`
              - Epoch - the orbit epoch.

            * - :py:attr:`~FUEL_DENSITY`
              - Fuel Density - the density of the fuel tank.

            * - :py:attr:`~K1`
              - GPS Solar Radiation Pressure K1 - if you are using a non-spherical SRP model, this field defines the model's K1 (scale) value.

            * - :py:attr:`~K2`
              - GPS Solar Radiation Pressure K2 - if you are using a non-spherical SRP model, this field defines the model's K2 (Y bias) value.

            * - :py:attr:`~KEPLERIAN_ECCENTRICITY`
              - Eccentricity - the ratio of the distance between the foci to the major axis of the orbital ellipse. Dimensionless.

            * - :py:attr:`~KEPLERIAN_INC`
              - Inclination - the angle from the +Z axis of the coordinate system to the angular momentum vector of the spacecraft's orbit.

            * - :py:attr:`~KEPLERIAN_RAAN`
              - Right Ascension of Ascending Node - the angle between the X direction of the coordinate system and the point where the orbit crosses the X-Y plane in the +Z direction.

            * - :py:attr:`~KEPLERIAN_SMA`
              - Semimajor Axis - half the length of the major (longest) axis of the orbital ellipse.

            * - :py:attr:`~KEPLERIAN_TA`
              - True Anomaly - the angle from the periapsis of the orbit to the spacecraft's position vector, measured in the direction of spacecraft motion.

            * - :py:attr:`~KEPLERIAN_W`
              - Argument of Periapsis - the angle measured in the direction of spacecraft motion, in the orbit plane, from the ascending node to the periapsis of the orbit.

            * - :py:attr:`~RADIATION_PRESSURE_AREA`
              - Radiation Pressure (Albedo/Thermal) Area - the cross-sectional area of the spacecraft assumed perpendicular to the direction of central body radiation, used for central body radiation (albedo / thermal pressure) calculations.

            * - :py:attr:`~CK`
              - Radiation Pressure (Albedo/Thermal) Coefficient (Ck) - the reflectivity of the spacecraft used for central body radiation pressure (albedo / thermal pressure) calculations, where 2.0 is fully reflective and 1.0 is not reflective at all.

            * - :py:attr:`~SPHERICAL_AZ`
              - Velocity Azimuth - the angle in the spacecraft local horizontal plane between the projection of the velocity vector onto that plane and the local +Z direction measured as positive in the clockwise direction from north.

            * - :py:attr:`~SPHERICAL_DEC`
              - Declination - the angle from the X-Y plane of the coordinate system to the spacecraft position vector.

            * - :py:attr:`~SPHERICAL_HORIZONTAL_FPA`
              - Horizontal Flight Path Angle - the complement of the angle between the spacecraft velocity vector and the radius vector (90 deg minus the vertical flight path angle).

            * - :py:attr:`~SPHERICAL_RA`
              - Right Ascension - angle measured in the inertial equatorial plane from the inertial X axis in a right-handed sense about the inertial Z axis to the spacecraft position vector.

            * - :py:attr:`~SPHERICAL_R_MAGNITUDE`
              - Radius Magnitude - the magnitude of the spacecraft position vector.

            * - :py:attr:`~SPHERICAL_V_MAGNITUDE`
              - Velocity Magnitude - the magnitude of the spacecraft velocity vector.

            * - :py:attr:`~SRP_AREA`
              - Solar Radiation Pressure (Spherical) Area - the cross-sectional area of the spacecraft assumed perpendicular to the direction of solar radiation, used for solar radiation calculations.

            * - :py:attr:`~TANK_PRESSURE`
              - Tank Pressure - the fuel tank pressure.

            * - :py:attr:`~TANK_TEMP`
              - Tank Temperature - the temperature of the fuel tank.

            * - :py:attr:`~TARGET_VEC_IN_ASYMP_DEC`
              - Declination of Incoming Asymptote - the declination of the incoming asymptote in the selected coordinate system.

            * - :py:attr:`~TARGET_VEC_IN_ASYMP_RA`
              - Right Ascension of Incoming Asymptote - the right ascension of the hyperbolic incoming asymptote in the selected coordinate system.

            * - :py:attr:`~TARGET_VEC_IN_VEL_AZ_AT_PERIAPSIS`
              - Velocity Azimuth at Periapsis - the inertial flight path azimuth of the trajectory measured at periapsis.

            * - :py:attr:`~TARGET_VEC_IN_C3`
              - C3 Energy - the energy of the orbit, computed as - mu / a, where mu is the gravity constant of the central body and a is the semimajor axis.

            * - :py:attr:`~TARGET_VEC_IN_RAD_OF_PERIAPSIS`
              - Radius of Periapsis - distance from the center of mass of the central body to the periapsis of the hyperbolic orbit.

            * - :py:attr:`~TARGET_VEC_IN_TRUE_ANOMALY`
              - True Anomaly - the angle from the periapsis of the orbit to the spacecraft's position vector, measured in the direction of spacecraft motion.

            * - :py:attr:`~TARGET_VEC_OUT_ASYMP_DEC`
              - Declination of Outgoing Asymptote - the declination of the outgoing asymptote in the selected coordinate system.

            * - :py:attr:`~TARGET_VEC_OUT_ASYMP_RA`
              - Right Ascension of Outgoing Asymptote - the right ascension of the hyperbolic outgoing asymptote in the selected coordinate system.

            * - :py:attr:`~TARGET_VEC_OUT_VEL_AZ_AT_PERIAPSIS`
              - Velocity Azimuth at Periapsis - the inertial flight path azimuth of the trajectory measured at periapsis.

            * - :py:attr:`~TARGET_VEC_OUT_C3`
              - C3 Energy - the energy of the orbit, computed as - mu / a, where mu is the gravity constant of the central body and a is the semimajor axis.

            * - :py:attr:`~TARGET_VEC_OUT_RAD_OF_PERIAPSIS`
              - Radius of Periapsis - distance from the center of mass of the central body to the periapsis of the hyperbolic orbit.

            * - :py:attr:`~TARGET_VEC_OUT_TRUE_ANOMALY`
              - True Anomaly - the angle from the periapsis of the orbit to the spacecraft's position vector, measured in the direction of spacecraft motion.

            * - :py:attr:`~MAX_FUEL_MASS`
              - Maximum Fuel Mass - the maximum fuel mass of the spacecraft; this parameter specifically applies to Finite Maneuver segments that are being executed in Backward Sequences.

            * - :py:attr:`~TANK_VOLUME`
              - Tank Volume - the volume of the fuel tank.

            * - :py:attr:`~DELAUNAY_G`
              - G - Magnitude of orbital angular momentum, (G: sqrt(GM * p)).

            * - :py:attr:`~DELAUNAY_H`
              - H - Z component of orbital angular momentum, (H: G cos(inc)).

            * - :py:attr:`~DELAUNAY_INC`
              - Inclination - The angle between the angular momentum vector (perpendicular to the plane of the orbit) and the inertial Z axis.

            * - :py:attr:`~DELAUNAY_L`
              - L - Related to two-body orbital energy, (L: sqrt(GM * a)).

            * - :py:attr:`~DELAUNAY_MEAN_ANOMALY`
              - Mean Anomaly - The angle from the eccentricity vector to a position vector where the satellite would be if it were always moving at its average angular rate.

            * - :py:attr:`~DELAUNAY_RAAN`
              - Right Ascension of Ascending Node - The angle from the inertial X axis to the ascending node measured in a right-handed sense about the inertial Z axis in the equatorial plane.

            * - :py:attr:`~DELAUNAY_SEMI_LATUS_RECTUM`
              - Semi-latus Rectum - Distance from focus to orbit at true anomaly of 90 degrees.

            * - :py:attr:`~DELAUNAY_SMA`
              - Semimajor Axis - Half the length of the major (longest) axis of the orbital ellipse.

            * - :py:attr:`~DELAUNAY_W`
              - Argument of Periapsis - The angle from the ascending node to the eccentricity vector measured in the direction of the satellite's motion and in the orbit plane.

            * - :py:attr:`~EQUINOCTIAL_H`
              - H - With K, describe the shape and position of periapsis of the orbit, (H: ecc * sin(RAAN + w)).

            * - :py:attr:`~EQUINOCTIAL_K`
              - K - With H, describe the shape and position of periapsis of the orbit, (K: ecc * cos(RAAN + w)).

            * - :py:attr:`~EQUINOCTIAL_MEAN_LONGITUDE`
              - Mean Longitude - (RAAN + w + M).

            * - :py:attr:`~EQUINOCTIAL_MEAN_MOTION`
              - Mean Motion - The number of orbits per day (86400 sec/period), based on assumed two-body motion.

            * - :py:attr:`~EQUINOCTIAL_P`
              - P - With Q, describes the orientation of the orbit plane, (P: tan(inc/2) * sin(RAAN)).

            * - :py:attr:`~EQUINOCTIAL_Q`
              - Q - With P, describes the orientation of the orbit plane, (Q: tan(inc/2) * cos(RAAN)).

            * - :py:attr:`~EQUINOCTIAL_SMA`
              - Semimajor Axis - Half the length of the major (longest) axis of the orbital ellipse.

            * - :py:attr:`~MIXED_SPHERICAL_ALTITUDE`
              - Altitude - The object's position above or below the reference ellipsoid. Altitude is measured along a normal to the surface of the reference ellipsoid.

            * - :py:attr:`~MIXED_SPHERICAL_AZIMUTH`
              - Azimuth - The angle in the satellite local horizontal plane between the projection of the inertial velocity vector onto this plane and the local north direction measured as positive in the clockwise direction.

            * - :py:attr:`~MIXED_SPHERICAL_HORIZONTAL_FPA`
              - Horizontal Flight Path Angle - The complement of the angle between the inertial velocity vector and the radius vector.

            * - :py:attr:`~MIXED_SPHERICAL_LATITUDE`
              - Latitude - The geodetic latitude of a point is the angle between the normal to the reference ellipsoid that passes through the satellite position and the equatorial plane.

            * - :py:attr:`~MIXED_SPHERICAL_LONGITUDE`
              - Longitude.

            * - :py:attr:`~MIXED_SPHERICAL_VERTICAL_FPA`
              - Vertical Flight Path Angle -  The angle between the inertial velocity vector and the radius vector.

            * - :py:attr:`~MIXED_SPHERICAL_V_MAGNITUDE`
              - Velocity Magnitude - The magnitude of the inertial velocity vector.

            * - :py:attr:`~SPHERICAL_VERTICAL_FPA`
              - Vertical Flight Path Angle -  The angle between the inertial velocity vector and the radius vector.

            * - :py:attr:`~KEPLERIAN_APOAPSIS_ALTITUDE_SHAPE`
              - Apoapsis Altitude - Shape Parameter - Distance from the surface of the central body to the point of maximum radius in the orbit.

            * - :py:attr:`~KEPLERIAN_APOAPSIS_ALTITUDE_SIZE`
              - Apoapsis Altitude - Size Parameter - Distance from the surface of the central body to the point of maximum radius in the orbit.

            * - :py:attr:`~KEPLERIAN_APOAPSIS_RAD_SHAPE`
              - Apoapsis Radius - Shape Parameter - Distance from the center of the central body to the point of maximum radius in the orbit.

            * - :py:attr:`~KEPLERIAN_APOAPSIS_RAD_SIZE`
              - Apoapsis Radius - Size Parameter - Distance from the center of the central body to the point of maximum radius in the orbit.

            * - :py:attr:`~KEPLERIAN_ARG_LAT`
              - Argument of Latitude - The sum of the True Anomaly and the Argument of Perigee.

            * - :py:attr:`~KEPLERIAN_ECCENTRICITY_ANOMALY`
              - Eccentric Anomaly - Angle measured with an origin at the center of the ellipse from the direction of perigee to a point on a circumscribing circle from which a line perpendicular to the SMA intersects the position of the satellite on the ellipse.

            * - :py:attr:`~KEPLERIAN_LAN`
              - Longitude of Ascending Node - Longitude of the Ascending Node is the Earth-fixed longitude where the satellite has crossed the inertial equator from south to north based on an assumption of two-body motion.

            * - :py:attr:`~KEPLERIAN_MEAN_ANOMALY`
              - Mean Anomaly - The angle from the eccentricity vector to a position vector where the satellite would be if it were always moving at its average angular rate.

            * - :py:attr:`~KEPLERIAN_MEAN_MOTION`
              - Mean Motion - The number of orbits per day (86400 sec/period), based on assumed two-body motion.

            * - :py:attr:`~KEPLERIAN_PERIAPSIS_ALTITUDE_SHAPE`
              - Periapsis Altitude - Shape Parameter - Distance from the surface of the central body to the point of minimum radius in the orbit.

            * - :py:attr:`~KEPLERIAN_PERIAPSIS_ALTITUDE_SIZE`
              - Periapsis Altitude - Size Parameter - Distance from the surface of the central body to the point of minimum radius in the orbit.

            * - :py:attr:`~KEPLERIAN_PERIAPSIS_RAD_SHAPE`
              - Periapsis Radius - Shape Parameter - Distance from the center of the central body to the point of minimum radius in the orbit.

            * - :py:attr:`~KEPLERIAN_PERIAPSIS_RAD_SIZE`
              - Periapsis Radius - Size Parameter - Distance from the surface of the central body to the point of minimum radius in the orbit.

            * - :py:attr:`~KEPLERIAN_PERIOD`
              - Period - The duration of one orbit, based on assumed two-body motion.

            * - :py:attr:`~KEPLERIAN_TIME_PAST_AN`
              - Time Past Ascending Node - The elapsed time since the last ascending node crossing based on assumed two-body motion.

            * - :py:attr:`~KEPLERIAN_TIME_PAST_PERIAPSIS`
              - Time Past Periapsis - The elapsed time since the last perigee passage based on assumed two-body motion.

            * - :py:attr:`~SPHERICAL_RANGE_RATE_DEC`
              - Declination - the angle from the X-Y plane of the coordinate system to the spacecraft position vector.

            * - :py:attr:`~SPHERICAL_RANGE_RATE_RA`
              - Right Ascension - angle measured in the inertial equatorial plane from the inertial X axis in a right-handed sense about the inertial Z axis to the spacecraft position vector.

            * - :py:attr:`~SPHERICAL_RANGE_RATE_RANGE`
              - Range - distance of an object from the center point of the coordinate system.

            * - :py:attr:`~SPHERICAL_RANGE_RATE_DEC_RATE`
              - Declination Rate - the change of the declination angle over time.

            * - :py:attr:`~SPHERICAL_RANGE_RATE_RA_RATE`
              - Right Ascension Rate - the change of the right ascension angle over time.

            * - :py:attr:`~SPHERICAL_RANGE_RATE_RANGE_RATE`
              - Range Rate - the change in the range over time.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import CONTROL_INIT_STATE


