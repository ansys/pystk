SystemNoiseTemperature
======================

.. py:class:: ansys.stk.core.stkobjects.SystemNoiseTemperature

   Class defining system noise temperature.

.. py:currentmodule:: SystemNoiseTemperature

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SystemNoiseTemperature.compute_type`
              - Gets or sets the system noise temperature compute type.
            * - :py:attr:`~ansys.stk.core.stkobjects.SystemNoiseTemperature.constant_noise_temperature`
              - Gets or sets the constant system noise temperature value.
            * - :py:attr:`~ansys.stk.core.stkobjects.SystemNoiseTemperature.antenna_to_lna_line_temperature`
              - Gets or sets the antenna to LNA line temperature.
            * - :py:attr:`~ansys.stk.core.stkobjects.SystemNoiseTemperature.lna_to_receiver_line_temperature`
              - Gets or sets the LNA to receiver line temperature.
            * - :py:attr:`~ansys.stk.core.stkobjects.SystemNoiseTemperature.lna_noise_figure`
              - Gets or sets the LNA noise figure.
            * - :py:attr:`~ansys.stk.core.stkobjects.SystemNoiseTemperature.lna_temperature`
              - Gets or sets the LNA temperature.
            * - :py:attr:`~ansys.stk.core.stkobjects.SystemNoiseTemperature.antenna_noise_temperature`
              - Gets the interface for setting the antenna noise temperature parameters.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SystemNoiseTemperature


Property detail
---------------

.. py:property:: compute_type
    :canonical: ansys.stk.core.stkobjects.SystemNoiseTemperature.compute_type
    :type: NOISE_TEMPERATURE_COMPUTE_TYPE

    Gets or sets the system noise temperature compute type.

.. py:property:: constant_noise_temperature
    :canonical: ansys.stk.core.stkobjects.SystemNoiseTemperature.constant_noise_temperature
    :type: float

    Gets or sets the constant system noise temperature value.

.. py:property:: antenna_to_lna_line_temperature
    :canonical: ansys.stk.core.stkobjects.SystemNoiseTemperature.antenna_to_lna_line_temperature
    :type: float

    Gets or sets the antenna to LNA line temperature.

.. py:property:: lna_to_receiver_line_temperature
    :canonical: ansys.stk.core.stkobjects.SystemNoiseTemperature.lna_to_receiver_line_temperature
    :type: float

    Gets or sets the LNA to receiver line temperature.

.. py:property:: lna_noise_figure
    :canonical: ansys.stk.core.stkobjects.SystemNoiseTemperature.lna_noise_figure
    :type: float

    Gets or sets the LNA noise figure.

.. py:property:: lna_temperature
    :canonical: ansys.stk.core.stkobjects.SystemNoiseTemperature.lna_temperature
    :type: float

    Gets or sets the LNA temperature.

.. py:property:: antenna_noise_temperature
    :canonical: ansys.stk.core.stkobjects.SystemNoiseTemperature.antenna_noise_temperature
    :type: AntennaNoiseTemperature

    Gets the interface for setting the antenna noise temperature parameters.


