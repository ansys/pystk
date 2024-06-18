ICentralBodyEphemerisAnalyticOrbit
==================================

.. py:class:: ICentralBodyEphemerisAnalyticOrbit

   ICentralBodyEphemeris
   
   Properties for the Analytic Orbit ephemeris source.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~epoch`
            * - :py:meth:`~semi_major_axis`
            * - :py:meth:`~semi_major_axis_rate`
            * - :py:meth:`~eccentricity`
            * - :py:meth:`~eccentricity_rate`
            * - :py:meth:`~inclination`
            * - :py:meth:`~inclination_rate`
            * - :py:meth:`~raan`
            * - :py:meth:`~raan_rate`
            * - :py:meth:`~arg_of_periapsis`
            * - :py:meth:`~arg_of_periapsis_rate`
            * - :py:meth:`~mean_longitude`
            * - :py:meth:`~mean_longitude_rate`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ICentralBodyEphemerisAnalyticOrbit


Property detail
---------------

.. py:property:: epoch
    :canonical: ansys.stk.core.stkobjects.astrogator.ICentralBodyEphemerisAnalyticOrbit.epoch
    :type: float

    Gets or sets the epoch. Dimensionless.

.. py:property:: semi_major_axis
    :canonical: ansys.stk.core.stkobjects.astrogator.ICentralBodyEphemerisAnalyticOrbit.semi_major_axis
    :type: float

    Gets or sets the semi-major axis; one-half the distance along the long axis of the elliptical orbit. Uses Distance Dimension.

.. py:property:: semi_major_axis_rate
    :canonical: ansys.stk.core.stkobjects.astrogator.ICentralBodyEphemerisAnalyticOrbit.semi_major_axis_rate
    :type: float

    Gets or sets the semi-major axis rate of change. Uses Rate Dimension.

.. py:property:: eccentricity
    :canonical: ansys.stk.core.stkobjects.astrogator.ICentralBodyEphemerisAnalyticOrbit.eccentricity
    :type: float

    Gets or sets the eccentricity; the ratio of the distance between the two foci of the ellipse and its major axis. Dimensionless.

.. py:property:: eccentricity_rate
    :canonical: ansys.stk.core.stkobjects.astrogator.ICentralBodyEphemerisAnalyticOrbit.eccentricity_rate
    :type: float

    Gets or sets the eccentricity rate of change. Dimensionless.

.. py:property:: inclination
    :canonical: ansys.stk.core.stkobjects.astrogator.ICentralBodyEphemerisAnalyticOrbit.inclination
    :type: typing.Any

    Gets or sets the inclination; the angle from the Z axis of the inertial coordinate system to the orbit angular velocity vector. Uses Angle Dimension.

.. py:property:: inclination_rate
    :canonical: ansys.stk.core.stkobjects.astrogator.ICentralBodyEphemerisAnalyticOrbit.inclination_rate
    :type: float

    Gets or sets the inclination rate of change. Uses AngleRate Dimension.

.. py:property:: raan
    :canonical: ansys.stk.core.stkobjects.astrogator.ICentralBodyEphemerisAnalyticOrbit.raan
    :type: typing.Any

    Gets or sets the right ascension; the angle from the X axis of the inertial coordinate system to the point where the orbit crosses the X-Y plane in the +Z direction. Uses Angle Dimension.

.. py:property:: raan_rate
    :canonical: ansys.stk.core.stkobjects.astrogator.ICentralBodyEphemerisAnalyticOrbit.raan_rate
    :type: float

    Gets or sets the right ascension rate of change. Uses AngleRate Dimension.

.. py:property:: arg_of_periapsis
    :canonical: ansys.stk.core.stkobjects.astrogator.ICentralBodyEphemerisAnalyticOrbit.arg_of_periapsis
    :type: typing.Any

    Gets or sets the argument of periapsis; The angle measured in direction of the body's orbital motion, and in the orbit plane, from the ascending node to the periapsis of the orbit. Uses Angle Dimension.

.. py:property:: arg_of_periapsis_rate
    :canonical: ansys.stk.core.stkobjects.astrogator.ICentralBodyEphemerisAnalyticOrbit.arg_of_periapsis_rate
    :type: float

    Gets or sets the argument of periapsis rate of change. Uses AngleRate Dimension.

.. py:property:: mean_longitude
    :canonical: ansys.stk.core.stkobjects.astrogator.ICentralBodyEphemerisAnalyticOrbit.mean_longitude
    :type: typing.Any

    Gets or sets the mean longitude; the sum of the Right Ascension of the Ascending Node, the Argument of Periapsis and the Mean Anomaly. Uses Angle Dimension.

.. py:property:: mean_longitude_rate
    :canonical: ansys.stk.core.stkobjects.astrogator.ICentralBodyEphemerisAnalyticOrbit.mean_longitude_rate
    :type: float

    Gets or sets the mean longitude rate of change. Uses AngleRate Dimension.


