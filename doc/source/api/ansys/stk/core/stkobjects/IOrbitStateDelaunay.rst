IOrbitStateDelaunay
===================

.. py:class:: ansys.stk.core.stkobjects.IOrbitStateDelaunay

   IOrbitState
   
   Delaunay coordinate type, using a set of canonical action-angle variables, which are commonly used in general perturbation theories.

.. py:currentmodule:: IOrbitStateDelaunay

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateDelaunay.coordinate_system_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateDelaunay.coordinate_system`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateDelaunay.l_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateDelaunay.l`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateDelaunay.h_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateDelaunay.h`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateDelaunay.g_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateDelaunay.g`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateDelaunay.supported_coordinate_system_types`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateDelaunay.mean_anomaly`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateDelaunay.arg_of_periapsis`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateDelaunay.raan`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateDelaunay.state_epoch`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IOrbitStateDelaunay


Property detail
---------------

.. py:property:: coordinate_system_type
    :canonical: ansys.stk.core.stkobjects.IOrbitStateDelaunay.coordinate_system_type
    :type: COORDINATE_SYSTEM

    Gets or sets the coordinate system being used.

.. py:property:: coordinate_system
    :canonical: ansys.stk.core.stkobjects.IOrbitStateDelaunay.coordinate_system
    :type: IOrbitStateCoordinateSystem

    Get the coordinate system and coordinate epoch.

.. py:property:: l_type
    :canonical: ansys.stk.core.stkobjects.IOrbitStateDelaunay.l_type
    :type: DELAUNAY_L_TYPE

    Option for Delaunay L (default or L/SQRT(mu).

.. py:property:: l
    :canonical: ansys.stk.core.stkobjects.IOrbitStateDelaunay.l
    :type: IDelaunayActionVariable

    Value of L or L/SQRT(mu).

.. py:property:: h_type
    :canonical: ansys.stk.core.stkobjects.IOrbitStateDelaunay.h_type
    :type: DELAUNAY_H_TYPE

    Option for Delaunay H (default or H/SQRT(mu).

.. py:property:: h
    :canonical: ansys.stk.core.stkobjects.IOrbitStateDelaunay.h
    :type: IDelaunayActionVariable

    Value of H or H/SQRT(mu).

.. py:property:: g_type
    :canonical: ansys.stk.core.stkobjects.IOrbitStateDelaunay.g_type
    :type: DELAUNAY_G_TYPE

    Option for Delaunay G (default or G/SQRT(mu).

.. py:property:: g
    :canonical: ansys.stk.core.stkobjects.IOrbitStateDelaunay.g
    :type: IDelaunayActionVariable

    Value of G or G/SQRT(mu).

.. py:property:: supported_coordinate_system_types
    :canonical: ansys.stk.core.stkobjects.IOrbitStateDelaunay.supported_coordinate_system_types
    :type: list

    Returns an array of supported coordinate system types.

.. py:property:: mean_anomaly
    :canonical: ansys.stk.core.stkobjects.IOrbitStateDelaunay.mean_anomaly
    :type: float

    Mean Anomaly (l). Uses Angle Dimension.

.. py:property:: arg_of_periapsis
    :canonical: ansys.stk.core.stkobjects.IOrbitStateDelaunay.arg_of_periapsis
    :type: float

    Argument of periapsis (g). Uses Angle Dimension.

.. py:property:: raan
    :canonical: ansys.stk.core.stkobjects.IOrbitStateDelaunay.raan
    :type: float

    RAAN (h). Uses Angle Dimension.

.. py:property:: state_epoch
    :canonical: ansys.stk.core.stkobjects.IOrbitStateDelaunay.state_epoch
    :type: ITimeToolEventSmartEpoch

    Smart epoch component allows the user to configure the state epoch explicitly or implicitly (using a pre-defined or custom time instant component).


