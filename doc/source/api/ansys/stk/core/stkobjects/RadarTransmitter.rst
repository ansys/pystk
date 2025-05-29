RadarTransmitter
================

.. py:class:: ansys.stk.core.stkobjects.RadarTransmitter

   Class defining the radar transmitter.

.. py:currentmodule:: RadarTransmitter

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarTransmitter.set_polarization_type`
              - Set the current polarization type.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarTransmitter.set_filter`
              - Do not use this method, as it is deprecated. Use FilterComponentLinking on RadarTransmitter instead. Sets the current filter model by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarTransmitter.frequency_specification`
              - Get or set the frequency specification.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarTransmitter.frequency`
              - Get or set the frequency.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarTransmitter.wavelength`
              - Get or set the wavelength.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarTransmitter.power`
              - Get or set the power.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarTransmitter.post_transmit_gains_losses`
              - Get the collection of additional post transmit gains and losses.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarTransmitter.enable_polarization`
              - Get or set the enable polarization option.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarTransmitter.enable_orthogonal_polarization`
              - Get or set the option for enabling the orthogonal polarization.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarTransmitter.polarization`
              - Get the polarization.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarTransmitter.power_amplifier_bandwidth`
              - Get or set the power amplifier bandwidth.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarTransmitter.enable_filter`
              - Get or set the flag determines whether or not to enable the Filter.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarTransmitter.supported_filters`
              - Do not use this property, as it is deprecated. Use FilterComponentLinking on RadarTransmitter instead. Gets an array of supported filter model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarTransmitter.filter`
              - Do not use this property, as it is deprecated. Use FilterComponentLinking on RadarTransmitter instead. Gets the current filter model.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarTransmitter.filter_component_linking`
              - Get the link/embed controller for managing the filter model component.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RadarTransmitter


Property detail
---------------

.. py:property:: frequency_specification
    :canonical: ansys.stk.core.stkobjects.RadarTransmitter.frequency_specification
    :type: RadarFrequencySpecificationType

    Get or set the frequency specification.

.. py:property:: frequency
    :canonical: ansys.stk.core.stkobjects.RadarTransmitter.frequency
    :type: float

    Get or set the frequency.

.. py:property:: wavelength
    :canonical: ansys.stk.core.stkobjects.RadarTransmitter.wavelength
    :type: float

    Get or set the wavelength.

.. py:property:: power
    :canonical: ansys.stk.core.stkobjects.RadarTransmitter.power
    :type: float

    Get or set the power.

.. py:property:: post_transmit_gains_losses
    :canonical: ansys.stk.core.stkobjects.RadarTransmitter.post_transmit_gains_losses
    :type: AdditionalGainLossCollection

    Get the collection of additional post transmit gains and losses.

.. py:property:: enable_polarization
    :canonical: ansys.stk.core.stkobjects.RadarTransmitter.enable_polarization
    :type: bool

    Get or set the enable polarization option.

.. py:property:: enable_orthogonal_polarization
    :canonical: ansys.stk.core.stkobjects.RadarTransmitter.enable_orthogonal_polarization
    :type: bool

    Get or set the option for enabling the orthogonal polarization.

.. py:property:: polarization
    :canonical: ansys.stk.core.stkobjects.RadarTransmitter.polarization
    :type: IPolarization

    Get the polarization.

.. py:property:: power_amplifier_bandwidth
    :canonical: ansys.stk.core.stkobjects.RadarTransmitter.power_amplifier_bandwidth
    :type: float

    Get or set the power amplifier bandwidth.

.. py:property:: enable_filter
    :canonical: ansys.stk.core.stkobjects.RadarTransmitter.enable_filter
    :type: bool

    Get or set the flag determines whether or not to enable the Filter.

.. py:property:: supported_filters
    :canonical: ansys.stk.core.stkobjects.RadarTransmitter.supported_filters
    :type: list

    Do not use this property, as it is deprecated. Use FilterComponentLinking on RadarTransmitter instead. Gets an array of supported filter model names.

.. py:property:: filter
    :canonical: ansys.stk.core.stkobjects.RadarTransmitter.filter
    :type: IRFFilterModel

    Do not use this property, as it is deprecated. Use FilterComponentLinking on RadarTransmitter instead. Gets the current filter model.

.. py:property:: filter_component_linking
    :canonical: ansys.stk.core.stkobjects.RadarTransmitter.filter_component_linking
    :type: IComponentLinkEmbedControl

    Get the link/embed controller for managing the filter model component.


Method detail
-------------














.. py:method:: set_polarization_type(self, value: PolarizationType) -> None
    :canonical: ansys.stk.core.stkobjects.RadarTransmitter.set_polarization_type

    Set the current polarization type.

    :Parameters:

        **value** : :obj:`~PolarizationType`


    :Returns:

        :obj:`~None`







.. py:method:: set_filter(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.RadarTransmitter.set_filter

    Do not use this method, as it is deprecated. Use FilterComponentLinking on RadarTransmitter instead. Sets the current filter model by name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~None`



