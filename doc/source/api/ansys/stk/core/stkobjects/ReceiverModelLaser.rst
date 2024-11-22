ReceiverModelLaser
==================

.. py:class:: ansys.stk.core.stkobjects.ReceiverModelLaser

   Bases: :py:class:`~ansys.stk.core.stkobjects.IReceiverModel`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining a laser receiver model.

.. py:currentmodule:: ReceiverModelLaser

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelLaser.set_filter`
              - Do not use this method, as it is deprecated. Use FilterComponentLinking on IAgReceiverModelLaser instead. Sets the current filter model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelLaser.set_demodulator`
              - Set the current demodulator model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelLaser.set_polarization_type`
              - Set the current polarization type.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelLaser.enable_filter`
              - Gets or set the flag determines whether or not to enable the Filter.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelLaser.supported_filters`
              - This property is deprecated. Use FilterComponentLinking on IAgReceiverModelLaser instead. Gets an array of supported filter model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelLaser.filter`
              - This property is deprecated. Use FilterComponentLinking on IAgReceiverModelLaser instead. Gets the current filter model.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelLaser.pre_receive_gains_losses`
              - Gets the collection of additional pre-receive gains and losses.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelLaser.pre_demodulator_gains_losses`
              - Gets the collection of additional pre-demod gains and losses.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelLaser.link_margin`
              - Gets the interface for configuring the link margin computation parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelLaser.scale_bandwidth_automatically`
              - Gets or set the auto scale bandwidth option.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelLaser.bandwidth`
              - Gets or set the bandwidth.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelLaser.select_demodulator_automatically`
              - Gets or set the auto select demodulator option.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelLaser.supported_demodulators`
              - Gets an array of supported demodulator model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelLaser.demodulator`
              - Gets the current demodulator model.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelLaser.enable_polarization`
              - Gets or sets the enable polarization option.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelLaser.polarization`
              - Gets the polarization.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelLaser.track_frequency_automatically`
              - Gets or set the auto track frequency option.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelLaser.frequency`
              - Gets or set the frequency.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelLaser.antenna_control`
              - Gets the receiver antenna control.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelLaser.detector_gain`
              - Gets or set the detector gain.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelLaser.detector_efficiency`
              - Gets or set the detector efficiency.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelLaser.detector_dark_current`
              - Gets or set the detector dark current.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelLaser.detector_noise_figure`
              - Gets or set the detector noise figure.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelLaser.detector_noise_temperature`
              - Gets or set the detector noise temperature.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelLaser.detector_load_impedance`
              - Gets or set the detector load impedance.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelLaser.use_avalanche_photo_detector_model`
              - Gets or set the flag for using the APD detector model.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelLaser.propagation_loss_models`
              - This property is deprecated. The laser propagation loss models can be accessed from the LaserEnvironment property.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverModelLaser.filter_component_linking`
              - Gets the link/embed controller for managing the filter model component.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ReceiverModelLaser


Property detail
---------------

.. py:property:: enable_filter
    :canonical: ansys.stk.core.stkobjects.ReceiverModelLaser.enable_filter
    :type: bool

    Gets or set the flag determines whether or not to enable the Filter.

.. py:property:: supported_filters
    :canonical: ansys.stk.core.stkobjects.ReceiverModelLaser.supported_filters
    :type: list

    This property is deprecated. Use FilterComponentLinking on IAgReceiverModelLaser instead. Gets an array of supported filter model names.

.. py:property:: filter
    :canonical: ansys.stk.core.stkobjects.ReceiverModelLaser.filter
    :type: IRFFilterModel

    This property is deprecated. Use FilterComponentLinking on IAgReceiverModelLaser instead. Gets the current filter model.

.. py:property:: pre_receive_gains_losses
    :canonical: ansys.stk.core.stkobjects.ReceiverModelLaser.pre_receive_gains_losses
    :type: AdditionalGainLossCollection

    Gets the collection of additional pre-receive gains and losses.

.. py:property:: pre_demodulator_gains_losses
    :canonical: ansys.stk.core.stkobjects.ReceiverModelLaser.pre_demodulator_gains_losses
    :type: AdditionalGainLossCollection

    Gets the collection of additional pre-demod gains and losses.

.. py:property:: link_margin
    :canonical: ansys.stk.core.stkobjects.ReceiverModelLaser.link_margin
    :type: LinkMargin

    Gets the interface for configuring the link margin computation parameters.

