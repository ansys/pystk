IReceiverModelLaser
===================

.. py:class:: ansys.stk.core.stkobjects.IReceiverModelLaser

   object
   
   Provide access to the properties and methods defining a laser receiver model.

.. py:currentmodule:: IReceiverModelLaser

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelLaser.set_filter`
              - Set the current filter model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelLaser.set_demodulator`
              - Set the current demodulator model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelLaser.set_polarization_type`
              - Set the current polarization type.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelLaser.enable_filter`
              - Gets or set the flag determines whether or not to enable the Filter.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelLaser.supported_filters`
              - Gets an array of supported filter model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelLaser.filter`
              - Gets the current filter model.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelLaser.pre_receive_gains_losses`
              - Gets the collection of additional pre-receive gains and losses.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelLaser.pre_demod_gains_losses`
              - Gets the collection of additional pre-demod gains and losses.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelLaser.link_margin`
              - Gets the interface for configuring the link margin computation parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelLaser.auto_scale_bandwidth`
              - Gets or set the auto scale bandwidth option.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelLaser.bandwidth`
              - Gets or set the bandwidth.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelLaser.auto_select_demodulator`
              - Gets or set the auto select demodulator option.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelLaser.supported_demodulators`
              - Gets an array of supported demodulator model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelLaser.demodulator`
              - Gets the current demodulator model.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelLaser.enable_polarization`
              - Gets or sets the enable polarization option.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelLaser.polarization`
              - Gets the polarization.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelLaser.auto_track_frequency`
              - Gets or set the auto track frequency option.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelLaser.frequency`
              - Gets or set the frequency.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelLaser.antenna_control`
              - Gets the receiver antenna control.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelLaser.detector_gain`
              - Gets or set the detector gain.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelLaser.detector_efficiency`
              - Gets or set the detector efficiency.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelLaser.detector_dark_current`
              - Gets or set the detector dark current.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelLaser.detector_noise_figure`
              - Gets or set the detector noise figure.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelLaser.detector_noise_temperature`
              - Gets or set the detector noise temperature.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelLaser.detector_load_impedance`
              - Gets or set the detector load impedance.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelLaser.use_apd_detector_model`
              - Gets or set the flag for using the APD detector model.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelLaser.propagation_loss_models`
              - This property is deprecated. The laser propagation loss models can be accessed from the LaserEnvironment property.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IReceiverModelLaser


Property detail
---------------

.. py:property:: enable_filter
    :canonical: ansys.stk.core.stkobjects.IReceiverModelLaser.enable_filter
    :type: bool

    Gets or set the flag determines whether or not to enable the Filter.

.. py:property:: supported_filters
    :canonical: ansys.stk.core.stkobjects.IReceiverModelLaser.supported_filters
    :type: list

    Gets an array of supported filter model names.

.. py:property:: filter
    :canonical: ansys.stk.core.stkobjects.IReceiverModelLaser.filter
    :type: IRFFilterModel

    Gets the current filter model.

.. py:property:: pre_receive_gains_losses
    :canonical: ansys.stk.core.stkobjects.IReceiverModelLaser.pre_receive_gains_losses
    :type: IAdditionalGainLossCollection

    Gets the collection of additional pre-receive gains and losses.

.. py:property:: pre_demod_gains_losses
    :canonical: ansys.stk.core.stkobjects.IReceiverModelLaser.pre_demod_gains_losses
    :type: IAdditionalGainLossCollection

    Gets the collection of additional pre-demod gains and losses.

.. py:property:: link_margin
    :canonical: ansys.stk.core.stkobjects.IReceiverModelLaser.link_margin
    :type: ILinkMargin

    Gets the interface for configuring the link margin computation parameters.

.. py:property:: auto_scale_bandwidth
    :canonical: ansys.stk.core.stkobjects.IReceiverModelLaser.auto_scale_bandwidth
    :type: bool

    Gets or set the auto scale bandwidth option.

.. py:property:: bandwidth
    :canonical: ansys.stk.core.stkobjects.IReceiverModelLaser.bandwidth
    :type: float

    Gets or set the bandwidth.

.. py:property:: auto_select_demodulator
    :canonical: ansys.stk.core.stkobjects.IReceiverModelLaser.auto_select_demodulator
    :type: bool

    Gets or set the auto select demodulator option.

.. py:property:: supported_demodulators
    :canonical: ansys.stk.core.stkobjects.IReceiverModelLaser.supported_demodulators
    :type: list

    Gets an array of supported demodulator model names.

.. py:property:: demodulator
    :canonical: ansys.stk.core.stkobjects.IReceiverModelLaser.demodulator
    :type: IDemodulatorModel

    Gets the current demodulator model.

.. py:property:: enable_polarization
    :canonical: ansys.stk.core.stkobjects.IReceiverModelLaser.enable_polarization
    :type: bool

    Gets or sets the enable polarization option.

.. py:property:: polarization
    :canonical: ansys.stk.core.stkobjects.IReceiverModelLaser.polarization
    :type: IPolarization

    Gets the polarization.

.. py:property:: auto_track_frequency
    :canonical: ansys.stk.core.stkobjects.IReceiverModelLaser.auto_track_frequency
    :type: bool

    Gets or set the auto track frequency option.

.. py:property:: frequency
    :canonical: ansys.stk.core.stkobjects.IReceiverModelLaser.frequency
    :type: float

    Gets or set the frequency.

.. py:property:: antenna_control
    :canonical: ansys.stk.core.stkobjects.IReceiverModelLaser.antenna_control
    :type: IAntennaControl

    Gets the receiver antenna control.

.. py:property:: detector_gain
    :canonical: ansys.stk.core.stkobjects.IReceiverModelLaser.detector_gain
    :type: float

    Gets or set the detector gain.

.. py:property:: detector_efficiency
    :canonical: ansys.stk.core.stkobjects.IReceiverModelLaser.detector_efficiency
    :type: float

    Gets or set the detector efficiency.

.. py:property:: detector_dark_current
    :canonical: ansys.stk.core.stkobjects.IReceiverModelLaser.detector_dark_current
    :type: float

    Gets or set the detector dark current.

.. py:property:: detector_noise_figure
    :canonical: ansys.stk.core.stkobjects.IReceiverModelLaser.detector_noise_figure
    :type: float

    Gets or set the detector noise figure.

.. py:property:: detector_noise_temperature
    :canonical: ansys.stk.core.stkobjects.IReceiverModelLaser.detector_noise_temperature
    :type: float

    Gets or set the detector noise temperature.

.. py:property:: detector_load_impedance
    :canonical: ansys.stk.core.stkobjects.IReceiverModelLaser.detector_load_impedance
    :type: float

    Gets or set the detector load impedance.

.. py:property:: use_apd_detector_model
    :canonical: ansys.stk.core.stkobjects.IReceiverModelLaser.use_apd_detector_model
    :type: bool

    Gets or set the flag for using the APD detector model.

.. py:property:: propagation_loss_models
    :canonical: ansys.stk.core.stkobjects.IReceiverModelLaser.propagation_loss_models
    :type: ILaserPropagationLossModels

    This property is deprecated. The laser propagation loss models can be accessed from the LaserEnvironment property.


Method detail
-------------




.. py:method:: set_filter(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.IReceiverModelLaser.set_filter

    Set the current filter model by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`












.. py:method:: set_demodulator(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.IReceiverModelLaser.set_demodulator

    Set the current demodulator model by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`




.. py:method:: set_polarization_type(self, val: POLARIZATION_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.IReceiverModelLaser.set_polarization_type

    Set the current polarization type.

    :Parameters:

    **val** : :obj:`~POLARIZATION_TYPE`

    :Returns:

        :obj:`~None`






















