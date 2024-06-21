IExportToolTimePeriod
=====================

.. py:class:: ansys.stk.core.stkobjects.IExportToolTimePeriod

   object
   
   Specify Time Period.

.. py:currentmodule:: IExportToolTimePeriod

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IExportToolTimePeriod.start`
            * - :py:attr:`~ansys.stk.core.stkobjects.IExportToolTimePeriod.stop`
            * - :py:attr:`~ansys.stk.core.stkobjects.IExportToolTimePeriod.time_period_type`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IExportToolTimePeriod


Property detail
---------------

.. py:property:: start
    :canonical: ansys.stk.core.stkobjects.IExportToolTimePeriod.start
    :type: typing.Any

    Gets or sets the start time of export interval. Uses DateFormate Dimension.

.. py:property:: stop
    :canonical: ansys.stk.core.stkobjects.IExportToolTimePeriod.stop
    :type: typing.Any

    Gets or sets the stop time of export interval. Uses DateFormat Dimension.

.. py:property:: time_period_type
    :canonical: ansys.stk.core.stkobjects.IExportToolTimePeriod.time_period_type
    :type: EXPORT_TOOL_TIME_PERIOD

    Specifies the time period type to use.


