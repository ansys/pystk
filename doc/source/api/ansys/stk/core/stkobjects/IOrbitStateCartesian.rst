IOrbitStateCartesian
====================

.. py:class:: ansys.stk.core.stkobjects.IOrbitStateCartesian

   IOrbitState
   
   Cartesian coordinate type.

.. py:currentmodule:: IOrbitStateCartesian

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateCartesian.coordinate_system_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateCartesian.coordinate_system`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateCartesian.x_position`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateCartesian.y_position`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateCartesian.z_position`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateCartesian.x_velocity`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateCartesian.y_velocity`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateCartesian.z_velocity`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateCartesian.supported_coordinate_system_types`
            * - :py:attr:`~ansys.stk.core.stkobjects.IOrbitStateCartesian.state_epoch`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IOrbitStateCartesian


Property detail
---------------

.. py:property:: coordinate_system_type
    :canonical: ansys.stk.core.stkobjects.IOrbitStateCartesian.coordinate_system_type
    :type: COORDINATE_SYSTEM

    Coordinate system being used.

.. py:property:: coordinate_system
    :canonical: ansys.stk.core.stkobjects.IOrbitStateCartesian.coordinate_system
    :type: IOrbitStateCoordinateSystem

    Get the coordinate system and epoch.

.. py:property:: x_position
    :canonical: ansys.stk.core.stkobjects.IOrbitStateCartesian.x_position
    :type: float

    X position component.Uses Distance Dimension.

.. py:property:: y_position
    :canonical: ansys.stk.core.stkobjects.IOrbitStateCartesian.y_position
    :type: float

    Y position component. Uses Distance Dimension.

.. py:property:: z_position
    :canonical: ansys.stk.core.stkobjects.IOrbitStateCartesian.z_position
    :type: float

    Z position component. Uses Distance Dimension.

.. py:property:: x_velocity
    :canonical: ansys.stk.core.stkobjects.IOrbitStateCartesian.x_velocity
    :type: float

    X velocity component. Uses Rate Dimension.

.. py:property:: y_velocity
    :canonical: ansys.stk.core.stkobjects.IOrbitStateCartesian.y_velocity
    :type: float

    Y velocity component. Uses Rate Dimension.

.. py:property:: z_velocity
    :canonical: ansys.stk.core.stkobjects.IOrbitStateCartesian.z_velocity
    :type: float

    Z velocity component. Uses Rate Dimension.

.. py:property:: supported_coordinate_system_types
    :canonical: ansys.stk.core.stkobjects.IOrbitStateCartesian.supported_coordinate_system_types
    :type: list

    Returns an array of supported coordinate system types.

.. py:property:: state_epoch
    :canonical: ansys.stk.core.stkobjects.IOrbitStateCartesian.state_epoch
    :type: ITimeToolEventSmartEpoch

    Smart epoch component allows the user to configure the state epoch explicitly or implicitly (using a pre-defined or custom time instant component).


