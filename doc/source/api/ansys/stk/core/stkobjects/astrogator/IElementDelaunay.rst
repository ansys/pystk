IElementDelaunay
================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IElementDelaunay

   IElement
   
   Properties for Delaunay elements.

.. py:currentmodule:: IElementDelaunay

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementDelaunay.mean_anomaly`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementDelaunay.arg_of_periapsis`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementDelaunay.raan`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementDelaunay.delaunay_l`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementDelaunay.semi_major_axis`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementDelaunay.delaunay_g`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementDelaunay.semilatus_rectum`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementDelaunay.delaunay_h`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IElementDelaunay.inclination`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IElementDelaunay


Property detail
---------------

.. py:property:: mean_anomaly
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementDelaunay.mean_anomaly
    :type: typing.Any

    Gets or sets the angle from the eccentricity vector to a position vector where the satellite would be if it were always moving at its average angular rate (l). Uses Angle Dimension.

.. py:property:: arg_of_periapsis
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementDelaunay.arg_of_periapsis
    :type: typing.Any

    Gets or sets the angle from the ascending node to the eccentricity vector (lowest point of orbit) measured in the direction of the satellite's motion and in the orbit plane (g). Uses Angle Dimension.

.. py:property:: raan
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementDelaunay.raan
    :type: typing.Any

    Gets or sets the angle from the inertial X axis to the ascending node measured in a right-handed sense about the inertial Z axis in the equatorial plane (h). Uses Angle Dimension.

.. py:property:: delaunay_l
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementDelaunay.delaunay_l
    :type: float

    Related to the two-body orbital energy. Defined as sqrt(GM * a).   Uses AreaRate Dimension.

.. py:property:: semi_major_axis
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementDelaunay.semi_major_axis
    :type: float

    One-half the distance along the long axis of the elliptical orbit. Uses Distance Dimension.

.. py:property:: delaunay_g
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementDelaunay.delaunay_g
    :type: float

    Gets or sets the magnitude of the orbital angular momentum. Defined as sqrt(GM * p). Uses AreaRate Dimension.

.. py:property:: semilatus_rectum
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementDelaunay.semilatus_rectum
    :type: float

    Semi-latus Rectum. Uses Distance Dimension.

.. py:property:: delaunay_h
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementDelaunay.delaunay_h
    :type: float

    Gets or sets the Z component of the orbital angular momentum. Defined as G cos(inc).  Uses AreaRate Dimension.

.. py:property:: inclination
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementDelaunay.inclination
    :type: typing.Any

    Gets or sets the angle between the angular momentum vector (perpendicular to the plane of the orbit) and the inertial Z axis. Uses Angle Dimension.


