PropagatorSGP4Segment
=====================

.. py:class:: ansys.stk.core.stkobjects.PropagatorSGP4Segment

   SGP4 propagator segment.

.. py:currentmodule:: PropagatorSGP4Segment

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4Segment.ssc_number`
              - Catalog number of the spacecraft, if created by a 2-line element set.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4Segment.revolution_number`
              - Rev. Number. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4Segment.epoch`
              - Universal date and time at which the specified orbit elements are true. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4Segment.inclination`
              - Angle between the angular momentum vector (perpendicular to the plane of the orbit) and the inertial Z-axis. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4Segment.argument_of_periapsis`
              - Angle from the ascending node to the eccentricity vector (lowest point of orbit) measured in the direction of the satellite's motion. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4Segment.right_ascension_ascending_node`
              - Angle from the inertial X-axis to the ascending node. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4Segment.eccentricity`
              - Value between 1 and 0 representing the ellipticality of the orbit. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4Segment.mean_motion`
              - A measure of the osculating period of the orbit, expressed as an angular rate. Uses AngleRate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4Segment.mean_anomaly`
              - Angle from the eccentricity vector to a position vector where the satellite would be if it were always moving at its average angular rate. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4Segment.mean_motion_dot`
              - First time derivative of mean motion. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4Segment.motion_dot_dot`
              - Second time derivative of mean motion. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4Segment.bstar`
              - Drag term for the satellite.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4Segment.classification`
              - One-letter classification indicator. U - Unclassified, C - Classified, S - Secret.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4Segment.international_designator`
              - International designation of the satellite.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4Segment.switching_method`
              - Method used to switch between element sets.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4Segment.range`
              - How far apart the satellites are when switching occurs.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4Segment.switch_time`
              - Get or set the time of the switch between one element set and a second set. Not used when the Switching Method is Disabled.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4Segment.enabled`
              - Enable/disable the segment.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import PropagatorSGP4Segment


Property detail
---------------

.. py:property:: ssc_number
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4Segment.ssc_number
    :type: str

    Catalog number of the spacecraft, if created by a 2-line element set.

.. py:property:: revolution_number
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4Segment.revolution_number
    :type: int

    Rev. Number. Dimensionless.

.. py:property:: epoch
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4Segment.epoch
    :type: float

    Universal date and time at which the specified orbit elements are true. Dimensionless.

.. py:property:: inclination
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4Segment.inclination
    :type: typing.Any

    Angle between the angular momentum vector (perpendicular to the plane of the orbit) and the inertial Z-axis. Uses Angle Dimension.

.. py:property:: argument_of_periapsis
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4Segment.argument_of_periapsis
    :type: typing.Any

    Angle from the ascending node to the eccentricity vector (lowest point of orbit) measured in the direction of the satellite's motion. Uses Angle Dimension.

.. py:property:: right_ascension_ascending_node
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4Segment.right_ascension_ascending_node
    :type: typing.Any

    Angle from the inertial X-axis to the ascending node. Uses Angle Dimension.

.. py:property:: eccentricity
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4Segment.eccentricity
    :type: float

    Value between 1 and 0 representing the ellipticality of the orbit. Dimensionless.

.. py:property:: mean_motion
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4Segment.mean_motion
    :type: typing.Any

    A measure of the osculating period of the orbit, expressed as an angular rate. Uses AngleRate Dimension.

.. py:property:: mean_anomaly
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4Segment.mean_anomaly
    :type: typing.Any

    Angle from the eccentricity vector to a position vector where the satellite would be if it were always moving at its average angular rate. Uses Angle Dimension.

.. py:property:: mean_motion_dot
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4Segment.mean_motion_dot
    :type: float

    First time derivative of mean motion. Dimensionless.

.. py:property:: motion_dot_dot
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4Segment.motion_dot_dot
    :type: float

    Second time derivative of mean motion. Dimensionless.

.. py:property:: bstar
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4Segment.bstar
    :type: float

    Drag term for the satellite.

.. py:property:: classification
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4Segment.classification
    :type: str

    One-letter classification indicator. U - Unclassified, C - Classified, S - Secret.

.. py:property:: international_designator
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4Segment.international_designator
    :type: str

    International designation of the satellite.

.. py:property:: switching_method
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4Segment.switching_method
    :type: PropagatorSGP4SwitchMethod

    Method used to switch between element sets.

.. py:property:: range
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4Segment.range
    :type: float

    How far apart the satellites are when switching occurs.

.. py:property:: switch_time
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4Segment.switch_time
    :type: typing.Any

    Get or set the time of the switch between one element set and a second set. Not used when the Switching Method is Disabled.

.. py:property:: enabled
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4Segment.enabled
    :type: bool

    Enable/disable the segment.


