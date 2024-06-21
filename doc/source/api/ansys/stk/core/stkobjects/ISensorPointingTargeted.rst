ISensorPointingTargeted
=======================

.. py:class:: ansys.stk.core.stkobjects.ISensorPointingTargeted

   object
   
   IAgSnPtTargeted Interface for targeted sensors.

.. py:currentmodule:: ISensorPointingTargeted

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorPointingTargeted.boresight`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorPointingTargeted.boresight_data`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorPointingTargeted.enable_access_times`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorPointingTargeted.access_times`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorPointingTargeted.schedule_times`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorPointingTargeted.targets`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorPointingTargeted.available_targets`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorPointingTargeted.advanced`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorPointingTargeted.save_target_access`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ISensorPointingTargeted


Property detail
---------------

.. py:property:: boresight
    :canonical: ansys.stk.core.stkobjects.ISensorPointingTargeted.boresight
    :type: SENSOR_POINTING_TARGETED_BORESIGHT_TYPE

    The targeted sensor's boresight type, a member of the AgESnPtTrgtBsightType enumeration.

.. py:property:: boresight_data
    :canonical: ansys.stk.core.stkobjects.ISensorPointingTargeted.boresight_data
    :type: ISensorPointingTargetedBoresight

    Get orientation data for the selected boresight type.

.. py:property:: enable_access_times
    :canonical: ansys.stk.core.stkobjects.ISensorPointingTargeted.enable_access_times
    :type: bool

    Opt whether to use periods of access between the sensor and its target(s) as target times.

.. py:property:: access_times
    :canonical: ansys.stk.core.stkobjects.ISensorPointingTargeted.access_times
    :type: IAccessTimeCollection

    Get the access periods between the sensor and its target(s).

.. py:property:: schedule_times
    :canonical: ansys.stk.core.stkobjects.ISensorPointingTargeted.schedule_times
    :type: IScheduleTimeCollection

    Get the user-scheduled target times.

.. py:property:: targets
    :canonical: ansys.stk.core.stkobjects.ISensorPointingTargeted.targets
    :type: ISensorTargetCollection

    Get the collection of objects assigned as targets for the sensor.

.. py:property:: available_targets
    :canonical: ansys.stk.core.stkobjects.ISensorPointingTargeted.available_targets
    :type: list

    Get the collection of objects available as targets for the sensor.

.. py:property:: advanced
    :canonical: ansys.stk.core.stkobjects.ISensorPointingTargeted.advanced
    :type: ISensorAccessAdvanced

    Get advanced targeting properties used for access computations.

.. py:property:: save_target_access
    :canonical: ansys.stk.core.stkobjects.ISensorPointingTargeted.save_target_access
    :type: bool

    Whether to Save Target Access.


