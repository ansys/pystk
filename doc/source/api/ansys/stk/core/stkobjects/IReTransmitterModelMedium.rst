IReTransmitterModelMedium
=========================

.. py:class:: ansys.stk.core.stkobjects.IReTransmitterModelMedium

   object
   
   Provide access to the properties and methods defining a medium re-transmitter model.

.. py:currentmodule:: IReTransmitterModelMedium

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IReTransmitterModelMedium.set_polarization_type`
              - Set the current polarization type.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReTransmitterModelMedium.set_filter`
              - Set the current filter model by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IReTransmitterModelMedium.enable_polarization`
              - Gets or sets the enable polarization option.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReTransmitterModelMedium.polarization`
              - Gets the polarization.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReTransmitterModelMedium.post_transmit_gains_losses`
              - Gets the collection of additional post transmit gains and losses.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReTransmitterModelMedium.enable_filter`
              - Gets or set the flag determines whether or not to enable the Filter.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReTransmitterModelMedium.supported_filters`
              - Gets an array of supported filter model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReTransmitterModelMedium.filter`
              - Gets the current filter model.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReTransmitterModelMedium.saturated_power`
              - Gets or sets the saturated power.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReTransmitterModelMedium.antenna_gain`
              - Gets or sets the antenna gain.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IReTransmitterModelMedium


Property detail
---------------

.. py:property:: enable_polarization
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModelMedium.enable_polarization
    :type: bool

    Gets or sets the enable polarization option.

.. py:property:: polarization
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModelMedium.polarization
    :type: IPolarization

    Gets the polarization.

.. py:property:: post_transmit_gains_losses
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModelMedium.post_transmit_gains_losses
    :type: IAdditionalGainLossCollection

    Gets the collection of additional post transmit gains and losses.

.. py:property:: enable_filter
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModelMedium.enable_filter
    :type: bool

    Gets or set the flag determines whether or not to enable the Filter.

.. py:property:: supported_filters
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModelMedium.supported_filters
    :type: list

    Gets an array of supported filter model names.

.. py:property:: filter
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModelMedium.filter
    :type: IRFFilterModel

    Gets the current filter model.

.. py:property:: saturated_power
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModelMedium.saturated_power
    :type: float

    Gets or sets the saturated power.

.. py:property:: antenna_gain
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModelMedium.antenna_gain
    :type: float

    Gets or sets the antenna gain.


Method detail
-------------



.. py:method:: set_polarization_type(self, val: POLARIZATION_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModelMedium.set_polarization_type

    Set the current polarization type.

    :Parameters:

    **val** : :obj:`~POLARIZATION_TYPE`

    :Returns:

        :obj:`~None`






.. py:method:: set_filter(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModelMedium.set_filter

    Set the current filter model by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`






