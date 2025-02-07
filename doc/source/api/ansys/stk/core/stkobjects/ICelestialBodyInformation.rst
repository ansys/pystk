ICelestialBodyInformation
=========================

.. py:class:: ansys.stk.core.stkobjects.ICelestialBodyInformation

   The interface represents information associated with a celestial body.

.. py:currentmodule:: ICelestialBodyInformation

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ICelestialBodyInformation.get_last_computed_direction_in_icrf`
              - Return the last computed direction vector in ICRF.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ICelestialBodyInformation.identifier`
              - Get the identification of the star as per star catalog.
            * - :py:attr:`~ansys.stk.core.stkobjects.ICelestialBodyInformation.catalog_name`
              - Get a name of the star catalog.
            * - :py:attr:`~ansys.stk.core.stkobjects.ICelestialBodyInformation.right_ascension`
              - Right ascention. Use the ``Angle`` dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ICelestialBodyInformation.declination`
              - Declination. Use the ``Angle`` dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ICelestialBodyInformation.parallax`
              - Trigonometric parallax. Use the ``Angle`` dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ICelestialBodyInformation.velocity`
              - Radial velocity.
            * - :py:attr:`~ansys.stk.core.stkobjects.ICelestialBodyInformation.visual_magnitude`
              - Visual magnitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.ICelestialBodyInformation.b_minus_v`
              - Johnson B-V color index.
            * - :py:attr:`~ansys.stk.core.stkobjects.ICelestialBodyInformation.effective_temperature`
              - Star's effective temperature. Use the ``Temperature`` dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ICelestialBodyInformation.magnitude_to_irradiance_conversion_factor`
              - Magnitude to irradiance conversion factor is not given directly in any catalog. This factor converts the Planck function radiance to a rescaled irradiance at Earth's distance from the star. Unitless.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ICelestialBodyInformation


Property detail
---------------

.. py:property:: identifier
    :canonical: ansys.stk.core.stkobjects.ICelestialBodyInformation.identifier
    :type: str

    Get the identification of the star as per star catalog.

.. py:property:: catalog_name
    :canonical: ansys.stk.core.stkobjects.ICelestialBodyInformation.catalog_name
    :type: str

    Get a name of the star catalog.

.. py:property:: right_ascension
    :canonical: ansys.stk.core.stkobjects.ICelestialBodyInformation.right_ascension
    :type: float

    Right ascention. Use the ``Angle`` dimension.

.. py:property:: declination
    :canonical: ansys.stk.core.stkobjects.ICelestialBodyInformation.declination
    :type: float

    Declination. Use the ``Angle`` dimension.

.. py:property:: parallax
    :canonical: ansys.stk.core.stkobjects.ICelestialBodyInformation.parallax
    :type: float

    Trigonometric parallax. Use the ``Angle`` dimension.

.. py:property:: velocity
    :canonical: ansys.stk.core.stkobjects.ICelestialBodyInformation.velocity
    :type: float

    Radial velocity.

.. py:property:: visual_magnitude
    :canonical: ansys.stk.core.stkobjects.ICelestialBodyInformation.visual_magnitude
    :type: float

    Visual magnitude.

.. py:property:: b_minus_v
    :canonical: ansys.stk.core.stkobjects.ICelestialBodyInformation.b_minus_v
    :type: float

    Johnson B-V color index.

.. py:property:: effective_temperature
    :canonical: ansys.stk.core.stkobjects.ICelestialBodyInformation.effective_temperature
    :type: float

    Star's effective temperature. Use the ``Temperature`` dimension.

.. py:property:: magnitude_to_irradiance_conversion_factor
    :canonical: ansys.stk.core.stkobjects.ICelestialBodyInformation.magnitude_to_irradiance_conversion_factor
    :type: float

    Magnitude to irradiance conversion factor is not given directly in any catalog. This factor converts the Planck function radiance to a rescaled irradiance at Earth's distance from the star. Unitless.


Method detail
-------------











.. py:method:: get_last_computed_direction_in_icrf(self) -> ICartesian3Vector
    :canonical: ansys.stk.core.stkobjects.ICelestialBodyInformation.get_last_computed_direction_in_icrf

    Return the last computed direction vector in ICRF.

    :Returns:

        :obj:`~ICartesian3Vector`

