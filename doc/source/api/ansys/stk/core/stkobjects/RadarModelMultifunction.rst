RadarModelMultifunction
=======================

.. py:class:: ansys.stk.core.stkobjects.RadarModelMultifunction

   Bases: :py:class:`~ansys.stk.core.stkobjects.IRadarModel`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining a multifunction radar model.

.. py:currentmodule:: RadarModelMultifunction

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelMultifunction.set_pointing_strategy_type`
              - Set the current pointing strategy type.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelMultifunction.transmitter`
              - Gets the radar transmitter.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelMultifunction.receiver`
              - Gets the radar receiver.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelMultifunction.clutter_geometry`
              - This property is deprecated.Use the Clutter property instead.Gets the radar clutter geometry.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelMultifunction.jamming`
              - Gets the radar jamming.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelMultifunction.location`
              - Gets the radar location object.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelMultifunction.detection_processing`
              - Gets the radar detection processing object.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelMultifunction.pointing_strategy`
              - Gets the pointing strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelMultifunction.antenna_beams`
              - Gets the antenna beams collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelMultifunction.waveform_strategy_settings`
              - Gets the waveform selection strategy settings.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModelMultifunction.clutter`
              - Gets the radar clutter settings.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RadarModelMultifunction


Property detail
---------------

.. py:property:: transmitter
    :canonical: ansys.stk.core.stkobjects.RadarModelMultifunction.transmitter
    :type: RadarTransmitterMultifunction

    Gets the radar transmitter.

.. py:property:: receiver
    :canonical: ansys.stk.core.stkobjects.RadarModelMultifunction.receiver
    :type: RadarReceiver

    Gets the radar receiver.

.. py:property:: clutter_geometry
    :canonical: ansys.stk.core.stkobjects.RadarModelMultifunction.clutter_geometry
    :type: RadarClutterGeometry

    This property is deprecated.Use the Clutter property instead.Gets the radar clutter geometry.

.. py:property:: jamming
    :canonical: ansys.stk.core.stkobjects.RadarModelMultifunction.jamming
    :type: RadarJamming

    Gets the radar jamming.

.. py:property:: location
    :canonical: ansys.stk.core.stkobjects.RadarModelMultifunction.location
    :type: CommRadCartesianLocation

    Gets the radar location object.

.. py:property:: detection_processing
    :canonical: ansys.stk.core.stkobjects.RadarModelMultifunction.detection_processing
    :type: RadarMultifunctionDetectionProcessing

    Gets the radar detection processing object.

.. py:property:: pointing_strategy
    :canonical: ansys.stk.core.stkobjects.RadarModelMultifunction.pointing_strategy
    :type: IPointingStrategy

    Gets the pointing strategy.

.. py:property:: antenna_beams
    :canonical: ansys.stk.core.stkobjects.RadarModelMultifunction.antenna_beams
    :type: RadarAntennaBeamCollection

    Gets the antenna beams collection.

.. py:property:: waveform_strategy_settings
    :canonical: ansys.stk.core.stkobjects.RadarModelMultifunction.waveform_strategy_settings
    :type: RadarMultifunctionWaveformStrategySettings

    Gets the waveform selection strategy settings.

.. py:property:: clutter
    :canonical: ansys.stk.core.stkobjects.RadarModelMultifunction.clutter
    :type: RadarClutter

    Gets the radar clutter settings.


Method detail
-------------







.. py:method:: set_pointing_strategy_type(self, value: POINTING_STRATEGY_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.RadarModelMultifunction.set_pointing_strategy_type

    Set the current pointing strategy type.

    :Parameters:

    **value** : :obj:`~POINTING_STRATEGY_TYPE`

    :Returns:

        :obj:`~None`





