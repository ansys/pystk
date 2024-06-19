IReTransmitterModelSimple
=========================

.. py:class:: IReTransmitterModelSimple

   object
   
   Provide access to the properties and methods defining a simple re-transmitter model.

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

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~enable_polarization`
            * - :py:meth:`~polarization`
            * - :py:meth:`~post_transmit_gains_losses`
            * - :py:meth:`~enable_filter`
            * - :py:meth:`~supported_filters`
            * - :py:meth:`~filter`
            * - :py:meth:`~saturated_eirp`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IReTransmitterModelSimple


Property detail
---------------

.. py:property:: enable_polarization
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModelSimple.enable_polarization
    :type: bool

    Gets or sets the enable polarization option.

.. py:property:: polarization
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModelSimple.polarization
    :type: IAgPolarization

    Gets the polarization.

.. py:property:: post_transmit_gains_losses
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModelSimple.post_transmit_gains_losses
    :type: IAgAdditionalGainLossCollection

    Gets the collection of additional post transmit gains and losses.

.. py:property:: enable_filter
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModelSimple.enable_filter
    :type: bool

    Gets or set the flag determines whether or not to enable the Filter.

.. py:property:: supported_filters
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModelSimple.supported_filters
    :type: list

    Gets an array of supported filter model names.

.. py:property:: filter
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModelSimple.filter
    :type: IAgRFFilterModel

    Gets the current filter model.

.. py:property:: saturated_eirp
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModelSimple.saturated_eirp
    :type: float

    Gets or sets the saturated eirp.


Method detail
-------------



.. py:method:: set_polarization_type(self, val: POLARIZATION_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModelSimple.set_polarization_type

    Set the current polarization type.

    :Parameters:

    **val** : :obj:`~POLARIZATION_TYPE`

    :Returns:

        :obj:`~None`






.. py:method:: set_filter(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModelSimple.set_filter

    Set the current filter model by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`




