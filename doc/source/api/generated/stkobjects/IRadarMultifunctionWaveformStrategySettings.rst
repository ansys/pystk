IRadarMultifunctionWaveformStrategySettings
===========================================

.. py:class:: IRadarMultifunctionWaveformStrategySettings

   object
   
   Interface which defines a multifunction radar waveform strategy settings.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~short_range_limit`
            * - :py:meth:`~medium_range_limit`
            * - :py:meth:`~long_range_limit`
            * - :py:meth:`~supported_short_range_waveforms`
            * - :py:meth:`~supported_medium_range_waveforms`
            * - :py:meth:`~supported_long_range_waveforms`
            * - :py:meth:`~supported_ultra_long_range_waveforms`
            * - :py:meth:`~short_range_default_waveform`
            * - :py:meth:`~medium_range_default_waveform`
            * - :py:meth:`~long_range_default_waveform`
            * - :py:meth:`~ultra_long_range_default_waveform`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarMultifunctionWaveformStrategySettings


Property detail
---------------

.. py:property:: short_range_limit
    :canonical: ansys.stk.core.stkobjects.IRadarMultifunctionWaveformStrategySettings.short_range_limit
    :type: float

    Gets or sets the short range limit value.

.. py:property:: medium_range_limit
    :canonical: ansys.stk.core.stkobjects.IRadarMultifunctionWaveformStrategySettings.medium_range_limit
    :type: float

    Gets or sets the medium range limit value.

.. py:property:: long_range_limit
    :canonical: ansys.stk.core.stkobjects.IRadarMultifunctionWaveformStrategySettings.long_range_limit
    :type: float

    Gets or sets the long range limit value.

.. py:property:: supported_short_range_waveforms
    :canonical: ansys.stk.core.stkobjects.IRadarMultifunctionWaveformStrategySettings.supported_short_range_waveforms
    :type: list

    Gets an array of supported short range waveform names.

.. py:property:: supported_medium_range_waveforms
    :canonical: ansys.stk.core.stkobjects.IRadarMultifunctionWaveformStrategySettings.supported_medium_range_waveforms
    :type: list

    Gets an array of supported medium range waveform names.

.. py:property:: supported_long_range_waveforms
    :canonical: ansys.stk.core.stkobjects.IRadarMultifunctionWaveformStrategySettings.supported_long_range_waveforms
    :type: list

    Gets an array of supported long range waveform names.

.. py:property:: supported_ultra_long_range_waveforms
    :canonical: ansys.stk.core.stkobjects.IRadarMultifunctionWaveformStrategySettings.supported_ultra_long_range_waveforms
    :type: list

    Gets an array of supported ultra long range waveform names.

.. py:property:: short_range_default_waveform
    :canonical: ansys.stk.core.stkobjects.IRadarMultifunctionWaveformStrategySettings.short_range_default_waveform
    :type: str

    Gets or sets the short range default waveform.

.. py:property:: medium_range_default_waveform
    :canonical: ansys.stk.core.stkobjects.IRadarMultifunctionWaveformStrategySettings.medium_range_default_waveform
    :type: str

    Gets or sets the medium range default waveform.

.. py:property:: long_range_default_waveform
    :canonical: ansys.stk.core.stkobjects.IRadarMultifunctionWaveformStrategySettings.long_range_default_waveform
    :type: str

    Gets or sets the long range default waveform.

.. py:property:: ultra_long_range_default_waveform
    :canonical: ansys.stk.core.stkobjects.IRadarMultifunctionWaveformStrategySettings.ultra_long_range_default_waveform
    :type: str

    Gets or sets the ultra long range default waveform.


