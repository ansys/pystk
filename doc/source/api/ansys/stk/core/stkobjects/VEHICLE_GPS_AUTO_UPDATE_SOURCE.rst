VEHICLE_GPS_AUTO_UPDATE_SOURCE
==============================

.. py:class:: VEHICLE_GPS_AUTO_UPDATE_SOURCE

   IntEnum


.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~GPS_AUTO_UPDATE_SOURCE_UNKNOWN`
              - Unknown or unsupported TLE source.

            * - :py:attr:`~GPS_AUTO_UPDATE_SOURCE_ONLINE`
              - Auto update the GPS propagator with GPS elements from an online source (AGI server).

            * - :py:attr:`~GPS_AUTO_UPDATE_SOURCE_FILE`
              - Auto update the GPS propagator with GPS elements from file.

            * - :py:attr:`~GPS_AUTO_UPDATE_SOURCE_NONE`
              - Manually specify the almanac with GPS elements.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VEHICLE_GPS_AUTO_UPDATE_SOURCE


