Star
====

.. py:class:: ansys.stk.core.stkobjects.Star

   Bases: :py:class:`~ansys.stk.core.stkobjects.ISTKObject`, :py:class:`~ansys.stk.core.stkobjects.ILifetimeInformation`

   Class defining the Star object.

.. py:currentmodule:: Star

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Star.location_right_ascension`
              - The star's right ascension: the angle in the equatorial plane measured in a right-handed sense about the inertial Z-axis from the inertial X-axis. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Star.location_declination`
              - The star's declination: the angle from the inertial equator measured toward the inertial positive Z-axis. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Star.proper_motion_right_ascension`
              - Motion of star relative to solar system barycenter expressed in arc seconds per year. Here, right ascension refers to motion in equatorial plane measured in a right-handed sense about the inertial Z-axis from inertial X-axis. Uses AngleRate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Star.proper_motion_declination`
              - Motion of the star relative to the solar system barycenter expressed in arc seconds per year. Here, declination refers to motion from the inertial equator measured towards the inertial positive Z-axis. Uses AngleRate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Star.parallax`
              - Annual parallax: motion of a star due to changes in the Earth's position relative to the solar system barycenter. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Star.epoch`
              - Epoch of the star position information as a Julian epoch (yyyy.yy). The Julian epoch is related to the Julian date by the expression JD = 2451545.0 + (yyyy.yy - 2000.0) x 365.25, where 2451545.0 (TT) represents the standard J2000 epoch.
            * - :py:attr:`~ansys.stk.core.stkobjects.Star.magnitude`
              - Magnitude, the visual brightness of the star. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.Star.graphics`
              - Get the star's 2D Graphics properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.Star.access_constraints`
              - Get the constraints imposed on the star.
            * - :py:attr:`~ansys.stk.core.stkobjects.Star.graphics_3d`
              - Get the star's 3D Graphics properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.Star.reference_frame`
              - Return a reference frame.
            * - :py:attr:`~ansys.stk.core.stkobjects.Star.proper_motion_radial_velocity`
              - Property motion radial velocity. Uses Distance dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Star


Property detail
---------------

.. py:property:: location_right_ascension
    :canonical: ansys.stk.core.stkobjects.Star.location_right_ascension
    :type: typing.Any

    The star's right ascension: the angle in the equatorial plane measured in a right-handed sense about the inertial Z-axis from the inertial X-axis. Uses Angle Dimension.

.. py:property:: location_declination
    :canonical: ansys.stk.core.stkobjects.Star.location_declination
    :type: typing.Any

    The star's declination: the angle from the inertial equator measured toward the inertial positive Z-axis. Uses Angle Dimension.

.. py:property:: proper_motion_right_ascension
    :canonical: ansys.stk.core.stkobjects.Star.proper_motion_right_ascension
    :type: float

    Motion of star relative to solar system barycenter expressed in arc seconds per year. Here, right ascension refers to motion in equatorial plane measured in a right-handed sense about the inertial Z-axis from inertial X-axis. Uses AngleRate Dimension.

.. py:property:: proper_motion_declination
    :canonical: ansys.stk.core.stkobjects.Star.proper_motion_declination
    :type: float

    Motion of the star relative to the solar system barycenter expressed in arc seconds per year. Here, declination refers to motion from the inertial equator measured towards the inertial positive Z-axis. Uses AngleRate Dimension.

.. py:property:: parallax
    :canonical: ansys.stk.core.stkobjects.Star.parallax
    :type: typing.Any

    Annual parallax: motion of a star due to changes in the Earth's position relative to the solar system barycenter. Uses Angle Dimension.

.. py:property:: epoch
    :canonical: ansys.stk.core.stkobjects.Star.epoch
    :type: str

    Epoch of the star position information as a Julian epoch (yyyy.yy). The Julian epoch is related to the Julian date by the expression JD = 2451545.0 + (yyyy.yy - 2000.0) x 365.25, where 2451545.0 (TT) represents the standard J2000 epoch.

.. py:property:: magnitude
    :canonical: ansys.stk.core.stkobjects.Star.magnitude
    :type: float

    Magnitude, the visual brightness of the star. Dimensionless.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.Star.graphics
    :type: StarGraphics

    Get the star's 2D Graphics properties.

.. py:property:: access_constraints
    :canonical: ansys.stk.core.stkobjects.Star.access_constraints
    :type: AccessConstraintCollection

    Get the constraints imposed on the star.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.Star.graphics_3d
    :type: StarGraphics3D

    Get the star's 3D Graphics properties.

.. py:property:: reference_frame
    :canonical: ansys.stk.core.stkobjects.Star.reference_frame
    :type: StarReferenceFrame

    Return a reference frame.

.. py:property:: proper_motion_radial_velocity
    :canonical: ansys.stk.core.stkobjects.Star.proper_motion_radial_velocity
    :type: float

    Property motion radial velocity. Uses Distance dimension.


