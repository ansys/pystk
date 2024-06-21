IOrbitStateEquinoctial
======================

.. py:class:: ansys.stk.core.stkobjects.IOrbitStateEquinoctial

   IOrbitState
   
   Equinoctial coordinate type, which uses the center of the Earth as the origin and the plane of the satellite's orbit as the reference plane.

.. py:currentmodule:: IOrbitStateEquinoctial

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateEquinoctial.coordinate_system_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateEquinoctial.coordinate_system`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateEquinoctial.size_shape_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateEquinoctial.size_shape`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateEquinoctial.h`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateEquinoctial.k`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateEquinoctial.p`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateEquinoctial.q`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateEquinoctial.mean_longitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateEquinoctial.formulation`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateEquinoctial.supported_coordinate_system_types`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateEquinoctial.state_epoch`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IOrbitStateEquinoctial


Property detail
---------------

.. py:property:: coordinate_system_type
    :canonical: ansys.stk.core.stkobjects.IOrbitStateEquinoctial.coordinate_system_type
    :type: COORDINATE_SYSTEM

    Gets or sets the coordinate system being used.

.. py:property:: coordinate_system
    :canonical: ansys.stk.core.stkobjects.IOrbitStateEquinoctial.coordinate_system
    :type: IOrbitStateCoordinateSystem

    Get the coordinate system and coordinate epoch.

.. py:property:: size_shape_type
    :canonical: ansys.stk.core.stkobjects.IOrbitStateEquinoctial.size_shape_type
    :type: EQUINOCTIAL_SIZE_SHAPE

    Gets or sets the orbit size option can be Mean Motion or Semimajor Axis.

.. py:property:: size_shape
    :canonical: ansys.stk.core.stkobjects.IOrbitStateEquinoctial.size_shape
    :type: IClassicalSizeShape

    Get the value of Mean Motion or Semimajor Axis.

.. py:property:: h
    :canonical: ansys.stk.core.stkobjects.IOrbitStateEquinoctial.h
    :type: float

    H/K collectively describe the shape of the satellite's orbit and the position of perigee. Dimensionless.

.. py:property:: k
    :canonical: ansys.stk.core.stkobjects.IOrbitStateEquinoctial.k
    :type: float

    H/K collectively describe the shape of the satellite's orbit and the position of perigee. Dimensionless.

.. py:property:: p
    :canonical: ansys.stk.core.stkobjects.IOrbitStateEquinoctial.p
    :type: float

    P/Q collectively describe the orientation of the satellite's orbit plane. Dimensionless.

.. py:property:: q
    :canonical: ansys.stk.core.stkobjects.IOrbitStateEquinoctial.q
    :type: float

    P/Q collectively describe the orientation of the satellite's orbit plane. Dimensionless.

.. py:property:: mean_longitude
    :canonical: ansys.stk.core.stkobjects.IOrbitStateEquinoctial.mean_longitude
    :type: float

    Specifies a satellite's position within its orbit at epoch and equals the sum of the classical RAAN, Argument of Perigee, and Mean Anomaly. Uses Angle dimension.

.. py:property:: formulation
    :canonical: ansys.stk.core.stkobjects.IOrbitStateEquinoctial.formulation
    :type: EQUINOCTIAL_FORMULATION

    Gets or sets the Formulation can be Retrograde or Posigrade.

.. py:property:: supported_coordinate_system_types
    :canonical: ansys.stk.core.stkobjects.IOrbitStateEquinoctial.supported_coordinate_system_types
    :type: list

    Returns an array of supported coordinate system types.

.. py:property:: state_epoch
    :canonical: ansys.stk.core.stkobjects.IOrbitStateEquinoctial.state_epoch
    :type: ITimeToolEventSmartEpoch

    Smart epoch component allows the user to configure the state epoch explicitly or implicitly (using a pre-defined or custom time instant component).


