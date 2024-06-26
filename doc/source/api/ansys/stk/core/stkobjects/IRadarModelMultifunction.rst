IRadarModelMultifunction
========================

.. py:class:: ansys.stk.core.stkobjects.IRadarModelMultifunction

   object
   
   Provide access to the properties and methods defining a multifunction radar model.

.. py:currentmodule:: IRadarModelMultifunction

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarModelMultifunction.set_pointing_strategy_type`
              - Set the current pointing strategy type.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarModelMultifunction.transmitter`
              - Gets the radar transmitter.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarModelMultifunction.receiver`
              - Gets the radar receiver.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarModelMultifunction.clutter_geometry`
              - This property is deprecated.Use the Clutter property instead.Gets the radar clutter geometry.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarModelMultifunction.jamming`
              - Gets the radar jamming.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarModelMultifunction.location`
              - Gets the radar location object.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarModelMultifunction.detection_processing`
              - Gets the radar detection processing object.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarModelMultifunction.pointing_strategy`
              - Gets the pointing strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarModelMultifunction.antenna_beams`
              - Gets the antenna beams collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarModelMultifunction.waveform_strategy_settings`
              - Gets the waveform selection strategy settings.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarModelMultifunction.clutter`
              - Gets the radar clutter settings.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarModelMultifunction


Property detail
---------------

.. py:property:: transmitter
    :canonical: ansys.stk.core.stkobjects.IRadarModelMultifunction.transmitter
    :type: IRadarTransmitterMultifunction

    Gets the radar transmitter.

.. py:property:: receiver
    :canonical: ansys.stk.core.stkobjects.IRadarModelMultifunction.receiver
    :type: IRadarReceiver

    Gets the radar receiver.

.. py:property:: clutter_geometry
    :canonical: ansys.stk.core.stkobjects.IRadarModelMultifunction.clutter_geometry
    :type: IRadarClutterGeometry

    This property is deprecated.Use the Clutter property instead.Gets the radar clutter geometry.

.. py:property:: jamming
    :canonical: ansys.stk.core.stkobjects.IRadarModelMultifunction.jamming
    :type: IRadarJamming

    Gets the radar jamming.

.. py:property:: location
    :canonical: ansys.stk.core.stkobjects.IRadarModelMultifunction.location
    :type: ICRLocation

    Gets the radar location object.

.. py:property:: detection_processing
    :canonical: ansys.stk.core.stkobjects.IRadarModelMultifunction.detection_processing
    :type: IRadarMultifunctionDetectionProcessing

    Gets the radar detection processing object.

.. py:property:: pointing_strategy
    :canonical: ansys.stk.core.stkobjects.IRadarModelMultifunction.pointing_strategy
    :type: IPointingStrategy

    Gets the pointing strategy.

.. py:property:: antenna_beams
    :canonical: ansys.stk.core.stkobjects.IRadarModelMultifunction.antenna_beams
    :type: IRadarAntennaBeamCollection

    Gets the antenna beams collection.

.. py:property:: waveform_strategy_settings
    :canonical: ansys.stk.core.stkobjects.IRadarModelMultifunction.waveform_strategy_settings
    :type: IRadarMultifunctionWaveformStrategySettings

    Gets the waveform selection strategy settings.

.. py:property:: clutter
    :canonical: ansys.stk.core.stkobjects.IRadarModelMultifunction.clutter
    :type: IRadarClutter

    Gets the radar clutter settings.


Method detail
-------------







.. py:method:: set_pointing_strategy_type(self, val: POINTING_STRATEGY_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.IRadarModelMultifunction.set_pointing_strategy_type

    Set the current pointing strategy type.

    :Parameters:

    **val** : :obj:`~POINTING_STRATEGY_TYPE`

    :Returns:

        :obj:`~None`





