ElementDelaunay
===============

.. py:class:: ansys.stk.core.stkobjects.astrogator.ElementDelaunay

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IElement`

   Delaunay elements.

.. py:currentmodule:: ElementDelaunay

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementDelaunay.mean_anomaly`
              - Gets or sets the angle from the eccentricity vector to a position vector where the satellite would be if it were always moving at its average angular rate (l). Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementDelaunay.arg_of_periapsis`
              - Gets or sets the angle from the ascending node to the eccentricity vector (lowest point of orbit) measured in the direction of the satellite's motion and in the orbit plane (g). Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementDelaunay.raan`
              - Gets or sets the angle from the inertial X axis to the ascending node measured in a right-handed sense about the inertial Z axis in the equatorial plane (h). Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementDelaunay.delaunay_l`
              - Related to the two-body orbital energy. Defined as sqrt(GM * a).   Uses AreaRate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementDelaunay.semi_major_axis`
              - One-half the distance along the long axis of the elliptical orbit. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementDelaunay.delaunay_g`
              - Gets or sets the magnitude of the orbital angular momentum. Defined as sqrt(GM * p). Uses AreaRate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementDelaunay.semilatus_rectum`
              - Semi-latus Rectum. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementDelaunay.delaunay_h`
              - Gets or sets the Z component of the orbital angular momentum. Defined as G cos(inc).  Uses AreaRate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementDelaunay.inclination`
              - Gets or sets the angle between the angular momentum vector (perpendicular to the plane of the orbit) and the inertial Z axis. Uses Angle Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ElementDelaunay


Property detail
---------------

.. py:property:: mean_anomaly
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementDelaunay.mean_anomaly
    :type: typing.Any

    Gets or sets the angle from the eccentricity vector to a position vector where the satellite would be if it were always moving at its average angular rate (l). Uses Angle Dimension.

.. py:property:: arg_of_periapsis
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementDelaunay.arg_of_periapsis
    :type: typing.Any

    Gets or sets the angle from the ascending node to the eccentricity vector (lowest point of orbit) measured in the direction of the satellite's motion and in the orbit plane (g). Uses Angle Dimension.

.. py:property:: raan
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementDelaunay.raan
    :type: typing.Any

    Gets or sets the angle from the inertial X axis to the ascending node measured in a right-handed sense about the inertial Z axis in the equatorial plane (h). Uses Angle Dimension.

.. py:property:: delaunay_l
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementDelaunay.delaunay_l
    :type: float

    Related to the two-body orbital energy. Defined as sqrt(GM * a).   Uses AreaRate Dimension.

.. py:property:: semi_major_axis
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementDelaunay.semi_major_axis
    :type: float

    One-half the distance along the long axis of the elliptical orbit. Uses Distance Dimension.

.. py:property:: delaunay_g
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementDelaunay.delaunay_g
    :type: float

    Gets or sets the magnitude of the orbital angular momentum. Defined as sqrt(GM * p). Uses AreaRate Dimension.

.. py:property:: semilatus_rectum
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementDelaunay.semilatus_rectum
    :type: float

    Semi-latus Rectum. Uses Distance Dimension.

.. py:property:: delaunay_h
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementDelaunay.delaunay_h
    :type: float

    Gets or sets the Z component of the orbital angular momentum. Defined as G cos(inc).  Uses AreaRate Dimension.

.. py:property:: inclination
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementDelaunay.inclination
    :type: typing.Any

    Gets or sets the angle between the angular momentum vector (perpendicular to the plane of the orbit) and the inertial Z axis. Uses Angle Dimension.


