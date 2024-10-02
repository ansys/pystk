OrbitStateCartesian
===================

.. py:class:: ansys.stk.core.stkobjects.OrbitStateCartesian

   Bases: :py:class:`~ansys.stk.core.stkobjects.IOrbitState`

   Cartesian coordinate type.

.. py:currentmodule:: OrbitStateCartesian

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateCartesian.coordinate_system_type`
              - Coordinate system being used.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateCartesian.coordinate_system`
              - Get the coordinate system and epoch.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateCartesian.x_position`
              - X position component.Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateCartesian.y_position`
              - Y position component. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateCartesian.z_position`
              - Z position component. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateCartesian.x_velocity`
              - X velocity component. Uses Rate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateCartesian.y_velocity`
              - Y velocity component. Uses Rate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateCartesian.z_velocity`
              - Z velocity component. Uses Rate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateCartesian.supported_coordinate_system_types`
              - Returns an array of supported coordinate system types.
            * - :py:attr:`~ansys.stk.core.stkobjects.OrbitStateCartesian.state_epoch`
              - Smart epoch component allows the user to configure the state epoch explicitly or implicitly (using a pre-defined or custom time instant component).



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import OrbitStateCartesian


Property detail
---------------

.. py:property:: coordinate_system_type
    :canonical: ansys.stk.core.stkobjects.OrbitStateCartesian.coordinate_system_type
    :type: COORDINATE_SYSTEM

    Coordinate system being used.

.. py:property:: coordinate_system
    :canonical: ansys.stk.core.stkobjects.OrbitStateCartesian.coordinate_system
    :type: OrbitStateCoordinateSystem

    Get the coordinate system and epoch.

.. py:property:: x_position
    :canonical: ansys.stk.core.stkobjects.OrbitStateCartesian.x_position
    :type: float

    X position component.Uses Distance Dimension.

.. py:property:: y_position
    :canonical: ansys.stk.core.stkobjects.OrbitStateCartesian.y_position
    :type: float

    Y position component. Uses Distance Dimension.

.. py:property:: z_position
    :canonical: ansys.stk.core.stkobjects.OrbitStateCartesian.z_position
    :type: float

    Z position component. Uses Distance Dimension.

.. py:property:: x_velocity
    :canonical: ansys.stk.core.stkobjects.OrbitStateCartesian.x_velocity
    :type: float

    X velocity component. Uses Rate Dimension.

.. py:property:: y_velocity
    :canonical: ansys.stk.core.stkobjects.OrbitStateCartesian.y_velocity
    :type: float

    Y velocity component. Uses Rate Dimension.

.. py:property:: z_velocity
    :canonical: ansys.stk.core.stkobjects.OrbitStateCartesian.z_velocity
    :type: float

    Z velocity component. Uses Rate Dimension.

.. py:property:: supported_coordinate_system_types
    :canonical: ansys.stk.core.stkobjects.OrbitStateCartesian.supported_coordinate_system_types
    :type: list

    Returns an array of supported coordinate system types.

.. py:property:: state_epoch
    :canonical: ansys.stk.core.stkobjects.OrbitStateCartesian.state_epoch
    :type: ITimeToolInstantSmartEpoch

    Smart epoch component allows the user to configure the state epoch explicitly or implicitly (using a pre-defined or custom time instant component).


