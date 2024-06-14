IRadarMultifunctionDetectionProcessing
======================================

.. py:class:: IRadarMultifunctionDetectionProcessing

   object
   
   Interface which represents multifunction radar detection processing.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_probability_of_detection`
              - Set the probability of detection algorithm by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~supported_probability_of_detection`
            * - :py:meth:`~probability_of_detection`
            * - :py:meth:`~pulse_integration_type`
            * - :py:meth:`~pulse_integration`
            * - :py:meth:`~enable_resolution_override`
            * - :py:meth:`~range_cell_resolution`
            * - :py:meth:`~azimuth_resolution`
            * - :py:meth:`~enable_pulse_canceller`
            * - :py:meth:`~number_of_pulses_to_cancel`
            * - :py:meth:`~enable_coherent_pulses`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarMultifunctionDetectionProcessing


Property detail
---------------

.. py:property:: supported_probability_of_detection
    :canonical: ansys.stk.core.stkobjects.IRadarMultifunctionDetectionProcessing.supported_probability_of_detection
    :type: list

    Gets an array of supported model names.

.. py:property:: probability_of_detection
    :canonical: ansys.stk.core.stkobjects.IRadarMultifunctionDetectionProcessing.probability_of_detection
    :type: "IAgRadarProbabilityOfDetection"

    Gets the interface for setting the probability of detection parameters.

.. py:property:: pulse_integration_type
    :canonical: ansys.stk.core.stkobjects.IRadarMultifunctionDetectionProcessing.pulse_integration_type
    :type: "RADAR_PULSE_INTEGRATION_TYPE"

    Gets or sets the pulse integration type.

.. py:property:: pulse_integration
    :canonical: ansys.stk.core.stkobjects.IRadarMultifunctionDetectionProcessing.pulse_integration
    :type: "IAgRadarPulseIntegration"

    Gets the interface for setting pulse integration parameters.

.. py:property:: enable_resolution_override
    :canonical: ansys.stk.core.stkobjects.IRadarMultifunctionDetectionProcessing.enable_resolution_override
    :type: bool

    Gets or sets the flag for overriding the computed range and azimuth resolution values.

.. py:property:: range_cell_resolution
    :canonical: ansys.stk.core.stkobjects.IRadarMultifunctionDetectionProcessing.range_cell_resolution
    :type: float

    Gets or sets the overriding range cell resolution value.

.. py:property:: azimuth_resolution
    :canonical: ansys.stk.core.stkobjects.IRadarMultifunctionDetectionProcessing.azimuth_resolution
    :type: float

    Gets or sets the overriding azimuth resolution value.

.. py:property:: enable_pulse_canceller
    :canonical: ansys.stk.core.stkobjects.IRadarMultifunctionDetectionProcessing.enable_pulse_canceller
    :type: bool

    Gets or sets the flag for enabling pulse cancellation.

.. py:property:: number_of_pulses_to_cancel
    :canonical: ansys.stk.core.stkobjects.IRadarMultifunctionDetectionProcessing.number_of_pulses_to_cancel
    :type: int

    Gets or sets the number of pulses to cancel.

.. py:property:: enable_coherent_pulses
    :canonical: ansys.stk.core.stkobjects.IRadarMultifunctionDetectionProcessing.enable_coherent_pulses
    :type: bool

    Gets or sets the flag for modeling coherent pulses.


Method detail
-------------


.. py:method:: set_probability_of_detection(self, name:str) -> None

    Set the probability of detection algorithm by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`

















