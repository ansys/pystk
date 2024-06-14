ITimeToolIntervalsFilter
========================

.. py:class:: ITimeToolIntervalsFilter

   object
   
   The filter selects intervals of at least/most certain duration.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~duration_kind`
            * - :py:meth:`~interval_duration`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolIntervalsFilter


Property detail
---------------

.. py:property:: duration_kind
    :canonical: ansys.stk.core.vgt.ITimeToolIntervalsFilter.duration_kind
    :type: "CRDN_INTERVAL_DURATION_KIND"

    Choose a duration type (at least/at most).

.. py:property:: interval_duration
    :canonical: ansys.stk.core.vgt.ITimeToolIntervalsFilter.interval_duration
    :type: float

    The interval duration.


