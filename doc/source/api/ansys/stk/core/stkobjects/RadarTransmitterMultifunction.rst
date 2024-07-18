RadarTransmitterMultifunction
=============================

.. py:class:: ansys.stk.core.stkobjects.RadarTransmitterMultifunction

   Bases: 

   Class defining the multifunction radar transmitter.

.. py:currentmodule:: RadarTransmitterMultifunction

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarTransmitterMultifunction.set_polarization_type`
              - Set the current polarization type.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarTransmitterMultifunction.set_filter`
              - Set the current filter model by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarTransmitterMultifunction.post_transmit_gains_losses`
              - Gets the collection of additional post transmit gains and losses.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarTransmitterMultifunction.enable_polarization`
              - Gets or sets the enable polarization option.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarTransmitterMultifunction.enable_ortho_polarization`
              - Gets or sets the option for enabling the orthogonal polarization.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarTransmitterMultifunction.polarization`
              - Gets the polarization.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarTransmitterMultifunction.power_amp_bandwidth`
              - Gets or sets the power amplifier bandwidth.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarTransmitterMultifunction.enable_filter`
              - Gets or set the flag determines whether or not to enable the Filter.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarTransmitterMultifunction.supported_filters`
              - Gets an array of supported filter model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarTransmitterMultifunction.filter`
              - Gets the current filter model.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarTransmitterMultifunction.max_power_limit`
              - Gets or sets the power.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RadarTransmitterMultifunction


Property detail
---------------

.. py:property:: post_transmit_gains_losses
    :canonical: ansys.stk.core.stkobjects.RadarTransmitterMultifunction.post_transmit_gains_losses
    :type: IAdditionalGainLossCollection

    Gets the collection of additional post transmit gains and losses.

.. py:property:: enable_polarization
    :canonical: ansys.stk.core.stkobjects.RadarTransmitterMultifunction.enable_polarization
    :type: bool

    Gets or sets the enable polarization option.

.. py:property:: enable_ortho_polarization
    :canonical: ansys.stk.core.stkobjects.RadarTransmitterMultifunction.enable_ortho_polarization
    :type: bool

    Gets or sets the option for enabling the orthogonal polarization.

.. py:property:: polarization
    :canonical: ansys.stk.core.stkobjects.RadarTransmitterMultifunction.polarization
    :type: IPolarization

    Gets the polarization.

.. py:property:: power_amp_bandwidth
    :canonical: ansys.stk.core.stkobjects.RadarTransmitterMultifunction.power_amp_bandwidth
    :type: float

    Gets or sets the power amplifier bandwidth.

.. py:property:: enable_filter
    :canonical: ansys.stk.core.stkobjects.RadarTransmitterMultifunction.enable_filter
    :type: bool

    Gets or set the flag determines whether or not to enable the Filter.

.. py:property:: supported_filters
    :canonical: ansys.stk.core.stkobjects.RadarTransmitterMultifunction.supported_filters
    :type: list

    Gets an array of supported filter model names.

.. py:property:: filter
    :canonical: ansys.stk.core.stkobjects.RadarTransmitterMultifunction.filter
    :type: IRFFilterModel

    Gets the current filter model.

.. py:property:: max_power_limit
    :canonical: ansys.stk.core.stkobjects.RadarTransmitterMultifunction.max_power_limit
    :type: float

    Gets or sets the power.


Method detail
-------------






.. py:method:: set_polarization_type(self, val: POLARIZATION_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.RadarTransmitterMultifunction.set_polarization_type

    Set the current polarization type.

    :Parameters:

    **val** : :obj:`~POLARIZATION_TYPE`

    :Returns:

        :obj:`~None`







.. py:method:: set_filter(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.RadarTransmitterMultifunction.set_filter

    Set the current filter model by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`




