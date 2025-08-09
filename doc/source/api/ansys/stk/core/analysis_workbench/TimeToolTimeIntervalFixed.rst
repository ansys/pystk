TimeToolTimeIntervalFixed
=========================

.. py:class:: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalFixed

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ITimeToolTimeInterval`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Interval defined between two explicitly specified start and stop times. Stop date/time is required to be at or after start.

.. py:currentmodule:: TimeToolTimeIntervalFixed

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalFixed.set_interval`
              - Set interval's start and stop times.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalFixed.start_time`
              - The start time of the interval.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalFixed.stop_time`
              - The stop time of the interval.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import TimeToolTimeIntervalFixed


Property detail
---------------

.. py:property:: start_time
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalFixed.start_time
    :type: typing.Any

    The start time of the interval.

.. py:property:: stop_time
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalFixed.stop_time
    :type: typing.Any

    The stop time of the interval.


Method detail
-------------

.. py:method:: set_interval(self, start_epoch: typing.Any, stop_epoch: typing.Any) -> None
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalFixed.set_interval

    Set interval's start and stop times.

    :Parameters:

        **start_epoch** : :obj:`~typing.Any`

        **stop_epoch** : :obj:`~typing.Any`


    :Returns:

        :obj:`~None`



