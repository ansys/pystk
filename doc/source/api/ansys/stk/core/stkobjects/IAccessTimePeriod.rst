IAccessTimePeriod
=================

.. py:class:: ansys.stk.core.stkobjects.IAccessTimePeriod

   object
   
   Allow configuring the object's access interval.

.. py:currentmodule:: IAccessTimePeriod

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessTimePeriod.start_time`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessTimePeriod.stop_time`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessTimePeriod.duration`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAccessTimePeriod.access_interval`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAccessTimePeriod


Property detail
---------------

.. py:property:: start_time
    :canonical: ansys.stk.core.stkobjects.IAccessTimePeriod.start_time
    :type: ITimePeriodValue

    Gets a start time. Uses DateFormat Dimension.

.. py:property:: stop_time
    :canonical: ansys.stk.core.stkobjects.IAccessTimePeriod.stop_time
    :type: ITimePeriodValue

    Gets a stop time. Uses DateFormat Dimension.

.. py:property:: duration
    :canonical: ansys.stk.core.stkobjects.IAccessTimePeriod.duration
    :type: typing.Any

    A time duration. The value is a relative duration (i.e. \"+1 day\", \"+1 hour\").

.. py:property:: access_interval
    :canonical: ansys.stk.core.stkobjects.IAccessTimePeriod.access_interval
    :type: ITimeToolEventIntervalSmartInterval

    Returns an access interval.


