IElementKeplerian
=================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IElementKeplerian

   IElement
   
   Properties for Keplerian elements.

.. py:currentmodule:: IElementKeplerian

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementKeplerian.semi_major_axis`
              - One-half the distance along the long axis of the elliptical orbit. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementKeplerian.eccentricity`
              - Describes the shape of the ellipse (a real number >= 0 and <1, where 0 = a circular orbit). Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementKeplerian.inclination`
              - Gets or sets the angle between the angular momentum vector (perpendicular to the plane of the orbit) and the inertial Z axis. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementKeplerian.raan`
              - Gets or sets the angle from the inertial X axis to the ascending node measured in a right-handed sense about the inertial Z axis in the equatorial plane. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementKeplerian.arg_of_periapsis`
              - Gets or sets the angle from the ascending node to the eccentricity vector (lowest point of orbit) measured in the direction of the satellite's motion and in the orbit plane. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementKeplerian.true_anomaly`
              - Gets or sets the angle from the eccentricity vector (points toward perigee) to the satellite position vector, measured in the direction of satellite motion and in the orbit plane. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementKeplerian.apoapsis_altitude_size`
              - Measured from the \"surface\" of the Earth to the points of maximum and minimum radius in the orbit. For these values, the surface of the Earth is modeled as a sphere whose radius equals the equatorial radius of the Earth. Uses Distance dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementKeplerian.apoapsis_radius_size`
              - Measured from the center of the Earth to the points of maximum and minimum radius in the orbit. Uses Distance dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementKeplerian.mean_motion`
              - Gets or sets the uniform rate of the satellite in a circular orbit of the same period, typically expressed as degrees or radians per second, or as revolutions per day. Uses AngleRate dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementKeplerian.periapsis_altitude_size`
              - Measured from the \"surface\" of the Earth to the points of maximum and minimum radius in the orbit. For these values, the surface of the Earth is modeled as a sphere whose radius equals the equatorial radius of the Earth. Uses Distance dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementKeplerian.periapsis_radius_size`
              - Measured from the center of the Earth to the points of maximum and minimum radius in the orbit. Uses Distance dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementKeplerian.period`
              - Gets or sets the duration of one orbit, based on assumed two-body motion. Uses Time dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementKeplerian.lan`
              - Gets or sets the Earth-fixed longitude where the satellite has crossed the inertial equator (the intersection of the ground track and the inertial equator) from south to north based on an assumption of two-body motion. Uses Angle dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementKeplerian.arg_of_latitude`
              - Gets or sets the sum of the True Anomaly and the Argument of Perigee. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementKeplerian.eccentric_anomaly`
              - Angle measured with origin at the center of the ellipse from the direction of perigee to a point on a circumscribing circle from which a line perpendicular to the SMA intersects the position of the satellite on the ellipse. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementKeplerian.mean_anomaly`
              - Gets or sets the angle from the eccentricity vector to a position vector where the satellite would be if it were always moving at its average angular rate. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementKeplerian.time_past_asc_node`
              - Gets or sets the elapsed time since the last ascending node crossing based on assumed two-body motion. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementKeplerian.time_past_periapsis`
              - Gets or sets the elapsed time since the last perigee passage based on assumed two-body motion. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementKeplerian.element_type`
              - Which type of element (osculating or mean).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementKeplerian.apoapsis_altitude_shape`
              - Describes the shape of the ellipse. Uses Distance dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementKeplerian.apoapsis_radius_shape`
              - Describes the shape of the ellipse. Uses Distance dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementKeplerian.periapsis_altitude_shape`
              - Describes the shape of the ellipse. Uses Distance dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementKeplerian.periapsis_radius_shape`
              - Describes the shape of the ellipse. Uses Distance dimension.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IElementKeplerian


Property detail
---------------

.. py:property:: semi_major_axis
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementKeplerian.semi_major_axis
    :type: float

    One-half the distance along the long axis of the elliptical orbit. Uses Distance Dimension.

.. py:property:: eccentricity
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementKeplerian.eccentricity
    :type: float

    Describes the shape of the ellipse (a real number >= 0 and <1, where 0 = a circular orbit). Dimensionless.

.. py:property:: inclination
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementKeplerian.inclination
    :type: typing.Any

    Gets or sets the angle between the angular momentum vector (perpendicular to the plane of the orbit) and the inertial Z axis. Uses Angle Dimension.

