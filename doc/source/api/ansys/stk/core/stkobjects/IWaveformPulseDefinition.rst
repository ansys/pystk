IWaveformPulseDefinition
========================

.. py:class:: ansys.stk.core.stkobjects.IWaveformPulseDefinition

   object
   
   Provide access to the properties and methods defining the pulse definition for a rectangular pulsed waveform.

.. py:currentmodule:: IWaveformPulseDefinition

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IWaveformPulseDefinition.prf_mode`
            * - :py:attr:`~ansys.stk.core.stkobjects.IWaveformPulseDefinition.prf`
            * - :py:attr:`~ansys.stk.core.stkobjects.IWaveformPulseDefinition.unambiguous_range`
            * - :py:attr:`~ansys.stk.core.stkobjects.IWaveformPulseDefinition.unambiguous_velocity`
            * - :py:attr:`~ansys.stk.core.stkobjects.IWaveformPulseDefinition.pulse_width_mode`
            * - :py:attr:`~ansys.stk.core.stkobjects.IWaveformPulseDefinition.pulse_width`
            * - :py:attr:`~ansys.stk.core.stkobjects.IWaveformPulseDefinition.duty_factor`
            * - :py:attr:`~ansys.stk.core.stkobjects.IWaveformPulseDefinition.number_of_pulses`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IWaveformPulseDefinition


Property detail
---------------

.. py:property:: prf_mode
    :canonical: ansys.stk.core.stkobjects.IWaveformPulseDefinition.prf_mode
    :type: PRF_MODE

    Gets or sets the prf mode enumeration.

.. py:property:: prf
    :canonical: ansys.stk.core.stkobjects.IWaveformPulseDefinition.prf
    :type: float

    Gets or sets the pulse repetition frequency.

.. py:property:: unambiguous_range
    :canonical: ansys.stk.core.stkobjects.IWaveformPulseDefinition.unambiguous_range
    :type: float

    Gets or sets the unambiguous range.

.. py:property:: unambiguous_velocity
    :canonical: ansys.stk.core.stkobjects.IWaveformPulseDefinition.unambiguous_velocity
    :type: float

    Gets or sets the unambiguous velocity.

.. py:property:: pulse_width_mode
    :canonical: ansys.stk.core.stkobjects.IWaveformPulseDefinition.pulse_width_mode
    :type: PULSE_WIDTH_MODE

    Gets or sets the pulse width mode enumeration.

.. py:property:: pulse_width
    :canonical: ansys.stk.core.stkobjects.IWaveformPulseDefinition.pulse_width
    :type: float

    Gets or sets the pulse width.

.. py:property:: duty_factor
    :canonical: ansys.stk.core.stkobjects.IWaveformPulseDefinition.duty_factor
    :type: float

    Gets or sets the duty factor.

.. py:property:: number_of_pulses
    :canonical: ansys.stk.core.stkobjects.IWaveformPulseDefinition.number_of_pulses
    :type: int

    Gets or sets the number of pulses.


