ReTransmitterModelSimple
========================

.. py:class:: ansys.stk.core.stkobjects.ReTransmitterModelSimple

   Bases: :py:class:`~ansys.stk.core.stkobjects.IReTransmitterModel`, :py:class:`~ansys.stk.core.stkobjects.ITransmitterModel`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining a simple re-transmitter model.

.. py:currentmodule:: ReTransmitterModelSimple

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ReTransmitterModelSimple.set_polarization_type`
              - Set the current polarization type.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReTransmitterModelSimple.set_filter`
              - Set the current filter model by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ReTransmitterModelSimple.enable_polarization`
              - Gets or sets the enable polarization option.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReTransmitterModelSimple.polarization`
              - Gets the polarization.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReTransmitterModelSimple.post_transmit_gains_losses`
              - Gets the collection of additional post transmit gains and losses.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReTransmitterModelSimple.enable_filter`
              - Gets or set the flag determines whether or not to enable the Filter.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReTransmitterModelSimple.supported_filters`
              - Gets an array of supported filter model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReTransmitterModelSimple.filter`
              - Gets the current filter model.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReTransmitterModelSimple.saturated_eirp`
              - Gets or sets the saturated eirp.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ReTransmitterModelSimple


Property detail
---------------

.. py:property:: enable_polarization
    :canonical: ansys.stk.core.stkobjects.ReTransmitterModelSimple.enable_polarization
    :type: bool

    Gets or sets the enable polarization option.

.. py:property:: polarization
    :canonical: ansys.stk.core.stkobjects.ReTransmitterModelSimple.polarization
    :type: IPolarization

    Gets the polarization.

.. py:property:: post_transmit_gains_losses
    :canonical: ansys.stk.core.stkobjects.ReTransmitterModelSimple.post_transmit_gains_losses
    :type: AdditionalGainLossCollection

    Gets the collection of additional post transmit gains and losses.

.. py:property:: enable_filter
    :canonical: ansys.stk.core.stkobjects.ReTransmitterModelSimple.enable_filter
    :type: bool

    Gets or set the flag determines whether or not to enable the Filter.

.. py:property:: supported_filters
    :canonical: ansys.stk.core.stkobjects.ReTransmitterModelSimple.supported_filters
    :type: list

    Gets an array of supported filter model names.

.. py:property:: filter
    :canonical: ansys.stk.core.stkobjects.ReTransmitterModelSimple.filter
    :type: IRFFilterModel

    Gets the current filter model.

.. py:property:: saturated_eirp
    :canonical: ansys.stk.core.stkobjects.ReTransmitterModelSimple.saturated_eirp
    :type: float

    Gets or sets the saturated eirp.


Method detail
-------------



.. py:method:: set_polarization_type(self, val: POLARIZATION_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.ReTransmitterModelSimple.set_polarization_type

    Set the current polarization type.

    :Parameters:

    **val** : :obj:`~POLARIZATION_TYPE`

    :Returns:

        :obj:`~None`






.. py:method:: set_filter(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.ReTransmitterModelSimple.set_filter

    Set the current filter model by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`




