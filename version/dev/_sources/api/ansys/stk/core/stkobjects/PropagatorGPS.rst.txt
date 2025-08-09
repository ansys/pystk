PropagatorGPS
=============

.. py:class:: ansys.stk.core.stkobjects.PropagatorGPS

   GPS propagator.

.. py:currentmodule:: PropagatorGPS

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorGPS.propagate`
              - Propagates the satellite's path using the specified time interval.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorGPS.automatic_update_enabled`
              - Whether automatic update is enabled.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorGPS.automatic_update_settings`
              - Allow configuring the auto-update parameters and settings. AutoUpdateEnabled must be set to true in order to be able to change the auto-update properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorGPS.available_prns`
              - Return an array of available satellite Ids.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorGPS.ephemeris_interval`
              - Get the propagator's ephemeris interval.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorGPS.prn`
              - Get or set the satellite PRN number per ICD-GPS-200. This is a required data item as it is the GPS user's primary means of identifying GPS satellites. It is equivalent to the space vehicle identification (SVID) number of the satellite.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorGPS.specify_catalog`
              - Specify a catalog. AutoUpdateEnabled must be set to false in order to select an almanac.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorGPS.step`
              - Step size. Uses Time Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import PropagatorGPS


Property detail
---------------

.. py:property:: automatic_update_enabled
    :canonical: ansys.stk.core.stkobjects.PropagatorGPS.automatic_update_enabled
    :type: bool

    Whether automatic update is enabled.

.. py:property:: automatic_update_settings
    :canonical: ansys.stk.core.stkobjects.PropagatorGPS.automatic_update_settings
    :type: VehicleGPSAutoUpdate

    Allow configuring the auto-update parameters and settings. AutoUpdateEnabled must be set to true in order to be able to change the auto-update properties.

.. py:property:: available_prns
    :canonical: ansys.stk.core.stkobjects.PropagatorGPS.available_prns
    :type: list

    Return an array of available satellite Ids.

.. py:property:: ephemeris_interval
    :canonical: ansys.stk.core.stkobjects.PropagatorGPS.ephemeris_interval
    :type: ITimeToolTimeIntervalSmartInterval

    Get the propagator's ephemeris interval.

.. py:property:: prn
    :canonical: ansys.stk.core.stkobjects.PropagatorGPS.prn
    :type: int

    Get or set the satellite PRN number per ICD-GPS-200. This is a required data item as it is the GPS user's primary means of identifying GPS satellites. It is equivalent to the space vehicle identification (SVID) number of the satellite.

.. py:property:: specify_catalog
    :canonical: ansys.stk.core.stkobjects.PropagatorGPS.specify_catalog
    :type: VehicleGPSSpecifyAlmanac

    Specify a catalog. AutoUpdateEnabled must be set to false in order to select an almanac.

.. py:property:: step
    :canonical: ansys.stk.core.stkobjects.PropagatorGPS.step
    :type: float

    Step size. Uses Time Dimension.


Method detail
-------------








.. py:method:: propagate(self) -> None
    :canonical: ansys.stk.core.stkobjects.PropagatorGPS.propagate

    Propagates the satellite's path using the specified time interval.

    :Returns:

        :obj:`~None`




