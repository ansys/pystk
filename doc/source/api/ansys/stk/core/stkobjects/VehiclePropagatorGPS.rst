VehiclePropagatorGPS
====================

.. py:class:: ansys.stk.core.stkobjects.VehiclePropagatorGPS

   GPS propagator.

.. py:currentmodule:: VehiclePropagatorGPS

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorGPS.propagate`
              - Propagates the satellite's path using the specified time interval.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorGPS.step`
              - Step size. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorGPS.prn`
              - Gets or sets the satellite PRN number per ICD-GPS-200. This is a required data item as it is the GPS user's primary means of identifying GPS satellites. It is equivalent to the space vehicle identification (SVID) number of the satellite.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorGPS.available_prns`
              - Returns an array of available satellite Ids.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorGPS.auto_update_enabled`
              - Whether automatic update is enabled.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorGPS.auto_update`
              - Allows configuring the auto-update parameters and settings. AutoUpdateEnabled must be set to true in order to be able to change the auto-update properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorGPS.specify_catalog`
              - Specify a catalog. AutoUpdateEnabled must be set to false in order to select an almanac.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorGPS.ephemeris_interval`
              - Get the propagator's ephemeris interval.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehiclePropagatorGPS


Property detail
---------------

.. py:property:: step
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorGPS.step
    :type: float

    Step size. Uses Time Dimension.

.. py:property:: prn
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorGPS.prn
    :type: int

    Gets or sets the satellite PRN number per ICD-GPS-200. This is a required data item as it is the GPS user's primary means of identifying GPS satellites. It is equivalent to the space vehicle identification (SVID) number of the satellite.

.. py:property:: available_prns
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorGPS.available_prns
    :type: list

    Returns an array of available satellite Ids.

.. py:property:: auto_update_enabled
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorGPS.auto_update_enabled
    :type: bool

    Whether automatic update is enabled.

.. py:property:: auto_update
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorGPS.auto_update
    :type: VehicleGPSAutoUpdate

    Allows configuring the auto-update parameters and settings. AutoUpdateEnabled must be set to true in order to be able to change the auto-update properties.

.. py:property:: specify_catalog
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorGPS.specify_catalog
    :type: VehicleGPSSpecifyAlmanac

    Specify a catalog. AutoUpdateEnabled must be set to false in order to select an almanac.

.. py:property:: ephemeris_interval
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorGPS.ephemeris_interval
    :type: ITimeToolTimeIntervalSmartInterval

    Get the propagator's ephemeris interval.


Method detail
-------------

.. py:method:: propagate(self) -> None
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorGPS.propagate

    Propagates the satellite's path using the specified time interval.

    :Returns:

        :obj:`~None`











