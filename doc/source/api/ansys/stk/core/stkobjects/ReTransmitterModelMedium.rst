ReTransmitterModelMedium
========================

.. py:class:: ansys.stk.core.stkobjects.ReTransmitterModelMedium

   Bases: :py:class:`~ansys.stk.core.stkobjects.IReTransmitterModel`, :py:class:`~ansys.stk.core.stkobjects.ITransmitterModel`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining a medium re-transmitter model.

.. py:currentmodule:: ReTransmitterModelMedium

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ReTransmitterModelMedium.set_polarization_type`
              - Set the current polarization type.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ReTransmitterModelMedium.antenna_gain`
              - Get or set the antenna gain.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReTransmitterModelMedium.enable_filter`
              - Get or set the flag determines whether or not to enable the Filter.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReTransmitterModelMedium.enable_polarization`
              - Get or set the enable polarization option.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReTransmitterModelMedium.filter_component_linking`
              - Get the link/embed controller for managing the filter model component.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReTransmitterModelMedium.polarization`
              - Get the polarization.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReTransmitterModelMedium.post_transmit_gains_losses`
              - Get the collection of additional post transmit gains and losses.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReTransmitterModelMedium.saturated_power`
              - Get or set the saturated power.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ReTransmitterModelMedium


Property detail
---------------

.. py:property:: antenna_gain
    :canonical: ansys.stk.core.stkobjects.ReTransmitterModelMedium.antenna_gain
    :type: float

    Get or set the antenna gain.

.. py:property:: enable_filter
    :canonical: ansys.stk.core.stkobjects.ReTransmitterModelMedium.enable_filter
    :type: bool

    Get or set the flag determines whether or not to enable the Filter.

.. py:property:: enable_polarization
    :canonical: ansys.stk.core.stkobjects.ReTransmitterModelMedium.enable_polarization
    :type: bool

    Get or set the enable polarization option.

.. py:property:: filter_component_linking
    :canonical: ansys.stk.core.stkobjects.ReTransmitterModelMedium.filter_component_linking
    :type: IComponentLinkEmbedControl

    Get the link/embed controller for managing the filter model component.

.. py:property:: polarization
    :canonical: ansys.stk.core.stkobjects.ReTransmitterModelMedium.polarization
    :type: IPolarization

    Get the polarization.

.. py:property:: post_transmit_gains_losses
    :canonical: ansys.stk.core.stkobjects.ReTransmitterModelMedium.post_transmit_gains_losses
    :type: AdditionalGainLossCollection

    Get the collection of additional post transmit gains and losses.

.. py:property:: saturated_power
    :canonical: ansys.stk.core.stkobjects.ReTransmitterModelMedium.saturated_power
    :type: float

    Get or set the saturated power.


Method detail
-------------












.. py:method:: set_polarization_type(self, value: PolarizationType) -> None
    :canonical: ansys.stk.core.stkobjects.ReTransmitterModelMedium.set_polarization_type

    Set the current polarization type.

    :Parameters:

        **value** : :obj:`~PolarizationType`


    :Returns:

        :obj:`~None`

