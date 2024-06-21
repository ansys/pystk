IWaveformSelectionStrategyRangeLimits
=====================================

.. py:class:: ansys.stk.core.stkobjects.IWaveformSelectionStrategyRangeLimits

   object
   
   Provide the base interface for a waveform selection strategy which produces a waveform based on target range.

.. py:currentmodule:: IWaveformSelectionStrategyRangeLimits

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IWaveformSelectionStrategyRangeLimits.short_range_limit`
            * - :py:attr:`~ansys.stk.core.stkobjects.IWaveformSelectionStrategyRangeLimits.override_default_short_range_waveform`
            * - :py:attr:`~ansys.stk.core.stkobjects.IWaveformSelectionStrategyRangeLimits.supported_short_range_waveforms`
            * - :py:attr:`~ansys.stk.core.stkobjects.IWaveformSelectionStrategyRangeLimits.short_range_waveform`
            * - :py:attr:`~ansys.stk.core.stkobjects.IWaveformSelectionStrategyRangeLimits.medium_range_limit`
            * - :py:attr:`~ansys.stk.core.stkobjects.IWaveformSelectionStrategyRangeLimits.override_default_medium_range_waveform`
            * - :py:attr:`~ansys.stk.core.stkobjects.IWaveformSelectionStrategyRangeLimits.supported_medium_range_waveforms`
            * - :py:attr:`~ansys.stk.core.stkobjects.IWaveformSelectionStrategyRangeLimits.medium_range_waveform`
            * - :py:attr:`~ansys.stk.core.stkobjects.IWaveformSelectionStrategyRangeLimits.long_range_limit`
            * - :py:attr:`~ansys.stk.core.stkobjects.IWaveformSelectionStrategyRangeLimits.override_default_long_range_waveform`
            * - :py:attr:`~ansys.stk.core.stkobjects.IWaveformSelectionStrategyRangeLimits.supported_long_range_waveforms`
            * - :py:attr:`~ansys.stk.core.stkobjects.IWaveformSelectionStrategyRangeLimits.long_range_waveform`
            * - :py:attr:`~ansys.stk.core.stkobjects.IWaveformSelectionStrategyRangeLimits.override_default_ultra_long_range_waveform`
            * - :py:attr:`~ansys.stk.core.stkobjects.IWaveformSelectionStrategyRangeLimits.supported_ultra_long_range_waveforms`
            * - :py:attr:`~ansys.stk.core.stkobjects.IWaveformSelectionStrategyRangeLimits.ultra_long_range_waveform`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IWaveformSelectionStrategyRangeLimits


Property detail
---------------

.. py:property:: short_range_limit
    :canonical: ansys.stk.core.stkobjects.IWaveformSelectionStrategyRangeLimits.short_range_limit
    :type: float

    Gets the short range limit value.

.. py:property:: override_default_short_range_waveform
    :canonical: ansys.stk.core.stkobjects.IWaveformSelectionStrategyRangeLimits.override_default_short_range_waveform
    :type: bool

    Gets or sets a value indicating whether or not to override the default short range waveform.

.. py:property:: supported_short_range_waveforms
    :canonical: ansys.stk.core.stkobjects.IWaveformSelectionStrategyRangeLimits.supported_short_range_waveforms
    :type: list

    Gets an array of supported short range waveform names.

.. py:property:: short_range_waveform
    :canonical: ansys.stk.core.stkobjects.IWaveformSelectionStrategyRangeLimits.short_range_waveform
    :type: str

    Gets or sets the short range waveform.

.. py:property:: medium_range_limit
    :canonical: ansys.stk.core.stkobjects.IWaveformSelectionStrategyRangeLimits.medium_range_limit
    :type: float

    Gets the medium range limit value.

.. py:property:: override_default_medium_range_waveform
    :canonical: ansys.stk.core.stkobjects.IWaveformSelectionStrategyRangeLimits.override_default_medium_range_waveform
    :type: bool

    Gets or sets a value indicating whether or not to override the default medium range waveform.

.. py:property:: supported_medium_range_waveforms
    :canonical: ansys.stk.core.stkobjects.IWaveformSelectionStrategyRangeLimits.supported_medium_range_waveforms
    :type: list

    Gets an array of supported medium range waveform names.

.. py:property:: medium_range_waveform
    :canonical: ansys.stk.core.stkobjects.IWaveformSelectionStrategyRangeLimits.medium_range_waveform
    :type: str

    Gets or sets the medium range waveform.

.. py:property:: long_range_limit
    :canonical: ansys.stk.core.stkobjects.IWaveformSelectionStrategyRangeLimits.long_range_limit
    :type: float

    Gets the long range limit value.

.. py:property:: override_default_long_range_waveform
    :canonical: ansys.stk.core.stkobjects.IWaveformSelectionStrategyRangeLimits.override_default_long_range_waveform
    :type: bool

    Gets or sets a value indicating whether or not to override the default long range waveform.

.. py:property:: supported_long_range_waveforms
    :canonical: ansys.stk.core.stkobjects.IWaveformSelectionStrategyRangeLimits.supported_long_range_waveforms
    :type: list

    Gets an array of supported long range waveform names.

.. py:property:: long_range_waveform
    :canonical: ansys.stk.core.stkobjects.IWaveformSelectionStrategyRangeLimits.long_range_waveform
    :type: str

    Gets or sets the long range waveform.

.. py:property:: override_default_ultra_long_range_waveform
    :canonical: ansys.stk.core.stkobjects.IWaveformSelectionStrategyRangeLimits.override_default_ultra_long_range_waveform
    :type: bool

    Gets or sets a value indicating whether or not to override the default ultra long range waveform.

.. py:property:: supported_ultra_long_range_waveforms
    :canonical: ansys.stk.core.stkobjects.IWaveformSelectionStrategyRangeLimits.supported_ultra_long_range_waveforms
    :type: list

    Gets an array of supported ultra long range waveform names.

.. py:property:: ultra_long_range_waveform
    :canonical: ansys.stk.core.stkobjects.IWaveformSelectionStrategyRangeLimits.ultra_long_range_waveform
    :type: str

    Gets or sets the ultra long range waveform.


