RadarAntennaBeam
================

.. py:class:: ansys.stk.core.stkobjects.RadarAntennaBeam

   Class defining a radar antenna beam.

.. py:currentmodule:: RadarAntennaBeam

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarAntennaBeam.set_activity_type`
              - Set the activity type.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarAntennaBeam.set_pointing_strategy_type`
              - Set the current pointing strategy type.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarAntennaBeam.set_waveform_selection_strategy`
              - Set the current waveform selection strategy.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarAntennaBeam.activity`
              - Get the activity.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarAntennaBeam.beam_width`
              - Get or set the antenna beamwidth.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarAntennaBeam.gain`
              - Get or set the antenna mainlobe gain.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarAntennaBeam.identifier`
              - Get or set the antenna beam identifier.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarAntennaBeam.pointing_strategy`
              - Get the pointing strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarAntennaBeam.waveform_selection_strategy`
              - Get the waveform selection strategy.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RadarAntennaBeam


Property detail
---------------

.. py:property:: activity
    :canonical: ansys.stk.core.stkobjects.RadarAntennaBeam.activity
    :type: IRadarActivity

    Get the activity.

.. py:property:: beam_width
    :canonical: ansys.stk.core.stkobjects.RadarAntennaBeam.beam_width
    :type: float

    Get or set the antenna beamwidth.

.. py:property:: gain
    :canonical: ansys.stk.core.stkobjects.RadarAntennaBeam.gain
    :type: float

    Get or set the antenna mainlobe gain.

.. py:property:: identifier
    :canonical: ansys.stk.core.stkobjects.RadarAntennaBeam.identifier
    :type: str

    Get or set the antenna beam identifier.

.. py:property:: pointing_strategy
    :canonical: ansys.stk.core.stkobjects.RadarAntennaBeam.pointing_strategy
    :type: IPointingStrategy

    Get the pointing strategy.

.. py:property:: waveform_selection_strategy
    :canonical: ansys.stk.core.stkobjects.RadarAntennaBeam.waveform_selection_strategy
    :type: IWaveformSelectionStrategy

    Get the waveform selection strategy.


Method detail
-------------









.. py:method:: set_activity_type(self, activity_type: RadarActivityType) -> None
    :canonical: ansys.stk.core.stkobjects.RadarAntennaBeam.set_activity_type

    Set the activity type.

    :Parameters:

        **activity_type** : :obj:`~RadarActivityType`


    :Returns:

        :obj:`~None`

.. py:method:: set_pointing_strategy_type(self, value: PointingStrategyType) -> None
    :canonical: ansys.stk.core.stkobjects.RadarAntennaBeam.set_pointing_strategy_type

    Set the current pointing strategy type.

    :Parameters:

        **value** : :obj:`~PointingStrategyType`


    :Returns:

        :obj:`~None`

.. py:method:: set_waveform_selection_strategy(self, value: WaveformSelectionStrategyType) -> None
    :canonical: ansys.stk.core.stkobjects.RadarAntennaBeam.set_waveform_selection_strategy

    Set the current waveform selection strategy.

    :Parameters:

        **value** : :obj:`~WaveformSelectionStrategyType`


    :Returns:

        :obj:`~None`


