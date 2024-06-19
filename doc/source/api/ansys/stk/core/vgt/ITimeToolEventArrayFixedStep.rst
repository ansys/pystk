ITimeToolEventArrayFixedStep
============================

.. py:class:: ITimeToolEventArrayFixedStep

   object
   
   Defined by taking fixed time steps from specified time reference and adding sampled times to array if they fall within specified bounding interval list.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~bounding_interval_list`
            * - :py:meth:`~sampling_time_step`
            * - :py:meth:`~include_interval_edges`
            * - :py:meth:`~reference_type`
            * - :py:meth:`~reference_time_instant`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolEventArrayFixedStep


Property detail
---------------

.. py:property:: bounding_interval_list
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayFixedStep.bounding_interval_list
    :type: IAgCrdnEventIntervalList

    The bounding interval list.

.. py:property:: sampling_time_step
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayFixedStep.sampling_time_step
    :type: float

    The sampling time step.

.. py:property:: include_interval_edges
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayFixedStep.include_interval_edges
    :type: bool

    Specify whether to include interval edges.

.. py:property:: reference_type
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayFixedStep.reference_type
    :type: CRDN_SAMPLED_REFERENCE_TIME

    Specify the time reference from which fixed sampling time steps are taken. Note: selecting Start/Stop of each Interval resets the time reference for each interval, whereas other types maintain single reference for entire array.

.. py:property:: reference_time_instant
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayFixedStep.reference_time_instant
    :type: IAgCrdnEvent

    The reference time instant. Only applicable if the ReferenceType is set to time instant.


