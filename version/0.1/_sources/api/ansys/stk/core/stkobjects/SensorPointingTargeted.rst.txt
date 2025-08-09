SensorPointingTargeted
======================

.. py:class:: ansys.stk.core.stkobjects.SensorPointingTargeted

   Bases: :py:class:`~ansys.stk.core.stkobjects.ISensorPointing`

   Class defining the targeted pointing type for a Sensor.

.. py:currentmodule:: SensorPointingTargeted

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SensorPointingTargeted.boresight`
              - The targeted sensor's boresight type, a member of the SensorPointingTargetedBoresightType enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorPointingTargeted.boresight_data`
              - Get orientation data for the selected boresight type.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorPointingTargeted.enable_access_times`
              - Opt whether to use periods of access between the sensor and its target(s) as target times.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorPointingTargeted.access_times`
              - Get the access periods between the sensor and its target(s).
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorPointingTargeted.schedule_times`
              - Get the user-scheduled target times.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorPointingTargeted.targets`
              - Get the collection of objects assigned as targets for the sensor.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorPointingTargeted.available_targets`
              - Get the collection of objects available as targets for the sensor.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorPointingTargeted.advanced`
              - Get advanced targeting properties used for access computations.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorPointingTargeted.save_target_access`
              - Whether to Save Target Access.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SensorPointingTargeted


Property detail
---------------

.. py:property:: boresight
    :canonical: ansys.stk.core.stkobjects.SensorPointingTargeted.boresight
    :type: SensorPointingTargetedBoresightType

    The targeted sensor's boresight type, a member of the SensorPointingTargetedBoresightType enumeration.

.. py:property:: boresight_data
    :canonical: ansys.stk.core.stkobjects.SensorPointingTargeted.boresight_data
    :type: ISensorPointingTargetedBoresight

    Get orientation data for the selected boresight type.

.. py:property:: enable_access_times
    :canonical: ansys.stk.core.stkobjects.SensorPointingTargeted.enable_access_times
    :type: bool

    Opt whether to use periods of access between the sensor and its target(s) as target times.

.. py:property:: access_times
    :canonical: ansys.stk.core.stkobjects.SensorPointingTargeted.access_times
    :type: AccessTargetTimesCollection

    Get the access periods between the sensor and its target(s).

.. py:property:: schedule_times
    :canonical: ansys.stk.core.stkobjects.SensorPointingTargeted.schedule_times
    :type: ScheduleTimeCollection

    Get the user-scheduled target times.

.. py:property:: targets
    :canonical: ansys.stk.core.stkobjects.SensorPointingTargeted.targets
    :type: SensorTargetCollection

    Get the collection of objects assigned as targets for the sensor.

.. py:property:: available_targets
    :canonical: ansys.stk.core.stkobjects.SensorPointingTargeted.available_targets
    :type: list

    Get the collection of objects available as targets for the sensor.

.. py:property:: advanced
    :canonical: ansys.stk.core.stkobjects.SensorPointingTargeted.advanced
    :type: SensorAccessAdvancedSettings

    Get advanced targeting properties used for access computations.

.. py:property:: save_target_access
    :canonical: ansys.stk.core.stkobjects.SensorPointingTargeted.save_target_access
    :type: bool

    Whether to Save Target Access.


