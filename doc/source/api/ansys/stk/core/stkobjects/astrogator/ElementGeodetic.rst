ElementGeodetic
===============

.. py:class:: ansys.stk.core.stkobjects.astrogator.ElementGeodetic

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IElement`

   Geodetic elements.

.. py:currentmodule:: ElementGeodetic

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementGeodetic.altitude`
              - Measured along an outward normal to the surface of the ellipsoid. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementGeodetic.altitude_rate`
              - Get or set the rate of change of the altitude. Uses Rate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementGeodetic.latitude`
              - Measured in degrees from -90.0 deg to +90.0 deg. The geodetic latitude of a point is the angle between the normal to the reference ellipsoid and the equatorial plane. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementGeodetic.latitude_rate`
              - Get or set the rate of change of the satellite's latitude. Uses Rate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementGeodetic.longitude`
              - Measured in degrees from -360.0 deg to +360.0 deg. The longitude of a point is the angle between the projection of the position vector in the equatorial plane and the prime meridian. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementGeodetic.longitude_rate`
              - Get or set the rate of change of the satellite's longitude. Uses Rate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementGeodetic.radius_magnitude`
              - Measured from the center of the Earth. Specified as distance above or below the reference ellipsoid. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementGeodetic.radius_rate`
              - Get or set the rate of change of the radius. Uses Rate Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ElementGeodetic


Property detail
---------------

.. py:property:: altitude
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementGeodetic.altitude
    :type: float

    Measured along an outward normal to the surface of the ellipsoid. Uses Distance Dimension.

.. py:property:: altitude_rate
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementGeodetic.altitude_rate
    :type: float

    Get or set the rate of change of the altitude. Uses Rate Dimension.

.. py:property:: latitude
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementGeodetic.latitude
    :type: typing.Any

    Measured in degrees from -90.0 deg to +90.0 deg. The geodetic latitude of a point is the angle between the normal to the reference ellipsoid and the equatorial plane. Uses Angle Dimension.

.. py:property:: latitude_rate
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementGeodetic.latitude_rate
    :type: float

    Get or set the rate of change of the satellite's latitude. Uses Rate Dimension.

.. py:property:: longitude
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementGeodetic.longitude
    :type: typing.Any

    Measured in degrees from -360.0 deg to +360.0 deg. The longitude of a point is the angle between the projection of the position vector in the equatorial plane and the prime meridian. Uses Angle Dimension.

.. py:property:: longitude_rate
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementGeodetic.longitude_rate
    :type: float

    Get or set the rate of change of the satellite's longitude. Uses Rate Dimension.

.. py:property:: radius_magnitude
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementGeodetic.radius_magnitude
    :type: float

    Measured from the center of the Earth. Specified as distance above or below the reference ellipsoid. Uses Distance Dimension.

.. py:property:: radius_rate
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementGeodetic.radius_rate
    :type: float

    Get or set the rate of change of the radius. Uses Rate Dimension.


