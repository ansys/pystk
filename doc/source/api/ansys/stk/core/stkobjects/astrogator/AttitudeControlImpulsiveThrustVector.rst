AttitudeControlImpulsiveThrustVector
====================================

.. py:class:: ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveThrustVector

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsive`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControl`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The thrust vector attitude control for an impulsive maneuver.

.. py:currentmodule:: AttitudeControlImpulsiveThrustVector

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveThrustVector.assign_cartesian`
              - Assign all three Cartesian components of the DeltaV vector (dimension: SmallDistance/Time).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveThrustVector.query_cartesian`
              - Get all three Cartesian components of the DeltaV vector as an array (dimension: SmallDistance/Time).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveThrustVector.assign_spherical`
              - Assign all three spherical components of the DeltaV vector (order Az, El, Mag; dimensions: Angle, Angle, SmallDistance/Time).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveThrustVector.query_spherical`
              - Get all three spherical components of the DeltaV vector as an array (order Az, El, Mag; dimensions: Angle, Angle, SmallDistance/Time).

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveThrustVector.thrust_axes_name`
              - Get or set the thrust axes.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveThrustVector.body_constraint_vector`
              - Define a constraint vector in spacecraft body coordinates to complete the attitude definition.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveThrustVector.allow_negative_spherical_magnitude`
              - True if the spherical magnitude should be allowed to be less than zero.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveThrustVector.coord_type`
              - Get or set the coordinate representation for the DeltaV.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveThrustVector.x`
              - Get or set the Cartesian X component of the impulsive DeltaV (dimension: SmallDistance/Time).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveThrustVector.y`
              - Get or set the Cartesian Y component of the impulsive DeltaV (dimension: SmallDistance/Time).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveThrustVector.z`
              - Get or set the Cartesian Z component of the impulsive DeltaV (dimension: SmallDistance/Time).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveThrustVector.azimuth`
              - Get or set the spherical Azimuth angle of the impulsive DeltaV (dimension: Angle).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveThrustVector.elevation`
              - Get or set the spherical Elevation angle of the impulsive DeltaV (dimension: Angle).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveThrustVector.magnitude`
              - Get or set the spherical Magnitude of the impulsive DeltaV (dimension: SmallDistance/Time).



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import AttitudeControlImpulsiveThrustVector


Property detail
---------------

.. py:property:: thrust_axes_name
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveThrustVector.thrust_axes_name
    :type: str

    Get or set the thrust axes.

.. py:property:: body_constraint_vector
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveThrustVector.body_constraint_vector
    :type: IDirection

    Define a constraint vector in spacecraft body coordinates to complete the attitude definition.

.. py:property:: allow_negative_spherical_magnitude
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveThrustVector.allow_negative_spherical_magnitude
    :type: bool

    True if the spherical magnitude should be allowed to be less than zero.

.. py:property:: coord_type
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveThrustVector.coord_type
    :type: ImpulsiveDeltaVRepresentation

    Get or set the coordinate representation for the DeltaV.

.. py:property:: x
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveThrustVector.x
    :type: float

    Get or set the Cartesian X component of the impulsive DeltaV (dimension: SmallDistance/Time).

.. py:property:: y
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveThrustVector.y
    :type: float

    Get or set the Cartesian Y component of the impulsive DeltaV (dimension: SmallDistance/Time).

.. py:property:: z
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveThrustVector.z
    :type: float

    Get or set the Cartesian Z component of the impulsive DeltaV (dimension: SmallDistance/Time).

.. py:property:: azimuth
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveThrustVector.azimuth
    :type: typing.Any

    Get or set the spherical Azimuth angle of the impulsive DeltaV (dimension: Angle).

.. py:property:: elevation
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveThrustVector.elevation
    :type: typing.Any

    Get or set the spherical Elevation angle of the impulsive DeltaV (dimension: Angle).

.. py:property:: magnitude
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveThrustVector.magnitude
    :type: float

    Get or set the spherical Magnitude of the impulsive DeltaV (dimension: SmallDistance/Time).


Method detail
-------------




















.. py:method:: assign_cartesian(self, x_value: float, y_value: float, z_value: float) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveThrustVector.assign_cartesian

    Assign all three Cartesian components of the DeltaV vector (dimension: SmallDistance/Time).

    :Parameters:

        **x_value** : :obj:`~float`

        **y_value** : :obj:`~float`

        **z_value** : :obj:`~float`


    :Returns:

        :obj:`~None`

.. py:method:: query_cartesian(self) -> list
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveThrustVector.query_cartesian

    Get all three Cartesian components of the DeltaV vector as an array (dimension: SmallDistance/Time).

    :Returns:

        :obj:`~list`

.. py:method:: assign_spherical(self, azimuth_value: typing.Any, elevation_value: typing.Any, magnitude_value: float) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveThrustVector.assign_spherical

    Assign all three spherical components of the DeltaV vector (order Az, El, Mag; dimensions: Angle, Angle, SmallDistance/Time).

    :Parameters:

        **azimuth_value** : :obj:`~typing.Any`

        **elevation_value** : :obj:`~typing.Any`

        **magnitude_value** : :obj:`~float`


    :Returns:

        :obj:`~None`

.. py:method:: query_spherical(self) -> list
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveThrustVector.query_spherical

    Get all three spherical components of the DeltaV vector as an array (order Az, El, Mag; dimensions: Angle, Angle, SmallDistance/Time).

    :Returns:

        :obj:`~list`

