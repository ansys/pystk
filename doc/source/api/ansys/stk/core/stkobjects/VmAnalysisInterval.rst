VmAnalysisInterval
==================

.. py:class:: ansys.stk.core.stkobjects.VmAnalysisInterval

   Bases: 

   Class defining the volumetric analysis interval.

.. py:currentmodule:: VmAnalysisInterval

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VmAnalysisInterval.set_evaluation_of_spatial_calc_type`
              - Evaluate spatial calculation type, using the AgEVmSpatialCalcEvalType enumeration.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VmAnalysisInterval.analysis_interval`
              - The volume analysis interval or interval list.
            * - :py:attr:`~ansys.stk.core.stkobjects.VmAnalysisInterval.evaluation_of_spatial_calc_type`
              - Get evaluation of spatial calculation type. A member of the AgEVmSpatialCalcEvalType enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.VmAnalysisInterval.time_array`
              - The time array when Evaluation of spatial calculation at times from time array is used.
            * - :py:attr:`~ansys.stk.core.stkobjects.VmAnalysisInterval.step_size`
              - Gets or sets the step size.
            * - :py:attr:`~ansys.stk.core.stkobjects.VmAnalysisInterval.available_analysis_intervals`
              - Get the available analysis intervals.
            * - :py:attr:`~ansys.stk.core.stkobjects.VmAnalysisInterval.available_times_from_time_array`
              - Get the available times from time array.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VmAnalysisInterval


Property detail
---------------

.. py:property:: analysis_interval
    :canonical: ansys.stk.core.stkobjects.VmAnalysisInterval.analysis_interval
    :type: str

    The volume analysis interval or interval list.

.. py:property:: evaluation_of_spatial_calc_type
    :canonical: ansys.stk.core.stkobjects.VmAnalysisInterval.evaluation_of_spatial_calc_type
    :type: VM_SPATIAL_CALC_EVAL_TYPE

    Get evaluation of spatial calculation type. A member of the AgEVmSpatialCalcEvalType enumeration.

.. py:property:: time_array
    :canonical: ansys.stk.core.stkobjects.VmAnalysisInterval.time_array
    :type: str

    The time array when Evaluation of spatial calculation at times from time array is used.

.. py:property:: step_size
    :canonical: ansys.stk.core.stkobjects.VmAnalysisInterval.step_size
    :type: float

    Gets or sets the step size.

.. py:property:: available_analysis_intervals
    :canonical: ansys.stk.core.stkobjects.VmAnalysisInterval.available_analysis_intervals
    :type: list

    Get the available analysis intervals.

.. py:property:: available_times_from_time_array
    :canonical: ansys.stk.core.stkobjects.VmAnalysisInterval.available_times_from_time_array
    :type: list

    Get the available times from time array.


Method detail
-------------




.. py:method:: set_evaluation_of_spatial_calc_type(self, spatialCalcEvalType: VM_SPATIAL_CALC_EVAL_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.VmAnalysisInterval.set_evaluation_of_spatial_calc_type

    Evaluate spatial calculation type, using the AgEVmSpatialCalcEvalType enumeration.

    :Parameters:

    **spatialCalcEvalType** : :obj:`~VM_SPATIAL_CALC_EVAL_TYPE`

    :Returns:

        :obj:`~None`







