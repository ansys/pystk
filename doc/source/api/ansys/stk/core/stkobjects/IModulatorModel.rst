IModulatorModel
===============

.. py:class:: ansys.stk.core.stkobjects.IModulatorModel

   Provide access to the properties and methods defining a modulator model.

.. py:currentmodule:: IModulatorModel

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IModulatorModel.name`
              - Gets the modulator model name.
            * - :py:attr:`~ansys.stk.core.stkobjects.IModulatorModel.type`
              - Gets the modulator model type enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.IModulatorModel.enable_signal_psd`
              - Gets or sets the option for modeling signal PSD.
            * - :py:attr:`~ansys.stk.core.stkobjects.IModulatorModel.psd_limit_multiplier`
              - Gets or sets the PSD limit multiplier.
            * - :py:attr:`~ansys.stk.core.stkobjects.IModulatorModel.enable_cdma_spread`
              - Gets or sets the option for modeling CDMA spread.
            * - :py:attr:`~ansys.stk.core.stkobjects.IModulatorModel.chips_per_bit`
              - Gets or sets the chips per bit.
            * - :py:attr:`~ansys.stk.core.stkobjects.IModulatorModel.spreading_gain`
              - Gets the spreading gain.
            * - :py:attr:`~ansys.stk.core.stkobjects.IModulatorModel.scale_bandwidth_automatically`
              - Gets or sets the option for auto scaling the bandwidth.
            * - :py:attr:`~ansys.stk.core.stkobjects.IModulatorModel.symmetric_bandwidth`
              - Gets or sets the option for specifying symmetric bandwidth.
            * - :py:attr:`~ansys.stk.core.stkobjects.IModulatorModel.upper_bandwidth_limit`
              - Gets or sets the upper bandwidth limit.
            * - :py:attr:`~ansys.stk.core.stkobjects.IModulatorModel.lower_bandwidth_limit`
              - Gets or sets the lower bandwidth limit.
            * - :py:attr:`~ansys.stk.core.stkobjects.IModulatorModel.bandwidth`
              - Gets or sets the filter bandwidth.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IModulatorModel


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.IModulatorModel.name
    :type: str

    Gets the modulator model name.

.. py:property:: type
    :canonical: ansys.stk.core.stkobjects.IModulatorModel.type
    :type: MODULATOR_MODEL_TYPE

    Gets the modulator model type enumeration.

.. py:property:: enable_signal_psd
    :canonical: ansys.stk.core.stkobjects.IModulatorModel.enable_signal_psd
    :type: bool

    Gets or sets the option for modeling signal PSD.

.. py:property:: psd_limit_multiplier
    :canonical: ansys.stk.core.stkobjects.IModulatorModel.psd_limit_multiplier
    :type: int

    Gets or sets the PSD limit multiplier.

.. py:property:: enable_cdma_spread
    :canonical: ansys.stk.core.stkobjects.IModulatorModel.enable_cdma_spread
    :type: bool

    Gets or sets the option for modeling CDMA spread.

.. py:property:: chips_per_bit
    :canonical: ansys.stk.core.stkobjects.IModulatorModel.chips_per_bit
    :type: int

    Gets or sets the chips per bit.

.. py:property:: spreading_gain
    :canonical: ansys.stk.core.stkobjects.IModulatorModel.spreading_gain
    :type: float

    Gets the spreading gain.

.. py:property:: scale_bandwidth_automatically
    :canonical: ansys.stk.core.stkobjects.IModulatorModel.scale_bandwidth_automatically
    :type: bool

    Gets or sets the option for auto scaling the bandwidth.

.. py:property:: symmetric_bandwidth
    :canonical: ansys.stk.core.stkobjects.IModulatorModel.symmetric_bandwidth
    :type: bool

    Gets or sets the option for specifying symmetric bandwidth.

.. py:property:: upper_bandwidth_limit
    :canonical: ansys.stk.core.stkobjects.IModulatorModel.upper_bandwidth_limit
    :type: float

    Gets or sets the upper bandwidth limit.

.. py:property:: lower_bandwidth_limit
    :canonical: ansys.stk.core.stkobjects.IModulatorModel.lower_bandwidth_limit
    :type: float

    Gets or sets the lower bandwidth limit.

.. py:property:: bandwidth
    :canonical: ansys.stk.core.stkobjects.IModulatorModel.bandwidth
    :type: float

    Gets or sets the filter bandwidth.


