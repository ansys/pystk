ElementSpherical
================

.. py:class:: ansys.stk.core.stkobjects.astrogator.ElementSpherical

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IElement`

   Spherical elements.

.. py:currentmodule:: ElementSpherical

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementSpherical.right_ascension`
              - Defined as the angle from the X axis to the projection of the satellite position vector in the equatorial plane measured as positive in the direction of the Y axis. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementSpherical.declination`
              - Defined as the angle between the satellite position vector and the inertial equatorial plane measured as positive toward the positive inertial Z axis. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementSpherical.radius_magnitude`
              - Gets or sets the magnitude of the satellite position vector. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementSpherical.horizontal_flight_path_angle`
              - Horizontal (Hor FPA) or vertical (Ver FPA) flight path angle. The angle between the velocity vector and the radius vector (vertical) or the complement of this angle (horizontal). Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementSpherical.velocity_azimuth`
              - Gets or sets the angle in the satellite local horizontal plane between the projection of the velocity vector onto this plane and the local north direction measured as positive in the clockwise direction. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementSpherical.velocity_magnitude`
              - Gets or sets the magnitude of the velocity vector. Uses Rate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementSpherical.vertical_flight_path_angle`
              - Horizontal (Hor FPA) or vertical (Ver FPA) flight path angle. The angle between the velocity vector and the radius vector (vertical) or the complement of this angle (horizontal). Uses Angle Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ElementSpherical


Property detail
---------------

.. py:property:: right_ascension
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementSpherical.right_ascension
    :type: typing.Any

    Defined as the angle from the X axis to the projection of the satellite position vector in the equatorial plane measured as positive in the direction of the Y axis. Uses Angle Dimension.

.. py:property:: declination
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementSpherical.declination
    :type: typing.Any

    Defined as the angle between the satellite position vector and the inertial equatorial plane measured as positive toward the positive inertial Z axis. Uses Angle Dimension.

.. py:property:: radius_magnitude
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementSpherical.radius_magnitude
    :type: float

    Gets or sets the magnitude of the satellite position vector. Uses Distance Dimension.

.. py:property:: horizontal_flight_path_angle
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementSpherical.horizontal_flight_path_angle
    :type: typing.Any

    Horizontal (Hor FPA) or vertical (Ver FPA) flight path angle. The angle between the velocity vector and the radius vector (vertical) or the complement of this angle (horizontal). Uses Angle Dimension.

.. py:property:: velocity_azimuth
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementSpherical.velocity_azimuth
    :type: typing.Any

    Gets or sets the angle in the satellite local horizontal plane between the projection of the velocity vector onto this plane and the local north direction measured as positive in the clockwise direction. Uses Angle Dimension.

.. py:property:: velocity_magnitude
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementSpherical.velocity_magnitude
    :type: float

    Gets or sets the magnitude of the velocity vector. Uses Rate Dimension.

.. py:property:: vertical_flight_path_angle
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementSpherical.vertical_flight_path_angle
    :type: typing.Any

    Horizontal (Hor FPA) or vertical (Ver FPA) flight path angle. The angle between the velocity vector and the radius vector (vertical) or the complement of this angle (horizontal). Uses Angle Dimension.


