VehicleGraphics3DOrbitTickMarks
===============================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics3DOrbitTickMarks

   Bases: 

   Tick mark for satellites.

.. py:currentmodule:: VehicleGraphics3DOrbitTickMarks

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DOrbitTickMarks.time_between_ticks`
              - Time between tick marks: the time elapsed between each milestone indicated by a tick mark along the satellite's path. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DOrbitTickMarks.ground_track`
              - Get the ground track tick marks.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DOrbitTickMarks.orbit`
              - Get the orbit track tick marks.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics3DOrbitTickMarks


Property detail
---------------

.. py:property:: time_between_ticks
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DOrbitTickMarks.time_between_ticks
    :type: float

    Time between tick marks: the time elapsed between each milestone indicated by a tick mark along the satellite's path. Uses Time Dimension.

.. py:property:: ground_track
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DOrbitTickMarks.ground_track
    :type: IVehicleGraphics3DPathTickMarks

    Get the ground track tick marks.

.. py:property:: orbit
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DOrbitTickMarks.orbit
    :type: IVehicleGraphics3DPathTickMarks

    Get the orbit track tick marks.


