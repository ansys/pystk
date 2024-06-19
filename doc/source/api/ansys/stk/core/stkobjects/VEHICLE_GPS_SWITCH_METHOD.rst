VEHICLE_GPS_SWITCH_METHOD
=========================

.. py:class:: VEHICLE_GPS_SWITCH_METHOD

   IntEnum


.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~GPS_SWITCH_METHOD_EPOCH`
              - Switch between TLE sets based on the epoch of the TLE.

            * - :py:attr:`~GPS_SWITCH_METHOD_MIDPOINT`
              - Switch between TLE sets based on the mid-point between two TLE epochs.

            * - :py:attr:`~GPS_SWITCH_METHOD_TCA`
              - Switch between TLE sets based on the time of closest approach, calculated by propagating the first and second TLE sets over the time period between their respective epochs and determining the point at which the two paths are nearest each other.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VEHICLE_GPS_SWITCH_METHOD


