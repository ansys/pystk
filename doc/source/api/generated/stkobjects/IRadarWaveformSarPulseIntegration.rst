IRadarWaveformSarPulseIntegration
=================================

.. py:class:: IRadarWaveformSarPulseIntegration

   object
   
   Provide access to the properties and methods defining the pulse integration for a SAR waveform.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~azimuth_broadening_factor`
            * - :py:meth:`~range_broadening_factor`
            * - :py:meth:`~if_bandwidth`
            * - :py:meth:`~analysis_mode`
            * - :py:meth:`~analysis_mode_value`
            * - :py:meth:`~multiplicative_noise_ratio`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarWaveformSarPulseIntegration


Property detail
---------------

.. py:property:: azimuth_broadening_factor
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformSarPulseIntegration.azimuth_broadening_factor
    :type: float

    Gets or sets the azimuth broadening factor.

.. py:property:: range_broadening_factor
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformSarPulseIntegration.range_broadening_factor
    :type: float

    Gets or sets the range broadening factor.

.. py:property:: if_bandwidth
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformSarPulseIntegration.if_bandwidth
    :type: float

    Gets or sets the IF bandwidth.

.. py:property:: analysis_mode
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformSarPulseIntegration.analysis_mode
    :type: "RADAR_SAR_PULSE_INTEGRATION_ANALYSIS_MODE_TYPE"

    Gets or sets the analysis mode enumeration.

.. py:property:: analysis_mode_value
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformSarPulseIntegration.analysis_mode_value
    :type: float

    Gets or sets the analysis mode value.

.. py:property:: multiplicative_noise_ratio
    :canonical: ansys.stk.core.stkobjects.IRadarWaveformSarPulseIntegration.multiplicative_noise_ratio
    :type: float

    Gets or sets the multiplicative noise ratio.


