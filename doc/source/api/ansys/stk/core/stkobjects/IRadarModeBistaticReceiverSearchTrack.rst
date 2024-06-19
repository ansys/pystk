IRadarModeBistaticReceiverSearchTrack
=====================================

.. py:class:: IRadarModeBistaticReceiverSearchTrack

   object
   
   Provide access to the properties and methods defining a bistatic receiver search/track mode.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_waveform_type`
              - Set the waveform type.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~waveform`
            * - :py:meth:`~doppler_clutter_filters`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarModeBistaticReceiverSearchTrack


Property detail
---------------

.. py:property:: waveform
    :canonical: ansys.stk.core.stkobjects.IRadarModeBistaticReceiverSearchTrack.waveform
    :type: IAgRadarWaveformSearchTrack

    Gets the interface for configuring the search/track waveform.

.. py:property:: doppler_clutter_filters
    :canonical: ansys.stk.core.stkobjects.IRadarModeBistaticReceiverSearchTrack.doppler_clutter_filters
    :type: IAgRadarDopplerClutterFilters

    Gets the IAgRadarDopplerClutterFilters interface for configuring the doppler clutter filters.


Method detail
-------------

.. py:method:: set_waveform_type(self, val: RADAR_WAVEFORM_SEARCH_TRACK_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.IRadarModeBistaticReceiverSearchTrack.set_waveform_type

    Set the waveform type.

    :Parameters:

    **val** : :obj:`~RADAR_WAVEFORM_SEARCH_TRACK_TYPE`

    :Returns:

        :obj:`~None`



