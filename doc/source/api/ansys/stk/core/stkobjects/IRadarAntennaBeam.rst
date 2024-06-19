IRadarAntennaBeam
=================

.. py:class:: IRadarAntennaBeam

   object
   
   Provide access to a radar antenna beam.

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
            * - :py:meth:`~set_activity_type`
              - Set the activity type.
            * - :py:meth:`~set_waveform_selection_strategy`
              - Set the current waveform selection strategy.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~id`
            * - :py:meth:`~pointing_strategy`
            * - :py:meth:`~gain`
            * - :py:meth:`~beam_width`
            * - :py:meth:`~activity`
            * - :py:meth:`~waveform_selection_strategy`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarAntennaBeam


Property detail
---------------

.. py:property:: id
    :canonical: ansys.stk.core.stkobjects.IRadarAntennaBeam.id
    :type: str

    Gets or sets the antenna beam identifier.

.. py:property:: pointing_strategy
    :canonical: ansys.stk.core.stkobjects.IRadarAntennaBeam.pointing_strategy
    :type: IAgPointingStrategy

    Gets the pointing strategy.

.. py:property:: gain
    :canonical: ansys.stk.core.stkobjects.IRadarAntennaBeam.gain
    :type: float

    Gets or sets the antenna mainlobe gain.

.. py:property:: beam_width
    :canonical: ansys.stk.core.stkobjects.IRadarAntennaBeam.beam_width
    :type: float

    Gets or sets the antenna beamwidth.

.. py:property:: activity
    :canonical: ansys.stk.core.stkobjects.IRadarAntennaBeam.activity
    :type: IAgRadarActivity

    Gets the activity.

.. py:property:: waveform_selection_strategy
    :canonical: ansys.stk.core.stkobjects.IRadarAntennaBeam.waveform_selection_strategy
    :type: IAgWaveformSelectionStrategy

    Gets the waveform selection strategy.


Method detail
-------------



.. py:method:: set_pointing_strategy_type(self, val: POINTING_STRATEGY_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.IRadarAntennaBeam.set_pointing_strategy_type

    Set the current pointing strategy type.

    :Parameters:

    **val** : :obj:`~POINTING_STRATEGY_TYPE`

    :Returns:

        :obj:`~None`






.. py:method:: set_activity_type(self, activityType: RADAR_ACTIVITY_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.IRadarAntennaBeam.set_activity_type

    Set the activity type.

    :Parameters:

    **activityType** : :obj:`~RADAR_ACTIVITY_TYPE`

    :Returns:

        :obj:`~None`


.. py:method:: set_waveform_selection_strategy(self, val: WAVEFORM_SELECTION_STRATEGY_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.IRadarAntennaBeam.set_waveform_selection_strategy

    Set the current waveform selection strategy.

    :Parameters:

    **val** : :obj:`~WAVEFORM_SELECTION_STRATEGY_TYPE`

    :Returns:

        :obj:`~None`


