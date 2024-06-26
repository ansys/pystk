IOrbitStateGeodetic
===================

.. py:class:: ansys.stk.core.stkobjects.IOrbitStateGeodetic

   IOrbitState
   
   Geodetic coordinate type (available only with a Fixed coordinate system).

.. py:currentmodule:: IOrbitStateGeodetic

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateGeodetic.coordinate_system_type`
              - Gets or sets the coordinate system being used. Note that the Geodetic coordinate type is available only if a Fixed coordinate system is selected.
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateGeodetic.coordinate_system`
              - Get the coordinate system and coordinate epoch. Note that with the Fixed coordinate system (required for the Geodetic coordinate type), the coordinate epoch is preset.
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateGeodetic.size_type`
              - Gets or sets the element (altitude or radius) used to specify size.
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateGeodetic.size`
              - Get the value of the altitude or radius.
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateGeodetic.latitude`
              - Gets or sets the angle between the normal to the reference ellipsoid and the equatorial plane. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateGeodetic.longitude`
              - Gets or sets the angle between the projection of the position vector in the equatorial plane and the prime meridian. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateGeodetic.latitude_rate`
              - Gets or sets the rate of change in latitude. Uses AngleRate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateGeodetic.longitude_rate`
              - Gets or sets the rate of change in longitude. Uses AngleRate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateGeodetic.supported_coordinate_system_types`
              - Returns an array of supported coordinate system types.
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateGeodetic.state_epoch`
              - Smart epoch component allows the user to configure the state epoch explicitly or implicitly (using a pre-defined or custom time instant component).


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IOrbitStateGeodetic


Property detail
---------------

.. py:property:: coordinate_system_type
    :canonical: ansys.stk.core.stkobjects.IOrbitStateGeodetic.coordinate_system_type
    :type: COORDINATE_SYSTEM

    Gets or sets the coordinate system being used. Note that the Geodetic coordinate type is available only if a Fixed coordinate system is selected.

.. py:property:: coordinate_system
    :canonical: ansys.stk.core.stkobjects.IOrbitStateGeodetic.coordinate_system
    :type: IOrbitStateCoordinateSystem

    Get the coordinate system and coordinate epoch. Note that with the Fixed coordinate system (required for the Geodetic coordinate type), the coordinate epoch is preset.

.. py:property:: size_type
    :canonical: ansys.stk.core.stkobjects.IOrbitStateGeodetic.size_type
    :type: GEODETIC_SIZE

    Gets or sets the element (altitude or radius) used to specify size.

.. py:property:: size
    :canonical: ansys.stk.core.stkobjects.IOrbitStateGeodetic.size
    :type: IGeodeticSize

    Get the value of the altitude or radius.

.. py:property:: latitude
    :canonical: ansys.stk.core.stkobjects.IOrbitStateGeodetic.latitude
    :type: float

    Gets or sets the angle between the normal to the reference ellipsoid and the equatorial plane. Uses Angle Dimension.

.. py:property:: longitude
    :canonical: ansys.stk.core.stkobjects.IOrbitStateGeodetic.longitude
    :type: float

    Gets or sets the angle between the projection of the position vector in the equatorial plane and the prime meridian. Uses Angle Dimension.

.. py:property:: latitude_rate
    :canonical: ansys.stk.core.stkobjects.IOrbitStateGeodetic.latitude_rate
    :type: float

    Gets or sets the rate of change in latitude. Uses AngleRate Dimension.

.. py:property:: longitude_rate
    :canonical: ansys.stk.core.stkobjects.IOrbitStateGeodetic.longitude_rate
    :type: float

    Gets or sets the rate of change in longitude. Uses AngleRate Dimension.

.. py:property:: supported_coordinate_system_types
    :canonical: ansys.stk.core.stkobjects.IOrbitStateGeodetic.supported_coordinate_system_types
    :type: list

    Returns an array of supported coordinate system types.

.. py:property:: state_epoch
    :canonical: ansys.stk.core.stkobjects.IOrbitStateGeodetic.state_epoch
    :type: ITimeToolEventSmartEpoch

    Smart epoch component allows the user to configure the state epoch explicitly or implicitly (using a pre-defined or custom time instant component).


