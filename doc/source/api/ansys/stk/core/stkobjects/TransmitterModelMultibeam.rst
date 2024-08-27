TransmitterModelMultibeam
=========================

.. py:class:: ansys.stk.core.stkobjects.TransmitterModelMultibeam

   Bases: :py:class:`~ansys.stk.core.stkobjects.ITransmitterModel`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining a multibeam transmitter model.

.. py:currentmodule:: TransmitterModelMultibeam

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelMultibeam.set_filter`
              - Set the current filter model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelMultibeam.set_modulator`
              - Set the current modulator model by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelMultibeam.data_rate`
              - Gets or sets the data rate.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelMultibeam.post_transmit_gains_losses`
              - Gets the collection of additional post transmit gains and losses.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelMultibeam.enable_filter`
              - Gets or set the flag determines whether or not to enable the Filter.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelMultibeam.supported_filters`
              - Gets an array of supported filter model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelMultibeam.filter`
              - Gets the current filter model.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelMultibeam.supported_modulators`
              - Gets an array of supported modulator model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelMultibeam.modulator`
              - Gets the current modulator model.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterModelMultibeam.antenna_system`
              - Gets the antenna system.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import TransmitterModelMultibeam


Property detail
---------------

.. py:property:: data_rate
    :canonical: ansys.stk.core.stkobjects.TransmitterModelMultibeam.data_rate
    :type: float

    Gets or sets the data rate.

.. py:property:: post_transmit_gains_losses
    :canonical: ansys.stk.core.stkobjects.TransmitterModelMultibeam.post_transmit_gains_losses
    :type: AdditionalGainLossCollection

    Gets the collection of additional post transmit gains and losses.

.. py:property:: enable_filter
    :canonical: ansys.stk.core.stkobjects.TransmitterModelMultibeam.enable_filter
    :type: bool

    Gets or set the flag determines whether or not to enable the Filter.

.. py:property:: supported_filters
    :canonical: ansys.stk.core.stkobjects.TransmitterModelMultibeam.supported_filters
    :type: list

    Gets an array of supported filter model names.

.. py:property:: filter
    :canonical: ansys.stk.core.stkobjects.TransmitterModelMultibeam.filter
    :type: IRFFilterModel

    Gets the current filter model.

.. py:property:: supported_modulators
    :canonical: ansys.stk.core.stkobjects.TransmitterModelMultibeam.supported_modulators
    :type: list

    Gets an array of supported modulator model names.

.. py:property:: modulator
    :canonical: ansys.stk.core.stkobjects.TransmitterModelMultibeam.modulator
    :type: IModulatorModel

    Gets the current modulator model.

.. py:property:: antenna_system
    :canonical: ansys.stk.core.stkobjects.TransmitterModelMultibeam.antenna_system
    :type: AntennaSystem

    Gets the antenna system.


Method detail
-------------







.. py:method:: set_filter(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.TransmitterModelMultibeam.set_filter

    Set the current filter model by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`



.. py:method:: set_modulator(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.TransmitterModelMultibeam.set_modulator

    Set the current modulator model by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`



