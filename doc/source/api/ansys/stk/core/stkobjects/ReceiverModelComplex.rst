ReceiverModelComplex
====================

.. py:class:: ansys.stk.core.stkobjects.ReceiverModelComplex

   Bases: :py:class:`~ansys.stk.core.stkobjects.IReceiverModel`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining a complex receiver model.

.. py:currentmodule:: ReceiverModelComplex

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.set_filter`
              - Do not use this method, as it is deprecated. Use FilterComponentLinking on ReceiverModelComplex instead. Sets the current filter model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.set_demodulator`
              - Set the current demodulator model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.set_polarization_type`
              - Set the current polarization type.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.enable_filter`
              - Get or set the flag determines whether or not to enable the Filter.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.supported_filters`
              - Do not use this property, as it is deprecated. Use FilterComponentLinking on ReceiverModelComplex instead. Gets an array of supported filter model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.filter`
              - Do not use this property, as it is deprecated. Use FilterComponentLinking on ReceiverModelComplex instead. Gets the current filter model.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.pre_receive_gains_losses`
              - Get the collection of additional pre-receive gains and losses.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.pre_demodulator_gains_losses`
              - Get the collection of additional pre-demod gains and losses.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.link_margin`
              - Get the interface for configuring the link margin computation parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.scale_bandwidth_automatically`
              - Get or set the auto scale bandwidth option.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.bandwidth`
              - Get or set the bandwidth.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.select_demodulator_automatically`
              - Get or set the auto select demodulator option.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.supported_demodulators`
              - Get an array of supported demodulator model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.demodulator`
              - Get the current demodulator model.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.use_rain`
              - Get or set the option for computing rain loss.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.supported_rain_outage_percent_values`
              - Get an array of supported rain outage percent values.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.rain_outage_percent`
              - Get or set the rain outage percent.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.enable_polarization`
              - Get or set the enable polarization option.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.polarization`
              - Get the polarization.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.track_frequency_automatically`
              - Get or set the auto track frequency option.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.frequency`
              - Get or set the frequency.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.antenna_control`
              - Get the receiver antenna control.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.antenna_to_lna_line_loss`
              - Get or set the antenna to LNA line loss.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.lna_gain`
              - Get or set the LNA gain.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.lna_to_receiver_line_loss`
              - Get or set the LNA to receiver line loss.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.system_noise_temperature`
              - Get the system noise temperature interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.interference`
              - Get the radio frequency interference.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.filter_component_linking`
              - Get the link/embed controller for managing the filter model component.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ReceiverModelComplex


Property detail
---------------

.. py:property:: enable_filter
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.enable_filter
    :type: bool

    Get or set the flag determines whether or not to enable the Filter.

.. py:property:: supported_filters
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.supported_filters
    :type: list

    Do not use this property, as it is deprecated. Use FilterComponentLinking on ReceiverModelComplex instead. Gets an array of supported filter model names.

.. py:property:: filter
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.filter
    :type: IRFFilterModel

    Do not use this property, as it is deprecated. Use FilterComponentLinking on ReceiverModelComplex instead. Gets the current filter model.

.. py:property:: pre_receive_gains_losses
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.pre_receive_gains_losses
    :type: AdditionalGainLossCollection

    Get the collection of additional pre-receive gains and losses.

.. py:property:: pre_demodulator_gains_losses
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.pre_demodulator_gains_losses
    :type: AdditionalGainLossCollection

    Get the collection of additional pre-demod gains and losses.

.. py:property:: link_margin
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.link_margin
    :type: LinkMargin

    Get the interface for configuring the link margin computation parameters.

.. py:property:: scale_bandwidth_automatically
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.scale_bandwidth_automatically
    :type: bool

    Get or set the auto scale bandwidth option.

.. py:property:: bandwidth
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.bandwidth
    :type: float

    Get or set the bandwidth.

.. py:property:: select_demodulator_automatically
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.select_demodulator_automatically
    :type: bool

    Get or set the auto select demodulator option.

.. py:property:: supported_demodulators
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.supported_demodulators
    :type: list

    Get an array of supported demodulator model names.

.. py:property:: demodulator
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.demodulator
    :type: IDemodulatorModel

    Get the current demodulator model.

.. py:property:: use_rain
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.use_rain
    :type: bool

    Get or set the option for computing rain loss.

.. py:property:: supported_rain_outage_percent_values
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.supported_rain_outage_percent_values
    :type: list

    Get an array of supported rain outage percent values.

.. py:property:: rain_outage_percent
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.rain_outage_percent
    :type: float

    Get or set the rain outage percent.

.. py:property:: enable_polarization
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.enable_polarization
    :type: bool

    Get or set the enable polarization option.

.. py:property:: polarization
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.polarization
    :type: IPolarization

    Get the polarization.

.. py:property:: track_frequency_automatically
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.track_frequency_automatically
    :type: bool

    Get or set the auto track frequency option.

.. py:property:: frequency
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.frequency
    :type: float

    Get or set the frequency.

.. py:property:: antenna_control
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.antenna_control
    :type: AntennaControl

    Get the receiver antenna control.

.. py:property:: antenna_to_lna_line_loss
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.antenna_to_lna_line_loss
    :type: float

    Get or set the antenna to LNA line loss.

.. py:property:: lna_gain
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.lna_gain
    :type: float

    Get or set the LNA gain.

.. py:property:: lna_to_receiver_line_loss
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.lna_to_receiver_line_loss
    :type: float

    Get or set the LNA to receiver line loss.

.. py:property:: system_noise_temperature
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.system_noise_temperature
    :type: SystemNoiseTemperature

    Get the system noise temperature interface.

.. py:property:: interference
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.interference
    :type: RFInterference

    Get the radio frequency interference.

.. py:property:: filter_component_linking
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.filter_component_linking
    :type: IComponentLinkEmbedControl

    Get the link/embed controller for managing the filter model component.


Method detail
-------------




.. py:method:: set_filter(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.set_filter

    Do not use this method, as it is deprecated. Use FilterComponentLinking on ReceiverModelComplex instead. Sets the current filter model by name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~None`












.. py:method:: set_demodulator(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.set_demodulator

    Set the current demodulator model by name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~None`









.. py:method:: set_polarization_type(self, value: PolarizationType) -> None
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.set_polarization_type

    Set the current polarization type.

    :Parameters:

        **value** : :obj:`~PolarizationType`


    :Returns:

        :obj:`~None`
















