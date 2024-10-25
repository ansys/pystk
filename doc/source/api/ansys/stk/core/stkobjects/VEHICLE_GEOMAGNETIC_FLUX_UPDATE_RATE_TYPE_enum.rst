VEHICLE_GEOMAGNETIC_FLUX_UPDATE_RATE_TYPE
=========================================

.. py:class:: ansys.stk.core.stkobjects.VEHICLE_GEOMAGNETIC_FLUX_UPDATE_RATE_TYPE

   IntEnum


.. py:currentmodule:: VEHICLE_GEOMAGNETIC_FLUX_UPDATE_RATE_TYPE

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~EVERY_3_HOURS`
              - 3-Hourly: updates using the eight values measured at three-hour intervals.

            * - :py:attr:`~INTERPOLATE_3_HOURLY_DATA`
              - 3-Hourly Interpolated: updates by interpolating the three-hour values.

            * - :py:attr:`~DAILY`
              - Daily.

            * - :py:attr:`~CUBIC_SPLINE_3_HOURLY_DATA`
              - 3-Hourly Cubic Spline.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VEHICLE_GEOMAGNETIC_FLUX_UPDATE_RATE_TYPE


