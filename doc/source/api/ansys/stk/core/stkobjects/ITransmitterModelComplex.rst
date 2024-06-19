ITransmitterModelComplex
========================

.. py:class:: ITransmitterModelComplex

   object
   
   Provide access to the properties and methods defining a complex transmitter model.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_polarization_type`
              - Set the current polarization type.
            * - :py:meth:`~set_filter`
              - Set the current filter model by name.
            * - :py:meth:`~set_modulator`
              - Set the current modulator model by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~frequency`
            * - :py:meth:`~data_rate`
            * - :py:meth:`~power`
            * - :py:meth:`~antenna_control`
            * - :py:meth:`~enable_polarization`
            * - :py:meth:`~polarization`
            * - :py:meth:`~post_transmit_gains_losses`
            * - :py:meth:`~enable_filter`
            * - :py:meth:`~supported_filters`
            * - :py:meth:`~filter`
            * - :py:meth:`~supported_modulators`
            * - :py:meth:`~modulator`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ITransmitterModelComplex


Property detail
---------------

.. py:property:: frequency
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelComplex.frequency
    :type: float

    Gets or sets the carrier frequency.

.. py:property:: data_rate
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelComplex.data_rate
    :type: float

    Gets or sets the data rate.

.. py:property:: power
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelComplex.power
    :type: float

    Gets or sets the power.

.. py:property:: antenna_control
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelComplex.antenna_control
    :type: IAgAntennaControl

    Gets the receiver antenna control.

.. py:property:: enable_polarization
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelComplex.enable_polarization
    :type: bool

    Gets or sets the enable polarization option.

.. py:property:: polarization
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelComplex.polarization
    :type: IAgPolarization

    Gets the polarization.

.. py:property:: post_transmit_gains_losses
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelComplex.post_transmit_gains_losses
    :type: IAgAdditionalGainLossCollection

    Gets the collection of additional post transmit gains and losses.

.. py:property:: enable_filter
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelComplex.enable_filter
    :type: bool

    Gets or set the flag determines whether or not to enable the Filter.

.. py:property:: supported_filters
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelComplex.supported_filters
    :type: list

    Gets an array of supported filter model names.

.. py:property:: filter
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelComplex.filter
    :type: IAgRFFilterModel

    Gets the current filter model.

.. py:property:: supported_modulators
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelComplex.supported_modulators
    :type: list

    Gets an array of supported modulator model names.

.. py:property:: modulator
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelComplex.modulator
    :type: IAgModulatorModel

    Gets the current modulator model.


Method detail
-------------










.. py:method:: set_polarization_type(self, val: POLARIZATION_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelComplex.set_polarization_type

    Set the current polarization type.

    :Parameters:

    **val** : :obj:`~POLARIZATION_TYPE`

    :Returns:

        :obj:`~None`






.. py:method:: set_filter(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelComplex.set_filter

    Set the current filter model by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`



.. py:method:: set_modulator(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelComplex.set_modulator

    Set the current modulator model by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`


