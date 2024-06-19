IRadarReceiver
==============

.. py:class:: IRadarReceiver

   object
   
   Interface which defines a radar receiver.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_polarization_type`
              - Set the current polarization type.
            * - :py:meth:`~set_filter`
              - Set the current filter model by name.
            * - :py:meth:`~set_rf_stc_type`
              - Set the RF STC Type.
            * - :py:meth:`~set_if_stc_type`
              - Set the IF STC Type.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~antenna_to_lna_line_loss`
            * - :py:meth:`~lna_gain`
            * - :py:meth:`~lna_to_receiver_line_loss`
            * - :py:meth:`~use_rain`
            * - :py:meth:`~supported_rain_outage_percent_values`
            * - :py:meth:`~rain_outage_percent`
            * - :py:meth:`~pre_receive_gains_losses`
            * - :py:meth:`~enable_polarization`
            * - :py:meth:`~enable_ortho_polarization`
            * - :py:meth:`~polarization`
            * - :py:meth:`~lna_bandwidth`
            * - :py:meth:`~enable_filter`
            * - :py:meth:`~supported_filters`
            * - :py:meth:`~filter`
            * - :py:meth:`~system_noise_temperature`
            * - :py:meth:`~enable_rf_stc`
            * - :py:meth:`~rf_stc`
            * - :py:meth:`~enable_if_stc`
            * - :py:meth:`~if_stc`
            * - :py:meth:`~supported_rf_stc_types`
            * - :py:meth:`~supported_if_stc_types`
            * - :py:meth:`~frequency`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarReceiver


Property detail
---------------

.. py:property:: antenna_to_lna_line_loss
    :canonical: ansys.stk.core.stkobjects.IRadarReceiver.antenna_to_lna_line_loss
    :type: float

    Gets or sets the antenna to LNA line loss.

.. py:property:: lna_gain
    :canonical: ansys.stk.core.stkobjects.IRadarReceiver.lna_gain
    :type: float

    Gets or sets the LNA gain.

.. py:property:: lna_to_receiver_line_loss
    :canonical: ansys.stk.core.stkobjects.IRadarReceiver.lna_to_receiver_line_loss
    :type: float

    Gets or sets the LNA to receiver line loss.

.. py:property:: use_rain
    :canonical: ansys.stk.core.stkobjects.IRadarReceiver.use_rain
    :type: bool

    Gets or sets the option for computing rain loss.

.. py:property:: supported_rain_outage_percent_values
    :canonical: ansys.stk.core.stkobjects.IRadarReceiver.supported_rain_outage_percent_values
    :type: list

    Gets an array of supported rain outage percent values.

.. py:property:: rain_outage_percent
    :canonical: ansys.stk.core.stkobjects.IRadarReceiver.rain_outage_percent
    :type: float

    Gets or sets the rain outage percent.

.. py:property:: pre_receive_gains_losses
    :canonical: ansys.stk.core.stkobjects.IRadarReceiver.pre_receive_gains_losses
    :type: IAgAdditionalGainLossCollection

    Gets the collection of additional pre-receive gains and losses.

.. py:property:: enable_polarization
    :canonical: ansys.stk.core.stkobjects.IRadarReceiver.enable_polarization
    :type: bool

    Gets or sets the enable polarization option.

.. py:property:: enable_ortho_polarization
    :canonical: ansys.stk.core.stkobjects.IRadarReceiver.enable_ortho_polarization
    :type: bool

    Gets or sets the option for enabling the orthogonal polarization.

.. py:property:: polarization
    :canonical: ansys.stk.core.stkobjects.IRadarReceiver.polarization
    :type: IAgPolarization

    Gets the polarization.

.. py:property:: lna_bandwidth
    :canonical: ansys.stk.core.stkobjects.IRadarReceiver.lna_bandwidth
    :type: float

    Gets or sets the LNA bandwidth.

.. py:property:: enable_filter
    :canonical: ansys.stk.core.stkobjects.IRadarReceiver.enable_filter
    :type: bool

    Gets or set the flag determines whether or not to enable the Filter.

.. py:property:: supported_filters
    :canonical: ansys.stk.core.stkobjects.IRadarReceiver.supported_filters
    :type: list

    Gets an array of supported model names.

.. py:property:: filter
    :canonical: ansys.stk.core.stkobjects.IRadarReceiver.filter
    :type: IAgRFFilterModel

    Gets the current filter model.

.. py:property:: system_noise_temperature
    :canonical: ansys.stk.core.stkobjects.IRadarReceiver.system_noise_temperature
    :type: IAgSystemNoiseTemperature

    Gets the system noise temperature interface.

.. py:property:: enable_rf_stc
    :canonical: ansys.stk.core.stkobjects.IRadarReceiver.enable_rf_stc
    :type: bool

    Gets or sets whether the RF STC is enabled.

.. py:property:: rf_stc
    :canonical: ansys.stk.core.stkobjects.IRadarReceiver.rf_stc
    :type: IAgRadarStcAttenuation

    Gets the RF STC.

.. py:property:: enable_if_stc
    :canonical: ansys.stk.core.stkobjects.IRadarReceiver.enable_if_stc
    :type: bool

    Gets or sets whether the IF STC is enabled.

.. py:property:: if_stc
    :canonical: ansys.stk.core.stkobjects.IRadarReceiver.if_stc
    :type: IAgRadarStcAttenuation

    Gets the IF STC.

.. py:property:: supported_rf_stc_types
    :canonical: ansys.stk.core.stkobjects.IRadarReceiver.supported_rf_stc_types
    :type: list

    Gets the RF STC Types.

.. py:property:: supported_if_stc_types
    :canonical: ansys.stk.core.stkobjects.IRadarReceiver.supported_if_stc_types
    :type: list

    Gets the IF STC Types.

.. py:property:: frequency
    :canonical: ansys.stk.core.stkobjects.IRadarReceiver.frequency
    :type: float

    Gets or sets the receiver center frequency.


Method detail
-------------

















.. py:method:: set_polarization_type(self, val: POLARIZATION_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.IRadarReceiver.set_polarization_type

    Set the current polarization type.

    :Parameters:

    **val** : :obj:`~POLARIZATION_TYPE`

    :Returns:

        :obj:`~None`







.. py:method:: set_filter(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.IRadarReceiver.set_filter

    Set the current filter model by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`





.. py:method:: set_rf_stc_type(self, typeName: str) -> None
    :canonical: ansys.stk.core.stkobjects.IRadarReceiver.set_rf_stc_type

    Set the RF STC Type.

    :Parameters:

    **typeName** : :obj:`~str`

    :Returns:

        :obj:`~None`




.. py:method:: set_if_stc_type(self, typeName: str) -> None
    :canonical: ansys.stk.core.stkobjects.IRadarReceiver.set_if_stc_type

    Set the IF STC Type.

    :Parameters:

    **typeName** : :obj:`~str`

    :Returns:

        :obj:`~None`






