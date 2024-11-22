ReceiverModelMedium
===================

.. py:class:: ansys.stk.core.stkobjects.ReceiverModelMedium

   Bases: :py:class:`~ansys.stk.core.stkobjects.IReceiverModel`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining a medium receiver model.

.. py:currentmodule:: ReceiverModelMedium

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelMedium.set_filter`
              - Do not use this method, as it is deprecated. Use FilterComponentLinking on IAgReceiverModelMedium instead. Sets the current filter model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelMedium.set_demodulator`
              - Set the current demodulator model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelMedium.set_polarization_type`
              - Set the current polarization type.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelMedium.enable_filter`
              - Gets or set the flag determines whether or not to enable the Filter.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelMedium.supported_filters`
              - This property is deprecated. Use FilterComponentLinking on IAgReceiverModelMedium instead. Gets an array of supported filter model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelMedium.filter`
              - This property is deprecated. Use FilterComponentLinking on IAgReceiverModelMedium instead. Gets the current filter model.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelMedium.pre_receive_gains_losses`
              - Gets the collection of additional pre-receive gains and losses.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelMedium.pre_demodulator_gains_losses`
              - Gets the collection of additional pre-demod gains and losses.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelMedium.link_margin`
              - Gets the interface for configuring the link margin computation parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelMedium.scale_bandwidth_automatically`
              - Gets or set the auto scale bandwidth option.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelMedium.bandwidth`
              - Gets or set the bandwidth.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelMedium.select_demodulator_automatically`
              - Gets or set the auto select demodulator option.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelMedium.supported_demodulators`
              - Gets an array of supported demodulator model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelMedium.demodulator`
              - Gets the current demodulator model.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelMedium.use_rain`
              - Gets or sets the option for computing rain loss.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelMedium.supported_rain_outage_percent_values`
              - Gets an array of supported rain outage percent values.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelMedium.rain_outage_percent`
              - Gets or sets the rain outage percent.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelMedium.enable_polarization`
              - Gets or sets the enable polarization option.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelMedium.polarization`
              - Gets the polarization.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelMedium.track_frequency_automatically`
              - Gets or set the auto track frequency option.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelMedium.frequency`
              - Gets or set the frequency.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelMedium.antenna_gain`
              - Gets or set the antennaGain.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelMedium.antenna_to_lna_line_loss`
              - Gets or sets the antenna to LNA line loss.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelMedium.lna_gain`
              - Gets or sets the LNA gain.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelMedium.lna_to_receiver_line_loss`
              - Gets or sets the LNA to receiver line loss.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelMedium.system_noise_temperature`
              - Gets the system noise temperature interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelMedium.interference`
              - Gets the radio frequency interference.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelMedium.filter_component_linking`
              - Gets the link/embed controller for managing the filter model component.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ReceiverModelMedium


Property detail
---------------

.. py:property:: enable_filter
    :canonical: ansys.stk.core.stkobjects.ReceiverModelMedium.enable_filter
    :type: bool

    Gets or set the flag determines whether or not to enable the Filter.

.. py:property:: supported_filters
    :canonical: ansys.stk.core.stkobjects.ReceiverModelMedium.supported_filters
    :type: list

    This property is deprecated. Use FilterComponentLinking on IAgReceiverModelMedium instead. Gets an array of supported filter model names.

.. py:property:: filter
    :canonical: ansys.stk.core.stkobjects.ReceiverModelMedium.filter
    :type: IRFFilterModel

    This property is deprecated. Use FilterComponentLinking on IAgReceiverModelMedium instead. Gets the current filter model.

.. py:property:: pre_receive_gains_losses
    :canonical: ansys.stk.core.stkobjects.ReceiverModelMedium.pre_receive_gains_losses
    :type: AdditionalGainLossCollection

    Gets the collection of additional pre-receive gains and losses.

.. py:property:: pre_demodulator_gains_losses
    :canonical: ansys.stk.core.stkobjects.ReceiverModelMedium.pre_demodulator_gains_losses
    :type: AdditionalGainLossCollection

    Gets the collection of additional pre-demod gains and losses.

.. py:property:: link_margin
    :canonical: ansys.stk.core.stkobjects.ReceiverModelMedium.link_margin
    :type: LinkMargin

    Gets the interface for configuring the link margin computation parameters.

