VehicleSpatialInfo
==================

.. py:class:: ansys.stk.core.stkobjects.VehicleSpatialInfo

   Represents a spatial information of the vehicle.

.. py:currentmodule:: VehicleSpatialInfo

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSpatialInfo.get_state`
              - Return a spatial state of the vehicle at specified time.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSpatialInfo.get_available_times`
              - Return a collection of available intervals.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSpatialInfo.recycle`
              - Controls whether to reuse the same spatial state object in subsequent calls to GetState.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleSpatialInfo


Property detail
---------------

.. py:property:: recycle
    :canonical: ansys.stk.core.stkobjects.VehicleSpatialInfo.recycle
    :type: bool

    Controls whether to reuse the same spatial state object in subsequent calls to GetState.


Method detail
-------------

.. py:method:: get_state(self, time: typing.Any) -> SpatialState
    :canonical: ansys.stk.core.stkobjects.VehicleSpatialInfo.get_state

    Return a spatial state of the vehicle at specified time.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~SpatialState`


.. py:method:: get_available_times(self) -> ImmutableIntervalCollection
    :canonical: ansys.stk.core.stkobjects.VehicleSpatialInfo.get_available_times

    Return a collection of available intervals.

    :Returns:

        :obj:`~ImmutableIntervalCollection`

