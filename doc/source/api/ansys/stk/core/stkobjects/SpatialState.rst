SpatialState
============

.. py:class:: ansys.stk.core.stkobjects.SpatialState

   Bases: 

   Represents a position and an attitude of an object.

.. py:currentmodule:: SpatialState

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SpatialState.query_velocity_fixed`
              - Return a velocity of the vehicle in central body fixed frame.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpatialState.query_velocity_inertial`
              - Return a velocity of the vehicle in central body inertial frame.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SpatialState.fixed_position`
              - Returns a position of the vehicle in central body fixed frame.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpatialState.inertial_position`
              - Returns a position of the vehicle in central body inertial frame.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpatialState.inertial_orientation`
              - Returns an attitude of the vehicle in central body inertial frame.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpatialState.fixed_orientation`
              - Returns an attitude of the vehicle in central body fixed frame.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpatialState.current_time`
              - Returns the current time.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpatialState.central_body`
              - Returns a name of the central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpatialState.start_time`
              - Returns the start time.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpatialState.stop_time`
              - Returns the stop time.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpatialState.is_available`
              - Returns whether the spatial state is valid.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SpatialState


Property detail
---------------

.. py:property:: fixed_position
    :canonical: ansys.stk.core.stkobjects.SpatialState.fixed_position
    :type: IPosition

    Returns a position of the vehicle in central body fixed frame.

.. py:property:: inertial_position
    :canonical: ansys.stk.core.stkobjects.SpatialState.inertial_position
    :type: IPosition

    Returns a position of the vehicle in central body inertial frame.

.. py:property:: inertial_orientation
    :canonical: ansys.stk.core.stkobjects.SpatialState.inertial_orientation
    :type: IOrientation

    Returns an attitude of the vehicle in central body inertial frame.

.. py:property:: fixed_orientation
    :canonical: ansys.stk.core.stkobjects.SpatialState.fixed_orientation
    :type: IOrientation

    Returns an attitude of the vehicle in central body fixed frame.

.. py:property:: current_time
    :canonical: ansys.stk.core.stkobjects.SpatialState.current_time
    :type: typing.Any

    Returns the current time.

.. py:property:: central_body
    :canonical: ansys.stk.core.stkobjects.SpatialState.central_body
    :type: str

    Returns a name of the central body.

.. py:property:: start_time
    :canonical: ansys.stk.core.stkobjects.SpatialState.start_time
    :type: typing.Any

    Returns the start time.

.. py:property:: stop_time
    :canonical: ansys.stk.core.stkobjects.SpatialState.stop_time
    :type: typing.Any

    Returns the stop time.

.. py:property:: is_available
    :canonical: ansys.stk.core.stkobjects.SpatialState.is_available
    :type: bool

    Returns whether the spatial state is valid.


Method detail
-------------










.. py:method:: query_velocity_fixed(self) -> typing.Tuple[float, float, float]
    :canonical: ansys.stk.core.stkobjects.SpatialState.query_velocity_fixed

    Return a velocity of the vehicle in central body fixed frame.

    :Returns:

        :obj:`~typing.Tuple[float, float, float]`

.. py:method:: query_velocity_inertial(self) -> typing.Tuple[float, float, float]
    :canonical: ansys.stk.core.stkobjects.SpatialState.query_velocity_inertial

    Return a velocity of the vehicle in central body inertial frame.

    :Returns:

        :obj:`~typing.Tuple[float, float, float]`

