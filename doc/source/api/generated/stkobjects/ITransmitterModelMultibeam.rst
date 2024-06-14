ITransmitterModelMultibeam
==========================

.. py:class:: ITransmitterModelMultibeam

   object
   
   Provide access to the properties and methods defining a multibeam transmitter model.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_filter`
              - Set the current filter model by name.
            * - :py:meth:`~set_modulator`
              - Set the current modulator model by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~data_rate`
            * - :py:meth:`~post_transmit_gains_losses`
            * - :py:meth:`~enable_filter`
            * - :py:meth:`~supported_filters`
            * - :py:meth:`~filter`
            * - :py:meth:`~supported_modulators`
            * - :py:meth:`~modulator`
            * - :py:meth:`~antenna_system`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ITransmitterModelMultibeam


Property detail
---------------

.. py:property:: data_rate
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelMultibeam.data_rate
    :type: float

    Gets or sets the data rate.

.. py:property:: post_transmit_gains_losses
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelMultibeam.post_transmit_gains_losses
    :type: "IAgAdditionalGainLossCollection"

    Gets the collection of additional post transmit gains and losses.

.. py:property:: enable_filter
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelMultibeam.enable_filter
    :type: bool

    Gets or set the flag determines whether or not to enable the Filter.

.. py:property:: supported_filters
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelMultibeam.supported_filters
    :type: list

    Gets an array of supported filter model names.

.. py:property:: filter
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelMultibeam.filter
    :type: "IAgRFFilterModel"

    Gets the current filter model.

.. py:property:: supported_modulators
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelMultibeam.supported_modulators
    :type: list

    Gets an array of supported modulator model names.

.. py:property:: modulator
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelMultibeam.modulator
    :type: "IAgModulatorModel"

    Gets the current modulator model.

.. py:property:: antenna_system
    :canonical: ansys.stk.core.stkobjects.ITransmitterModelMultibeam.antenna_system
    :type: "IAgAntennaSystem"

    Gets the antenna system.


Method detail
-------------







.. py:method:: set_filter(self, name:str) -> None

    Set the current filter model by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`



.. py:method:: set_modulator(self, name:str) -> None

    Set the current modulator model by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`



