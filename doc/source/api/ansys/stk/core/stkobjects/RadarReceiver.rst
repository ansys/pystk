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
              - Do not use this method, as it is deprecated. Use FilterComponentLinking on IAgRadarReceiver instead. Sets the current filter model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.set_rfstc_type`
              - Set the RF STC Type.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.set_ifstc_type`
              - Set the IF STC Type.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.antenna_to_lna_line_loss`
              - Get or set the antenna to LNA line loss.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.lna_gain`
              - Get or set the LNA gain.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.lna_to_receiver_line_loss`
              - Get or set the LNA to receiver line loss.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.use_rain`
              - Get or set the option for computing rain loss.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.supported_rain_outage_percent_values`
              - Get an array of supported rain outage percent values.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.rain_outage_percent`
              - Get or set the rain outage percent.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.pre_receive_gains_losses`
              - Get the collection of additional pre-receive gains and losses.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.enable_polarization`
              - Get or set the enable polarization option.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.enable_orthogonal_polarization`
              - Get or set the option for enabling the orthogonal polarization.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.polarization`
              - Get the polarization.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.lna_bandwidth`
              - Get or set the LNA bandwidth.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.enable_filter`
              - Get or set the flag determines whether or not to enable the Filter.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.supported_filters`
              - Do not use this property, as it is deprecated. Use FilterComponentLinking on IAgRadarReceiver instead. Gets an array of supported model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.filter`
              - Do not use this property, as it is deprecated. Use FilterComponentLinking on IAgRadarReceiver instead. Gets the current filter model.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.system_noise_temperature`
              - Get the system noise temperature interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.enable_rfstc`
              - Get or set whether the RF STC is enabled.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.rfstc`
              - Get the RF STC.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.enable_ifstc`
              - Get or set whether the IF STC is enabled.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.ifstc`
              - Get the IF STC.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.supported_rfstc_types`
              - Get the RF STC Types.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.supported_ifstc_types`
              - Get the IF STC Types.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.frequency`
              - Get or set the receiver center frequency.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarReceiver.filter_component_linking`
              - Get the link/embed controller for managing the filter model component.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RadarReceiver


Property detail
---------------

.. py:property:: antenna_to_lna_line_loss
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.antenna_to_lna_line_loss
    :type: float

    Get or set the antenna to LNA line loss.

.. py:property:: lna_gain
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.lna_gain
    :type: float

    Get or set the LNA gain.

.. py:property:: lna_to_receiver_line_loss
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.lna_to_receiver_line_loss
    :type: float

    Get or set the LNA to receiver line loss.

.. py:property:: use_rain
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.use_rain
    :type: bool

    Get or set the option for computing rain loss.

.. py:property:: supported_rain_outage_percent_values
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.supported_rain_outage_percent_values
    :type: list

    Get an array of supported rain outage percent values.

.. py:property:: rain_outage_percent
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.rain_outage_percent
    :type: float

    Get or set the rain outage percent.

.. py:property:: pre_receive_gains_losses
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.pre_receive_gains_losses
    :type: AdditionalGainLossCollection

    Get the collection of additional pre-receive gains and losses.

.. py:property:: enable_polarization
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.enable_polarization
    :type: bool

    Get or set the enable polarization option.

.. py:property:: enable_orthogonal_polarization
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.enable_orthogonal_polarization
    :type: bool

    Get or set the option for enabling the orthogonal polarization.

.. py:property:: polarization
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.polarization
    :type: IPolarization

    Get the polarization.

.. py:property:: lna_bandwidth
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.lna_bandwidth
    :type: float

    Get or set the LNA bandwidth.

.. py:property:: enable_filter
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.enable_filter
    :type: bool

    Get or set the flag determines whether or not to enable the Filter.

.. py:property:: supported_filters
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.supported_filters
    :type: list

    Do not use this property, as it is deprecated. Use FilterComponentLinking on IAgRadarReceiver instead. Gets an array of supported model names.

.. py:property:: filter
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.filter
    :type: IRFFilterModel

    Do not use this property, as it is deprecated. Use FilterComponentLinking on IAgRadarReceiver instead. Gets the current filter model.

.. py:property:: system_noise_temperature
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.system_noise_temperature
    :type: SystemNoiseTemperature

    Get the system noise temperature interface.

.. py:property:: enable_rfstc
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.enable_rfstc
    :type: bool

    Get or set whether the RF STC is enabled.

.. py:property:: rfstc
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.rfstc
    :type: IRadarSTCAttenuation

    Get the RF STC.

.. py:property:: enable_ifstc
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.enable_ifstc
    :type: bool

    Get or set whether the IF STC is enabled.

.. py:property:: ifstc
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.ifstc
    :type: IRadarSTCAttenuation

    Get the IF STC.

.. py:property:: supported_rfstc_types
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.supported_rfstc_types
    :type: list

    Get the RF STC Types.

.. py:property:: supported_ifstc_types
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.supported_ifstc_types
    :type: list

    Get the IF STC Types.

.. py:property:: frequency
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.frequency
    :type: float

    Get or set the receiver center frequency.

.. py:property:: filter_component_linking
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.filter_component_linking
    :type: IComponentLinkEmbedControl

    Get the link/embed controller for managing the filter model component.


Method detail
-------------

















.. py:method:: set_polarization_type(self, value: PolarizationType) -> None
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.set_polarization_type

    Set the current polarization type.

    :Parameters:

    **value** : :obj:`~PolarizationType`

    :Returns:

        :obj:`~None`







.. py:method:: set_filter(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.set_filter

    Do not use this method, as it is deprecated. Use FilterComponentLinking on IAgRadarReceiver instead. Sets the current filter model by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`





.. py:method:: set_rfstc_type(self, type_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.set_rfstc_type

    Set the RF STC Type.

    :Parameters:

    **type_name** : :obj:`~str`

    :Returns:

        :obj:`~None`




.. py:method:: set_ifstc_type(self, type_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.RadarReceiver.set_ifstc_type

    Set the IF STC Type.

    :Parameters:

    **type_name** : :obj:`~str`

    :Returns:

        :obj:`~None`







