IAccessConstraintTimeSlipRange
==============================

.. py:class:: ansys.stk.core.stkobjects.IAccessConstraintTimeSlipRange

   IAccessConstraint
   
   IAgAccessCnstrTimeSlipRange used to access the Time Slip Range.

.. py:currentmodule:: IAccessConstraintTimeSlipRange

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessConstraintTimeSlipRange.launch_window_start`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessConstraintTimeSlipRange.launch_window_end`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessConstraintTimeSlipRange.range`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAccessConstraintTimeSlipRange


Property detail
---------------

.. py:property:: launch_window_start
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintTimeSlipRange.launch_window_start
    :type: typing.Any

    Launch Window Start time. Uses DateFormat Dimension.

.. py:property:: launch_window_end
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintTimeSlipRange.launch_window_end
    :type: typing.Any

    Launch Window End time. Uses DateFormat Dimension.

.. py:property:: range
    :canonical: ansys.stk.core.stkobjects.IAccessConstraintTimeSlipRange.range
    :type: float

    Range of the launch window. When available, uses Distance Dimension.


