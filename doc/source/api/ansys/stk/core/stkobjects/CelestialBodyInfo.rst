CelestialBodyInfo
=================

.. py:class:: ansys.stk.core.stkobjects.CelestialBodyInfo

   Bases: 

   Represents a celestial body information.

.. py:currentmodule:: CelestialBodyInfo

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CelestialBodyInfo.get_last_computed_direction_in_icrf`
              - Return the last computed direction vector in ICRF.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CelestialBodyInfo.identifier`
              - Gets the identification of the star as per star catalog.
            * - :py:attr:`~ansys.stk.core.stkobjects.CelestialBodyInfo.catalog_name`
              - Gets a name of the star catalog.
            * - :py:attr:`~ansys.stk.core.stkobjects.CelestialBodyInfo.ra`
              - Right ascention. Use the \"Angle\" dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.CelestialBodyInfo.dec`
              - Declination. Use the \"Angle\" dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.CelestialBodyInfo.parallax`
              - Trigonometric parallax. Use the \"Angle\" dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.CelestialBodyInfo.velocity`
              - Radial velocity.
            * - :py:attr:`~ansys.stk.core.stkobjects.CelestialBodyInfo.visual_magnitude`
              - Visual magnitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.CelestialBodyInfo.bminus_v`
              - Johnson B-V color index.
            * - :py:attr:`~ansys.stk.core.stkobjects.CelestialBodyInfo.effective_temperature`
              - Star's effective temperature. Use the \"Temperature\" dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.CelestialBodyInfo.magnitude_to_irradiance_conversion_factor`
              - Magnitude to irradiance conversion factor is not given directly in any catalog. This factor converts the Planck function radiance to a rescaled irradiance at Earth's distance from the star. Unitless.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CelestialBodyInfo


Property detail
---------------

.. py:property:: identifier
    :canonical: ansys.stk.core.stkobjects.CelestialBodyInfo.identifier
    :type: str

    Gets the identification of the star as per star catalog.

.. py:property:: catalog_name
    :canonical: ansys.stk.core.stkobjects.CelestialBodyInfo.catalog_name
    :type: str

    Gets a name of the star catalog.

.. py:property:: ra
    :canonical: ansys.stk.core.stkobjects.CelestialBodyInfo.ra
    :type: float

    Right ascention. Use the \"Angle\" dimension.

.. py:property:: dec
    :canonical: ansys.stk.core.stkobjects.CelestialBodyInfo.dec
    :type: float

    Declination. Use the \"Angle\" dimension.

.. py:property:: parallax
    :canonical: ansys.stk.core.stkobjects.CelestialBodyInfo.parallax
    :type: float

    Trigonometric parallax. Use the \"Angle\" dimension.

.. py:property:: velocity
    :canonical: ansys.stk.core.stkobjects.CelestialBodyInfo.velocity
    :type: float

    Radial velocity.

.. py:property:: visual_magnitude
    :canonical: ansys.stk.core.stkobjects.CelestialBodyInfo.visual_magnitude
    :type: float

    Visual magnitude.

.. py:property:: bminus_v
    :canonical: ansys.stk.core.stkobjects.CelestialBodyInfo.bminus_v
    :type: float

    Johnson B-V color index.

.. py:property:: effective_temperature
    :canonical: ansys.stk.core.stkobjects.CelestialBodyInfo.effective_temperature
    :type: float

    Star's effective temperature. Use the \"Temperature\" dimension.

.. py:property:: magnitude_to_irradiance_conversion_factor
    :canonical: ansys.stk.core.stkobjects.CelestialBodyInfo.magnitude_to_irradiance_conversion_factor
    :type: float

    Magnitude to irradiance conversion factor is not given directly in any catalog. This factor converts the Planck function radiance to a rescaled irradiance at Earth's distance from the star. Unitless.


Method detail
-------------











.. py:method:: get_last_computed_direction_in_icrf(self) -> ICartesian3Vector
    :canonical: ansys.stk.core.stkobjects.CelestialBodyInfo.get_last_computed_direction_in_icrf

    Return the last computed direction vector in ICRF.

    :Returns:

        :obj:`~ICartesian3Vector`

