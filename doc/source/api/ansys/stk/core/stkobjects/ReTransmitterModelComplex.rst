ReTransmitterModelComplex
=========================

.. py:class:: ansys.stk.core.stkobjects.ReTransmitterModelComplex

   Bases: :py:class:`~ansys.stk.core.stkobjects.IReTransmitterModel`, :py:class:`~ansys.stk.core.stkobjects.ITransmitterModel`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining a complex re-transmitter model.

.. py:currentmodule:: ReTransmitterModelComplex

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ReTransmitterModelComplex.set_polarization_type`
              - Set the current polarization type.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReTransmitterModelComplex.set_filter`
              - Do not use this method, as it is deprecated. Use FilterComponentLinking on IAgReTransmitterModelComplex instead. Sets the current filter model by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ReTransmitterModelComplex.enable_polarization`
              - Get or set the enable polarization option.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReTransmitterModelComplex.polarization`
              - Get the polarization.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReTransmitterModelComplex.post_transmit_gains_losses`
              - Get the collection of additional post transmit gains and losses.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReTransmitterModelComplex.enable_filter`
              - Get or set the flag determines whether or not to enable the Filter.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReTransmitterModelComplex.supported_filters`
              - Do not use this property, as it is deprecated. Use FilterComponentLinking on IAgReTransmitterModelComplex instead. Gets an array of supported filter model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReTransmitterModelComplex.filter`
              - Do not use this property, as it is deprecated. Use FilterComponentLinking on IAgReTransmitterModelComplex instead. Gets the current filter model.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReTransmitterModelComplex.saturated_power`
              - Get or set the saturated power.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReTransmitterModelComplex.antenna_control`
              - Get the receiver antenna control.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReTransmitterModelComplex.filter_component_linking`
              - Get the link/embed controller for managing the filter model component.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ReTransmitterModelComplex


Property detail
---------------

.. py:property:: enable_polarization
    :canonical: ansys.stk.core.stkobjects.ReTransmitterModelComplex.enable_polarization
    :type: bool

    Get or set the enable polarization option.

.. py:property:: polarization
    :canonical: ansys.stk.core.stkobjects.ReTransmitterModelComplex.polarization
    :type: IPolarization

    Get the polarization.

.. py:property:: post_transmit_gains_losses
    :canonical: ansys.stk.core.stkobjects.ReTransmitterModelComplex.post_transmit_gains_losses
    :type: AdditionalGainLossCollection

    Get the collection of additional post transmit gains and losses.

.. py:property:: enable_filter
    :canonical: ansys.stk.core.stkobjects.ReTransmitterModelComplex.enable_filter
    :type: bool

    Get or set the flag determines whether or not to enable the Filter.

.. py:property:: supported_filters
    :canonical: ansys.stk.core.stkobjects.ReTransmitterModelComplex.supported_filters
    :type: list

    Do not use this property, as it is deprecated. Use FilterComponentLinking on IAgReTransmitterModelComplex instead. Gets an array of supported filter model names.

.. py:property:: filter
    :canonical: ansys.stk.core.stkobjects.ReTransmitterModelComplex.filter
    :type: IRFFilterModel

    Do not use this property, as it is deprecated. Use FilterComponentLinking on IAgReTransmitterModelComplex instead. Gets the current filter model.

.. py:property:: saturated_power
    :canonical: ansys.stk.core.stkobjects.ReTransmitterModelComplex.saturated_power
    :type: float

    Get or set the saturated power.

.. py:property:: antenna_control
    :canonical: ansys.stk.core.stkobjects.ReTransmitterModelComplex.antenna_control
    :type: AntennaControl

    Get the receiver antenna control.

.. py:property:: filter_component_linking
    :canonical: ansys.stk.core.stkobjects.ReTransmitterModelComplex.filter_component_linking
    :type: IComponentLinkEmbedControl

    Get the link/embed controller for managing the filter model component.


Method detail
-------------



.. py:method:: set_polarization_type(self, value: PolarizationType) -> None
    :canonical: ansys.stk.core.stkobjects.ReTransmitterModelComplex.set_polarization_type

    Set the current polarization type.

    :Parameters:

    **value** : :obj:`~PolarizationType`

    :Returns:

        :obj:`~None`






.. py:method:: set_filter(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.ReTransmitterModelComplex.set_filter

    Do not use this method, as it is deprecated. Use FilterComponentLinking on IAgReTransmitterModelComplex instead. Sets the current filter model by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`






