AccessConstraintIntervals
=========================

.. py:class:: ansys.stk.core.stkobjects.AccessConstraintIntervals

   Bases: :py:class:`~ansys.stk.core.stkobjects.IAccessConstraint`

   Class defining the Intervals constraint.

.. py:currentmodule:: AccessConstraintIntervals

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintIntervals.action_type`
              - Do not use this property, as it is deprecated. Use ExclIntvl instead to determine whether intervals are to be excluded or not. The action type (include or exclude).
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintIntervals.file_path`
              - Full path and name of file containing the intervals data.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintIntervals.filename`
              - Name of file containing the intervals data.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessConstraintIntervals.intervals`
              - Get the collection of intervals.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AccessConstraintIntervals


Property detail
---------------

.. py:property:: action_type
    :canonical: ansys.stk.core.stkobjects.AccessConstraintIntervals.action_type
    :type: ActionType

    Do not use this property, as it is deprecated. Use ExclIntvl instead to determine whether intervals are to be excluded or not. The action type (include or exclude).

.. py:property:: file_path
    :canonical: ansys.stk.core.stkobjects.AccessConstraintIntervals.file_path
    :type: str

    Full path and name of file containing the intervals data.

.. py:property:: filename
    :canonical: ansys.stk.core.stkobjects.AccessConstraintIntervals.filename
    :type: str

    Name of file containing the intervals data.

.. py:property:: intervals
    :canonical: ansys.stk.core.stkobjects.AccessConstraintIntervals.intervals
    :type: TimeIntervalCollection

    Get the collection of intervals.


