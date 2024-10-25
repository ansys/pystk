RadarReceiver
=============

.. py:class:: ansys.stk.core.stkobjects.RadarReceiver

   Class defining the radar transmitter.

.. py:currentmodule:: RadarReceiver

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.set_polarization_type`
              - Set the current polarization type.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.set_filter`
              - Set the current filter model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.set_rfstc_type`
              - Set the RF STC Type.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.set_ifstc_type`
              - Set the IF STC Type.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.antenna_to_lna_line_loss`
              - Gets or sets the antenna to LNA line loss.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.lna_gain`
              - Gets or sets the LNA gain.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.lna_to_receiver_line_loss`
              - Gets or sets the LNA to receiver line loss.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.use_rain`
              - Gets or sets the option for computing rain loss.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.supported_rain_outage_percent_values`
              - Gets an array of supported rain outage percent values.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.rain_outage_percent`
              - Gets or sets the rain outage percent.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.pre_receive_gains_losses`
              - Gets the collection of additional pre-receive gains and losses.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.enable_polarization`
              - Gets or sets the enable polarization option.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.enable_orthogonal_polarization`
              - Gets or sets the option for enabling the orthogonal polarization.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.polarization`
              - Gets the polarization.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.lna_bandwidth`
              - Gets or sets the LNA bandwidth.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.enable_filter`
              - Gets or set the flag determines whether or not to enable the Filter.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.supported_filters`
              - Gets an array of supported model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.filter`
              - Gets the current filter model.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.system_noise_temperature`
              - Gets the system noise temperature interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.enable_rfstc`
              - Gets or sets whether the RF STC is enabled.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.rfstc`
              - Gets the RF STC.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.enable_ifstc`
              - Gets or sets whether the IF STC is enabled.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.ifstc`
              - Gets the IF STC.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.supported_rfstc_types`
              - Gets the RF STC Types.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.supported_ifstc_types`
              - Gets the IF STC Types.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.frequency`
              - Gets or sets the receiver center frequency.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RadarReceiver


Property detail
---------------

.. py:property:: antenna_to_lna_line_loss
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.antenna_to_lna_line_loss
    :type: float

    Gets or sets the antenna to LNA line loss.

.. py:property:: lna_gain
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.lna_gain
    :type: float

    Gets or sets the LNA gain.

.. py:property:: lna_to_receiver_line_loss
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.lna_to_receiver_line_loss
    :type: float

    Gets or sets the LNA to receiver line loss.

.. py:property:: use_rain
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.use_rain
    :type: bool

    Gets or sets the option for computing rain loss.

.. py:property:: supported_rain_outage_percent_values
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.supported_rain_outage_percent_values
    :type: list

    Gets an array of supported rain outage percent values.

.. py:property:: rain_outage_percent
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.rain_outage_percent
    :type: float

    Gets or sets the rain outage percent.

.. py:property:: pre_receive_gains_losses
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.pre_receive_gains_losses
    :type: AdditionalGainLossCollection

    Gets the collection of additional pre-receive gains and losses.

.. py:property:: enable_polarization
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.enable_polarization
    :type: bool

    Gets or sets the enable polarization option.

.. py:property:: enable_orthogonal_polarization
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.enable_orthogonal_polarization
    :type: bool

    Gets or sets the option for enabling the orthogonal polarization.

.. py:property:: polarization
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.polarization
    :type: IPolarization

    Gets the polarization.

.. py:property:: lna_bandwidth
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.lna_bandwidth
    :type: float

    Gets or sets the LNA bandwidth.

.. py:property:: enable_filter
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.enable_filter
    :type: bool

    Gets or set the flag determines whether or not to enable the Filter.

.. py:property:: supported_filters
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.supported_filters
    :type: list

    Gets an array of supported model names.

.. py:property:: filter
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.filter
    :type: IRFFilterModel

    Gets the current filter model.

.. py:property:: system_noise_temperature
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.system_noise_temperature
    :type: SystemNoiseTemperature

    Gets the system noise temperature interface.

.. py:property:: enable_rfstc
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.enable_rfstc
    :type: bool

    Gets or sets whether the RF STC is enabled.

.. py:property:: rfstc
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.rfstc
    :type: IRadarSTCAttenuation

    Gets the RF STC.

.. py:property:: enable_ifstc
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.enable_ifstc
    :type: bool

    Gets or sets whether the IF STC is enabled.

.. py:property:: ifstc
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.ifstc
    :type: IRadarSTCAttenuation

    Gets the IF STC.

.. py:property:: supported_rfstc_types
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.supported_rfstc_types
    :type: list

    Gets the RF STC Types.

.. py:property:: supported_ifstc_types
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.supported_ifstc_types
    :type: list

    Gets the IF STC Types.

.. py:property:: frequency
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.frequency
    :type: float

    Gets or sets the receiver center frequency.


Method detail
-------------

















.. py:method:: set_polarization_type(self, val: POLARIZATION_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.set_polarization_type

    Set the current polarization type.

    :Parameters:

    **val** : :obj:`~POLARIZATION_TYPE`

    :Returns:

        :obj:`~None`







.. py:method:: set_filter(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.set_filter

    Set the current filter model by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`





.. py:method:: set_rfstc_type(self, typeName: str) -> None
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.set_rfstc_type

    Set the RF STC Type.

    :Parameters:

    **typeName** : :obj:`~str`

    :Returns:

        :obj:`~None`




.. py:method:: set_ifstc_type(self, typeName: str) -> None
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.set_ifstc_type

    Set the IF STC Type.

    :Parameters:

    **typeName** : :obj:`~str`

    :Returns:

        :obj:`~None`






