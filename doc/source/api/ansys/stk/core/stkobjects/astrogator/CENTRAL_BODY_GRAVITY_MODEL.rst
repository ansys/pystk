CENTRAL_BODY_GRAVITY_MODEL
==========================

.. py:class:: CENTRAL_BODY_GRAVITY_MODEL

   IntEnum


.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ZONALS_TO_J4`
              - ZonalsToJ4 - (various) Gravity model for all central bodies except Sun, Earth and Moon.

            * - :py:attr:`~EARTH_SIMPLE`
              - Earth Simple gravity model.

            * - :py:attr:`~WGS84`
              - WGS84 - (Earth) World Geodetic System 1984; WGS 84 was created by the Defense Mapping Agency (DMA).

            * - :py:attr:`~EGM96`
              - EGM96 - (Earth) Earth Gravity Model 1996, a geopotential model of the Earth consisting of spherical harmonic coefficients complete to degree and order 360. Developed jointly by NGA (formerly known as NIMA), NASA Goddard and Ohio State University.

            * - :py:attr:`~GEMT1`
              - GEMT1 - (Earth) Goddard Earth Model T1.

            * - :py:attr:`~JGM2`
              - JGM2 - (Earth) Joint Gravity Model version 2, a model that describes the Earth gravity field up to degree and order 70, developed by NASA/GSFC Space Geodesy Branch, the University of Texas Center for Space Research and CNES.

            * - :py:attr:`~JGM3`
              - JGM3 - (Earth) Joint Gravity Model version 3, a model that describes the Earth gravity field up to degree and order 70, developed by the University of Texas and NASA/GSFC.

            * - :py:attr:`~WSG84EGM96`
              - WGS84 EGM96 - (Earth) Uses the coefficients from EGM96 with the shape model of WGS84. This model is the recommended gravity model of the WGS84 definition document: NIMA TR8350.2, Third Edition, 4 July 1997.

            * - :py:attr:`~WGS84_OLD`
              - WGS84 old - (Earth) Old version of WGS84.

            * - :py:attr:`~GLGM2`
              - GLGM2 - (Moon) GM = 4.9028029535968e+12, reference distance = 1,738,000 m.

            * - :py:attr:`~LP165P`
              - LP165P - (Moon) GM = 4.902801056E+12, reference distance = 1,738,000.0 m.

            * - :py:attr:`~ICARUS1987`
              - Icarus1987 - (Mercury) GM = 2.203209e+013, reference distance = 2,439,000 m. Reference: Anderson, J. J., Colombo, G., Esposito, P. B., Lau E. L., and Trager, G. B. 'The Mass, Gravity Field, and Ephemeris of Mercury', Icarus 71, 337-349, 1987.

            * - :py:attr:`~MGNP180U`
              - MGNP180U - (Venus) GM = 3.248585920790000E+14, reference distance = 6,051,000.0 m.

            * - :py:attr:`~GMM1`
              - GMM1 - (Mars) GM = 4.28283579647735e+13, reference distance = 3,394,200.0 m.

            * - :py:attr:`~GMM2B`
              - GMM2B - (Mars) GM = 4.28283719012840e+13, reference distance = 3,397,000 m. Reference: These numbers came from the GMM-2B model published at `NASA <https://www.nasa.gov/>`_ and were gotten from Journal of Geophysical Research, November 2000.

            * - :py:attr:`~MARS50_C`
              - Mars50c - (Mars) GM = 4.2828370371000e+13, reference distance = 3,394,200 m.

            * - :py:attr:`~JUP230`
              - JUP230 - (Jupiter) GM = 1.26686535e+017, reference distance = 71,492,000 m. Reference: Jacobson, R. A. The JUP230 orbit solution, 2003.

            * - :py:attr:`~ASTRON2004`
              - Astron2004 - (Saturn) GM = 3.7931284e+016, reference distance = 60,330,000 m.

            * - :py:attr:`~ASTRON_ASTRO1991`
              - AstronAstro1991 - (Neptune) GM = 6.835107e+015, reference distance = 25,225,000 m.

            * - :py:attr:`~ICARUS2001`
              - Icarus2001 - (Callisto) GM = 7.179292e+12, reference distance = 2,410,300 m.

            * - :py:attr:`~SCIENCE1998`
              - Science1998 - (Europa) GM =3.20272e+012, reference distance = 1,565,000 m.

            * - :py:attr:`~NATURE1996`
              - Nature1996 - (Ganymede) GM = 9.8866e+12, reference distance = 2,634,000 m.

            * - :py:attr:`~J_GEO_RES2001`
              - JGeoRes2001 - (Io) GM = 5.96e+12, reference distance = 1,821,600 m.

            * - :py:attr:`~GGM01C`
              - GGM01C - (Earth).

            * - :py:attr:`~GGM02C`
              - GGM02C - (Earth).

            * - :py:attr:`~WGS72_ZONALS_TO_J4`
              - WGS72 ZonalsToJ4 - (Earth).

            * - :py:attr:`~LP100J`
              - LP100J - (Moon).

            * - :py:attr:`~LP100K`
              - LP100K - (Moon).

            * - :py:attr:`~LP150Q`
              - LP150Q - (Moon).

            * - :py:attr:`~LP75G`
              - LP75G - (Moon).


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import CENTRAL_BODY_GRAVITY_MODEL


