IStar
=====

.. py:class:: IStar

   object
   
   Provide access to the properties and methods used in defining a star object.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~location_right_ascension`
            * - :py:meth:`~location_declination`
            * - :py:meth:`~proper_motion_right_ascension`
            * - :py:meth:`~proper_motion_declination`
            * - :py:meth:`~parallax`
            * - :py:meth:`~epoch`
            * - :py:meth:`~magnitude`
            * - :py:meth:`~graphics`
            * - :py:meth:`~access_constraints`
            * - :py:meth:`~graphics_3d`
            * - :py:meth:`~reference_frame`
            * - :py:meth:`~proper_motion_radial_velocity`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IStar


Property detail
---------------

.. py:property:: location_right_ascension
    :canonical: ansys.stk.core.stkobjects.IStar.location_right_ascension
    :type: typing.Any

    The star's right ascension: the angle in the equatorial plane measured in a right-handed sense about the inertial Z-axis from the inertial X-axis. Uses Angle Dimension.

.. py:property:: location_declination
    :canonical: ansys.stk.core.stkobjects.IStar.location_declination
    :type: typing.Any

    The star's declination: the angle from the inertial equator measured toward the inertial positive Z-axis. Uses Angle Dimension.

.. py:property:: proper_motion_right_ascension
    :canonical: ansys.stk.core.stkobjects.IStar.proper_motion_right_ascension
    :type: float

    Motion of star relative to solar system barycenter expressed in arc seconds per year. Here, right ascension refers to motion in equatorial plane measured in a right-handed sense about the inertial Z-axis from inertial X-axis. Uses AngleRate Dimension.

.. py:property:: proper_motion_declination
    :canonical: ansys.stk.core.stkobjects.IStar.proper_motion_declination
    :type: float

    Motion of the star relative to the solar system barycenter expressed in arc seconds per year. Here, declination refers to motion from the inertial equator measured towards the inertial positive Z-axis. Uses AngleRate Dimension.

.. py:property:: parallax
    :canonical: ansys.stk.core.stkobjects.IStar.parallax
    :type: typing.Any

    Annual parallax: motion of a star due to changes in the Earth's position relative to the solar system barycenter. Uses Angle Dimension.

.. py:property:: epoch
    :canonical: ansys.stk.core.stkobjects.IStar.epoch
    :type: str

    Epoch of the star position information as a Julian epoch (yyyy.yy). The Julian epoch is related to the Julian date by the expression JD = 2451545.0 + (yyyy.yy - 2000.0) x 365.25, where 2451545.0 (TT) represents the standard J2000 epoch.

.. py:property:: magnitude
    :canonical: ansys.stk.core.stkobjects.IStar.magnitude
    :type: float

    Magnitude, the visual brightness of the star. Dimensionless.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.IStar.graphics
    :type: IAgStGraphics

    Get the star's 2D Graphics properties.

.. py:property:: access_constraints
    :canonical: ansys.stk.core.stkobjects.IStar.access_constraints
    :type: IAgAccessConstraintCollection

    Get the constraints imposed on the star.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.IStar.graphics_3d
    :type: IAgStVO

    Get the star's 3D Graphics properties.

.. py:property:: reference_frame
    :canonical: ansys.stk.core.stkobjects.IStar.reference_frame
    :type: STAR_REFERENCE_FRAME

    Returns a reference frame.

.. py:property:: proper_motion_radial_velocity
    :canonical: ansys.stk.core.stkobjects.IStar.proper_motion_radial_velocity
    :type: float

    Property motion radial velocity. Uses Distance dimension.


