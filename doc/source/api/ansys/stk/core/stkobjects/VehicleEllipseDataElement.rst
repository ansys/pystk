VehicleEllipseDataElement
=========================

.. py:class:: ansys.stk.core.stkobjects.VehicleEllipseDataElement

   Ground ellipse data.

.. py:currentmodule:: VehicleEllipseDataElement

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEllipseDataElement.time`
              - Time of the ellipse. Uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEllipseDataElement.custom_position`
              - Opt whether to specify a custom position for the center of the ellipse. Otherwise the object's center is used.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEllipseDataElement.latitude`
              - Get or set the latitude of the center of the ellipse. Read-only unless you opt to specify a custom position. Uses Latitude Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEllipseDataElement.longitude`
              - Get or set the longitude of the center of the ellipse. Read-only unless you opt to specify a custom position. Uses Longitude Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEllipseDataElement.semi_major_axis`
              - Get or set the semimajor axis of the ellipse. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEllipseDataElement.semi_minor_axis`
              - Get or set the semiminor axis of the ellipse. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEllipseDataElement.bearing`
              - Get or set the bearing of the ellipse: the angle, measured in an easterly direction, between the major axis and the local North direction. Uses Angle Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleEllipseDataElement


Property detail
---------------

.. py:property:: time
    :canonical: ansys.stk.core.stkobjects.VehicleEllipseDataElement.time
    :type: typing.Any

    Time of the ellipse. Uses DateFormat Dimension.

.. py:property:: custom_position
    :canonical: ansys.stk.core.stkobjects.VehicleEllipseDataElement.custom_position
    :type: bool

    Opt whether to specify a custom position for the center of the ellipse. Otherwise the object's center is used.

.. py:property:: latitude
    :canonical: ansys.stk.core.stkobjects.VehicleEllipseDataElement.latitude
    :type: typing.Any

    Get or set the latitude of the center of the ellipse. Read-only unless you opt to specify a custom position. Uses Latitude Dimension.

.. py:property:: longitude
    :canonical: ansys.stk.core.stkobjects.VehicleEllipseDataElement.longitude
    :type: typing.Any

    Get or set the longitude of the center of the ellipse. Read-only unless you opt to specify a custom position. Uses Longitude Dimension.

.. py:property:: semi_major_axis
    :canonical: ansys.stk.core.stkobjects.VehicleEllipseDataElement.semi_major_axis
    :type: float

    Get or set the semimajor axis of the ellipse. Uses Distance Dimension.

.. py:property:: semi_minor_axis
    :canonical: ansys.stk.core.stkobjects.VehicleEllipseDataElement.semi_minor_axis
    :type: float

    Get or set the semiminor axis of the ellipse. Uses Distance Dimension.

.. py:property:: bearing
    :canonical: ansys.stk.core.stkobjects.VehicleEllipseDataElement.bearing
    :type: typing.Any

    Get or set the bearing of the ellipse: the angle, measured in an easterly direction, between the major axis and the local North direction. Uses Angle Dimension.


