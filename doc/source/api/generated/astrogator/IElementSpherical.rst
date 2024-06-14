IElementSpherical
=================

.. py:class:: IElementSpherical

   IElement
   
   Properties for Spherical elements.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~right_ascension`
            * - :py:meth:`~declination`
            * - :py:meth:`~radius_magnitude`
            * - :py:meth:`~horizontal_flight_path_angle`
            * - :py:meth:`~velocity_azimuth`
            * - :py:meth:`~velocity_magnitude`
            * - :py:meth:`~vertical_flight_path_angle`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IElementSpherical


Property detail
---------------

.. py:property:: right_ascension
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementSpherical.right_ascension
    :type: typing.Any

    Defined as the angle from the X axis to the projection of the satellite position vector in the equatorial plane measured as positive in the direction of the Y axis. Uses Angle Dimension.

.. py:property:: declination
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementSpherical.declination
    :type: typing.Any

    Defined as the angle between the satellite position vector and the inertial equatorial plane measured as positive toward the positive inertial Z axis. Uses Angle Dimension.

.. py:property:: radius_magnitude
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementSpherical.radius_magnitude
    :type: float

    Gets or sets the magnitude of the satellite position vector. Uses Distance Dimension.

.. py:property:: horizontal_flight_path_angle
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementSpherical.horizontal_flight_path_angle
    :type: typing.Any

    Horizontal (Hor FPA) or vertical (Ver FPA) flight path angle. The angle between the velocity vector and the radius vector (vertical) or the complement of this angle (horizontal). Uses Angle Dimension.

.. py:property:: velocity_azimuth
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementSpherical.velocity_azimuth
    :type: typing.Any

    Gets or sets the angle in the satellite local horizontal plane between the projection of the velocity vector onto this plane and the local north direction measured as positive in the clockwise direction. Uses Angle Dimension.

.. py:property:: velocity_magnitude
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementSpherical.velocity_magnitude
    :type: float

    Gets or sets the magnitude of the velocity vector. Uses Rate Dimension.

.. py:property:: vertical_flight_path_angle
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementSpherical.vertical_flight_path_angle
    :type: typing.Any

    Horizontal (Hor FPA) or vertical (Ver FPA) flight path angle. The angle between the velocity vector and the radius vector (vertical) or the complement of this angle (horizontal). Uses Angle Dimension.


