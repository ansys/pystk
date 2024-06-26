IVehicleEllipseDataElement
==========================

.. py:class:: ansys.stk.core.stkobjects.IVehicleEllipseDataElement

   object
   
   Ground ellipse data.

.. py:currentmodule:: IVehicleEllipseDataElement

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEllipseDataElement.time`
              - Time of the ellipse. Uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEllipseDataElement.custom_position`
              - Opt whether to specify a custom position for the center of the ellipse. Otherwise the object's center is used.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEllipseDataElement.latitude`
              - Gets or sets the latitude of the center of the ellipse. Read-only unless you opt to specify a custom position. Uses Latitude Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEllipseDataElement.longitude`
              - Gets or sets the longitude of the center of the ellipse. Read-only unless you opt to specify a custom position. Uses Longitude Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEllipseDataElement.semi_major_axis`
              - Gets or sets the semimajor axis of the ellipse. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEllipseDataElement.semi_minor_axis`
              - Gets or sets the semiminor axis of the ellipse. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEllipseDataElement.bearing`
              - Gets or sets the bearing of the ellipse: the angle, measured in an easterly direction, between the major axis and the local North direction. Uses Angle Dimension.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleEllipseDataElement


Property detail
---------------

.. py:property:: time
    :canonical: ansys.stk.core.stkobjects.IVehicleEllipseDataElement.time
    :type: typing.Any

    Time of the ellipse. Uses DateFormat Dimension.

.. py:property:: custom_position
    :canonical: ansys.stk.core.stkobjects.IVehicleEllipseDataElement.custom_position
    :type: bool

    Opt whether to specify a custom position for the center of the ellipse. Otherwise the object's center is used.

.. py:property:: latitude
    :canonical: ansys.stk.core.stkobjects.IVehicleEllipseDataElement.latitude
    :type: typing.Any

    Gets or sets the latitude of the center of the ellipse. Read-only unless you opt to specify a custom position. Uses Latitude Dimension.

.. py:property:: longitude
    :canonical: ansys.stk.core.stkobjects.IVehicleEllipseDataElement.longitude
    :type: typing.Any

    Gets or sets the longitude of the center of the ellipse. Read-only unless you opt to specify a custom position. Uses Longitude Dimension.

.. py:property:: semi_major_axis
    :canonical: ansys.stk.core.stkobjects.IVehicleEllipseDataElement.semi_major_axis
    :type: float

    Gets or sets the semimajor axis of the ellipse. Uses Distance Dimension.

.. py:property:: semi_minor_axis
    :canonical: ansys.stk.core.stkobjects.IVehicleEllipseDataElement.semi_minor_axis
    :type: float

    Gets or sets the semiminor axis of the ellipse. Uses Distance Dimension.

.. py:property:: bearing
    :canonical: ansys.stk.core.stkobjects.IVehicleEllipseDataElement.bearing
    :type: typing.Any

    Gets or sets the bearing of the ellipse: the angle, measured in an easterly direction, between the major axis and the local North direction. Uses Angle Dimension.


