TransmitterModelComplex
=======================

.. py:class:: ansys.stk.core.stkobjects.TransmitterModelComplex

   Bases: :py:class:`~ansys.stk.core.stkobjects.ITransmitterModel`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining a complex transmitter model.

.. py:currentmodule:: TransmitterModelComplex

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelComplex.set_polarization_type`
              - Set the current polarization type.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelComplex.set_filter`
              - Do not use this method, as it is deprecated. Use FilterComponentLinking on IAgTransmitterModelComplex instead. Sets the current filter model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelComplex.set_modulator`
              - Set the current modulator model by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelComplex.frequency`
              - Get or set the carrier frequency.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelComplex.data_rate`
              - Get or set the data rate.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelComplex.power`
              - Get or set the power.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelComplex.antenna_control`
              - Get the receiver antenna control.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelComplex.enable_polarization`
              - Get or set the enable polarization option.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelComplex.polarization`
              - Get the polarization.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelComplex.post_transmit_gains_losses`
              - Get the collection of additional post transmit gains and losses.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelComplex.enable_filter`
              - Get or set the flag determines whether or not to enable the Filter.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelComplex.supported_filters`
              - Do not use this property, as it is deprecated. Use FilterComponentLinking on IAgTransmitterModelComplex instead. Gets an array of supported filter model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelComplex.filter`
              - Do not use this property, as it is deprecated. Use FilterComponentLinking on IAgTransmitterModelComplex instead. Gets the current filter model.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelComplex.supported_modulators`
              - Get an array of supported modulator model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelComplex.modulator`
              - Get the current modulator model.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelComplex.filter_component_linking`
              - Get the link/embed controller for managing the filter model component.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import TransmitterModelComplex


Property detail
---------------

.. py:property:: frequency
    :canonical: ansys.stk.core.stkobjects.TransmitterModelComplex.frequency
    :type: float

    Get or set the carrier frequency.

.. py:property:: data_rate
    :canonical: ansys.stk.core.stkobjects.TransmitterModelComplex.data_rate
    :type: float

    Get or set the data rate.

.. py:property:: power
    :canonical: ansys.stk.core.stkobjects.TransmitterModelComplex.power
    :type: float

    Get or set the power.

.. py:property:: antenna_control
    :canonical: ansys.stk.core.stkobjects.TransmitterModelComplex.antenna_control
    :type: AntennaControl

    Get the receiver antenna control.

.. py:property:: enable_polarization
    :canonical: ansys.stk.core.stkobjects.TransmitterModelComplex.enable_polarization
    :type: bool

    Get or set the enable polarization option.

.. py:property:: polarization
    :canonical: ansys.stk.core.stkobjects.TransmitterModelComplex.polarization
    :type: IPolarization

    Get the polarization.

.. py:property:: post_transmit_gains_losses
    :canonical: ansys.stk.core.stkobjects.TransmitterModelComplex.post_transmit_gains_losses
    :type: AdditionalGainLossCollection

    Get the collection of additional post transmit gains and losses.

.. py:property:: enable_filter
    :canonical: ansys.stk.core.stkobjects.TransmitterModelComplex.enable_filter
    :type: bool

    Get or set the flag determines whether or not to enable the Filter.

.. py:property:: supported_filters
    :canonical: ansys.stk.core.stkobjects.TransmitterModelComplex.supported_filters
    :type: list

    Do not use this property, as it is deprecated. Use FilterComponentLinking on IAgTransmitterModelComplex instead. Gets an array of supported filter model names.

.. py:property:: filter
    :canonical: ansys.stk.core.stkobjects.TransmitterModelComplex.filter
    :type: IRFFilterModel

    Do not use this property, as it is deprecated. Use FilterComponentLinking on IAgTransmitterModelComplex instead. Gets the current filter model.

.. py:property:: supported_modulators
    :canonical: ansys.stk.core.stkobjects.TransmitterModelComplex.supported_modulators
    :type: list

    Get an array of supported modulator model names.

.. py:property:: modulator
    :canonical: ansys.stk.core.stkobjects.TransmitterModelComplex.modulator
    :type: IModulatorModel

    Get the current modulator model.

.. py:property:: filter_component_linking
    :canonical: ansys.stk.core.stkobjects.TransmitterModelComplex.filter_component_linking
    :type: IComponentLinkEmbedControl

    Get the link/embed controller for managing the filter model component.


Method detail
-------------










.. py:method:: set_polarization_type(self, value: PolarizationType) -> None
    :canonical: ansys.stk.core.stkobjects.TransmitterModelComplex.set_polarization_type

    Set the current polarization type.

    :Parameters:

    **value** : :obj:`~PolarizationType`

    :Returns:

        :obj:`~None`






.. py:method:: set_filter(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.TransmitterModelComplex.set_filter

    Do not use this method, as it is deprecated. Use FilterComponentLinking on IAgTransmitterModelComplex instead. Sets the current filter model by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`



.. py:method:: set_modulator(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.TransmitterModelComplex.set_modulator

    Set the current modulator model by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`