.. py:property:: scale_bandwidth_automatically
    :canonical: ansys.stk.core.stkobjects.ReceiverModelLaser.scale_bandwidth_automatically
    :type: bool

    Gets or set the auto scale bandwidth option.

.. py:property:: bandwidth
    :canonical: ansys.stk.core.stkobjects.ReceiverModelLaser.bandwidth
    :type: float

    Gets or set the bandwidth.

.. py:property:: select_demodulator_automatically
    :canonical: ansys.stk.core.stkobjects.ReceiverModelLaser.select_demodulator_automatically
    :type: bool

    Gets or set the auto select demodulator option.

.. py:property:: supported_demodulators
    :canonical: ansys.stk.core.stkobjects.ReceiverModelLaser.supported_demodulators
    :type: list

    Gets an array of supported demodulator model names.

.. py:property:: demodulator
    :canonical: ansys.stk.core.stkobjects.ReceiverModelLaser.demodulator
    :type: IDemodulatorModel

    Gets the current demodulator model.

.. py:property:: enable_polarization
    :canonical: ansys.stk.core.stkobjects.ReceiverModelLaser.enable_polarization
    :type: bool

    Gets or sets the enable polarization option.

.. py:property:: polarization
    :canonical: ansys.stk.core.stkobjects.ReceiverModelLaser.polarization
    :type: IPolarization

    Gets the polarization.

.. py:property:: track_frequency_automatically
    :canonical: ansys.stk.core.stkobjects.ReceiverModelLaser.track_frequency_automatically
    :type: bool

    Gets or set the auto track frequency option.

.. py:property:: frequency
    :canonical: ansys.stk.core.stkobjects.ReceiverModelLaser.frequency
    :type: float

    Gets or set the frequency.

.. py:property:: antenna_control
    :canonical: ansys.stk.core.stkobjects.ReceiverModelLaser.antenna_control
    :type: AntennaControl

    Gets the receiver antenna control.

.. py:property:: detector_gain
    :canonical: ansys.stk.core.stkobjects.ReceiverModelLaser.detector_gain
    :type: float

    Gets or set the detector gain.

.. py:property:: detector_efficiency
    :canonical: ansys.stk.core.stkobjects.ReceiverModelLaser.detector_efficiency
    :type: float

    Gets or set the detector efficiency.

.. py:property:: detector_dark_current
    :canonical: ansys.stk.core.stkobjects.ReceiverModelLaser.detector_dark_current
    :type: float

    Gets or set the detector dark current.

.. py:property:: detector_noise_figure
    :canonical: ansys.stk.core.stkobjects.ReceiverModelLaser.detector_noise_figure
    :type: float

    Gets or set the detector noise figure.

.. py:property:: detector_noise_temperature
    :canonical: ansys.stk.core.stkobjects.ReceiverModelLaser.detector_noise_temperature
    :type: float

    Gets or set the detector noise temperature.

.. py:property:: detector_load_impedance
    :canonical: ansys.stk.core.stkobjects.ReceiverModelLaser.detector_load_impedance
    :type: float

    Gets or set the detector load impedance.

.. py:property:: use_avalanche_photo_detector_model
    :canonical: ansys.stk.core.stkobjects.ReceiverModelLaser.use_avalanche_photo_detector_model
    :type: bool

    Gets or set the flag for using the APD detector model.

.. py:property:: propagation_loss_models
    :canonical: ansys.stk.core.stkobjects.ReceiverModelLaser.propagation_loss_models
    :type: LaserPropagationLossModels

    This property is deprecated. The laser propagation loss models can be accessed from the LaserEnvironment property.

.. py:property:: filter_component_linking
    :canonical: ansys.stk.core.stkobjects.ReceiverModelLaser.filter_component_linking
    :type: IComponentLinkEmbedControl

    Gets the link/embed controller for managing the filter model component.


Method detail
-------------




.. py:method:: set_filter(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.ReceiverModelLaser.set_filter

    Do not use this method, as it is deprecated. Use FilterComponentLinking on IAgReceiverModelLaser instead. Sets the current filter model by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`












.. py:method:: set_demodulator(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.ReceiverModelLaser.set_demodulator

    Set the current demodulator model by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`




.. py:method:: set_polarization_type(self, value: POLARIZATION_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.ReceiverModelLaser.set_polarization_type

    Set the current polarization type.

    :Parameters:

    **value** : :obj:`~POLARIZATION_TYPE`

    :Returns:

        :obj:`~None`























