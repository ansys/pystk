IVehicleGraphics3DOrbitTickMarks
================================

.. py:class:: IVehicleGraphics3DOrbitTickMarks

   object
   
   Tick mark interface for satellites.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~time_between_ticks`
            * - :py:meth:`~ground_track`
            * - :py:meth:`~orbit`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics3DOrbitTickMarks


Property detail
---------------

.. py:property:: time_between_ticks
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DOrbitTickMarks.time_between_ticks
    :type: float

    Time between tick marks: the time elapsed between each milestone indicated by a tick mark along the satellite's path. Uses Time Dimension.

.. py:property:: ground_track
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DOrbitTickMarks.ground_track
    :type: "IAgVeVOPathTickMarks"

    Get the ground track tick marks.

.. py:property:: orbit
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DOrbitTickMarks.orbit
    :type: "IAgVeVOPathTickMarks"

    Get the orbit track tick marks.


