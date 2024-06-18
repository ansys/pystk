IAccessConstraintIntervals
==========================

.. py:class:: IAccessConstraintIntervals

   IAccessConstraint
   
   Access Constraint used for time intervals.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~filename`
            * - :py:meth:`~action_type`
            * - :py:meth:`~intervals`
            * - :py:meth:`~file_path`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAccessConstraintIntervals


Property detail
---------------

.. py:property:: filename
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintIntervals.filename
    :type: str

    Name of file containing the intervals data.

.. py:property:: action_type
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintIntervals.action_type
    :type: "ACTION_TYPE"

    This property is deprecated. Use ExclIntvl instead to determine whether intervals are to be excluded or not. The action type (include or exclude).

.. py:property:: intervals
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintIntervals.intervals
    :type: "IAgIntervalCollection"

    Gets the collection of intervals.

.. py:property:: file_path
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintIntervals.file_path
    :type: str

    Full path and name of file containing the intervals data.


