TransmitterModelSimple
======================

.. py:class:: ansys.stk.core.stkobjects.TransmitterModelSimple

   Bases: :py:class:`~ansys.stk.core.stkobjects.ITransmitterModel`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining a simple transmitter model.

.. py:currentmodule:: TransmitterModelSimple

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelSimple.set_polarization_type`
              - Set the current polarization type.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelSimple.set_filter`
              - Do not use this method, as it is deprecated. Use FilterComponentLinking on TransmitterModelSimple instead. Sets the current filter model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelSimple.set_modulator`
              - Set the current modulator model by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelSimple.frequency`
              - Get or set the carrier frequency.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelSimple.data_rate`
              - Get or set the data rate.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelSimple.eirp`
              - Get or set the EIRP.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelSimple.enable_polarization`
              - Get or set the enable polarization option.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelSimple.polarization`
              - Get the polarization.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelSimple.post_transmit_gains_losses`
              - Get the collection of additional post transmit gains and losses.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelSimple.enable_filter`
              - Get or set the flag determines whether or not to enable the Filter.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelSimple.supported_filters`
              - Do not use this property, as it is deprecated. Use FilterComponentLinking on TransmitterModelSimple instead. Gets an array of supported filter model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelSimple.filter`
              - Do not use this property, as it is deprecated. Use FilterComponentLinking on TransmitterModelSimple instead. Gets the current filter model.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelSimple.supported_modulators`
              - Get an array of supported modulator model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelSimple.modulator`
              - Get the current modulator model.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelSimple.filter_component_linking`
              - Get the link/embed controller for managing the filter model component.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import TransmitterModelSimple


Property detail
---------------

.. py:property:: frequency
    :canonical: ansys.stk.core.stkobjects.TransmitterModelSimple.frequency
    :type: float

    Get or set the carrier frequency.

.. py:property:: data_rate
    :canonical: ansys.stk.core.stkobjects.TransmitterModelSimple.data_rate
    :type: float

    Get or set the data rate.

.. py:property:: eirp
    :canonical: ansys.stk.core.stkobjects.TransmitterModelSimple.eirp
    :type: float

    Get or set the EIRP.

.. py:property:: enable_polarization
    :canonical: ansys.stk.core.stkobjects.TransmitterModelSimple.enable_polarization
    :type: bool

    Get or set the enable polarization option.

.. py:property:: polarization
    :canonical: ansys.stk.core.stkobjects.TransmitterModelSimple.polarization
    :type: IPolarization

    Get the polarization.

.. py:property:: post_transmit_gains_losses
    :canonical: ansys.stk.core.stkobjects.TransmitterModelSimple.post_transmit_gains_losses
    :type: AdditionalGainLossCollection

    Get the collection of additional post transmit gains and losses.

.. py:property:: enable_filter
    :canonical: ansys.stk.core.stkobjects.TransmitterModelSimple.enable_filter
    :type: bool

    Get or set the flag determines whether or not to enable the Filter.

.. py:property:: supported_filters
    :canonical: ansys.stk.core.stkobjects.TransmitterModelSimple.supported_filters
    :type: list

    Do not use this property, as it is deprecated. Use FilterComponentLinking on TransmitterModelSimple instead. Gets an array of supported filter model names.

.. py:property:: filter
    :canonical: ansys.stk.core.stkobjects.TransmitterModelSimple.filter
    :type: IRFFilterModel

    Do not use this property, as it is deprecated. Use FilterComponentLinking on TransmitterModelSimple instead. Gets the current filter model.

.. py:property:: supported_modulators
    :canonical: ansys.stk.core.stkobjects.TransmitterModelSimple.supported_modulators
    :type: list

    Get an array of supported modulator model names.

.. py:property:: modulator
    :canonical: ansys.stk.core.stkobjects.TransmitterModelSimple.modulator
    :type: IModulatorModel

    Get the current modulator model.

.. py:property:: filter_component_linking
    :canonical: ansys.stk.core.stkobjects.TransmitterModelSimple.filter_component_linking
    :type: IComponentLinkEmbedControl

    Get the link/embed controller for managing the filter model component.


Method detail
-------------









.. py:method:: set_polarization_type(self, value: PolarizationType) -> None
    :canonical: ansys.stk.core.stkobjects.TransmitterModelSimple.set_polarization_type

    Set the current polarization type.

    :Parameters:

        **value** : :obj:`~PolarizationType`


    :Returns:

        :obj:`~None`






.. py:method:: set_filter(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.TransmitterModelSimple.set_filter

    Do not use this method, as it is deprecated. Use FilterComponentLinking on TransmitterModelSimple instead. Sets the current filter model by name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~None`



.. py:method:: set_modulator(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.TransmitterModelSimple.set_modulator

    Set the current modulator model by name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~None`



