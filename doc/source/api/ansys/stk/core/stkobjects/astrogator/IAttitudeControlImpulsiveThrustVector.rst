IAttitudeControlImpulsiveThrustVector
=====================================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveThrustVector

   IAttitudeControlImpulsive
   
   Properties for the Thrust Vector attitude control for an Impulsive Maneuver.

.. py:currentmodule:: IAttitudeControlImpulsiveThrustVector

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveThrustVector.assign_cartesian`
              - Assign all three Cartesian components of the DeltaV vector (dimension: SmallDistance/Time).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveThrustVector.query_cartesian`
              - Get all three Cartesian components of the DeltaV vector as an array (dimension: SmallDistance/Time).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveThrustVector.assign_spherical`
              - Assign all three spherical components of the DeltaV vector (order Az, El, Mag; dimensions: Angle, Angle, SmallDistance/Time).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveThrustVector.query_spherical`
              - Get all three spherical components of the DeltaV vector as an array (order Az, El, Mag; dimensions: Angle, Angle, SmallDistance/Time).

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveThrustVector.thrust_axes_name`
              - Gets or sets the thrust axes.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveThrustVector.body_constraint_vector`
              - Defines a constraint vector in spacecraft body coordinates to complete the attitude definition.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveThrustVector.allow_negative_spherical_magnitude`
              - True if the spherical magnitude should be allowed to be less than zero.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveThrustVector.coord_type`
              - Gets or sets the coordinate representation for the DeltaV.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveThrustVector.x`
              - Gets or sets the Cartesian X component of the impulsive DeltaV (dimension: SmallDistance/Time).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveThrustVector.y`
              - Gets or sets the Cartesian Y component of the impulsive DeltaV (dimension: SmallDistance/Time).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveThrustVector.z`
              - Gets or sets the Cartesian Z component of the impulsive DeltaV (dimension: SmallDistance/Time).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveThrustVector.azimuth`
              - Gets or sets the spherical Azimuth angle of the impulsive DeltaV (dimension: Angle).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveThrustVector.elevation`
              - Gets or sets the spherical Elevation angle of the impulsive DeltaV (dimension: Angle).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveThrustVector.magnitude`
              - Gets or sets the spherical Magnitude of the impulsive DeltaV (dimension: SmallDistance/Time).


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IAttitudeControlImpulsiveThrustVector


Property detail
---------------

.. py:property:: thrust_axes_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveThrustVector.thrust_axes_name
    :type: str

    Gets or sets the thrust axes.

.. py:property:: body_constraint_vector
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveThrustVector.body_constraint_vector
    :type: IDirection

    Defines a constraint vector in spacecraft body coordinates to complete the attitude definition.

.. py:property:: allow_negative_spherical_magnitude
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveThrustVector.allow_negative_spherical_magnitude
    :type: bool

    True if the spherical magnitude should be allowed to be less than zero.

.. py:property:: coord_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveThrustVector.coord_type
    :type: IMP_DELTA_V_REP

    Gets or sets the coordinate representation for the DeltaV.

.. py:property:: x
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveThrustVector.x
    :type: float

    Gets or sets the Cartesian X component of the impulsive DeltaV (dimension: SmallDistance/Time).

.. py:property:: y
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveThrustVector.y
    :type: float

    Gets or sets the Cartesian Y component of the impulsive DeltaV (dimension: SmallDistance/Time).

.. py:property:: z
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveThrustVector.z
    :type: float

    Gets or sets the Cartesian Z component of the impulsive DeltaV (dimension: SmallDistance/Time).

.. py:property:: azimuth
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveThrustVector.azimuth
    :type: typing.Any

    Gets or sets the spherical Azimuth angle of the impulsive DeltaV (dimension: Angle).

.. py:property:: elevation
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveThrustVector.elevation
    :type: typing.Any

    Gets or sets the spherical Elevation angle of the impulsive DeltaV (dimension: Angle).

.. py:property:: magnitude
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveThrustVector.magnitude
    :type: float

    Gets or sets the spherical Magnitude of the impulsive DeltaV (dimension: SmallDistance/Time).


Method detail
-------------




















.. py:method:: assign_cartesian(self, xVal: float, yVal: float, zVal: float) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveThrustVector.assign_cartesian

    Assign all three Cartesian components of the DeltaV vector (dimension: SmallDistance/Time).

    :Parameters:

    **xVal** : :obj:`~float`
    **yVal** : :obj:`~float`
    **zVal** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: query_cartesian(self) -> list
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveThrustVector.query_cartesian

    Get all three Cartesian components of the DeltaV vector as an array (dimension: SmallDistance/Time).

    :Returns:

        :obj:`~list`

.. py:method:: assign_spherical(self, azVal: typing.Any, elVal: typing.Any, magVal: float) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveThrustVector.assign_spherical

    Assign all three spherical components of the DeltaV vector (order Az, El, Mag; dimensions: Angle, Angle, SmallDistance/Time).

    :Parameters:

    **azVal** : :obj:`~typing.Any`
    **elVal** : :obj:`~typing.Any`
    **magVal** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: query_spherical(self) -> list
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveThrustVector.query_spherical

    Get all three spherical components of the DeltaV vector as an array (order Az, El, Mag; dimensions: Angle, Angle, SmallDistance/Time).

    :Returns:

        :obj:`~list`

