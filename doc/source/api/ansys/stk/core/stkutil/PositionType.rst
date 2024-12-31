PositionType
============

.. py:class:: ansys.stk.core.stkutil.PositionType

   IntEnum


.. py:currentmodule:: PositionType

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~CARTESIAN`
              - Cartesian: position specified in terms of the X, Y and Z components of the object's position vector, where the Z-axis points to the North pole, and the X-axis crosses 0 degrees latitude/0 degrees longitude.

            * - :py:attr:`~CYLINDRICAL`
              - Cylindrical: position specified in terms of radius (polar), longitude (measured in degrees from -360.0 degrees to +360.0 degrees), and the Z component of the object's position vector.

            * - :py:attr:`~GEOCENTRIC`
              - Geocentric: position specified in terms of latitude (spherical latitude of the sub-point on the surface of the Earth), longitude and altitude.

            * - :py:attr:`~GEODETIC`
              - Geodetic: position specified in terms of latitude (angle between the normal to the reference ellipsoid and the equatorial plane), longitude and altitude.

            * - :py:attr:`~SPHERICAL`
              - Spherical: position specified in terms of latitude (spherical latitude of the sub-point on the surface of the Earth), longitude and radius (distance of the object from the center of the Earth).

            * - :py:attr:`~PLANETOCENTRIC`
              - Planetocentric: position specified in terms of latitude (spherical latitude of the sub-point on the surface of the Earth), longitude and altitude.

            * - :py:attr:`~PLANETODETIC`
              - Planetodetic: position specified in terms of latitude (angle between the normal to the reference ellipsoid and the equatorial plane), longitude and altitude.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkutil import PositionType


