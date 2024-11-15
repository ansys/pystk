OrbitStateDelaunay
==================

.. py:class:: ansys.stk.core.stkobjects.OrbitStateDelaunay

   Bases: :py:class:`~ansys.stk.core.stkobjects.IOrbitState`

   Delaunay coordinate type, using a set of canonical action-angle variables, which are commonly used in general perturbation theories.

.. py:currentmodule:: OrbitStateDelaunay

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateDelaunay.coordinate_system_type`
              - Gets or sets the coordinate system being used.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateDelaunay.coordinate_system`
              - Get the coordinate system and coordinate epoch.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateDelaunay.l_type`
              - Option for Delaunay L (default or L/SQRT(mu).
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateDelaunay.l`
              - Value of L or L/SQRT(mu).
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateDelaunay.h_type`
              - Option for Delaunay H (default or H/SQRT(mu).
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateDelaunay.h`
              - Value of H or H/SQRT(mu).
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateDelaunay.g_type`
              - Option for Delaunay G (default or G/SQRT(mu).
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateDelaunay.g`
              - Value of G or G/SQRT(mu).
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateDelaunay.supported_coordinate_system_types`
              - Returns an array of supported coordinate system types.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateDelaunay.mean_anomaly`
              - Mean Anomaly (l). Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateDelaunay.argument_of_periapsis`
              - Argument of periapsis (g). Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateDelaunay.right_ascension_ascending_node`
              - RAAN (h). Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateDelaunay.state_epoch`
              - Smart epoch component allows the user to configure the state epoch explicitly or implicitly (using a pre-defined or custom time instant component).



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import OrbitStateDelaunay


Property detail
---------------

.. py:property:: coordinate_system_type
    :canonical: ansys.stk.core.stkobjects.OrbitStateDelaunay.coordinate_system_type
    :type: COORDINATE_SYSTEM

    Gets or sets the coordinate system being used.

.. py:property:: coordinate_system
    :canonical: ansys.stk.core.stkobjects.OrbitStateDelaunay.coordinate_system
    :type: OrbitStateCoordinateSystem

    Get the coordinate system and coordinate epoch.

.. py:property:: l_type
    :canonical: ansys.stk.core.stkobjects.OrbitStateDelaunay.l_type
    :type: DELAUNAY_L_TYPE

    Option for Delaunay L (default or L/SQRT(mu).

.. py:property:: l
    :canonical: ansys.stk.core.stkobjects.OrbitStateDelaunay.l
    :type: IDelaunayActionVariable

    Value of L or L/SQRT(mu).

.. py:property:: h_type
    :canonical: ansys.stk.core.stkobjects.OrbitStateDelaunay.h_type
    :type: DELAUNAY_H_TYPE

    Option for Delaunay H (default or H/SQRT(mu).

.. py:property:: h
    :canonical: ansys.stk.core.stkobjects.OrbitStateDelaunay.h
    :type: IDelaunayActionVariable

    Value of H or H/SQRT(mu).

.. py:property:: g_type
    :canonical: ansys.stk.core.stkobjects.OrbitStateDelaunay.g_type
    :type: DELAUNAY_G_TYPE

    Option for Delaunay G (default or G/SQRT(mu).

.. py:property:: g
    :canonical: ansys.stk.core.stkobjects.OrbitStateDelaunay.g
    :type: IDelaunayActionVariable

    Value of G or G/SQRT(mu).

.. py:property:: supported_coordinate_system_types
    :canonical: ansys.stk.core.stkobjects.OrbitStateDelaunay.supported_coordinate_system_types
    :type: list

    Returns an array of supported coordinate system types.

.. py:property:: mean_anomaly
    :canonical: ansys.stk.core.stkobjects.OrbitStateDelaunay.mean_anomaly
    :type: float

    Mean Anomaly (l). Uses Angle Dimension.

.. py:property:: argument_of_periapsis
    :canonical: ansys.stk.core.stkobjects.OrbitStateDelaunay.argument_of_periapsis
    :type: float

    Argument of periapsis (g). Uses Angle Dimension.

.. py:property:: right_ascension_ascending_node
    :canonical: ansys.stk.core.stkobjects.OrbitStateDelaunay.right_ascension_ascending_node
    :type: float

    RAAN (h). Uses Angle Dimension.

.. py:property:: state_epoch
    :canonical: ansys.stk.core.stkobjects.OrbitStateDelaunay.state_epoch
    :type: ITimeToolInstantSmartEpoch

    Smart epoch component allows the user to configure the state epoch explicitly or implicitly (using a pre-defined or custom time instant component).


