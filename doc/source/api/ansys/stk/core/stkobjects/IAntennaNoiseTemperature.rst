IAntennaNoiseTemperature
========================

.. py:class:: ansys.stk.core.stkobjects.IAntennaNoiseTemperature

   object
   
   Provide access to the antenna noise temperature parameters.

.. py:currentmodule:: IAntennaNoiseTemperature

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaNoiseTemperature.compute_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaNoiseTemperature.constant_noise_temperature`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaNoiseTemperature.use_earth`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaNoiseTemperature.use_sun`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaNoiseTemperature.use_atmosphere`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaNoiseTemperature.use_urban_terrestrial`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaNoiseTemperature.use_rain`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaNoiseTemperature.use_clouds_fog`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaNoiseTemperature.use_tropo_scint`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaNoiseTemperature.use_cosmic_background`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaNoiseTemperature.inherit_scenario_earth_temperature`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaNoiseTemperature.local_earth_temperature`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaNoiseTemperature.other_noise_temperature`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaNoiseTemperature.use_external`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaNoiseTemperature.external_noise_file`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaNoiseTemperature.use_iono_fading`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAntennaNoiseTemperature


Property detail
---------------

.. py:property:: compute_type
    :canonical: ansys.stk.core.stkobjects.IAntennaNoiseTemperature.compute_type
    :type: NOISE_TEMP_COMPUTE_TYPE

    Gets or sets the system noise temperature compute type.

.. py:property:: constant_noise_temperature
    :canonical: ansys.stk.core.stkobjects.IAntennaNoiseTemperature.constant_noise_temperature
    :type: float

    Gets or sets the constant system noise temperature value.

.. py:property:: use_earth
    :canonical: ansys.stk.core.stkobjects.IAntennaNoiseTemperature.use_earth
    :type: bool

    Gets or sets the flag to use noise due to the earth.

.. py:property:: use_sun
    :canonical: ansys.stk.core.stkobjects.IAntennaNoiseTemperature.use_sun
    :type: bool

    Gets or sets the flag to use noise due to the sun.

.. py:property:: use_atmosphere
    :canonical: ansys.stk.core.stkobjects.IAntennaNoiseTemperature.use_atmosphere
    :type: bool

    Gets or sets the flag to use noise due to the atmosphere.

.. py:property:: use_urban_terrestrial
    :canonical: ansys.stk.core.stkobjects.IAntennaNoiseTemperature.use_urban_terrestrial
    :type: bool

    Gets or sets the flag to use noise due to the urban/terrestrial.

.. py:property:: use_rain
    :canonical: ansys.stk.core.stkobjects.IAntennaNoiseTemperature.use_rain
    :type: bool

    Gets or sets the flag to use noise due to the rain.

.. py:property:: use_clouds_fog
    :canonical: ansys.stk.core.stkobjects.IAntennaNoiseTemperature.use_clouds_fog
    :type: bool

    Gets or sets the flag to use noise due to the clouds and fog.

.. py:property:: use_tropo_scint
    :canonical: ansys.stk.core.stkobjects.IAntennaNoiseTemperature.use_tropo_scint
    :type: bool

    Gets or sets the flag to use noise due to the tropospheric scintillation.

.. py:property:: use_cosmic_background
    :canonical: ansys.stk.core.stkobjects.IAntennaNoiseTemperature.use_cosmic_background
    :type: bool

    Gets or sets the flag to use noise due to the cosmic background.

.. py:property:: inherit_scenario_earth_temperature
    :canonical: ansys.stk.core.stkobjects.IAntennaNoiseTemperature.inherit_scenario_earth_temperature
    :type: bool

    Gets or sets the flag to inherit the scenairo earth temperature.

.. py:property:: local_earth_temperature
    :canonical: ansys.stk.core.stkobjects.IAntennaNoiseTemperature.local_earth_temperature
    :type: float

    Gets or sets the local earth temperature.

.. py:property:: other_noise_temperature
    :canonical: ansys.stk.core.stkobjects.IAntennaNoiseTemperature.other_noise_temperature
    :type: float

    Gets or sets additional misc. noise temperature.

.. py:property:: use_external
    :canonical: ansys.stk.core.stkobjects.IAntennaNoiseTemperature.use_external
    :type: bool

    Gets or sets the flag to use noise due to an external source.

.. py:property:: external_noise_file
    :canonical: ansys.stk.core.stkobjects.IAntennaNoiseTemperature.external_noise_file
    :type: str

    Gets or sets the external noise file path.

.. py:property:: use_iono_fading
    :canonical: ansys.stk.core.stkobjects.IAntennaNoiseTemperature.use_iono_fading
    :type: bool

    Gets or sets the flag to use noise due to the ionospheric fading.


