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
              - Set the current filter model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.set_demodulator`
              - Set the current demodulator model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.set_polarization_type`
              - Set the current polarization type.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.enable_filter`
              - Gets or set the flag determines whether or not to enable the Filter.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.supported_filters`
              - Gets an array of supported filter model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.filter`
              - Gets the current filter model.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.pre_receive_gains_losses`
              - Gets the collection of additional pre-receive gains and losses.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.pre_demod_gains_losses`
              - Gets the collection of additional pre-demod gains and losses.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.link_margin`
              - Gets the interface for configuring the link margin computation parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.auto_scale_bandwidth`
              - Gets or set the auto scale bandwidth option.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.bandwidth`
              - Gets or set the bandwidth.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.auto_select_demodulator`
              - Gets or set the auto select demodulator option.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.supported_demodulators`
              - Gets an array of supported demodulator model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.demodulator`
              - Gets the current demodulator model.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.use_rain`
              - Gets or sets the option for computing rain loss.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.supported_rain_outage_percent_values`
              - Gets an array of supported rain outage percent values.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.rain_outage_percent`
              - Gets or sets the rain outage percent.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.enable_polarization`
              - Gets or sets the enable polarization option.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.polarization`
              - Gets the polarization.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.auto_track_frequency`
              - Gets or set the auto track frequency option.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.frequency`
              - Gets or set the frequency.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.antenna_control`
              - Gets the receiver antenna control.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.antenna_to_lna_line_loss`
              - Gets or sets the antenna to LNA line loss.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.lna_gain`
              - Gets or sets the LNA gain.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.lna_to_receiver_line_loss`
              - Gets or sets the LNA to receiver line loss.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.system_noise_temperature`
              - Gets the system noise temperature interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelComplex.interference`
              - Gets the radio frequency interference.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ReceiverModelComplex


Property detail
---------------

.. py:property:: enable_filter
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.enable_filter
    :type: bool

    Gets or set the flag determines whether or not to enable the Filter.

.. py:property:: supported_filters
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.supported_filters
    :type: list

    Gets an array of supported filter model names.

.. py:property:: filter
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.filter
    :type: IRFFilterModel

    Gets the current filter model.

.. py:property:: pre_receive_gains_losses
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.pre_receive_gains_losses
    :type: AdditionalGainLossCollection

    Gets the collection of additional pre-receive gains and losses.

.. py:property:: pre_demod_gains_losses
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.pre_demod_gains_losses
    :type: AdditionalGainLossCollection

    Gets the collection of additional pre-demod gains and losses.

.. py:property:: link_margin
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.link_margin
    :type: LinkMargin

    Gets the interface for configuring the link margin computation parameters.

.. py:property:: auto_scale_bandwidth
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.auto_scale_bandwidth
    :type: bool

    Gets or set the auto scale bandwidth option.

.. py:property:: bandwidth
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.bandwidth
    :type: float

    Gets or set the bandwidth.

.. py:property:: auto_select_demodulator
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.auto_select_demodulator
    :type: bool

    Gets or set the auto select demodulator option.

.. py:property:: supported_demodulators
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.supported_demodulators
    :type: list

    Gets an array of supported demodulator model names.

.. py:property:: demodulator
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.demodulator
    :type: IDemodulatorModel

    Gets the current demodulator model.

.. py:property:: use_rain
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.use_rain
    :type: bool

    Gets or sets the option for computing rain loss.

.. py:property:: supported_rain_outage_percent_values
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.supported_rain_outage_percent_values
    :type: list

    Gets an array of supported rain outage percent values.

.. py:property:: rain_outage_percent
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.rain_outage_percent
    :type: float

    Gets or sets the rain outage percent.

.. py:property:: enable_polarization
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.enable_polarization
    :type: bool

    Gets or sets the enable polarization option.

.. py:property:: polarization
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.polarization
    :type: IPolarization

    Gets the polarization.

.. py:property:: auto_track_frequency
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.auto_track_frequency
    :type: bool

    Gets or set the auto track frequency option.

.. py:property:: frequency
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.frequency
    :type: float

    Gets or set the frequency.

.. py:property:: antenna_control
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.antenna_control
    :type: AntennaControl

    Gets the receiver antenna control.

.. py:property:: antenna_to_lna_line_loss
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.antenna_to_lna_line_loss
    :type: float

    Gets or sets the antenna to LNA line loss.

.. py:property:: lna_gain
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.lna_gain
    :type: float

    Gets or sets the LNA gain.

.. py:property:: lna_to_receiver_line_loss
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.lna_to_receiver_line_loss
    :type: float

    Gets or sets the LNA to receiver line loss.

.. py:property:: system_noise_temperature
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.system_noise_temperature
    :type: SystemNoiseTemperature

    Gets the system noise temperature interface.

.. py:property:: interference
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.interference
    :type: RFInterference

    Gets the radio frequency interference.


Method detail
-------------




.. py:method:: set_filter(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.set_filter

    Set the current filter model by name.

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









.. py:method:: set_polarization_type(self, val: POLARIZATION_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.ReceiverModelComplex.set_polarization_type

    Set the current polarization type.

    :Parameters:

    **val** : :obj:`~POLARIZATION_TYPE`

    :Returns:

        :obj:`~None`















