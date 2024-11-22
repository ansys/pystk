TransmitterModelMedium
======================

.. py:class:: ansys.stk.core.stkobjects.TransmitterModelMedium

   Bases: :py:class:`~ansys.stk.core.stkobjects.ITransmitterModel`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining a medium transmitter model.

.. py:currentmodule:: TransmitterModelMedium

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelMedium.set_polarization_type`
              - Set the current polarization type.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelMedium.set_filter`
              - Do not use this method, as it is deprecated. Use FilterComponentLinking on IAgTransmitterModelMedium instead. Sets the current filter model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelMedium.set_modulator`
              - Set the current modulator model by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelMedium.frequency`
              - Gets or sets the carrier frequency.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelMedium.data_rate`
              - Gets or sets the data rate.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelMedium.power`
              - Gets or sets the power.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelMedium.antenna_gain`
              - Gets or sets the antenna gain.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelMedium.enable_polarization`
              - Gets or sets the enable polarization option.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelMedium.polarization`
              - Gets the polarization.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelMedium.post_transmit_gains_losses`
              - Gets the collection of additional post transmit gains and losses.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelMedium.enable_filter`
              - Gets or set the flag determines whether or not to enable the Filter.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelMedium.supported_filters`
              - This property is deprecated. Use FilterComponentLinking on IAgTransmitterModelMedium instead. Gets an array of supported filter model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelMedium.filter`
              - This property is deprecated. Use FilterComponentLinking on IAgTransmitterModelMedium instead. Gets the current filter model.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelMedium.supported_modulators`
              - Gets an array of supported modulator model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelMedium.modulator`
              - Gets the current modulator model.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelMedium.filter_component_linking`
              - Gets the link/embed controller for managing the filter model component.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import TransmitterModelMedium


Property detail
---------------

.. py:property:: frequency
    :canonical: ansys.stk.core.stkobjects.TransmitterModelMedium.frequency
    :type: float

    Gets or sets the carrier frequency.

.. py:property:: data_rate
    :canonical: ansys.stk.core.stkobjects.TransmitterModelMedium.data_rate
    :type: float

    Gets or sets the data rate.

.. py:property:: power
    :canonical: ansys.stk.core.stkobjects.TransmitterModelMedium.power
    :type: float

    Gets or sets the power.

.. py:property:: antenna_gain
    :canonical: ansys.stk.core.stkobjects.TransmitterModelMedium.antenna_gain
    :type: float

    Gets or sets the antenna gain.

.. py:property:: enable_polarization
    :canonical: ansys.stk.core.stkobjects.TransmitterModelMedium.enable_polarization
    :type: bool

    Gets or sets the enable polarization option.

.. py:property:: polarization
    :canonical: ansys.stk.core.stkobjects.TransmitterModelMedium.polarization
    :type: IPolarization

    Gets the polarization.

.. py:property:: post_transmit_gains_losses
    :canonical: ansys.stk.core.stkobjects.TransmitterModelMedium.post_transmit_gains_losses
    :type: AdditionalGainLossCollection

    Gets the collection of additional post transmit gains and losses.

.. py:property:: enable_filter
    :canonical: ansys.stk.core.stkobjects.TransmitterModelMedium.enable_filter
    :type: bool

    Gets or set the flag determines whether or not to enable the Filter.

.. py:property:: supported_filters
    :canonical: ansys.stk.core.stkobjects.TransmitterModelMedium.supported_filters
    :type: list

    This property is deprecated. Use FilterComponentLinking on IAgTransmitterModelMedium instead. Gets an array of supported filter model names.

.. py:property:: filter
    :canonical: ansys.stk.core.stkobjects.TransmitterModelMedium.filter
    :type: IRFFilterModel

    This property is deprecated. Use FilterComponentLinking on IAgTransmitterModelMedium instead. Gets the current filter model.

.. py:property:: supported_modulators
    :canonical: ansys.stk.core.stkobjects.TransmitterModelMedium.supported_modulators
    :type: list

    Gets an array of supported modulator model names.

.. py:property:: modulator
    :canonical: ansys.stk.core.stkobjects.TransmitterModelMedium.modulator
    :type: IModulatorModel

    Gets the current modulator model.

.. py:property:: filter_component_linking
    :canonical: ansys.stk.core.stkobjects.TransmitterModelMedium.filter_component_linking
    :type: IComponentLinkEmbedControl

    Gets the link/embed controller for managing the filter model component.


Method detail
-------------











.. py:method:: set_polarization_type(self, value: POLARIZATION_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.TransmitterModelMedium.set_polarization_type

    Set the current polarization type.

    :Parameters:

    **value** : :obj:`~POLARIZATION_TYPE`

    :Returns:

        :obj:`~None`






.. py:method:: set_filter(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.TransmitterModelMedium.set_filter

    Do not use this method, as it is deprecated. Use FilterComponentLinking on IAgTransmitterModelMedium instead. Sets the current filter model by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`



.. py:method:: set_modulator(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.TransmitterModelMedium.set_modulator

    Set the current modulator model by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`



