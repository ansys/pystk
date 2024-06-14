IVehicleTargetTimes
===================

.. py:class:: IVehicleTargetTimes

   object
   
   Target times for target pointing attitude.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~deconflict`
              - Deconflict intervals.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~use_access_times`
            * - :py:meth:`~access_times`
            * - :py:meth:`~schedule_times`


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
    :type: "IAgAccessTimeCollection"

    Get the access times.

.. py:property:: schedule_times
    :canonical: ansys.stk.core.stkobjects.IVehicleTargetTimes.schedule_times
    :type: "IAgVeScheduleTimesCollection"

    Get the scheduled times.


Method detail
-------------





.. py:method:: deconflict(self) -> None

    Deconflict intervals.

    :Returns:

        :obj:`~None`

