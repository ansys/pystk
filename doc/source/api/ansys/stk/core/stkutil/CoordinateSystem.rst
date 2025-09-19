CoordinateSystem
================

.. py:class:: ansys.stk.core.stkutil.CoordinateSystem

   IntEnum


.. py:currentmodule:: CoordinateSystem

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - Represents coordinate system not supported by the Object Model.

            * - :py:attr:`~ALIGNMENT_AT_EPOCH`
              - Alignment at Epoch: an inertial system coincident with ECF at the Coord Epoch. Often used to specify launch trajectories.

            * - :py:attr:`~B1950`
              - B1950: X points toward the mean vernal equinox and Z points along the mean rotation axis of the Earth at the beginning of the Besselian year 1950 and corresponds to 31 December 1949 22:09:07.2 or JD 2433282.423.

            * - :py:attr:`~FIXED`
              - Fixed: X is fixed at 0 deg longitude, Y is fixed at 90 deg longitude, and Z is directed toward the north pole.

            * - :py:attr:`~J2000`
              - J2000: X points toward the mean vernal equinox and Z points along the mean rotation axis of the Earth on 1 Jan 2000 at 12:00:00.00 TDB, which corresponds to JD 2451545.0 TDB.

            * - :py:attr:`~MEAN_OF_DATE`
              - Mean of Date: X points toward the mean vernal equinox and Z points along the mean rotation axis of the Earth at the Orbit Epoch.

            * - :py:attr:`~MEAN_OF_EPOCH`
              - Mean of Epoch: X points toward the mean vernal equinox and Z points along the mean rotation axis of the Earth at the Coord Epoch.

            * - :py:attr:`~TEME_OF_DATE`
              - TEME of Date: X points toward the mean vernal equinox and Z points along the true rotation axis of the Earth at the Orbit Epoch.

            * - :py:attr:`~TEME_OF_EPOCH`
              - TEME of Epoch: X points toward the mean vernal equinox and Z points along the true rotation axis of the Earth at the Coord Epoch.

            * - :py:attr:`~TRUE_OF_DATE`
              - True of Date: X points toward the true vernal equinox and Z points along the true rotation axis of the Earth at the Orbit Epoch.

            * - :py:attr:`~TRUE_OF_EPOCH`
              - True of Epoch: X points toward the true vernal equinox and Z points along the true rotation axis of the Earth at the Coord Epoch.

            * - :py:attr:`~TRUE_OF_REFERENCE_DATE`
              - True of Ref Date: A special case of True of Epoch. Instead of the Coord Epoch, this system uses a Reference Date defined in the Integration Control page of the scenario's PODS properties.

            * - :py:attr:`~ICRF`
              - ICRF: International Celestial Reference Frame.

            * - :py:attr:`~MEAN_EARTH`
              - Mean Earth.

            * - :py:attr:`~FIXED_NO_LIBRATION`
              - uses an analytic formula not modeling lunar libration.

            * - :py:attr:`~FIXED_IAU2003`
              - Fixed_IAU2003.

            * - :py:attr:`~PRINCIPAL_AXES421`
              - PrincipalAxes_421.

            * - :py:attr:`~PRINCIPAL_AXES403`
              - PrincipalAxes_403.

            * - :py:attr:`~INERTIAL`
              - Inertial.

            * - :py:attr:`~J2000_ECLIPTIC`
              - The mean ecliptic system evaluated at the J2000 epoch. The mean ecliptic plane is defined as the rotation of the J2000 XY plane about the J2000 X axis by the mean obliquity defined using FK5 IAU76 theory.

            * - :py:attr:`~TRUE_ECLIPTIC_OF_DATE`
              - The true ecliptic system, evaluated at each given time. The true ecliptic plane is defined as the rotation of the J2000 XY plane about the J2000 X axis by the true obliquity defined using FK5 IAU76 theory.

            * - :py:attr:`~PRINCIPAL_AXES430`
              - PrincipalAxes_430.

            * - :py:attr:`~TRUE_OF_DATE_ROTATING`
              - TrueOfDateRotating: Like the Fixed system, but ignores pole wander. The XY plane is the same as the XY plane of the TrueOfDate system, and the system rotates about the TrueOfDate Z-axis.

            * - :py:attr:`~ECLIPTIC_J2000ICRF`
              - EclipticJ2000ICRF: An ecliptic system that is a fixed offset of the ICRF system, found by rotating the ICRF system about its X-axis by the mean obliquity at the J2000 epoch (i.e., 84381.448 arcSecs). The ecliptic plane is the XY-plane of this system.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkutil import CoordinateSystem