.. py:property:: scale_bandwidth_automatically
    :canonical: ansys.stk.core.stkobjects.ReceiverModelMedium.scale_bandwidth_automatically
    :type: bool

    Gets or set the auto scale bandwidth option.

.. py:property:: bandwidth
    :canonical: ansys.stk.core.stkobjects.ReceiverModelMedium.bandwidth
    :type: float

    Gets or set the bandwidth.

.. py:property:: select_demodulator_automatically
    :canonical: ansys.stk.core.stkobjects.ReceiverModelMedium.select_demodulator_automatically
    :type: bool

    Gets or set the auto select demodulator option.

.. py:property:: supported_demodulators
    :canonical: ansys.stk.core.stkobjects.ReceiverModelMedium.supported_demodulators
    :type: list

    Gets an array of supported demodulator model names.

.. py:property:: demodulator
    :canonical: ansys.stk.core.stkobjects.ReceiverModelMedium.demodulator
    :type: IDemodulatorModel

    Gets the current demodulator model.

.. py:property:: use_rain
    :canonical: ansys.stk.core.stkobjects.ReceiverModelMedium.use_rain
    :type: bool

    Gets or sets the option for computing rain loss.

.. py:property:: supported_rain_outage_percent_values
    :canonical: ansys.stk.core.stkobjects.ReceiverModelMedium.supported_rain_outage_percent_values
    :type: list

    Gets an array of supported rain outage percent values.

.. py:property:: rain_outage_percent
    :canonical: ansys.stk.core.stkobjects.ReceiverModelMedium.rain_outage_percent
    :type: float

    Gets or sets the rain outage percent.

.. py:property:: enable_polarization
    :canonical: ansys.stk.core.stkobjects.ReceiverModelMedium.enable_polarization
    :type: bool

    Gets or sets the enable polarization option.

.. py:property:: polarization
    :canonical: ansys.stk.core.stkobjects.ReceiverModelMedium.polarization
    :type: IPolarization

    Gets the polarization.

.. py:property:: track_frequency_automatically
    :canonical: ansys.stk.core.stkobjects.ReceiverModelMedium.track_frequency_automatically
    :type: bool

    Gets or set the auto track frequency option.

.. py:property:: frequency
    :canonical: ansys.stk.core.stkobjects.ReceiverModelMedium.frequency
    :type: float

    Gets or set the frequency.

.. py:property:: antenna_gain
    :canonical: ansys.stk.core.stkobjects.ReceiverModelMedium.antenna_gain
    :type: float

    Gets or set the antennaGain.

.. py:property:: antenna_to_lna_line_loss
    :canonical: ansys.stk.core.stkobjects.ReceiverModelMedium.antenna_to_lna_line_loss
    :type: float

    Gets or sets the antenna to LNA line loss.

.. py:property:: lna_gain
    :canonical: ansys.stk.core.stkobjects.ReceiverModelMedium.lna_gain
    :type: float

    Gets or sets the LNA gain.

.. py:property:: lna_to_receiver_line_loss
    :canonical: ansys.stk.core.stkobjects.ReceiverModelMedium.lna_to_receiver_line_loss
    :type: float

    Gets or sets the LNA to receiver line loss.

.. py:property:: system_noise_temperature
    :canonical: ansys.stk.core.stkobjects.ReceiverModelMedium.system_noise_temperature
    :type: SystemNoiseTemperature

    Gets the system noise temperature interface.

.. py:property:: interference
    :canonical: ansys.stk.core.stkobjects.ReceiverModelMedium.interference
    :type: RFInterference

    Gets the radio frequency interference.

.. py:property:: filter_component_linking
    :canonical: ansys.stk.core.stkobjects.ReceiverModelMedium.filter_component_linking
    :type: IComponentLinkEmbedControl

    Gets the link/embed controller for managing the filter model component.


Method detail
-------------




.. py:method:: set_filter(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.ReceiverModelMedium.set_filter

    Do not use this method, as it is deprecated. Use FilterComponentLinking on IAgReceiverModelMedium instead. Sets the current filter model by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`












.. py:method:: set_demodulator(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.ReceiverModelMedium.set_demodulator

    Set the current demodulator model by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`









.. py:method:: set_polarization_type(self, value: POLARIZATION_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.ReceiverModelMedium.set_polarization_type

    Set the current polarization type.

    :Parameters:

    **value** : :obj:`~POLARIZATION_TYPE`

    :Returns:

        :obj:`~None`

















