IVehicleSGP4Segment
===================

.. py:class:: IVehicleSGP4Segment

   object
   
   Interface for SGP4 propagator.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~ssc_num`
            * - :py:meth:`~rev_number`
            * - :py:meth:`~epoch`
            * - :py:meth:`~inclination`
            * - :py:meth:`~arg_of_perigee`
            * - :py:meth:`~raan`
            * - :py:meth:`~eccentricity`
            * - :py:meth:`~mean_motion`
            * - :py:meth:`~mean_anomaly`
            * - :py:meth:`~mean_motion_dot`
            * - :py:meth:`~motion_dot_dot`
            * - :py:meth:`~b_star`
            * - :py:meth:`~classification`
            * - :py:meth:`~intl_designator`
            * - :py:meth:`~switching_method`
            * - :py:meth:`~range`
            * - :py:meth:`~switch_time`
            * - :py:meth:`~enabled`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleSGP4Segment


Property detail
---------------

.. py:property:: ssc_num
    :canonical: ansys.stk.core.stkobjects.IVehicleSGP4Segment.ssc_num
    :type: str

    Catalog number of the spacecraft, if created by a 2-line element set.

.. py:property:: rev_number
    :canonical: ansys.stk.core.stkobjects.IVehicleSGP4Segment.rev_number
    :type: int

    Rev. Number. Dimensionless.

.. py:property:: epoch
    :canonical: ansys.stk.core.stkobjects.IVehicleSGP4Segment.epoch
    :type: float

    Universal date and time at which the specified orbit elements are true. Dimensionless.

.. py:property:: inclination
    :canonical: ansys.stk.core.stkobjects.IVehicleSGP4Segment.inclination
    :type: typing.Any

    Angle between the angular momentum vector (perpendicular to the plane of the orbit) and the inertial Z-axis. Uses Angle Dimension.

.. py:property:: arg_of_perigee
    :canonical: ansys.stk.core.stkobjects.IVehicleSGP4Segment.arg_of_perigee
    :type: typing.Any

    Angle from the ascending node to the eccentricity vector (lowest point of orbit) measured in the direction of the satellite's motion. Uses Angle Dimension.

.. py:property:: raan
    :canonical: ansys.stk.core.stkobjects.IVehicleSGP4Segment.raan
    :type: typing.Any

    Angle from the inertial X-axis to the ascending node. Uses Angle Dimension.

.. py:property:: eccentricity
    :canonical: ansys.stk.core.stkobjects.IVehicleSGP4Segment.eccentricity
    :type: float

    Value between 1 and 0 representing the ellipticality of the orbit. Dimensionless.

.. py:property:: mean_motion
    :canonical: ansys.stk.core.stkobjects.IVehicleSGP4Segment.mean_motion
    :type: typing.Any

    A measure of the osculating period of the orbit, expressed as an angular rate. Uses AngleRate Dimension.

.. py:property:: mean_anomaly
    :canonical: ansys.stk.core.stkobjects.IVehicleSGP4Segment.mean_anomaly
    :type: typing.Any

    Angle from the eccentricity vector to a position vector where the satellite would be if it were always moving at its average angular rate. Uses Angle Dimension.

.. py:property:: mean_motion_dot
    :canonical: ansys.stk.core.stkobjects.IVehicleSGP4Segment.mean_motion_dot
    :type: float

    First time derivative of mean motion. Dimensionless.

.. py:property:: motion_dot_dot
    :canonical: ansys.stk.core.stkobjects.IVehicleSGP4Segment.motion_dot_dot
    :type: float

    Second time derivative of mean motion. Dimensionless.

.. py:property:: b_star
    :canonical: ansys.stk.core.stkobjects.IVehicleSGP4Segment.b_star
    :type: float

    Drag term for the satellite.

.. py:property:: classification
    :canonical: ansys.stk.core.stkobjects.IVehicleSGP4Segment.classification
    :type: str

    One-letter classification indicator. U - Unclassified, C - Classified, S - Secret.

.. py:property:: intl_designator
    :canonical: ansys.stk.core.stkobjects.IVehicleSGP4Segment.intl_designator
    :type: str

    International designation of the satellite.

.. py:property:: switching_method
    :canonical: ansys.stk.core.stkobjects.IVehicleSGP4Segment.switching_method
    :type: "VEHICLE_SGP4_SWITCH_METHOD"

    Method used to switch between element sets.

.. py:property:: range
    :canonical: ansys.stk.core.stkobjects.IVehicleSGP4Segment.range
    :type: float

    How far apart the satellites are when switching occurs.

.. py:property:: switch_time
    :canonical: ansys.stk.core.stkobjects.IVehicleSGP4Segment.switch_time
    :type: typing.Any

    Gets or sets the time of the switch between one element set and a second set. Not used when the Switching Method is Disabled.

.. py:property:: enabled
    :canonical: ansys.stk.core.stkobjects.IVehicleSGP4Segment.enabled
    :type: bool

    Enables/disables the segment.


