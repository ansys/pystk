AntennaNoiseTemperature
=======================

.. py:class:: ansys.stk.core.stkobjects.AntennaNoiseTemperature

   Class defining antenna noise temperature.

.. py:currentmodule:: AntennaNoiseTemperature

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaNoiseTemperature.compute_type`
              - Gets or sets the system noise temperature compute type.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaNoiseTemperature.constant_noise_temperature`
              - Gets or sets the constant system noise temperature value.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaNoiseTemperature.use_earth`
              - Gets or sets the flag to use noise due to the earth.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaNoiseTemperature.use_sun`
              - Gets or sets the flag to use noise due to the sun.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaNoiseTemperature.use_atmosphere`
              - Gets or sets the flag to use noise due to the atmosphere.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaNoiseTemperature.use_urban_terrestrial`
              - Gets or sets the flag to use noise due to the urban/terrestrial.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaNoiseTemperature.use_rain`
              - Gets or sets the flag to use noise due to the rain.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaNoiseTemperature.use_clouds_fog`
              - Gets or sets the flag to use noise due to the clouds and fog.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaNoiseTemperature.use_tropospheric_scintillation`
              - Gets or sets the flag to use noise due to the tropospheric scintillation.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaNoiseTemperature.use_cosmic_background`
              - Gets or sets the flag to use noise due to the cosmic background.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaNoiseTemperature.inherit_scenario_earth_temperature`
              - Gets or sets the flag to inherit the scenairo earth temperature.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaNoiseTemperature.local_earth_temperature`
              - Gets or sets the local earth temperature.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaNoiseTemperature.other_noise_temperature`
              - Gets or sets additional misc. noise temperature.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaNoiseTemperature.use_external`
              - Gets or sets the flag to use noise due to an external source.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaNoiseTemperature.external_noise_filename`
              - Gets or sets the external noise file path.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaNoiseTemperature.use_ionospheric_fading`
              - Gets or sets the flag to use noise due to the ionospheric fading.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AntennaNoiseTemperature


Property detail
---------------

.. py:property:: compute_type
    :canonical: ansys.stk.core.stkobjects.AntennaNoiseTemperature.compute_type
    :type: NOISE_TEMPERATURE_COMPUTE_TYPE

    Gets or sets the system noise temperature compute type.

.. py:property:: constant_noise_temperature
    :canonical: ansys.stk.core.stkobjects.AntennaNoiseTemperature.constant_noise_temperature
    :type: float

    Gets or sets the constant system noise temperature value.

.. py:property:: use_earth
    :canonical: ansys.stk.core.stkobjects.AntennaNoiseTemperature.use_earth
    :type: bool

    Gets or sets the flag to use noise due to the earth.

.. py:property:: use_sun
    :canonical: ansys.stk.core.stkobjects.AntennaNoiseTemperature.use_sun
    :type: bool

    Gets or sets the flag to use noise due to the sun.

.. py:property:: use_atmosphere
    :canonical: ansys.stk.core.stkobjects.AntennaNoiseTemperature.use_atmosphere
    :type: bool

    Gets or sets the flag to use noise due to the atmosphere.

.. py:property:: use_urban_terrestrial
    :canonical: ansys.stk.core.stkobjects.AntennaNoiseTemperature.use_urban_terrestrial
    :type: bool

    Gets or sets the flag to use noise due to the urban/terrestrial.

.. py:property:: use_rain
    :canonical: ansys.stk.core.stkobjects.AntennaNoiseTemperature.use_rain
    :type: bool

    Gets or sets the flag to use noise due to the rain.

.. py:property:: use_clouds_fog
    :canonical: ansys.stk.core.stkobjects.AntennaNoiseTemperature.use_clouds_fog
    :type: bool

    Gets or sets the flag to use noise due to the clouds and fog.

.. py:property:: use_tropospheric_scintillation
    :canonical: ansys.stk.core.stkobjects.AntennaNoiseTemperature.use_tropospheric_scintillation
    :type: bool

    Gets or sets the flag to use noise due to the tropospheric scintillation.

.. py:property:: use_cosmic_background
    :canonical: ansys.stk.core.stkobjects.AntennaNoiseTemperature.use_cosmic_background
    :type: bool

    Gets or sets the flag to use noise due to the cosmic background.

.. py:property:: inherit_scenario_earth_temperature
    :canonical: ansys.stk.core.stkobjects.AntennaNoiseTemperature.inherit_scenario_earth_temperature
    :type: bool

    Gets or sets the flag to inherit the scenairo earth temperature.

.. py:property:: local_earth_temperature
    :canonical: ansys.stk.core.stkobjects.AntennaNoiseTemperature.local_earth_temperature
    :type: float

    Gets or sets the local earth temperature.

.. py:property:: other_noise_temperature
    :canonical: ansys.stk.core.stkobjects.AntennaNoiseTemperature.other_noise_temperature
    :type: float

    Gets or sets additional misc. noise temperature.

.. py:property:: use_external
    :canonical: ansys.stk.core.stkobjects.AntennaNoiseTemperature.use_external
    :type: bool

    Gets or sets the flag to use noise due to an external source.

.. py:property:: external_noise_filename
    :canonical: ansys.stk.core.stkobjects.AntennaNoiseTemperature.external_noise_filename
    :type: str

    Gets or sets the external noise file path.

.. py:property:: use_ionospheric_fading
    :canonical: ansys.stk.core.stkobjects.AntennaNoiseTemperature.use_ionospheric_fading
    :type: bool

    Gets or sets the flag to use noise due to the ionospheric fading.


