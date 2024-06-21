ICelestialBodyInfo
==================

.. py:class:: ansys.stk.core.stkobjects.ICelestialBodyInfo

   object
   
   The interface represents information associated with a celestial body.

.. py:currentmodule:: ICelestialBodyInfo

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ICelestialBodyInfo.get_last_computed_direction_in_icrf`
              - Return the last computed direction vector in ICRF.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ICelestialBodyInfo.identifier`
            * - :py:attr:`~ansys.stk.core.stkobjects.ICelestialBodyInfo.catalog_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.ICelestialBodyInfo.ra`
            * - :py:attr:`~ansys.stk.core.stkobjects.ICelestialBodyInfo.dec`
            * - :py:attr:`~ansys.stk.core.stkobjects.ICelestialBodyInfo.parallax`
            * - :py:attr:`~ansys.stk.core.stkobjects.ICelestialBodyInfo.velocity`
            * - :py:attr:`~ansys.stk.core.stkobjects.ICelestialBodyInfo.visual_magnitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.ICelestialBodyInfo.bminus_v`
            * - :py:attr:`~ansys.stk.core.stkobjects.ICelestialBodyInfo.effective_temperature`
            * - :py:attr:`~ansys.stk.core.stkobjects.ICelestialBodyInfo.magnitude_to_irradiance_conversion_factor`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ICelestialBodyInfo


Property detail
---------------

.. py:property:: identifier
    :canonical: ansys.stk.core.stkobjects.ICelestialBodyInfo.identifier
    :type: str

    Gets the identification of the star as per star catalog.

.. py:property:: catalog_name
    :canonical: ansys.stk.core.stkobjects.ICelestialBodyInfo.catalog_name
    :type: str

    Gets a name of the star catalog.

.. py:property:: ra
    :canonical: ansys.stk.core.stkobjects.ICelestialBodyInfo.ra
    :type: float

    Right ascention. Use the \"Angle\" dimension.

.. py:property:: dec
    :canonical: ansys.stk.core.stkobjects.ICelestialBodyInfo.dec
    :type: float

    Declination. Use the \"Angle\" dimension.

.. py:property:: parallax
    :canonical: ansys.stk.core.stkobjects.ICelestialBodyInfo.parallax
    :type: float

    Trigonometric parallax. Use the \"Angle\" dimension.

.. py:property:: velocity
    :canonical: ansys.stk.core.stkobjects.ICelestialBodyInfo.velocity
    :type: float

    Radial velocity.

.. py:property:: visual_magnitude
    :canonical: ansys.stk.core.stkobjects.ICelestialBodyInfo.visual_magnitude
    :type: float

    Visual magnitude.

.. py:property:: bminus_v
    :canonical: ansys.stk.core.stkobjects.ICelestialBodyInfo.bminus_v
    :type: float

    Johnson B-V color index.

.. py:property:: effective_temperature
    :canonical: ansys.stk.core.stkobjects.ICelestialBodyInfo.effective_temperature
    :type: float

    Star's effective temperature. Use the \"Temperature\" dimension.

.. py:property:: magnitude_to_irradiance_conversion_factor
    :canonical: ansys.stk.core.stkobjects.ICelestialBodyInfo.magnitude_to_irradiance_conversion_factor
    :type: float

    Magnitude to irradiance conversion factor is not given directly in any catalog. This factor converts the Planck function radiance to a rescaled irradiance at Earth's distance from the star. Unitless.


Method detail
-------------











.. py:method:: get_last_computed_direction_in_icrf(self) -> ICartesian3Vector
    :canonical: ansys.stk.core.stkobjects.ICelestialBodyInfo.get_last_computed_direction_in_icrf

    Return the last computed direction vector in ICRF.

    :Returns:

        :obj:`~ICartesian3Vector`

