SpatialAnalysisToolConditionOverTime
====================================

.. py:class:: ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionOverTime

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ISpatialAnalysisToolVolume`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   An over time volume interface.

.. py:currentmodule:: SpatialAnalysisToolConditionOverTime

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionOverTime.duration_type`
              - Get or set the lighting conditions.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionOverTime.reference_intervals`
              - The reference interval list for the over time volume.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionOverTime.reference_volume`
              - Get or set the reference volume.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionOverTime.start_offset`
              - Set the offset with respect to current time to define the start of the sliding window, used when over time volume is set to Sliding Window.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionOverTime.stop_offset`
              - Set the offset with respect to current time to define the stop of the sliding window, used when over time volume is set to Sliding Window.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import SpatialAnalysisToolConditionOverTime


Property detail
---------------

.. py:property:: duration_type
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionOverTime.duration_type
    :type: SpatialConditionOverTypeDurationType

    Get or set the lighting conditions.

.. py:property:: reference_intervals
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionOverTime.reference_intervals
    :type: ITimeToolTimeIntervalList

    The reference interval list for the over time volume.

.. py:property:: reference_volume
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionOverTime.reference_volume
    :type: ISpatialAnalysisToolVolume

    Get or set the reference volume.

.. py:property:: start_offset
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionOverTime.start_offset
    :type: float

    Set the offset with respect to current time to define the start of the sliding window, used when over time volume is set to Sliding Window.

.. py:property:: stop_offset
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionOverTime.stop_offset
    :type: float

    Set the offset with respect to current time to define the stop of the sliding window, used when over time volume is set to Sliding Window.


