AccessTimePeriod
================

.. py:class:: ansys.stk.core.stkobjects.AccessTimePeriod

   Bases: :py:class:`~ansys.stk.core.stkobjects.ITimePeriod`, :py:class:`~ansys.stk.core.stkobjects.IAccessInterval`

   Allow configuring the object's access interval.

.. py:currentmodule:: AccessTimePeriod

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AccessTimePeriod.start_time`
              - Gets a start time. Uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessTimePeriod.stop_time`
              - Gets a stop time. Uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessTimePeriod.duration`
              - A time duration. The value is a relative duration (i.e. \"+1 day\", \"+1 hour\").
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessTimePeriod.access_interval`
              - Returns an access interval.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AccessTimePeriod


Property detail
---------------

.. py:property:: start_time
    :canonical: ansys.stk.core.stkobjects.AccessTimePeriod.start_time
    :type: TimePeriodValue

    Gets a start time. Uses DateFormat Dimension.

.. py:property:: stop_time
    :canonical: ansys.stk.core.stkobjects.AccessTimePeriod.stop_time
    :type: TimePeriodValue

    Gets a stop time. Uses DateFormat Dimension.

.. py:property:: duration
    :canonical: ansys.stk.core.stkobjects.AccessTimePeriod.duration
    :type: typing.Any

    A time duration. The value is a relative duration (i.e. \"+1 day\", \"+1 hour\").

.. py:property:: access_interval
    :canonical: ansys.stk.core.stkobjects.AccessTimePeriod.access_interval
    :type: ITimeToolTimeIntervalSmartInterval

    Returns an access interval.


