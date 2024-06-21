ITransmitterModelMedium
=======================

.. py:class:: ansys.stk.core.stkobjects.ITransmitterModelMedium

   object
   
   Provide access to the properties and methods defining a medium transmitter model.

.. py:currentmodule:: ITransmitterModelMedium

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ITransmitterModelMedium.set_polarization_type`
              - Set the current polarization type.
            * - :py:attr:`~ansys.stk.core.stkobjects.ITransmitterModelMedium.set_filter`
              - Set the current filter model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.ITransmitterModelMedium.set_modulator`
              - Set the current modulator model by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ITransmitterModelMedium.frequency`
            * - :py:attr:`~ansys.stk.core.stkobjects.ITransmitterModelMedium.data_rate`
            * - :py:attr:`~ansys.stk.core.stkobjects.ITransmitterModelMedium.power`
            * - :py:attr:`~ansys.stk.core.stkobjects.ITransmitterModelMedium.antenna_gain`
            * - :py:attr:`~ansys.stk.core.stkobjects.ITransmitterModelMedium.enable_polarization`
            * - :py:attr:`~ansys.stk.core.stkobjects.ITransmitterModelMedium.polarization`
            * - :py:attr:`~ansys.stk.core.stkobjects.ITransmitterModelMedium.post_transmit_gains_losses`
            * - :py:attr:`~ansys.stk.core.stkobjects.ITransmitterModelMedium.enable_filter`
            * - :py:attr:`~ansys.stk.core.stkobjects.ITransmitterModelMedium.supported_filters`
            * - :py:attr:`~ansys.stk.core.stkobjects.ITransmitterModelMedium.filter`
            * - :py:attr:`~ansys.stk.core.stkobjects.ITransmitterModelMedium.supported_modulators`
            * - :py:attr:`~ansys.stk.core.stkobjects.ITransmitterModelMedium.modulator`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ITransmitterModelMedium


Property detail
---------------

.. py:property:: frequency
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelMedium.frequency
    :type: float

    Gets or sets the carrier frequency.

.. py:property:: data_rate
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelMedium.data_rate
    :type: float

    Gets or sets the data rate.

.. py:property:: power
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelMedium.power
    :type: float

    Gets or sets the power.

.. py:property:: antenna_gain
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelMedium.antenna_gain
    :type: float

    Gets or sets the antenna gain.

.. py:property:: enable_polarization
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelMedium.enable_polarization
    :type: bool

    Gets or sets the enable polarization option.

.. py:property:: polarization
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelMedium.polarization
    :type: IPolarization

    Gets the polarization.

.. py:property:: post_transmit_gains_losses
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelMedium.post_transmit_gains_losses
    :type: IAdditionalGainLossCollection

    Gets the collection of additional post transmit gains and losses.

.. py:property:: enable_filter
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelMedium.enable_filter
    :type: bool

    Gets or set the flag determines whether or not to enable the Filter.

.. py:property:: supported_filters
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelMedium.supported_filters
    :type: list

    Gets an array of supported filter model names.

.. py:property:: filter
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelMedium.filter
    :type: IRFFilterModel

    Gets the current filter model.

.. py:property:: supported_modulators
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelMedium.supported_modulators
    :type: list

    Gets an array of supported modulator model names.

.. py:property:: modulator
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelMedium.modulator
    :type: IModulatorModel

    Gets the current modulator model.


Method detail
-------------











.. py:method:: set_polarization_type(self, val: POLARIZATION_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelMedium.set_polarization_type

    Set the current polarization type.

    :Parameters:

    **val** : :obj:`~POLARIZATION_TYPE`

    :Returns:

        :obj:`~None`






.. py:method:: set_filter(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelMedium.set_filter

    Set the current filter model by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`



.. py:method:: set_modulator(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelMedium.set_modulator

    Set the current modulator model by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`


