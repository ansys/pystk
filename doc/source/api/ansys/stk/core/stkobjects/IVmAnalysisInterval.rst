IVmAnalysisInterval
===================

.. py:class:: IVmAnalysisInterval

   object
   
   IAgVmAnalysisInterval Interface for volume analysis interval.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_evaluation_of_spatial_calc_type`
              - Evaluate spatial calculation type, using the AgEVmSpatialCalcEvalType enumeration.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~analysis_interval`
            * - :py:meth:`~evaluation_of_spatial_calc_type`
            * - :py:meth:`~time_array`
            * - :py:meth:`~step_size`
            * - :py:meth:`~available_analysis_intervals`
            * - :py:meth:`~available_times_from_time_array`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVmAnalysisInterval


Property detail
---------------

.. py:property:: analysis_interval
    :canonical: ansys.stk.core.stkobjects.IVmAnalysisInterval.analysis_interval
    :type: str

    The volume analysis interval or interval list.

.. py:property:: evaluation_of_spatial_calc_type
    :canonical: ansys.stk.core.stkobjects.IVmAnalysisInterval.evaluation_of_spatial_calc_type
    :type: VM_SPATIAL_CALC_EVAL_TYPE

    Get evaluation of spatial calculation type. A member of the AgEVmSpatialCalcEvalType enumeration.

.. py:property:: time_array
    :canonical: ansys.stk.core.stkobjects.IVmAnalysisInterval.time_array
    :type: str

    The time array when Evaluation of spatial calculation at times from time array is used.

.. py:property:: step_size
    :canonical: ansys.stk.core.stkobjects.IVmAnalysisInterval.step_size
    :type: float

    Gets or sets the step size.

.. py:property:: available_analysis_intervals
    :canonical: ansys.stk.core.stkobjects.IVmAnalysisInterval.available_analysis_intervals
    :type: list

    Get the available analysis intervals.

.. py:property:: available_times_from_time_array
    :canonical: ansys.stk.core.stkobjects.IVmAnalysisInterval.available_times_from_time_array
    :type: list

    Get the available times from time array.


Method detail
-------------




.. py:method:: set_evaluation_of_spatial_calc_type(self, spatialCalcEvalType: VM_SPATIAL_CALC_EVAL_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.IVmAnalysisInterval.set_evaluation_of_spatial_calc_type

    Evaluate spatial calculation type, using the AgEVmSpatialCalcEvalType enumeration.

    :Parameters:

    **spatialCalcEvalType** : :obj:`~VM_SPATIAL_CALC_EVAL_TYPE`

    :Returns:

        :obj:`~None`







