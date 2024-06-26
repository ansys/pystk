IElementMixedSpherical
======================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IElementMixedSpherical

   IElement
   
   Properties for Mixed Spherical elements.

.. py:currentmodule:: IElementMixedSpherical

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementMixedSpherical.longitude`
              - Measured from -180.0 deg to +360.0 deg. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementMixedSpherical.latitude`
              - Measured from -90.0 deg to +90.0 deg. The geodetic latitude of a point is the angle between (1) the normal to the reference ellipsoid that passes through the satellite position and (2) the equatorial plane. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementMixedSpherical.altitude`
              - Gets or sets the object's position above or below the reference ellipsoid. Altitude is measured along a normal to the surface of the reference ellipsoid. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementMixedSpherical.horizontal_flight_path_angle`
              - Horizontal (Hor FPA) or vertical (Ver FPA) flight path angle. The angle between the inertial velocity vector and the radius vector (vertical) or the complement of this angle (horizontal). Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementMixedSpherical.velocity_azimuth`
              - Gets or sets the angle in the satellite local horizontal plane between the projection of the inertial velocity vector onto this plane and the local north direction measured as positive in the clockwise direction. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementMixedSpherical.velocity_magnitude`
              - Gets or sets the angle in the satellite local horizontal plane between the projection of the inertial velocity vector onto this plane and the local north direction measured as positive in the clockwise direction. Uses Rate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementMixedSpherical.vertical_flight_path_angle`
              - Horizontal (Hor FPA) or vertical (Ver FPA) flight path angle. The angle between the inertial velocity vector and the radius vector (vertical) or the complement of this angle (horizontal). Uses Angle Dimension.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IElementMixedSpherical


Property detail
---------------

.. py:property:: longitude
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementMixedSpherical.longitude
    :type: typing.Any

    Measured from -180.0 deg to +360.0 deg. Uses Angle Dimension.

.. py:property:: latitude
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementMixedSpherical.latitude
    :type: typing.Any

    Measured from -90.0 deg to +90.0 deg. The geodetic latitude of a point is the angle between (1) the normal to the reference ellipsoid that passes through the satellite position and (2) the equatorial plane. Uses Angle Dimension.

.. py:property:: altitude
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementMixedSpherical.altitude
    :type: float

    Gets or sets the object's position above or below the reference ellipsoid. Altitude is measured along a normal to the surface of the reference ellipsoid. Uses Distance Dimension.

.. py:property:: horizontal_flight_path_angle
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementMixedSpherical.horizontal_flight_path_angle
    :type: typing.Any

    Horizontal (Hor FPA) or vertical (Ver FPA) flight path angle. The angle between the inertial velocity vector and the radius vector (vertical) or the complement of this angle (horizontal). Uses Angle Dimension.

.. py:property:: velocity_azimuth
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementMixedSpherical.velocity_azimuth
    :type: typing.Any

    Gets or sets the angle in the satellite local horizontal plane between the projection of the inertial velocity vector onto this plane and the local north direction measured as positive in the clockwise direction. Uses Angle Dimension.

.. py:property:: velocity_magnitude
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementMixedSpherical.velocity_magnitude
    :type: float

    Gets or sets the angle in the satellite local horizontal plane between the projection of the inertial velocity vector onto this plane and the local north direction measured as positive in the clockwise direction. Uses Rate Dimension.

.. py:property:: vertical_flight_path_angle
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementMixedSpherical.vertical_flight_path_angle
    :type: typing.Any

    Horizontal (Hor FPA) or vertical (Ver FPA) flight path angle. The angle between the inertial velocity vector and the radius vector (vertical) or the complement of this angle (horizontal). Uses Angle Dimension.


