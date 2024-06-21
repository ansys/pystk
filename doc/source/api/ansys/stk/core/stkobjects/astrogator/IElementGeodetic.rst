IElementGeodetic
================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IElementGeodetic

   IElement
   
   Properties for Geodetic elements.

.. py:currentmodule:: IElementGeodetic

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementGeodetic.latitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementGeodetic.longitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementGeodetic.altitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementGeodetic.radius_magnitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementGeodetic.latitude_rate`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementGeodetic.longitude_rate`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementGeodetic.altitude_rate`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementGeodetic.radius_rate`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IElementGeodetic


Property detail
---------------

.. py:property:: latitude
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementGeodetic.latitude
    :type: typing.Any

    Measured in degrees from -90.0 deg to +90.0 deg. The geodetic latitude of a point is the angle between the normal to the reference ellipsoid and the equatorial plane. Uses Angle Dimension.

.. py:property:: longitude
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementGeodetic.longitude
    :type: typing.Any

    Measured in degrees from -360.0 deg to +360.0 deg. The longitude of a point is the angle between the projection of the position vector in the equatorial plane and the prime meridian. Uses Angle Dimension.

.. py:property:: altitude
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementGeodetic.altitude
    :type: float

    Measured along an outward normal to the surface of the ellipsoid. Uses Distance Dimension.

.. py:property:: radius_magnitude
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementGeodetic.radius_magnitude
    :type: float

    Measured from the center of the Earth. Specified as distance above or below the reference ellipsoid. Uses Distance Dimension.

.. py:property:: latitude_rate
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementGeodetic.latitude_rate
    :type: float

    Gets or sets the rate of change of the satellite's latitude. Uses Rate Dimension.

.. py:property:: longitude_rate
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementGeodetic.longitude_rate
    :type: float

    Gets or sets the rate of change of the satellite's longitude. Uses Rate Dimension.

.. py:property:: altitude_rate
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementGeodetic.altitude_rate
    :type: float

    Gets or sets the rate of change of the altitude. Uses Rate Dimension.

.. py:property:: radius_rate
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementGeodetic.radius_rate
    :type: float

    Gets or sets the rate of change of the radius. Uses Rate Dimension.


