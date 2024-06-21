IRadarModeBistaticTransmitterSearchTrack
========================================

.. py:class:: ansys.stk.core.stkobjects.IRadarModeBistaticTransmitterSearchTrack

   object
   
   Provide access to the properties and methods defining a bistatic transmitter search/track mode.

.. py:currentmodule:: IRadarModeBistaticTransmitterSearchTrack

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarModeBistaticTransmitterSearchTrack.set_waveform_type`
              - Set the waveform type.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarModeBistaticTransmitterSearchTrack.waveform`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarModeBistaticTransmitterSearchTrack


Property detail
---------------

.. py:property:: waveform
    :canonical: ansys.stk.core.stkobjects.IRadarModeBistaticTransmitterSearchTrack.waveform
    :type: IRadarWaveformSearchTrack

    Gets the interface for configuring the search/track waveform.


Method detail
-------------

.. py:method:: set_waveform_type(self, val: RADAR_WAVEFORM_SEARCH_TRACK_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.IRadarModeBistaticTransmitterSearchTrack.set_waveform_type

    Set the waveform type.

    :Parameters:

    **val** : :obj:`~RADAR_WAVEFORM_SEARCH_TRACK_TYPE`

    :Returns:

        :obj:`~None`


