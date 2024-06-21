ISpatialState
=============

.. py:class:: ansys.stk.core.stkobjects.ISpatialState

   object
   
   Represents a position and an attitude of an object.

.. py:currentmodule:: ISpatialState

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ISpatialState.query_velocity_fixed`
              - Return a velocity of the vehicle in central body fixed frame.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISpatialState.query_velocity_inertial`
              - Return a velocity of the vehicle in central body inertial frame.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ISpatialState.fixed_position`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISpatialState.inertial_position`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISpatialState.inertial_orientation`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISpatialState.fixed_orientation`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISpatialState.current_time`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISpatialState.central_body`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISpatialState.start_time`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISpatialState.stop_time`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISpatialState.is_available`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ISpatialState


Property detail
---------------

.. py:property:: fixed_position
    :canonical: ansys.stk.core.stkobjects.ISpatialState.fixed_position
    :type: IPosition

    Returns a position of the vehicle in central body fixed frame.

.. py:property:: inertial_position
    :canonical: ansys.stk.core.stkobjects.ISpatialState.inertial_position
    :type: IPosition

    Returns a position of the vehicle in central body inertial frame.

.. py:property:: inertial_orientation
    :canonical: ansys.stk.core.stkobjects.ISpatialState.inertial_orientation
    :type: IOrientation

    Returns an attitude of the vehicle in central body inertial frame.

.. py:property:: fixed_orientation
    :canonical: ansys.stk.core.stkobjects.ISpatialState.fixed_orientation
    :type: IOrientation

    Returns an attitude of the vehicle in central body fixed frame.

.. py:property:: current_time
    :canonical: ansys.stk.core.stkobjects.ISpatialState.current_time
    :type: typing.Any

    Returns the current time.

.. py:property:: central_body
    :canonical: ansys.stk.core.stkobjects.ISpatialState.central_body
    :type: str

    Returns a name of the central body.

.. py:property:: start_time
    :canonical: ansys.stk.core.stkobjects.ISpatialState.start_time
    :type: typing.Any

    Returns the start time.

.. py:property:: stop_time
    :canonical: ansys.stk.core.stkobjects.ISpatialState.stop_time
    :type: typing.Any

    Returns the stop time.

.. py:property:: is_available
    :canonical: ansys.stk.core.stkobjects.ISpatialState.is_available
    :type: bool

    Returns whether the spatial state is valid.


Method detail
-------------










.. py:method:: query_velocity_fixed(self) -> typing.Tuple[float, float, float]
    :canonical: ansys.stk.core.stkobjects.ISpatialState.query_velocity_fixed

    Return a velocity of the vehicle in central body fixed frame.

    :Returns:

        :obj:`~typing.Tuple[float, float, float]`

.. py:method:: query_velocity_inertial(self) -> typing.Tuple[float, float, float]
    :canonical: ansys.stk.core.stkobjects.ISpatialState.query_velocity_inertial

    Return a velocity of the vehicle in central body inertial frame.

    :Returns:

        :obj:`~typing.Tuple[float, float, float]`

