VEHICLE_PROPAGATOR_TYPE
=======================

.. py:class:: ansys.stk.core.stkobjects.VEHICLE_PROPAGATOR_TYPE

   IntEnum


.. py:currentmodule:: VEHICLE_PROPAGATOR_TYPE

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN_PROPAGATOR`
              - Unknown propagator (all vehicles).

            * - :py:attr:`~PROPAGATOR_HPOP`
              - High Precision Orbit Propagator (satellites and missiles): handles circular, elliptical, parabolic and hyperbolic orbits at distances ranging from the surface of the Earth to the orbit of the Moon and beyond.

            * - :py:attr:`~PROPAGATOR_J2_PERTURBATION`
              - J2 Perturbation (1st-order) (satellites): accounts for secular variations in the orbit elements due to Earth oblateness, but does not model atmospheric drag or solar or lunar gravitational forces.

            * - :py:attr:`~PROPAGATOR_J4_PERTURBATION`
              - J4 Perburbation (2nd order) (satellites): accounts for secular variations in orbit elements due to Earth oblateness, but doesn't model atmos. drag or solar or lunar grav. forces. Includes 1st and 2nd order effects of J2 and 1st order effects of J4.

            * - :py:attr:`~PROPAGATOR_LOP`
              - Long-term Orbit Propagator (satellites): allows accurate prediction of the motion of a satellite's orbit over many months or years.

            * - :py:attr:`~PROPAGATOR_SGP4`
              - SGP4 (satellites): a standard AFSPACECOM propagator used with two-line mean element (TLE) sets.

            * - :py:attr:`~PROPAGATOR_SPICE`
              - SPICE (satellites): reads ephemeris from binary files that are in a standard format produced by the Jet Propulsion Laboratory (JPL).

            * - :py:attr:`~PROPAGATOR_STK_EXTERNAL`
              - STK external (all vehicles): allows you to read the ephemeris for a satellite from a file.

            * - :py:attr:`~PROPAGATOR_TWO_BODY`
              - Two Body(Keplerian motion) propagator (satellites and missiles): considers only the force of gravity from the Earth, which is modeled as a point mass.

            * - :py:attr:`~PROPAGATOR_USER_EXTERNAL`
              - User-External propagator.

            * - :py:attr:`~PROPAGATOR_GREAT_ARC`
              - Great Arc (aircraft, ships and ground vehicles): defines a point-by-point path over the surface of the Earth with position and altitude defined at each point.

            * - :py:attr:`~PROPAGATOR_BALLISTIC`
              - Ballistic (missiles): defines vehicles following an elliptical path that begins and ends at the Earth's surface.

            * - :py:attr:`~PROPAGATOR_SIMPLE_ASCENT`
              - Simple Ascent (launch vehicles): creates an ascent trajectory based on launch and insertion parameters.

            * - :py:attr:`~PROPAGATOR_ASTROGATOR`
              - Astrogator propagator.

            * - :py:attr:`~PROPAGATOR_REALTIME`
              - Realtime propagator.

            * - :py:attr:`~PROPAGATOR_GPS`
              - GPS propagator.

            * - :py:attr:`~PROPAGATOR_AVIATOR`
              - Aviator propagator.

            * - :py:attr:`~PROPAGATOR11_PARAM`
              - The 11-Parameter propagator models geostationary satellites using 11-Parameter files. The propagator uses an algorithm documented in Intelsat Earth Station Standards (IESS) IESS-412 (Rev. 2), available at www.celestrak.com.

            * - :py:attr:`~PROPAGATOR_SP3`
              - The SP3 propagator reads .sp3 files of type 'a' and 'c' and allows you to use multiple files in sequence. These files are used to provide precise GPS orbits from the National Geodetic Survey (NGS).


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VEHICLE_PROPAGATOR_TYPE


