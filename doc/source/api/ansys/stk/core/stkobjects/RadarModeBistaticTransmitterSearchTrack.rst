RadarModeBistaticTransmitterSearchTrack
=======================================

.. py:class:: ansys.stk.core.stkobjects.RadarModeBistaticTransmitterSearchTrack

   Bases: :py:class:`~ansys.stk.core.stkobjects.IRadarModeBistaticTransmitter`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining a bistatic transmitter search/track radar mode.

.. py:currentmodule:: RadarModeBistaticTransmitterSearchTrack

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModeBistaticTransmitterSearchTrack.set_waveform_type`
              - Set the waveform type.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModeBistaticTransmitterSearchTrack.waveform`
              - Get the interface for configuring the search/track waveform.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RadarModeBistaticTransmitterSearchTrack


Property detail
---------------

.. py:property:: waveform
    :canonical: ansys.stk.core.stkobjects.RadarModeBistaticTransmitterSearchTrack.waveform
    :type: IRadarWaveformSearchTrack

    Get the interface for configuring the search/track waveform.


Method detail
-------------

.. py:method:: set_waveform_type(self, value: RadarWaveformSearchTrackType) -> None
    :canonical: ansys.stk.core.stkobjects.RadarModeBistaticTransmitterSearchTrack.set_waveform_type

    Set the waveform type.

    :Parameters:

        **value** : :obj:`~RadarWaveformSearchTrackType`


    :Returns:

        :obj:`~None`


