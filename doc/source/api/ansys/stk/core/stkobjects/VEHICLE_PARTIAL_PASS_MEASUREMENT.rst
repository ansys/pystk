VEHICLE_PARTIAL_PASS_MEASUREMENT
================================

.. py:class:: VEHICLE_PARTIAL_PASS_MEASUREMENT

   IntEnum


.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ANGLE`
              - By Angle: angles are used to measure partial passes.

            * - :py:attr:`~MEAN_ARG_OF_LAT`
              - By Mean Argument of Latitude: passes are measured as the difference in the mean argument of latitude at the current time and that at the start of the pass break divided by 2 pi (argument of latitude = mean anomaly plus argument of perigee).

            * - :py:attr:`~TIME`
              - By Time: time is used to measure partial passes.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VEHICLE_PARTIAL_PASS_MEASUREMENT


