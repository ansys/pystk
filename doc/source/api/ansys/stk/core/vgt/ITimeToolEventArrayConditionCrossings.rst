ITimeToolEventArrayConditionCrossings
=====================================

.. py:class:: ITimeToolEventArrayConditionCrossings

   object
   
   Time array containing times at which the specified condition will change its satisfaction status. Determination is performed within the interval list using Sampling and Convergence parameters.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~satisfaction_crossing`
            * - :py:meth:`~condition`
            * - :py:meth:`~custom_time_limits`
            * - :py:meth:`~use_custom_time_limits`
            * - :py:meth:`~save_data_option`
            * - :py:meth:`~sampling`
            * - :py:meth:`~convergence`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolEventArrayConditionCrossings


Property detail
---------------

.. py:property:: satisfaction_crossing
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayConditionCrossings.satisfaction_crossing
    :type: CRDN_SATISFACTION_CROSSING

    The direction of interest for satisfaction crossing.

.. py:property:: condition
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayConditionCrossings.condition
    :type: IAgCrdnCondition

    The condition component.

.. py:property:: custom_time_limits
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayConditionCrossings.custom_time_limits
    :type: IAgCrdnEventIntervalList

    Specify the interval list within which satisfaction crossing times are sought. The default is set to overall availability of host object. The time limits will be used if UseCustomTimeLimits is set to true.

.. py:property:: use_custom_time_limits
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayConditionCrossings.use_custom_time_limits
    :type: bool

    Indicate whether to use specified custom time limits (see CustomTimeLimits).

.. py:property:: save_data_option
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayConditionCrossings.save_data_option
    :type: CRDN_SAVE_DATA_OPTION

    Determine if computed satisfaction crossing times are saved/loaded, or recomputed on load if necessary.

.. py:property:: sampling
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayConditionCrossings.sampling
    :type: IAgCrdnSampling

    The Sampling definition, which can use a fixed step, relative tolerance or curvature tolerance. Relative tolerance uses a combination of relative and absolute changes in scalar values between samples...

.. py:property:: convergence
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayConditionCrossings.convergence
    :type: IAgCrdnConverge

    The Convergence definition, which uses time tolerance to determine when crossing times are found.


