IReceiverModelLaser
===================

.. py:class:: IReceiverModelLaser

   object
   
   Provide access to the properties and methods defining a laser receiver model.

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
            * - :py:meth:`~set_polarization_type`
              - Set the current polarization type.

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
            * - :py:meth:`~enable_polarization`
            * - :py:meth:`~polarization`
            * - :py:meth:`~auto_track_frequency`
            * - :py:meth:`~frequency`
            * - :py:meth:`~antenna_control`
            * - :py:meth:`~detector_gain`
            * - :py:meth:`~detector_efficiency`
            * - :py:meth:`~detector_dark_current`
            * - :py:meth:`~detector_noise_figure`
            * - :py:meth:`~detector_noise_temperature`
            * - :py:meth:`~detector_load_impedance`
            * - :py:meth:`~use_apd_detector_model`
            * - :py:meth:`~propagation_loss_models`


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
    :type: "IAgRFFilterModel"

    Gets the current filter model.

.. py:property:: pre_receive_gains_losses
    :canonical: ansys.stk.core.stkobjects.IReceiverModelLaser.pre_receive_gains_losses
    :type: "IAgAdditionalGainLossCollection"

    Gets the collection of additional pre-receive gains and losses.

.. py:property:: pre_demod_gains_losses
    :canonical: ansys.stk.core.stkobjects.IReceiverModelLaser.pre_demod_gains_losses
    :type: "IAgAdditionalGainLossCollection"

    Gets the collection of additional pre-demod gains and losses.

.. py:property:: link_margin
    :canonical: ansys.stk.core.stkobjects.IReceiverModelLaser.link_margin
    :type: "IAgLinkMargin"

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
    :type: "IAgDemodulatorModel"

    Gets the current demodulator model.

.. py:property:: enable_polarization
    :canonical: ansys.stk.core.stkobjects.IReceiverModelLaser.enable_polarization
    :type: bool

    Gets or sets the enable polarization option.

.. py:property:: polarization
    :canonical: ansys.stk.core.stkobjects.IReceiverModelLaser.polarization
    :type: "IAgPolarization"

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
    :type: "IAgAntennaControl"

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
    :type: "IAgLaserPropagationLossModels"

    This property is deprecated. The laser propagation loss models can be accessed from the LaserEnvironment property.


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




.. py:method:: set_polarization_type(self, val:"POLARIZATION_TYPE") -> None

    Set the current polarization type.

    :Parameters:

    **val** : :obj:`~"POLARIZATION_TYPE"`

    :Returns:

        :obj:`~None`






















