IVehicleSpatialInfo
===================

.. py:class:: IVehicleSpatialInfo

   object
   
   Represents a spatial information of the vehicle.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~get_state`
              - Return a spatial state of the vehicle at specified time.
            * - :py:meth:`~get_available_times`
              - Return a collection of available intervals.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~recycle`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleSpatialInfo


Property detail
---------------

.. py:property:: recycle
    :canonical: ansys.stk.core.stkobjects.IVehicleSpatialInfo.recycle
    :type: bool

    Controls whether to reuse the same spatial state object in subsequent calls to GetState.


Method detail
-------------

.. py:method:: get_state(self, time:typing.Any) -> "ISpatialState"

    Return a spatial state of the vehicle at specified time.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~"ISpatialState"`


.. py:method:: get_available_times(self) -> "IImmutableIntervalCollection"

    Return a collection of available intervals.

    :Returns:

        :obj:`~"IImmutableIntervalCollection"`

