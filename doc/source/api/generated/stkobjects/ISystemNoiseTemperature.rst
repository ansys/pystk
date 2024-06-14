ISystemNoiseTemperature
=======================

.. py:class:: ISystemNoiseTemperature

   object
   
   Provide access to the system noise temperature parameters.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~compute_type`
            * - :py:meth:`~constant_noise_temperature`
            * - :py:meth:`~antenna_to_lna_line_temperature`
            * - :py:meth:`~lna_to_receiver_line_temperature`
            * - :py:meth:`~lna_noise_figure`
            * - :py:meth:`~lna_temperature`
            * - :py:meth:`~antenna_noise_temperature`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ISystemNoiseTemperature


Property detail
---------------

.. py:property:: compute_type
    :canonical: ansys.stk.core.stkobjects.ISystemNoiseTemperature.compute_type
    :type: "NOISE_TEMP_COMPUTE_TYPE"

    Gets or sets the system noise temperature compute type.

.. py:property:: constant_noise_temperature
    :canonical: ansys.stk.core.stkobjects.ISystemNoiseTemperature.constant_noise_temperature
    :type: float

    Gets or sets the constant system noise temperature value.

.. py:property:: antenna_to_lna_line_temperature
    :canonical: ansys.stk.core.stkobjects.ISystemNoiseTemperature.antenna_to_lna_line_temperature
    :type: float

    Gets or sets the antenna to LNA line temperature.

.. py:property:: lna_to_receiver_line_temperature
    :canonical: ansys.stk.core.stkobjects.ISystemNoiseTemperature.lna_to_receiver_line_temperature
    :type: float

    Gets or sets the LNA to receiver line temperature.

.. py:property:: lna_noise_figure
    :canonical: ansys.stk.core.stkobjects.ISystemNoiseTemperature.lna_noise_figure
    :type: float

    Gets or sets the LNA noise figure.

.. py:property:: lna_temperature
    :canonical: ansys.stk.core.stkobjects.ISystemNoiseTemperature.lna_temperature
    :type: float

    Gets or sets the LNA temperature.

.. py:property:: antenna_noise_temperature
    :canonical: ansys.stk.core.stkobjects.ISystemNoiseTemperature.antenna_noise_temperature
    :type: "IAgAntennaNoiseTemperature"

    Gets the interface for setting the antenna noise temperature parameters.


