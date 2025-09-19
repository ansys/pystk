RadarModeMonostaticSearchTrack
==============================

.. py:class:: ansys.stk.core.stkobjects.RadarModeMonostaticSearchTrack

   Bases: :py:class:`~ansys.stk.core.stkobjects.IRadarModeMonostatic`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining a monostatic search/track radar mode.

.. py:currentmodule:: RadarModeMonostaticSearchTrack

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModeMonostaticSearchTrack.set_waveform_type`
              - Set the waveform type.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModeMonostaticSearchTrack.doppler_clutter_filters`
              - Get the RadarDopplerClutterFilters interface for configuring the doppler clutter filters.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarModeMonostaticSearchTrack.waveform`
              - Get the interface for configuring the search/track waveform.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RadarModeMonostaticSearchTrack


Property detail
---------------

.. py:property:: doppler_clutter_filters
    :canonical: ansys.stk.core.stkobjects.RadarModeMonostaticSearchTrack.doppler_clutter_filters
    :type: RadarDopplerClutterFilters

    Get the RadarDopplerClutterFilters interface for configuring the doppler clutter filters.

.. py:property:: waveform
    :canonical: ansys.stk.core.stkobjects.RadarModeMonostaticSearchTrack.waveform
    :type: IRadarWaveformSearchTrack

    Get the interface for configuring the search/track waveform.


Method detail
-------------


.. py:method:: set_waveform_type(self, value: RadarWaveformSearchTrackType) -> None
    :canonical: ansys.stk.core.stkobjects.RadarModeMonostaticSearchTrack.set_waveform_type

    Set the waveform type.

    :Parameters:

        **value** : :obj:`~RadarWaveformSearchTrackType`


    :Returns:

        :obj:`~None`


