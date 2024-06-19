IModulatorModel
===============

.. py:class:: IModulatorModel

   object
   
   Provide access to the properties and methods defining a modulator model.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~name`
            * - :py:meth:`~type`
            * - :py:meth:`~enable_signal_psd`
            * - :py:meth:`~psd_limit_multiplier`
            * - :py:meth:`~enable_cdma_spread`
            * - :py:meth:`~chips_per_bit`
            * - :py:meth:`~spreading_gain`
            * - :py:meth:`~auto_scale_bandwidth`
            * - :py:meth:`~symmetric_bandwidth`
            * - :py:meth:`~upper_bandwidth_limit`
            * - :py:meth:`~lower_bandwidth_limit`
            * - :py:meth:`~bandwidth`


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

.. py:property:: auto_scale_bandwidth
    :canonical: ansys.stk.core.stkobjects.IModulatorModel.auto_scale_bandwidth
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


