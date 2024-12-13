SpatialAnalysisToolConditionOverTime
====================================

.. py:class:: ansys.stk.core.vgt.SpatialAnalysisToolConditionOverTime

   Bases: :py:class:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolume`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   An over time volume interface.

.. py:currentmodule:: SpatialAnalysisToolConditionOverTime

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolConditionOverTime.duration_type`
              - Sets/Returns the lighting conditions.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolConditionOverTime.reference_volume`
              - Sets/Returns the reference volume.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolConditionOverTime.reference_intervals`
              - The reference interval list for the over time volume.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolConditionOverTime.start_offset`
              - Set the offset with respect to current time to define the start of the sliding window, used when over time volume is set to Sliding Window.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolConditionOverTime.stop_offset`
              - Set the offset with respect to current time to define the stop of the sliding window, used when over time volume is set to Sliding Window.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import SpatialAnalysisToolConditionOverTime


Property detail
---------------

.. py:property:: duration_type
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolConditionOverTime.duration_type
    :type: SpatialConditionOverTypeDurationType

    Sets/Returns the lighting conditions.

.. py:property:: reference_volume
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolConditionOverTime.reference_volume
    :type: ISpatialAnalysisToolVolume

    Sets/Returns the reference volume.

.. py:property:: reference_intervals
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolConditionOverTime.reference_intervals
    :type: ITimeToolTimeIntervalList

    The reference interval list for the over time volume.

.. py:property:: start_offset
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolConditionOverTime.start_offset
    :type: float

    Set the offset with respect to current time to define the start of the sliding window, used when over time volume is set to Sliding Window.

.. py:property:: stop_offset
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolConditionOverTime.stop_offset
    :type: float

    Set the offset with respect to current time to define the stop of the sliding window, used when over time volume is set to Sliding Window.


