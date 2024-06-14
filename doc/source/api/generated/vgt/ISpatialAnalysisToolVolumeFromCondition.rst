ISpatialAnalysisToolVolumeFromCondition
=======================================

.. py:class:: ISpatialAnalysisToolVolumeFromCondition

   object
   
   A volume from conditioninterface.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~condition`
            * - :py:meth:`~use_custom_time_limits`
            * - :py:meth:`~custom_time_limits`
            * - :py:meth:`~sampling`
            * - :py:meth:`~convergence`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ISpatialAnalysisToolVolumeFromCondition


Property detail
---------------

.. py:property:: condition
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeFromCondition.condition
    :type: "IAgCrdnCondition"

    The condition component.

.. py:property:: use_custom_time_limits
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeFromCondition.use_custom_time_limits
    :type: bool

    Indicate whether to use specified custom time limits (see CustomTimeLimits).

.. py:property:: custom_time_limits
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeFromCondition.custom_time_limits
    :type: "IAgCrdnEventIntervalList"

    A custom interval list or a single interval. It is by default set to overall availability of host object. This determines time limits within extrema are sought. The time limits will be used if UseCustomTimeLimits is set to true.

.. py:property:: sampling
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeFromCondition.sampling
    :type: "IAgCrdnSampling"

    The Sampling definition, which can use a fixed step, relative tolerance or curvature tolerance. Relative tolerance uses a combination of relative and absolute changes in scalar values between samples...

.. py:property:: convergence
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeFromCondition.convergence
    :type: "IAgCrdnConverge"

    The Convergence definition, which uses time tolerance to determine when times of extrema are found.


