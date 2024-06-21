IVehicleTargetTimes
===================

.. py:class:: ansys.stk.core.stkobjects.IVehicleTargetTimes

   object
   
   Target times for target pointing attitude.

.. py:currentmodule:: IVehicleTargetTimes

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleTargetTimes.deconflict`
              - Deconflict intervals.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleTargetTimes.use_access_times`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleTargetTimes.access_times`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleTargetTimes.schedule_times`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleTargetTimes


Property detail
---------------

.. py:property:: use_access_times
    :canonical: ansys.stk.core.stkobjects.IVehicleTargetTimes.use_access_times
    :type: bool

    Opt whether to use access times as target times; otherwise, scheduled times are used.

.. py:property:: access_times
    :canonical: ansys.stk.core.stkobjects.IVehicleTargetTimes.access_times
    :type: IAccessTimeCollection

    Get the access times.

.. py:property:: schedule_times
    :canonical: ansys.stk.core.stkobjects.IVehicleTargetTimes.schedule_times
    :type: IVehicleScheduleTimesCollection

    Get the scheduled times.


Method detail
-------------





.. py:method:: deconflict(self) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleTargetTimes.deconflict

    Deconflict intervals.

    :Returns:

        :obj:`~None`

