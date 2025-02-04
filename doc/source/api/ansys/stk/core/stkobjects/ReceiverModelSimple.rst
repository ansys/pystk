ReceiverModelSimple
===================

.. py:class:: ansys.stk.core.stkobjects.ReceiverModelSimple

   Bases: :py:class:`~ansys.stk.core.stkobjects.IReceiverModel`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining a simple receiver model.

.. py:currentmodule:: ReceiverModelSimple

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelSimple.set_filter`
              - Do not use this method, as it is deprecated. Use FilterComponentLinking on IAgReceiverModelSimple instead. Sets the current filter model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelSimple.set_demodulator`
              - Set the current demodulator model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelSimple.set_polarization_type`
              - Set the current polarization type.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelSimple.enable_filter`
              - Gets or set the flag determines whether or not to enable the Filter.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelSimple.supported_filters`
              - This property is deprecated. Use FilterComponentLinking on IAgReceiverModelSimple instead. Gets an array of supported filter model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelSimple.filter`
              - This property is deprecated. Use FilterComponentLinking on IAgReceiverModelSimple instead. Gets the current filter model.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelSimple.pre_receive_gains_losses`
              - Gets the collection of additional pre-receive gains and losses.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelSimple.pre_demodulator_gains_losses`
              - Gets the collection of additional pre-demod gains and losses.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelSimple.link_margin`
              - Gets the interface for configuring the link margin computation parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelSimple.scale_bandwidth_automatically`
              - Gets or set the auto scale bandwidth option.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelSimple.bandwidth`
              - Gets or set the bandwidth.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelSimple.select_demodulator_automatically`
              - Gets or set the auto select demodulator option.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelSimple.supported_demodulators`
              - Gets an array of supported demodulator model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelSimple.demodulator`
              - Gets the current demodulator model.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelSimple.use_rain`
              - Gets or sets the option for computing rain loss.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelSimple.supported_rain_outage_percent_values`
              - Gets an array of supported rain outage percent values.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelSimple.rain_outage_percent`
              - Gets or sets the rain outage percent.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelSimple.enable_polarization`
              - Gets or sets the enable polarization option.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelSimple.polarization`
              - Gets the polarization.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelSimple.track_frequency_automatically`
              - Gets or set the auto track frequency option.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelSimple.frequency`
              - Gets or set the frequency.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelSimple.g_over_t`
              - Gets or set the G/T.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelSimple.interference`
              - Gets the radio frequency interference.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelSimple.filter_component_linking`
              - Gets the link/embed controller for managing the filter model component.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ReceiverModelSimple


Property detail
---------------

.. py:property:: enable_filter
    :canonical: ansys.stk.core.stkobjects.ReceiverModelSimple.enable_filter
    :type: bool

    Gets or set the flag determines whether or not to enable the Filter.

.. py:property:: supported_filters
    :canonical: ansys.stk.core.stkobjects.ReceiverModelSimple.supported_filters
    :type: list

    This property is deprecated. Use FilterComponentLinking on IAgReceiverModelSimple instead. Gets an array of supported filter model names.

.. py:property:: filter
    :canonical: ansys.stk.core.stkobjects.ReceiverModelSimple.filter
    :type: IRFFilterModel

    This property is deprecated. Use FilterComponentLinking on IAgReceiverModelSimple instead. Gets the current filter model.

.. py:property:: pre_receive_gains_losses
    :canonical: ansys.stk.core.stkobjects.ReceiverModelSimple.pre_receive_gains_losses
    :type: AdditionalGainLossCollection

    Gets the collection of additional pre-receive gains and losses.

.. py:property:: pre_demodulator_gains_losses
    :canonical: ansys.stk.core.stkobjects.ReceiverModelSimple.pre_demodulator_gains_losses
    :type: AdditionalGainLossCollection

    Gets the collection of additional pre-demod gains and losses.

.. py:property:: link_margin
    :canonical: ansys.stk.core.stkobjects.ReceiverModelSimple.link_margin
    :type: LinkMargin

    Gets the interface for configuring the link margin computation parameters.

.. py:property:: scale_bandwidth_automatically
    :canonical: ansys.stk.core.stkobjects.ReceiverModelSimple.scale_bandwidth_automatically
    :type: bool

    Gets or set the auto scale bandwidth option.

.. py:property:: bandwidth
    :canonical: ansys.stk.core.stkobjects.ReceiverModelSimple.bandwidth
    :type: float

    Gets or set the bandwidth.

.. py:property:: select_demodulator_automatically
    :canonical: ansys.stk.core.stkobjects.ReceiverModelSimple.select_demodulator_automatically
    :type: bool

    Gets or set the auto select demodulator option.

.. py:property:: supported_demodulators
    :canonical: ansys.stk.core.stkobjects.ReceiverModelSimple.supported_demodulators
    :type: list

    Gets an array of supported demodulator model names.

.. py:property:: demodulator
    :canonical: ansys.stk.core.stkobjects.ReceiverModelSimple.demodulator
    :type: IDemodulatorModel

    Gets the current demodulator model.

.. py:property:: use_rain
    :canonical: ansys.stk.core.stkobjects.ReceiverModelSimple.use_rain
    :type: bool

    Gets or sets the option for computing rain loss.

.. py:property:: supported_rain_outage_percent_values
    :canonical: ansys.stk.core.stkobjects.ReceiverModelSimple.supported_rain_outage_percent_values
    :type: list

    Gets an array of supported rain outage percent values.

.. py:property:: rain_outage_percent
    :canonical: ansys.stk.core.stkobjects.ReceiverModelSimple.rain_outage_percent
    :type: float

    Gets or sets the rain outage percent.

.. py:property:: enable_polarization
    :canonical: ansys.stk.core.stkobjects.ReceiverModelSimple.enable_polarization
    :type: bool

    Gets or sets the enable polarization option.

.. py:property:: polarization
    :canonical: ansys.stk.core.stkobjects.ReceiverModelSimple.polarization
    :type: IPolarization

    Gets the polarization.

.. py:property:: track_frequency_automatically
    :canonical: ansys.stk.core.stkobjects.ReceiverModelSimple.track_frequency_automatically
    :type: bool

    Gets or set the auto track frequency option.

.. py:property:: frequency
    :canonical: ansys.stk.core.stkobjects.ReceiverModelSimple.frequency
    :type: float

    Gets or set the frequency.

.. py:property:: g_over_t
    :canonical: ansys.stk.core.stkobjects.ReceiverModelSimple.g_over_t
    :type: float

    Gets or set the G/T.

.. py:property:: interference
    :canonical: ansys.stk.core.stkobjects.ReceiverModelSimple.interference
    :type: RFInterference

    Gets the radio frequency interference.

.. py:property:: filter_component_linking
    :canonical: ansys.stk.core.stkobjects.ReceiverModelSimple.filter_component_linking
    :type: IComponentLinkEmbedControl

    Gets the link/embed controller for managing the filter model component.


Method detail
-------------




.. py:method:: set_filter(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.ReceiverModelSimple.set_filter

    Do not use this method, as it is deprecated. Use FilterComponentLinking on IAgReceiverModelSimple instead. Sets the current filter model by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`












.. py:method:: set_demodulator(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.ReceiverModelSimple.set_demodulator

    Set the current demodulator model by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`









.. py:method:: set_polarization_type(self, value: PolarizationType) -> None
    :canonical: ansys.stk.core.stkobjects.ReceiverModelSimple.set_polarization_type

    Set the current polarization type.

    :Parameters:

    **value** : :obj:`~PolarizationType`

    :Returns:

        :obj:`~None`










