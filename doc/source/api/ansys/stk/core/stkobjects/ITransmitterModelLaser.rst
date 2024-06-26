ITransmitterModelLaser
======================

.. py:class:: ansys.stk.core.stkobjects.ITransmitterModelLaser

   object
   
   Provide access to the properties and methods defining a laser transmitter model.

.. py:currentmodule:: ITransmitterModelLaser

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ITransmitterModelLaser.set_polarization_type`
              - Set the current polarization type.
            * - :py:attr:`~ansys.stk.core.stkobjects.ITransmitterModelLaser.set_filter`
              - Set the current filter model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.ITransmitterModelLaser.set_modulator`
              - Set the current modulator model by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ITransmitterModelLaser.frequency`
              - Gets or sets the carrier frequency.
            * - :py:attr:`~ansys.stk.core.stkobjects.ITransmitterModelLaser.data_rate`
              - Gets or sets the data rate.
            * - :py:attr:`~ansys.stk.core.stkobjects.ITransmitterModelLaser.power`
              - Gets or sets the power.
            * - :py:attr:`~ansys.stk.core.stkobjects.ITransmitterModelLaser.antenna_control`
              - Gets the receiver antenna control.
            * - :py:attr:`~ansys.stk.core.stkobjects.ITransmitterModelLaser.enable_polarization`
              - Gets or sets the enable polarization option.
            * - :py:attr:`~ansys.stk.core.stkobjects.ITransmitterModelLaser.polarization`
              - Gets the polarization.
            * - :py:attr:`~ansys.stk.core.stkobjects.ITransmitterModelLaser.post_transmit_gains_losses`
              - Gets the collection of additional post transmit gains and losses.
            * - :py:attr:`~ansys.stk.core.stkobjects.ITransmitterModelLaser.enable_filter`
              - Gets or set the flag determines whether or not to enable the Filter.
            * - :py:attr:`~ansys.stk.core.stkobjects.ITransmitterModelLaser.supported_filters`
              - Gets an array of supported filter model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.ITransmitterModelLaser.filter`
              - Gets the current filter model.
            * - :py:attr:`~ansys.stk.core.stkobjects.ITransmitterModelLaser.supported_modulators`
              - Gets an array of supported modulator model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.ITransmitterModelLaser.modulator`
              - Gets the current modulator model.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ITransmitterModelLaser


Property detail
---------------

.. py:property:: frequency
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelLaser.frequency
    :type: float

    Gets or sets the carrier frequency.

.. py:property:: data_rate
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelLaser.data_rate
    :type: float

    Gets or sets the data rate.

.. py:property:: power
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelLaser.power
    :type: float

    Gets or sets the power.

.. py:property:: antenna_control
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelLaser.antenna_control
    :type: IAntennaControl

    Gets the receiver antenna control.

.. py:property:: enable_polarization
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelLaser.enable_polarization
    :type: bool

    Gets or sets the enable polarization option.

.. py:property:: polarization
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelLaser.polarization
    :type: IPolarization

    Gets the polarization.

.. py:property:: post_transmit_gains_losses
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelLaser.post_transmit_gains_losses
    :type: IAdditionalGainLossCollection

    Gets the collection of additional post transmit gains and losses.

.. py:property:: enable_filter
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelLaser.enable_filter
    :type: bool

    Gets or set the flag determines whether or not to enable the Filter.

.. py:property:: supported_filters
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelLaser.supported_filters
    :type: list

    Gets an array of supported filter model names.

.. py:property:: filter
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelLaser.filter
    :type: IRFFilterModel

    Gets the current filter model.

.. py:property:: supported_modulators
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelLaser.supported_modulators
    :type: list

    Gets an array of supported modulator model names.

.. py:property:: modulator
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelLaser.modulator
    :type: IModulatorModel

    Gets the current modulator model.


Method detail
-------------










.. py:method:: set_polarization_type(self, val: POLARIZATION_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelLaser.set_polarization_type

    Set the current polarization type.

    :Parameters:

    **val** : :obj:`~POLARIZATION_TYPE`

    :Returns:

        :obj:`~None`






.. py:method:: set_filter(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelLaser.set_filter

    Set the current filter model by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`



.. py:method:: set_modulator(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelLaser.set_modulator

    Set the current modulator model by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`


