IReceiverModelMedium
====================

.. py:class:: ansys.stk.core.stkobjects.IReceiverModelMedium

   object
   
   Provide access to the properties and methods defining a medium receiver model.

.. py:currentmodule:: IReceiverModelMedium

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelMedium.set_filter`
              - Set the current filter model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelMedium.set_demodulator`
              - Set the current demodulator model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelMedium.set_polarization_type`
              - Set the current polarization type.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelMedium.enable_filter`
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelMedium.supported_filters`
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelMedium.filter`
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelMedium.pre_receive_gains_losses`
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelMedium.pre_demod_gains_losses`
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelMedium.link_margin`
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelMedium.auto_scale_bandwidth`
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelMedium.bandwidth`
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelMedium.auto_select_demodulator`
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelMedium.supported_demodulators`
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelMedium.demodulator`
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelMedium.use_rain`
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelMedium.supported_rain_outage_percent_values`
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelMedium.rain_outage_percent`
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelMedium.enable_polarization`
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelMedium.polarization`
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelMedium.auto_track_frequency`
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelMedium.frequency`
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelMedium.antenna_gain`
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelMedium.antenna_to_lna_line_loss`
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelMedium.lna_gain`
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelMedium.lna_to_receiver_line_loss`
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelMedium.system_noise_temperature`
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelMedium.interference`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IReceiverModelMedium


Property detail
---------------

.. py:property:: enable_filter
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMedium.enable_filter
    :type: bool

    Gets or set the flag determines whether or not to enable the Filter.

.. py:property:: supported_filters
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMedium.supported_filters
    :type: list

    Gets an array of supported filter model names.

.. py:property:: filter
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMedium.filter
    :type: IRFFilterModel

    Gets the current filter model.

.. py:property:: pre_receive_gains_losses
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMedium.pre_receive_gains_losses
    :type: IAdditionalGainLossCollection

    Gets the collection of additional pre-receive gains and losses.

.. py:property:: pre_demod_gains_losses
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMedium.pre_demod_gains_losses
    :type: IAdditionalGainLossCollection

    Gets the collection of additional pre-demod gains and losses.

.. py:property:: link_margin
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMedium.link_margin
    :type: ILinkMargin

    Gets the interface for configuring the link margin computation parameters.

.. py:property:: auto_scale_bandwidth
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMedium.auto_scale_bandwidth
    :type: bool

    Gets or set the auto scale bandwidth option.

.. py:property:: bandwidth
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMedium.bandwidth
    :type: float

    Gets or set the bandwidth.

.. py:property:: auto_select_demodulator
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMedium.auto_select_demodulator
    :type: bool

    Gets or set the auto select demodulator option.

.. py:property:: supported_demodulators
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMedium.supported_demodulators
    :type: list

    Gets an array of supported demodulator model names.

.. py:property:: demodulator
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMedium.demodulator
    :type: IDemodulatorModel

    Gets the current demodulator model.

.. py:property:: use_rain
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMedium.use_rain
    :type: bool

    Gets or sets the option for computing rain loss.

.. py:property:: supported_rain_outage_percent_values
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMedium.supported_rain_outage_percent_values
    :type: list

    Gets an array of supported rain outage percent values.

.. py:property:: rain_outage_percent
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMedium.rain_outage_percent
    :type: float

    Gets or sets the rain outage percent.

.. py:property:: enable_polarization
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMedium.enable_polarization
    :type: bool

    Gets or sets the enable polarization option.

.. py:property:: polarization
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMedium.polarization
    :type: IPolarization

    Gets the polarization.

.. py:property:: auto_track_frequency
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMedium.auto_track_frequency
    :type: bool

    Gets or set the auto track frequency option.

.. py:property:: frequency
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMedium.frequency
    :type: float

    Gets or set the frequency.

.. py:property:: antenna_gain
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMedium.antenna_gain
    :type: float

    Gets or set the antennaGain.

.. py:property:: antenna_to_lna_line_loss
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMedium.antenna_to_lna_line_loss
    :type: float

    Gets or sets the antenna to LNA line loss.

.. py:property:: lna_gain
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMedium.lna_gain
    :type: float

    Gets or sets the LNA gain.

.. py:property:: lna_to_receiver_line_loss
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMedium.lna_to_receiver_line_loss
    :type: float

    Gets or sets the LNA to receiver line loss.

.. py:property:: system_noise_temperature
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMedium.system_noise_temperature
    :type: ISystemNoiseTemperature

    Gets the system noise temperature interface.

.. py:property:: interference
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMedium.interference
    :type: IRFInterference

    Gets the radio frequency interference.


Method detail
-------------




.. py:method:: set_filter(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMedium.set_filter

    Set the current filter model by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`












.. py:method:: set_demodulator(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMedium.set_demodulator

    Set the current demodulator model by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`









.. py:method:: set_polarization_type(self, val: POLARIZATION_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMedium.set_polarization_type

    Set the current polarization type.

    :Parameters:

    **val** : :obj:`~POLARIZATION_TYPE`

    :Returns:

        :obj:`~None`
















