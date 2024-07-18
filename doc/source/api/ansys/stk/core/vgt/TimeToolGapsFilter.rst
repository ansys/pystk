TimeToolGapsFilter
==================

.. py:class:: ansys.stk.core.vgt.TimeToolGapsFilter

   Bases: :py:class:`~ansys.stk.core.vgt.ITimeToolPruneFilter`

   The filter merges intervals unless they are separated by gaps of at least/most certain duration.

.. py:currentmodule:: TimeToolGapsFilter

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolGapsFilter.duration_kind`
              - Choose a duration type (at least/at most).
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolGapsFilter.gap_duration`
              - Duration of the gap.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import TimeToolGapsFilter


Property detail
---------------

.. py:property:: duration_kind
    :canonical: ansys.stk.core.vgt.TimeToolGapsFilter.duration_kind
    :type: CRDN_INTERVAL_DURATION_KIND

    Choose a duration type (at least/at most).

.. py:property:: gap_duration
    :canonical: ansys.stk.core.vgt.TimeToolGapsFilter.gap_duration
    :type: float

    Duration of the gap.


