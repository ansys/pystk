IRadarModelMultifunction
========================

.. py:class:: IRadarModelMultifunction

   object
   
   Provide access to the properties and methods defining a multifunction radar model.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_pointing_strategy_type`
              - Set the current pointing strategy type.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~transmitter`
            * - :py:meth:`~receiver`
            * - :py:meth:`~clutter_geometry`
            * - :py:meth:`~jamming`
            * - :py:meth:`~location`
            * - :py:meth:`~detection_processing`
            * - :py:meth:`~pointing_strategy`
            * - :py:meth:`~antenna_beams`
            * - :py:meth:`~waveform_strategy_settings`
            * - :py:meth:`~clutter`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarModelMultifunction


Property detail
---------------

.. py:property:: transmitter
    :canonical: ansys.stk.core.stkobjects.IRadarModelMultifunction.transmitter
    :type: "IAgRadarTransmitterMultifunction"

    Gets the radar transmitter.

.. py:property:: receiver
    :canonical: ansys.stk.core.stkobjects.IRadarModelMultifunction.receiver
    :type: "IAgRadarReceiver"

    Gets the radar receiver.

.. py:property:: clutter_geometry
    :canonical: ansys.stk.core.stkobjects.IRadarModelMultifunction.clutter_geometry
    :type: "IAgRadarClutterGeometry"

    This property is deprecated.Use the Clutter property instead.Gets the radar clutter geometry.

.. py:property:: jamming
    :canonical: ansys.stk.core.stkobjects.IRadarModelMultifunction.jamming
    :type: "IAgRadarJamming"

    Gets the radar jamming.

.. py:property:: location
    :canonical: ansys.stk.core.stkobjects.IRadarModelMultifunction.location
    :type: "IAgCRLocation"

    Gets the radar location object.

.. py:property:: detection_processing
    :canonical: ansys.stk.core.stkobjects.IRadarModelMultifunction.detection_processing
    :type: "IAgRadarMultifunctionDetectionProcessing"

    Gets the radar detection processing object.

.. py:property:: pointing_strategy
    :canonical: ansys.stk.core.stkobjects.IRadarModelMultifunction.pointing_strategy
    :type: "IAgPointingStrategy"

    Gets the pointing strategy.

.. py:property:: antenna_beams
    :canonical: ansys.stk.core.stkobjects.IRadarModelMultifunction.antenna_beams
    :type: "IAgRadarAntennaBeamCollection"

    Gets the antenna beams collection.

.. py:property:: waveform_strategy_settings
    :canonical: ansys.stk.core.stkobjects.IRadarModelMultifunction.waveform_strategy_settings
    :type: "IAgRadarMultifunctionWaveformStrategySettings"

    Gets the waveform selection strategy settings.

.. py:property:: clutter
    :canonical: ansys.stk.core.stkobjects.IRadarModelMultifunction.clutter
    :type: "IAgRadarClutter"

    Gets the radar clutter settings.


Method detail
-------------







.. py:method:: set_pointing_strategy_type(self, val:"POINTING_STRATEGY_TYPE") -> None

    Set the current pointing strategy type.

    :Parameters:

    **val** : :obj:`~"POINTING_STRATEGY_TYPE"`

    :Returns:

        :obj:`~None`





