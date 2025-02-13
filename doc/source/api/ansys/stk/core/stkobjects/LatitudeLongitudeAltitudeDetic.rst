LatitudeLongitudeAltitudeDetic
==============================

.. py:class:: ansys.stk.core.stkobjects.LatitudeLongitudeAltitudeDetic

   Bases: :py:class:`~ansys.stk.core.stkobjects.ILatitudeLongitudeAltitudePosition`

   Geodetic LLA position.

.. py:currentmodule:: LatitudeLongitudeAltitudeDetic

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.LatitudeLongitudeAltitudeDetic.latitude`
              - Latitude: angle above the x-y plane. Uses Latitude Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.LatitudeLongitudeAltitudeDetic.longitude`
              - Longitude: angle in x-y plane from x towards y. Uses Longitude Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.LatitudeLongitudeAltitudeDetic.altitude`
              - Altitude measured along the normal to the surface of an ellipsoid defined with reference to the central body. Uses Distance Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import LatitudeLongitudeAltitudeDetic


Property detail
---------------

.. py:property:: latitude
    :canonical: ansys.stk.core.stkobjects.LatitudeLongitudeAltitudeDetic.latitude
    :type: float

    Latitude: angle above the x-y plane. Uses Latitude Dimension.

.. py:property:: longitude
    :canonical: ansys.stk.core.stkobjects.LatitudeLongitudeAltitudeDetic.longitude
    :type: float

    Longitude: angle in x-y plane from x towards y. Uses Longitude Dimension.

.. py:property:: altitude
    :canonical: ansys.stk.core.stkobjects.LatitudeLongitudeAltitudeDetic.altitude
    :type: float

    Altitude measured along the normal to the surface of an ellipsoid defined with reference to the central body. Uses Distance Dimension.


