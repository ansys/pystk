VEHICLE_WAYPOINT_COMPUTATION_METHOD
===================================

.. py:class:: ansys.stk.core.stkobjects.VEHICLE_WAYPOINT_COMPUTATION_METHOD

   IntEnum


.. py:currentmodule:: VEHICLE_WAYPOINT_COMPUTATION_METHOD

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~DETERMINE_TIME_ACCELERATION_FROM_VELOCITY`
              - Derive time and acceleration from velocity (smooth rate).

            * - :py:attr:`~DETERMINE_TIME_FROM_VELOCITY_AND_ACCELERATION`
              - Derive time from velocity and acceleration.

            * - :py:attr:`~DETERMINE_VELOCITY_FROM_TIME`
              - Derive velocity from time (enforces a zero acceleration).


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VEHICLE_WAYPOINT_COMPUTATION_METHOD


