IReceiverModelMultibeam
=======================

.. py:class:: IReceiverModelMultibeam

   object
   
   Provide access to the properties and methods defining a multibeam receiver model.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_filter`
              - Set the current filter model by name.
            * - :py:meth:`~set_demodulator`
              - Set the current demodulator model by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~enable_filter`
            * - :py:meth:`~supported_filters`
            * - :py:meth:`~filter`
            * - :py:meth:`~pre_receive_gains_losses`
            * - :py:meth:`~pre_demod_gains_losses`
            * - :py:meth:`~link_margin`
            * - :py:meth:`~auto_scale_bandwidth`
            * - :py:meth:`~bandwidth`
            * - :py:meth:`~auto_select_demodulator`
            * - :py:meth:`~supported_demodulators`
            * - :py:meth:`~demodulator`
            * - :py:meth:`~use_rain`
            * - :py:meth:`~supported_rain_outage_percent_values`
            * - :py:meth:`~rain_outage_percent`
            * - :py:meth:`~auto_track_frequency`
            * - :py:meth:`~antenna_to_lna_line_loss`
            * - :py:meth:`~lna_gain`
            * - :py:meth:`~lna_to_receiver_line_loss`
            * - :py:meth:`~system_noise_temperature`
            * - :py:meth:`~antenna_system`
            * - :py:meth:`~interference`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IReceiverModelMultibeam


Property detail
---------------

.. py:property:: enable_filter
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMultibeam.enable_filter
    :type: bool

    Gets or set the flag determines whether or not to enable the Filter.

.. py:property:: supported_filters
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMultibeam.supported_filters
    :type: list

    Gets an array of supported filter model names.

.. py:property:: filter
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMultibeam.filter
    :type: "IAgRFFilterModel"

    Gets the current filter model.

.. py:property:: pre_receive_gains_losses
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMultibeam.pre_receive_gains_losses
    :type: "IAgAdditionalGainLossCollection"

    Gets the collection of additional pre-receive gains and losses.

.. py:property:: pre_demod_gains_losses
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMultibeam.pre_demod_gains_losses
    :type: "IAgAdditionalGainLossCollection"

    Gets the collection of additional pre-demod gains and losses.

.. py:property:: link_margin
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMultibeam.link_margin
    :type: "IAgLinkMargin"

    Gets the interface for configuring the link margin computation parameters.

.. py:property:: auto_scale_bandwidth
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMultibeam.auto_scale_bandwidth
    :type: bool

    Gets or set the auto scale bandwidth option.

.. py:property:: bandwidth
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMultibeam.bandwidth
    :type: float

    Gets or set the bandwidth.

.. py:property:: auto_select_demodulator
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMultibeam.auto_select_demodulator
    :type: bool

    Gets or set the auto select demodulator option.

.. py:property:: supported_demodulators
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMultibeam.supported_demodulators
    :type: list

    Gets an array of supported demodulator model names.

.. py:property:: demodulator
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMultibeam.demodulator
    :type: "IAgDemodulatorModel"

    Gets the current demodulator model.

.. py:property:: use_rain
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMultibeam.use_rain
    :type: bool

    Gets or sets the option for computing rain loss.

.. py:property:: supported_rain_outage_percent_values
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMultibeam.supported_rain_outage_percent_values
    :type: list

    Gets an array of supported rain outage percent values.

.. py:property:: rain_outage_percent
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMultibeam.rain_outage_percent
    :type: float

    Gets or sets the rain outage percent.

.. py:property:: auto_track_frequency
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMultibeam.auto_track_frequency
    :type: bool

    Gets or set the auto track frequency option.

.. py:property:: antenna_to_lna_line_loss
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMultibeam.antenna_to_lna_line_loss
    :type: float

    Gets or sets the antenna to LNA line loss.

.. py:property:: lna_gain
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMultibeam.lna_gain
    :type: float

    Gets or sets the LNA gain.

.. py:property:: lna_to_receiver_line_loss
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMultibeam.lna_to_receiver_line_loss
    :type: float

    Gets or sets the LNA to receiver line loss.

.. py:property:: system_noise_temperature
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMultibeam.system_noise_temperature
    :type: "IAgSystemNoiseTemperature"

    Gets the system noise temperature interface.

.. py:property:: antenna_system
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMultibeam.antenna_system
    :type: "IAgAntennaSystem"

    Gets the antenna system.

.. py:property:: interference
    :canonical: ansys.stk.core.stkobjects.IReceiverModelMultibeam.interference
    :type: "IAgRFInterference"

    Gets the radio frequency interference.


Method detail
-------------




.. py:method:: set_filter(self, name:str) -> None

    Set the current filter model by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`












.. py:method:: set_demodulator(self, name:str) -> None

    Set the current demodulator model by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`


















