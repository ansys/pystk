PropagatorSGP4SwitchMethod
==========================

.. py:class:: ansys.stk.core.stkobjects.PropagatorSGP4SwitchMethod

   IntEnum


.. py:currentmodule:: PropagatorSGP4SwitchMethod

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~EPOCH`
              - Epoch: switch between TLE sets based on the epoch of the TLE.

            * - :py:attr:`~MIDPOINT`
              - Mid-Point: switch between TLE sets based on the mid-point between two TLE epochs.

            * - :py:attr:`~TIME_OF_CLOSEST_APPROACH`
              - TCA: switch between TLE sets based on the time of closest approach.

            * - :py:attr:`~OVERRIDE`
              - Override: set the switching time between two TLE sets using the Start Time file.

            * - :py:attr:`~DISABLE`
              - Disable: ignore the selected TLE set (if you attempt to disable all of them, STK uses the first in the scenario time period).


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import PropagatorSGP4SwitchMethod


