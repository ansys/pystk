AttitudeControl
===============

.. py:class:: ansys.stk.core.stkobjects.astrogator.AttitudeControl

   IntEnum


.. py:currentmodule:: AttitudeControl

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~VELOCITY_VECTOR`
              - Along Velocity Vector (impulsive/finite) - the total thrust vector is aligned with the spacecraft's velocity vector.

            * - :py:attr:`~ANTI_VELOCITY_VECTOR`
              - Anti-Velocity Vector (impulsive/finite) - the total thrust vector is opposite to the spacecraft's velocity vector.

            * - :py:attr:`~ATTITUDE`
              - Attitude (impulsive/finite) - the thrust vector direction is defined using Euler Angles or a Quaternion.

            * - :py:attr:`~FILE`
              - File (impulsive/finite) - uses an attitude file to set the thrust vector direction.

            * - :py:attr:`~THRUST_VECTOR`
              - Thrust Vector (impulsive/finite) - the total thrust vector is explicitly specified in Cartesian or spherical form with respect to the thrust axes.

            * - :py:attr:`~PLUGIN`
              - Plugin (finite) - thrust vector direction is defined using a COM plugin.

            * - :py:attr:`~TIME_VARYING`
              - Time Varying (finite) - polynomial and sine representations for the azimuth and elevation of the thrust vector.

            * - :py:attr:`~LAGRANGE_INTERPOLATION`
              - Lagrange Interpolation (optimal finite, always set) - supports the 'Run current nodes' execution mode of the Optimal Finite Maneuver.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import AttitudeControl


