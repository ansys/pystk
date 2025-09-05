RadarTransmitterMultifunction
=============================

.. py:class:: ansys.stk.core.stkobjects.RadarTransmitterMultifunction

   Class defining the multifunction radar transmitter.

.. py:currentmodule:: RadarTransmitterMultifunction

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarTransmitterMultifunction.set_filter`
              - Do not use this method, as it is deprecated. Use FilterComponentLinking on RadarTransmitterMultifunction instead. Sets the current filter model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarTransmitterMultifunction.set_polarization_type`
              - Set the current polarization type.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarTransmitterMultifunction.enable_filter`
              - Get or set the flag determines whether or not to enable the Filter.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarTransmitterMultifunction.enable_orthogonal_polarization`
              - Get or set the option for enabling the orthogonal polarization.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarTransmitterMultifunction.enable_polarization`
              - Get or set the enable polarization option.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarTransmitterMultifunction.filter`
              - Do not use this property, as it is deprecated. Use FilterComponentLinking on RadarTransmitterMultifunction instead. Gets the current filter model.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarTransmitterMultifunction.filter_component_linking`
              - Get the link/embed controller for managing the filter model component.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarTransmitterMultifunction.maximum_power_limit`
              - Get or set the power.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarTransmitterMultifunction.polarization`
              - Get the polarization.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarTransmitterMultifunction.post_transmit_gains_losses`
              - Get the collection of additional post transmit gains and losses.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarTransmitterMultifunction.power_amplifier_bandwidth`
              - Get or set the power amplifier bandwidth.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarTransmitterMultifunction.supported_filters`
              - Do not use this property, as it is deprecated. Use FilterComponentLinking on RadarTransmitterMultifunction instead. Gets an array of supported filter model names.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RadarTransmitterMultifunction


Property detail
---------------

.. py:property:: enable_filter
    :canonical: ansys.stk.core.stkobjects.RadarTransmitterMultifunction.enable_filter
    :type: bool

    Get or set the flag determines whether or not to enable the Filter.

.. py:property:: enable_orthogonal_polarization
    :canonical: ansys.stk.core.stkobjects.RadarTransmitterMultifunction.enable_orthogonal_polarization
    :type: bool

    Get or set the option for enabling the orthogonal polarization.

.. py:property:: enable_polarization
    :canonical: ansys.stk.core.stkobjects.RadarTransmitterMultifunction.enable_polarization
    :type: bool

    Get or set the enable polarization option.

.. py:property:: filter
    :canonical: ansys.stk.core.stkobjects.RadarTransmitterMultifunction.filter
    :type: IRFFilterModel

    Do not use this property, as it is deprecated. Use FilterComponentLinking on RadarTransmitterMultifunction instead. Gets the current filter model.

.. py:property:: filter_component_linking
    :canonical: ansys.stk.core.stkobjects.RadarTransmitterMultifunction.filter_component_linking
    :type: IComponentLinkEmbedControl

    Get the link/embed controller for managing the filter model component.

.. py:property:: maximum_power_limit
    :canonical: ansys.stk.core.stkobjects.RadarTransmitterMultifunction.maximum_power_limit
    :type: float

    Get or set the power.

.. py:property:: polarization
    :canonical: ansys.stk.core.stkobjects.RadarTransmitterMultifunction.polarization
    :type: IPolarization

    Get the polarization.

.. py:property:: post_transmit_gains_losses
    :canonical: ansys.stk.core.stkobjects.RadarTransmitterMultifunction.post_transmit_gains_losses
    :type: AdditionalGainLossCollection

    Get the collection of additional post transmit gains and losses.

.. py:property:: power_amplifier_bandwidth
    :canonical: ansys.stk.core.stkobjects.RadarTransmitterMultifunction.power_amplifier_bandwidth
    :type: float

    Get or set the power amplifier bandwidth.

.. py:property:: supported_filters
    :canonical: ansys.stk.core.stkobjects.RadarTransmitterMultifunction.supported_filters
    :type: list

    Do not use this property, as it is deprecated. Use FilterComponentLinking on RadarTransmitterMultifunction instead. Gets an array of supported filter model names.


Method detail
-------------















.. py:method:: set_filter(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.RadarTransmitterMultifunction.set_filter

    Do not use this method, as it is deprecated. Use FilterComponentLinking on RadarTransmitterMultifunction instead. Sets the current filter model by name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: set_polarization_type(self, value: PolarizationType) -> None
    :canonical: ansys.stk.core.stkobjects.RadarTransmitterMultifunction.set_polarization_type

    Set the current polarization type.

    :Parameters:

        **value** : :obj:`~PolarizationType`


    :Returns:

        :obj:`~None`