.. py:property:: raan
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementKeplerian.raan
    :type: typing.Any

    Gets or sets the angle from the inertial X axis to the ascending node measured in a right-handed sense about the inertial Z axis in the equatorial plane. Uses Angle Dimension.

.. py:property:: arg_of_periapsis
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementKeplerian.arg_of_periapsis
    :type: typing.Any

    Gets or sets the angle from the ascending node to the eccentricity vector (lowest point of orbit) measured in the direction of the satellite's motion and in the orbit plane. Uses Angle Dimension.

.. py:property:: true_anomaly
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementKeplerian.true_anomaly
    :type: typing.Any

    Gets or sets the angle from the eccentricity vector (points toward perigee) to the satellite position vector, measured in the direction of satellite motion and in the orbit plane. Uses Angle Dimension.

.. py:property:: apoapsis_altitude_size
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementKeplerian.apoapsis_altitude_size
    :type: float

    Measured from the \"surface\" of the Earth to the points of maximum and minimum radius in the orbit. For these values, the surface of the Earth is modeled as a sphere whose radius equals the equatorial radius of the Earth. Uses Distance dimension.

.. py:property:: apoapsis_radius_size
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementKeplerian.apoapsis_radius_size
    :type: float

    Measured from the center of the Earth to the points of maximum and minimum radius in the orbit. Uses Distance dimension.

.. py:property:: mean_motion
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementKeplerian.mean_motion
    :type: float

    Gets or sets the uniform rate of the satellite in a circular orbit of the same period, typically expressed as degrees or radians per second, or as revolutions per day. Uses AngleRate dimension.

.. py:property:: periapsis_altitude_size
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementKeplerian.periapsis_altitude_size
    :type: float

    Measured from the \"surface\" of the Earth to the points of maximum and minimum radius in the orbit. For these values, the surface of the Earth is modeled as a sphere whose radius equals the equatorial radius of the Earth. Uses Distance dimension.

.. py:property:: periapsis_radius_size
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementKeplerian.periapsis_radius_size
    :type: float

    Measured from the center of the Earth to the points of maximum and minimum radius in the orbit. Uses Distance dimension.

.. py:property:: period
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementKeplerian.period
    :type: float

    Gets or sets the duration of one orbit, based on assumed two-body motion. Uses Time dimension.

.. py:property:: lan
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementKeplerian.lan
    :type: typing.Any

    Gets or sets the Earth-fixed longitude where the satellite has crossed the inertial equator (the intersection of the ground track and the inertial equator) from south to north based on an assumption of two-body motion. Uses Angle dimension.

.. py:property:: arg_of_latitude
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementKeplerian.arg_of_latitude
    :type: typing.Any

    Gets or sets the sum of the True Anomaly and the Argument of Perigee. Uses Angle Dimension.

.. py:property:: eccentric_anomaly
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementKeplerian.eccentric_anomaly
    :type: typing.Any

    Angle measured with origin at the center of the ellipse from the direction of perigee to a point on a circumscribing circle from which a line perpendicular to the SMA intersects the position of the satellite on the ellipse. Uses Angle Dimension.

.. py:property:: mean_anomaly
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementKeplerian.mean_anomaly
    :type: typing.Any

    Gets or sets the angle from the eccentricity vector to a position vector where the satellite would be if it were always moving at its average angular rate. Uses Angle Dimension.

.. py:property:: time_past_asc_node
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementKeplerian.time_past_asc_node
    :type: float

    Gets or sets the elapsed time since the last ascending node crossing based on assumed two-body motion. Uses Time Dimension.

.. py:property:: time_past_periapsis
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementKeplerian.time_past_periapsis
    :type: float

    Gets or sets the elapsed time since the last perigee passage based on assumed two-body motion. Uses Time Dimension.

.. py:property:: element_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementKeplerian.element_type
    :type: ELEMENT

    Which type of element (osculating or mean).

.. py:property:: apoapsis_altitude_shape
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementKeplerian.apoapsis_altitude_shape
    :type: float

    Describes the shape of the ellipse. Uses Distance dimension.

.. py:property:: apoapsis_radius_shape
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementKeplerian.apoapsis_radius_shape
    :type: float

    Describes the shape of the ellipse. Uses Distance dimension.

.. py:property:: periapsis_altitude_shape
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementKeplerian.periapsis_altitude_shape
    :type: float

    Describes the shape of the ellipse. Uses Distance dimension.

.. py:property:: periapsis_radius_shape
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementKeplerian.periapsis_radius_shape
    :type: float

    Describes the shape of the ellipse. Uses Distance dimension.


