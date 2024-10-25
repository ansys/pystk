VEHICLE_ALTITUDE_REFERENCE
==========================

.. py:class:: ansys.stk.core.stkobjects.VEHICLE_ALTITUDE_REFERENCE

   IntEnum


.. py:currentmodule:: VEHICLE_ALTITUDE_REFERENCE

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - Unknown.

            * - :py:attr:`~MEAN_SEA_LEVEL`
              - Referenced to Mean Sea Level.

            * - :py:attr:`~TERRAIN`
              - Referenced to the terrain under the vehicle's route (if terrain sources are loaded into the scenario).

            * - :py:attr:`~WGS84`
              - Referenced to the central body's reference ellipsoid (WGS84).

            * - :py:attr:`~ELLIPSOID`
              - Referenced to the central body's reference ellipsoid.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VEHICLE_ALTITUDE_REFERENCE


