IWaveformSelectionStrategyFixed
===============================

.. py:class:: ansys.stk.core.stkobjects.IWaveformSelectionStrategyFixed

   object
   
   Provide the base interface for a waveform selection strategy which produces a Fixed waveform.

.. py:currentmodule:: IWaveformSelectionStrategyFixed

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IWaveformSelectionStrategyFixed.supported_waveforms`
              - Gets an array of supported waveform names.
            * - :py:attr:`~ansys.stk.core.stkobjects.IWaveformSelectionStrategyFixed.fixed_waveform`
              - Gets or sets the fixed waveform.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IWaveformSelectionStrategyFixed


Property detail
---------------

.. py:property:: supported_waveforms
    :canonical: ansys.stk.core.stkobjects.IWaveformSelectionStrategyFixed.supported_waveforms
    :type: list

    Gets an array of supported waveform names.

.. py:property:: fixed_waveform
    :canonical: ansys.stk.core.stkobjects.IWaveformSelectionStrategyFixed.fixed_waveform
    :type: str

    Gets or sets the fixed waveform.


