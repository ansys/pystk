VEHICLE_GEOMAG_FLUX_UPDATE_RATE
===============================

.. py:class:: ansys.stk.core.stkobjects.VEHICLE_GEOMAG_FLUX_UPDATE_RATE

   IntEnum


.. py:currentmodule:: VEHICLE_GEOMAG_FLUX_UPDATE_RATE

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~HOURLY_3`
              - 3-Hourly: updates using the eight values measured at three-hour intervals.

            * - :py:attr:`~HOURLY_INTERP_3`
              - 3-Hourly Interpolated: updates by interpolating the three-hour values.

            * - :py:attr:`~DAILY`
              - Daily.

            * - :py:attr:`~HOURLY_CUBIC_SPLINE_3`
              - 3-Hourly Cubic Spline.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VEHICLE_GEOMAG_FLUX_UPDATE_RATE


