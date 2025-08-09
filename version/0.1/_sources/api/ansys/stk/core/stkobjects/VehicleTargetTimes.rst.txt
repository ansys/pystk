VehicleTargetTimes
==================

.. py:class:: ansys.stk.core.stkobjects.VehicleTargetTimes

   Target times for target pointing attitude.

.. py:currentmodule:: VehicleTargetTimes

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleTargetTimes.deconflict`
              - Deconflict intervals.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleTargetTimes.use_access_times`
              - Opt whether to use access times as target times; otherwise, scheduled times are used.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleTargetTimes.access_times`
              - Get the access times.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleTargetTimes.schedule_times`
              - Get the scheduled times.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleTargetTimes


Property detail
---------------

.. py:property:: use_access_times
    :canonical: ansys.stk.core.stkobjects.VehicleTargetTimes.use_access_times
    :type: bool

    Opt whether to use access times as target times; otherwise, scheduled times are used.

.. py:property:: access_times
    :canonical: ansys.stk.core.stkobjects.VehicleTargetTimes.access_times
    :type: AccessTargetTimesCollection

    Get the access times.

.. py:property:: schedule_times
    :canonical: ansys.stk.core.stkobjects.VehicleTargetTimes.schedule_times
    :type: AttitudeScheduleTimesCollection

    Get the scheduled times.


Method detail
-------------





.. py:method:: deconflict(self) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleTargetTimes.deconflict

    Deconflict intervals.

    :Returns:

        :obj:`~None`

