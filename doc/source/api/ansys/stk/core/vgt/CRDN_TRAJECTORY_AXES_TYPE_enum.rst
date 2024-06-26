CRDN_TRAJECTORY_AXES_TYPE
=========================

.. py:class:: ansys.stk.core.vgt.CRDN_TRAJECTORY_AXES_TYPE

   IntEnum


.. py:currentmodule:: CRDN_TRAJECTORY_AXES_TYPE

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ICR`
              - Intrack Crosstrack Radial Axes. The Z axis is outward along the position vector (radial); the Y axis is along the cross product of the position and velocity (crosstrack); the X axis is in the direction of motion and constructed as Y x Z (intrack).

            * - :py:attr:`~VNC`
              - Velocity - Normal - Co-normal Axes. The X axis is along the velocity vector; the Y axis is along the cross product of the position and velocity (normal); the Z axis is constructed as X x Y (co-normal).

            * - :py:attr:`~RIC`
              - Radial Intrack Crosstrack Axes. The X axis is outward along the position vector (radial); the Z axis is along the cross product of the position and velocity (crosstrack); the Y axis is in the direction of motion and is constructed as Z x X (intrack).

            * - :py:attr:`~LVLH`
              - Local Vertical, Local Horizontal Axes. The X axis is along the position vector (local vertical); the Z axis is along the cross product of the position and velocity; the Y axis is in the direction of motion and constructed as Z x X (local horizontal).

            * - :py:attr:`~VVLH`
              - Vehicle Velocity, Local Horizontal Axes. The Z axis is along the negative position vector; the Y axis is along the negative cross product of the position and velocity (local horizontal); the X axis is constructed as Z x Y (toward velocity).

            * - :py:attr:`~BBR`
              - Body-to-body Rotating Axes. The X axis is along the negative position vector; the Z axis is along the cross product of the position and velocity; the Y axis is constructed as Z x X.

            * - :py:attr:`~EQUINOCTIAL`
              - Equinoctial Axes. The Z axis is along the orbit normal; the X axis is along the fiducial direction located by rotating about Z-axis by negative of RAAN value; the Y axis is constructed as Z x X.

            * - :py:attr:`~NTC`
              - Normal - Tangential - Crosstrack Axes. The Y axis is along the velocity vector (tangential); the Z axis is along the cross product of the position and velocity (crosstrack); the X axis is constructed as Y x Z (normal).


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import CRDN_TRAJECTORY_AXES_TYPE


