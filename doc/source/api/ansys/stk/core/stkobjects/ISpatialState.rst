ISpatialState
=============

.. py:class:: ISpatialState

   object
   
   Represents a position and an attitude of an object.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~query_velocity_fixed`
              - Return a velocity of the vehicle in central body fixed frame.
            * - :py:meth:`~query_velocity_inertial`
              - Return a velocity of the vehicle in central body inertial frame.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~fixed_position`
            * - :py:meth:`~inertial_position`
            * - :py:meth:`~inertial_orientation`
            * - :py:meth:`~fixed_orientation`
            * - :py:meth:`~current_time`
            * - :py:meth:`~central_body`
            * - :py:meth:`~start_time`
            * - :py:meth:`~stop_time`
            * - :py:meth:`~is_available`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ISpatialState


Property detail
---------------

.. py:property:: fixed_position
    :canonical: ansys.stk.core.stkobjects.ISpatialState.fixed_position
    :type: IAgPosition

    Returns a position of the vehicle in central body fixed frame.

.. py:property:: inertial_position
    :canonical: ansys.stk.core.stkobjects.ISpatialState.inertial_position
    :type: IAgPosition

    Returns a position of the vehicle in central body inertial frame.

.. py:property:: inertial_orientation
    :canonical: ansys.stk.core.stkobjects.ISpatialState.inertial_orientation
    :type: IAgOrientation

    Returns an attitude of the vehicle in central body inertial frame.

.. py:property:: fixed_orientation
    :canonical: ansys.stk.core.stkobjects.ISpatialState.fixed_orientation
    :type: IAgOrientation

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

