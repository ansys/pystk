AircraftAccelerationMode
========================

.. py:class:: ansys.stk.core.stkobjects.aviator.AircraftAccelerationMode

   Bases: 

   Class defining the acceleration mode options for an advanced acceleration performance model of an Aviator aircraft.

.. py:currentmodule:: AircraftAccelerationMode

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAccelerationMode.accel_mode`
              - Opt whether to override the acceleration or deceleration of the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAccelerationMode.accel_g`
              - Gets or sets the rate of acceleration or deceleration of the aircraft if the accleeration mode is set to override.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AircraftAccelerationMode


Property detail
---------------

.. py:property:: accel_mode
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAccelerationMode.accel_mode
    :type: ACCELERATION_ADVANCED_ACCEL_MODE

    Opt whether to override the acceleration or deceleration of the aircraft.

.. py:property:: accel_g
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAccelerationMode.accel_g
    :type: float

    Gets or sets the rate of acceleration or deceleration of the aircraft if the accleeration mode is set to override.


