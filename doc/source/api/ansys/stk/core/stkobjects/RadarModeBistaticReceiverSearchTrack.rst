RadarModeBistaticReceiverSearchTrack
====================================

.. py:class:: ansys.stk.core.stkobjects.RadarModeBistaticReceiverSearchTrack

   Bases: :py:class:`~ansys.stk.core.stkobjects.IRadarModeBistaticReceiver`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining a bistatic receiver search/track radar mode.

.. py:currentmodule:: RadarModeBistaticReceiverSearchTrack

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModeBistaticReceiverSearchTrack.set_waveform_type`
              - Set the waveform type.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModeBistaticReceiverSearchTrack.waveform`
              - Gets the interface for configuring the search/track waveform.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModeBistaticReceiverSearchTrack.doppler_clutter_filters`
              - Gets the IAgRadarDopplerClutterFilters interface for configuring the doppler clutter filters.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RadarModeBistaticReceiverSearchTrack


Property detail
---------------

.. py:property:: waveform
    :canonical: ansys.stk.core.stkobjects.RadarModeBistaticReceiverSearchTrack.waveform
    :type: IRadarWaveformSearchTrack

    Gets the interface for configuring the search/track waveform.

.. py:property:: doppler_clutter_filters
    :canonical: ansys.stk.core.stkobjects.RadarModeBistaticReceiverSearchTrack.doppler_clutter_filters
    :type: RadarDopplerClutterFilters

    Gets the IAgRadarDopplerClutterFilters interface for configuring the doppler clutter filters.


Method detail
-------------

.. py:method:: set_waveform_type(self, value: RADAR_WAVEFORM_SEARCH_TRACK_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.RadarModeBistaticReceiverSearchTrack.set_waveform_type

    Set the waveform type.

    :Parameters:

    **value** : :obj:`~RADAR_WAVEFORM_SEARCH_TRACK_TYPE`

    :Returns:

        :obj:`~None`



