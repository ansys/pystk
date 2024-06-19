ISpatialAnalysisToolVolumeOverTime
==================================

.. py:class:: ISpatialAnalysisToolVolumeOverTime

   object
   
   An over time volume interface.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~duration_type`
            * - :py:meth:`~reference_volume`
            * - :py:meth:`~reference_intervals`
            * - :py:meth:`~start_offset`
            * - :py:meth:`~stop_offset`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ISpatialAnalysisToolVolumeOverTime


Property detail
---------------

.. py:property:: duration_type
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeOverTime.duration_type
    :type: CRDN_VOLUME_OVER_TIME_DURATION_TYPE

    Sets/Returns the lighting conditions.

.. py:property:: reference_volume
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeOverTime.reference_volume
    :type: IAgCrdnVolume

    Sets/Returns the reference volume.

.. py:property:: reference_intervals
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeOverTime.reference_intervals
    :type: IAgCrdnEventIntervalList

    The reference interval list for the over time volume.

.. py:property:: start_offset
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeOverTime.start_offset
    :type: float

    Set the offset with respect to current time to define the start of the sliding window, used when over time volume is set to Sliding Window.

.. py:property:: stop_offset
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeOverTime.stop_offset
    :type: float

    Set the offset with respect to current time to define the stop of the sliding window, used when over time volume is set to Sliding Window.


