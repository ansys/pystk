VEHICLE_SGP4_SWITCH_METHOD
==========================

.. py:class:: ansys.stk.core.stkobjects.VEHICLE_SGP4_SWITCH_METHOD

   IntEnum


.. py:currentmodule:: VEHICLE_SGP4_SWITCH_METHOD

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~SGP4_EPOCH`
              - Epoch: switch between TLE sets based on the epoch of the TLE.

            * - :py:attr:`~SGP4_MIDPOINT`
              - Mid-Point: switch between TLE sets based on the mid-point between two TLE epochs.

            * - :py:attr:`~SGP4TCA`
              - TCA: switch between TLE sets based on the time of closest approach.

            * - :py:attr:`~SGP4_OVERRIDE`
              - Override: set the switching time between two TLE sets using the Start Time file.

            * - :py:attr:`~SGP4_DISABLE`
              - Disable: ignore the selected TLE set (if you attempt to disable all of them, STK uses the first in the scenario time period).


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VEHICLE_SGP4_SWITCH_METHOD


