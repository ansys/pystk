ATMOSPHERIC_DENSITY_MODEL
=========================

.. py:class:: ansys.stk.core.stkobjects.ATMOSPHERIC_DENSITY_MODEL

   IntEnum


.. py:currentmodule:: ATMOSPHERIC_DENSITY_MODEL

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~STANDARD_ATMOS_MODEL_1976`
              - 1976 Standard Atmosphere: look-up model based on the satellite's altitude, with a valid range of 86km - 1000 km.

            * - :py:attr:`~CIRA72`
              - CIRA 1972: empirical model of atmospheric temperature and densities as recommended by the Committee on Space Research (COSPAR). Lower altitude boundary is 90 km.

            * - :py:attr:`~EXPONENTIAL_MODEL`
              - Do not use this enumeration, as it is deprecated. Exponential Model: uses equation calculating atmospheric density on basis of a specified altitude, reference density, reference altitude and scale altitude.

            * - :py:attr:`~HARRIS_PRIESTER`
              - Harris-Priester: takes into account a 10.7 cm solar flux level and diurnal bulge. Uses density tables. Valid range of 0-1000 km.

            * - :py:attr:`~JACCHIA_ROBERTS`
              - Jacchia-Roberts: similar to Jacchia 1971 (below) but uses analytical methods to improve performance. Lower altitude boundary is 90 km.

            * - :py:attr:`~JACCHIA60`
              - Jacchia 1960: outdated atmospheric model provided for making comparisons with other software. Lower altitude boundary is 0 km.

            * - :py:attr:`~JACCHIA70`
              - Jacchia 1970: computes atmospheric density based on the composition of the atmosphere, which depends on altitude as well as seasonal variation. Valid range is 100-2500 km.

            * - :py:attr:`~JACCHIA71`
              - Jacchia 1971: similar to Jacchia 1970 (above), with improved treatment of certain solar effects.

            * - :py:attr:`~MSIS00`
              - NRLMSISE 2000: finds the total density by accounting for the contribution of N, N2, O, O2, He, Ar and H. Includes anomalous oxygen. 2000 version, valid range of 0-1000 km.

            * - :py:attr:`~MSIS86`
              - MSIS 1986: finds the total density by accounting for the contribution of N2, O, O2, He, Ar and H. 1986 version, valid range of 90-1000 km.

            * - :py:attr:`~MSIS90`
              - MSISE 1990: finds the total density by accounting for the contribution of N2, O, O2, He, Ar and H. 1990 version, valid range of 0-1000 km.

            * - :py:attr:`~UNKNOWN_DENS_MODEL`
              - Unsupported or unknown atmospheric density model.

            * - :py:attr:`~USER_DEFINED`
              - Do not use this enumeration, as it is deprecated. This option is no longer available for IAgVeHPOPForceModelDrag. User-defined atmospheric density model.

            * - :py:attr:`~DTM2012`
              - DTM 2012: The Drag Temperature Model (DTM), 2012 version, is a semi-empirical model which computes the temperature, density, and composition of the thermosphere. Developed at CNES. Valid range of 120 - 1500 km.

            * - :py:attr:`~DTM2020`
              - DTM 2020: The Drag Temperature Model (DTM), 2020 version, is a semi-empirical model which computes the temperature, density, and composition of the thermosphere. Developed at CNES. Valid range of 120 - 1500 km.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ATMOSPHERIC_DENSITY_MODEL


