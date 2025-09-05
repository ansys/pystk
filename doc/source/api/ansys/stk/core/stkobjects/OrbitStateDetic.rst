OrbitStateDetic
===============

.. py:class:: ansys.stk.core.stkobjects.OrbitStateDetic

   Bases: :py:class:`~ansys.stk.core.stkobjects.IOrbitState`

   Geodetic coordinate type (available only with a Fixed coordinate system).

.. py:currentmodule:: OrbitStateDetic

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateDetic.coordinate_system`
              - Get the coordinate system and coordinate epoch. Note that with the Fixed coordinate system (required for the Geodetic coordinate type), the coordinate epoch is preset.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateDetic.coordinate_system_type`
              - Get or set the coordinate system being used. Note that the Geodetic coordinate type is available only if a Fixed coordinate system is selected.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateDetic.latitude`
              - Get or set the angle between the normal to the reference ellipsoid and the equatorial plane. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateDetic.latitude_rate`
              - Get or set the rate of change in latitude. Uses AngleRate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateDetic.longitude`
              - Get or set the angle between the projection of the position vector in the equatorial plane and the prime meridian. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateDetic.longitude_rate`
              - Get or set the rate of change in longitude. Uses AngleRate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateDetic.size`
              - Get the value of the altitude or radius.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateDetic.size_type`
              - Get or set the element (altitude or radius) used to specify size.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateDetic.state_epoch`
              - Smart epoch component allows the user to configure the state epoch explicitly or implicitly (using a pre-defined or custom time instant component).
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateDetic.supported_coordinate_system_types`
              - Return an array of supported coordinate system types.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import OrbitStateDetic


Property detail
---------------

.. py:property:: coordinate_system
    :canonical: ansys.stk.core.stkobjects.OrbitStateDetic.coordinate_system
    :type: OrbitStateCoordinateSystem

    Get the coordinate system and coordinate epoch. Note that with the Fixed coordinate system (required for the Geodetic coordinate type), the coordinate epoch is preset.

.. py:property:: coordinate_system_type
    :canonical: ansys.stk.core.stkobjects.OrbitStateDetic.coordinate_system_type
    :type: CoordinateSystem

    Get or set the coordinate system being used. Note that the Geodetic coordinate type is available only if a Fixed coordinate system is selected.

.. py:property:: latitude
    :canonical: ansys.stk.core.stkobjects.OrbitStateDetic.latitude
    :type: float

    Get or set the angle between the normal to the reference ellipsoid and the equatorial plane. Uses Angle Dimension.

.. py:property:: latitude_rate
    :canonical: ansys.stk.core.stkobjects.OrbitStateDetic.latitude_rate
    :type: float

    Get or set the rate of change in latitude. Uses AngleRate Dimension.

.. py:property:: longitude
    :canonical: ansys.stk.core.stkobjects.OrbitStateDetic.longitude
    :type: float

    Get or set the angle between the projection of the position vector in the equatorial plane and the prime meridian. Uses Angle Dimension.

.. py:property:: longitude_rate
    :canonical: ansys.stk.core.stkobjects.OrbitStateDetic.longitude_rate
    :type: float

    Get or set the rate of change in longitude. Uses AngleRate Dimension.

.. py:property:: size
    :canonical: ansys.stk.core.stkobjects.OrbitStateDetic.size
    :type: IGeodeticSize

    Get the value of the altitude or radius.

.. py:property:: size_type
    :canonical: ansys.stk.core.stkobjects.OrbitStateDetic.size_type
    :type: GeodeticSize

    Get or set the element (altitude or radius) used to specify size.

.. py:property:: state_epoch
    :canonical: ansys.stk.core.stkobjects.OrbitStateDetic.state_epoch
    :type: ITimeToolInstantSmartEpoch

    Smart epoch component allows the user to configure the state epoch explicitly or implicitly (using a pre-defined or custom time instant component).

.. py:property:: supported_coordinate_system_types
    :canonical: ansys.stk.core.stkobjects.OrbitStateDetic.supported_coordinate_system_types
    :type: list

    Return an array of supported coordinate system types.


