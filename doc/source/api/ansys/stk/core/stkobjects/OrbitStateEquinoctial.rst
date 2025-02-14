OrbitStateEquinoctial
=====================

.. py:class:: ansys.stk.core.stkobjects.OrbitStateEquinoctial

   Bases: :py:class:`~ansys.stk.core.stkobjects.IOrbitState`

   Equinoctial coordinate type, which uses the center of the Earth as the origin and the plane of the satellite's orbit as the reference plane.

.. py:currentmodule:: OrbitStateEquinoctial

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateEquinoctial.coordinate_system_type`
              - Get or set the coordinate system being used.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateEquinoctial.coordinate_system`
              - Get the coordinate system and coordinate epoch.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateEquinoctial.size_shape_type`
              - Get or set the orbit size option can be Mean Motion or Semimajor Axis.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateEquinoctial.size_shape`
              - Get the value of Mean Motion or Semimajor Axis.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateEquinoctial.h`
              - H/K collectively describe the shape of the satellite's orbit and the position of perigee. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateEquinoctial.k`
              - H/K collectively describe the shape of the satellite's orbit and the position of perigee. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateEquinoctial.p`
              - P/Q collectively describe the orientation of the satellite's orbit plane. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateEquinoctial.q`
              - P/Q collectively describe the orientation of the satellite's orbit plane. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateEquinoctial.mean_longitude`
              - Specify a satellite's position within its orbit at epoch and equals the sum of the classical RAAN, Argument of Perigee, and Mean Anomaly. Uses Angle dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateEquinoctial.formulation`
              - Get or set the Formulation can be Retrograde or Posigrade.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateEquinoctial.supported_coordinate_system_types`
              - Return an array of supported coordinate system types.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateEquinoctial.state_epoch`
              - Smart epoch component allows the user to configure the state epoch explicitly or implicitly (using a pre-defined or custom time instant component).



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import OrbitStateEquinoctial


Property detail
---------------

.. py:property:: coordinate_system_type
    :canonical: ansys.stk.core.stkobjects.OrbitStateEquinoctial.coordinate_system_type
    :type: CoordinateSystem

    Get or set the coordinate system being used.

.. py:property:: coordinate_system
    :canonical: ansys.stk.core.stkobjects.OrbitStateEquinoctial.coordinate_system
    :type: OrbitStateCoordinateSystem

    Get the coordinate system and coordinate epoch.

.. py:property:: size_shape_type
    :canonical: ansys.stk.core.stkobjects.OrbitStateEquinoctial.size_shape_type
    :type: EquinoctialSizeShape

    Get or set the orbit size option can be Mean Motion or Semimajor Axis.

.. py:property:: size_shape
    :canonical: ansys.stk.core.stkobjects.OrbitStateEquinoctial.size_shape
    :type: IClassicalSizeShape

    Get the value of Mean Motion or Semimajor Axis.

.. py:property:: h
    :canonical: ansys.stk.core.stkobjects.OrbitStateEquinoctial.h
    :type: float

    H/K collectively describe the shape of the satellite's orbit and the position of perigee. Dimensionless.

.. py:property:: k
    :canonical: ansys.stk.core.stkobjects.OrbitStateEquinoctial.k
    :type: float

    H/K collectively describe the shape of the satellite's orbit and the position of perigee. Dimensionless.

.. py:property:: p
    :canonical: ansys.stk.core.stkobjects.OrbitStateEquinoctial.p
    :type: float

    P/Q collectively describe the orientation of the satellite's orbit plane. Dimensionless.

.. py:property:: q
    :canonical: ansys.stk.core.stkobjects.OrbitStateEquinoctial.q
    :type: float

    P/Q collectively describe the orientation of the satellite's orbit plane. Dimensionless.

.. py:property:: mean_longitude
    :canonical: ansys.stk.core.stkobjects.OrbitStateEquinoctial.mean_longitude
    :type: float

    Specify a satellite's position within its orbit at epoch and equals the sum of the classical RAAN, Argument of Perigee, and Mean Anomaly. Uses Angle dimension.

.. py:property:: formulation
    :canonical: ansys.stk.core.stkobjects.OrbitStateEquinoctial.formulation
    :type: EquinoctialFormulation

    Get or set the Formulation can be Retrograde or Posigrade.

.. py:property:: supported_coordinate_system_types
    :canonical: ansys.stk.core.stkobjects.OrbitStateEquinoctial.supported_coordinate_system_types
    :type: list

    Return an array of supported coordinate system types.

.. py:property:: state_epoch
    :canonical: ansys.stk.core.stkobjects.OrbitStateEquinoctial.state_epoch
    :type: ITimeToolInstantSmartEpoch

    Smart epoch component allows the user to configure the state epoch explicitly or implicitly (using a pre-defined or custom time instant component).


