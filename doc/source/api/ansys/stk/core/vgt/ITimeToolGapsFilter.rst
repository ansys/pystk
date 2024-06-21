ITimeToolGapsFilter
===================

.. py:class:: ansys.stk.core.vgt.ITimeToolGapsFilter

   object
   
   The filter merges intervals unless they are separated by gaps of at least/most certain duration.

.. py:currentmodule:: ITimeToolGapsFilter

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolGapsFilter.duration_kind`
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolGapsFilter.gap_duration`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolGapsFilter


Property detail
---------------

.. py:property:: duration_kind
    :canonical: ansys.stk.core.vgt.ITimeToolGapsFilter.duration_kind
    :type: CRDN_INTERVAL_DURATION_KIND

    Choose a duration type (at least/at most).

.. py:property:: gap_duration
    :canonical: ansys.stk.core.vgt.ITimeToolGapsFilter.gap_duration
    :type: float

    Duration of the gap.


