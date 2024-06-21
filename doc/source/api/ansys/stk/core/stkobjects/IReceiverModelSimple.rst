IReceiverModelSimple
====================

.. py:class:: ansys.stk.core.stkobjects.IReceiverModelSimple

   object
   
   Provide access to the properties and methods defining a simple receiver model.

.. py:currentmodule:: IReceiverModelSimple

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelSimple.set_filter`
              - Set the current filter model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelSimple.set_demodulator`
              - Set the current demodulator model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelSimple.set_polarization_type`
              - Set the current polarization type.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelSimple.enable_filter`
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelSimple.supported_filters`
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelSimple.filter`
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelSimple.pre_receive_gains_losses`
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelSimple.pre_demod_gains_losses`
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelSimple.link_margin`
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelSimple.auto_scale_bandwidth`
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelSimple.bandwidth`
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelSimple.auto_select_demodulator`
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelSimple.supported_demodulators`
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelSimple.demodulator`
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelSimple.use_rain`
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelSimple.supported_rain_outage_percent_values`
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelSimple.rain_outage_percent`
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelSimple.enable_polarization`
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelSimple.polarization`
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelSimple.auto_track_frequency`
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelSimple.frequency`
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelSimple.g_over_t`
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverModelSimple.interference`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IReceiverModelSimple


Property detail
---------------

.. py:property:: enable_filter
    :canonical: ansys.stk.core.stkobjects.IReceiverModelSimple.enable_filter
    :type: bool

    Gets or set the flag determines whether or not to enable the Filter.

.. py:property:: supported_filters
    :canonical: ansys.stk.core.stkobjects.IReceiverModelSimple.supported_filters
    :type: list

    Gets an array of supported filter model names.

.. py:property:: filter
    :canonical: ansys.stk.core.stkobjects.IReceiverModelSimple.filter
    :type: IRFFilterModel

    Gets the current filter model.

.. py:property:: pre_receive_gains_losses
    :canonical: ansys.stk.core.stkobjects.IReceiverModelSimple.pre_receive_gains_losses
    :type: IAdditionalGainLossCollection

    Gets the collection of additional pre-receive gains and losses.

.. py:property:: pre_demod_gains_losses
    :canonical: ansys.stk.core.stkobjects.IReceiverModelSimple.pre_demod_gains_losses
    :type: IAdditionalGainLossCollection

    Gets the collection of additional pre-demod gains and losses.

.. py:property:: link_margin
    :canonical: ansys.stk.core.stkobjects.IReceiverModelSimple.link_margin
    :type: ILinkMargin

    Gets the interface for configuring the link margin computation parameters.

.. py:property:: auto_scale_bandwidth
    :canonical: ansys.stk.core.stkobjects.IReceiverModelSimple.auto_scale_bandwidth
    :type: bool

    Gets or set the auto scale bandwidth option.

.. py:property:: bandwidth
    :canonical: ansys.stk.core.stkobjects.IReceiverModelSimple.bandwidth
    :type: float

    Gets or set the bandwidth.

.. py:property:: auto_select_demodulator
    :canonical: ansys.stk.core.stkobjects.IReceiverModelSimple.auto_select_demodulator
    :type: bool

    Gets or set the auto select demodulator option.

.. py:property:: supported_demodulators
    :canonical: ansys.stk.core.stkobjects.IReceiverModelSimple.supported_demodulators
    :type: list

    Gets an array of supported demodulator model names.

.. py:property:: demodulator
    :canonical: ansys.stk.core.stkobjects.IReceiverModelSimple.demodulator
    :type: IDemodulatorModel

    Gets the current demodulator model.

.. py:property:: use_rain
    :canonical: ansys.stk.core.stkobjects.IReceiverModelSimple.use_rain
    :type: bool

    Gets or sets the option for computing rain loss.

.. py:property:: supported_rain_outage_percent_values
    :canonical: ansys.stk.core.stkobjects.IReceiverModelSimple.supported_rain_outage_percent_values
    :type: list

    Gets an array of supported rain outage percent values.

.. py:property:: rain_outage_percent
    :canonical: ansys.stk.core.stkobjects.IReceiverModelSimple.rain_outage_percent
    :type: float

    Gets or sets the rain outage percent.

.. py:property:: enable_polarization
    :canonical: ansys.stk.core.stkobjects.IReceiverModelSimple.enable_polarization
    :type: bool

    Gets or sets the enable polarization option.

.. py:property:: polarization
    :canonical: ansys.stk.core.stkobjects.IReceiverModelSimple.polarization
    :type: IPolarization

    Gets the polarization.

.. py:property:: auto_track_frequency
    :canonical: ansys.stk.core.stkobjects.IReceiverModelSimple.auto_track_frequency
    :type: bool

    Gets or set the auto track frequency option.

.. py:property:: frequency
    :canonical: ansys.stk.core.stkobjects.IReceiverModelSimple.frequency
    :type: float

    Gets or set the frequency.

.. py:property:: g_over_t
    :canonical: ansys.stk.core.stkobjects.IReceiverModelSimple.g_over_t
    :type: float

    Gets or set the G/T.

.. py:property:: interference
    :canonical: ansys.stk.core.stkobjects.IReceiverModelSimple.interference
    :type: IRFInterference

    Gets the radio frequency interference.


Method detail
-------------




.. py:method:: set_filter(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.IReceiverModelSimple.set_filter

    Set the current filter model by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`












.. py:method:: set_demodulator(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.IReceiverModelSimple.set_demodulator

    Set the current demodulator model by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`









.. py:method:: set_polarization_type(self, val: POLARIZATION_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.IReceiverModelSimple.set_polarization_type

    Set the current polarization type.

    :Parameters:

    **val** : :obj:`~POLARIZATION_TYPE`

    :Returns:

        :obj:`~None`









