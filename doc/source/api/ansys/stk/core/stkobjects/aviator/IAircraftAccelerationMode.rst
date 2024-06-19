IAircraftAccelerationMode
=========================

.. py:class:: IAircraftAccelerationMode

   object
   
   Interface used to set the Acceleration Mode for the Advanced Acceleration Model of an aircraft.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~accel_mode`
            * - :py:meth:`~accel_g`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAircraftAccelerationMode


Property detail
---------------

.. py:property:: accel_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAccelerationMode.accel_mode
    :type: ACCELERATION_ADVANCED_ACCEL_MODE

    Opt whether to override the acceleration or deceleration of the aircraft.

.. py:property:: accel_g
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAccelerationMode.accel_g
    :type: float

    Gets or sets the rate of acceleration or deceleration of the aircraft if the accleeration mode is set to override.


