TimeToolInstantTimeOffset
=========================

.. py:class:: ansys.stk.core.analysis_workbench.TimeToolInstantTimeOffset

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ITimeToolInstant`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Event at fixed offset from specified reference event.

.. py:currentmodule:: TimeToolInstantTimeOffset

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolInstantTimeOffset.reference_time_instant`
              - The reference time instant.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolInstantTimeOffset.time_offset`
              - The time offset from the ReferenceTimeInstant. The value is in ``TimeUnit`` dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import TimeToolInstantTimeOffset


Property detail
---------------

.. py:property:: reference_time_instant
    :canonical: ansys.stk.core.analysis_workbench.TimeToolInstantTimeOffset.reference_time_instant
    :type: ITimeToolInstant

    The reference time instant.

.. py:property:: time_offset
    :canonical: ansys.stk.core.analysis_workbench.TimeToolInstantTimeOffset.time_offset
    :type: float

    The time offset from the ReferenceTimeInstant. The value is in ``TimeUnit`` dimension.


