IVehicleRealtimeCartesianPoints
===============================

.. py:class:: IVehicleRealtimeCartesianPoints

   object
   
   Add one ephemeris point using cartesian coordinates.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~add_position`
              - Add an ephemeris point. Epoch uses DateFormat dimension.
            * - :py:meth:`~add`
              - Add an ephemeris point using position and velocity. Epoch uses DateFormat dimension.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleRealtimeCartesianPoints



Method detail
-------------

.. py:method:: add_position(self, time: typing.Any, x: float, y: float, z: float) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleRealtimeCartesianPoints.add_position

    Add an ephemeris point. Epoch uses DateFormat dimension.

    :Parameters:

    **time** : :obj:`~typing.Any`
    **x** : :obj:`~float`
    **y** : :obj:`~float`
    **z** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: add(self, time: typing.Any, x: float, y: float, z: float, vx: float, vy: float, vz: float) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleRealtimeCartesianPoints.add

    Add an ephemeris point using position and velocity. Epoch uses DateFormat dimension.

    :Parameters:

    **time** : :obj:`~typing.Any`
    **x** : :obj:`~float`
    **y** : :obj:`~float`
    **z** : :obj:`~float`
    **vx** : :obj:`~float`
    **vy** : :obj:`~float`
    **vz** : :obj:`~float`

    :Returns:

        :obj:`~None`

