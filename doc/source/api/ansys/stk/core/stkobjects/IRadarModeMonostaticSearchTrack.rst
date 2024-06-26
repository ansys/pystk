IRadarModeMonostaticSearchTrack
===============================

.. py:class:: ansys.stk.core.stkobjects.IRadarModeMonostaticSearchTrack

   object
   
   Provide access to the properties and methods defining a monostatic search/track mode.

.. py:currentmodule:: IRadarModeMonostaticSearchTrack

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarModeMonostaticSearchTrack.set_waveform_type`
              - Set the waveform type.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarModeMonostaticSearchTrack.waveform`
              - Gets the interface for configuring the search/track waveform.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarModeMonostaticSearchTrack.doppler_clutter_filters`
              - Gets the IAgRadarDopplerClutterFilters interface for configuring the doppler clutter filters.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarModeMonostaticSearchTrack


Property detail
---------------

.. py:property:: waveform
    :canonical: ansys.stk.core.stkobjects.IRadarModeMonostaticSearchTrack.waveform
    :type: IRadarWaveformSearchTrack

    Gets the interface for configuring the search/track waveform.

.. py:property:: doppler_clutter_filters
    :canonical: ansys.stk.core.stkobjects.IRadarModeMonostaticSearchTrack.doppler_clutter_filters
    :type: IRadarDopplerClutterFilters

    Gets the IAgRadarDopplerClutterFilters interface for configuring the doppler clutter filters.


Method detail
-------------

.. py:method:: set_waveform_type(self, val: RADAR_WAVEFORM_SEARCH_TRACK_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.IRadarModeMonostaticSearchTrack.set_waveform_type

    Set the waveform type.

    :Parameters:

    **val** : :obj:`~RADAR_WAVEFORM_SEARCH_TRACK_TYPE`

    :Returns:

        :obj:`~None`



