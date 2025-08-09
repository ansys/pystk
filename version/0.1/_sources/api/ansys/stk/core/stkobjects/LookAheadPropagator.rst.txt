LookAheadPropagator
===================

.. py:class:: ansys.stk.core.stkobjects.LookAheadPropagator

   IntEnum


.. py:currentmodule:: LookAheadPropagator

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - Reserved for look ahead propagators that are not currently supported.

            * - :py:attr:`~HOLD_CENTRAL_BODY_INERTIAL_POSITION`
              - The HoldCBIPosition look ahead propagator keeps position and velocity constant in the inertial (i.e., CBI) frame.

            * - :py:attr:`~HOLD_CENTRAL_BODY_FIXED_POSITION`
              - The HoldCBFPosition look ahead propagator keeps position and velocity constant in the fixed (i.e., CBF) frame.

            * - :py:attr:`~TWO_BODY`
              - Two-Body is an analytical propagator that generates ephemeris by evaluating a formula.

            * - :py:attr:`~J2_PERTURBATION`
              - The J2 Perturbation (first-order) propagator accounts for secular variations in the orbit elements due to Earth oblateness.

            * - :py:attr:`~J4_PERTURBATION`
              - The J4 Perturbation (second-order) propagator accounts for secular variations in the orbit elements due to Earth oblateness.

            * - :py:attr:`~DEAD_RECKONING`
              - The DeadReckon look ahead propagator projects the motion of the vehicle along a straight line, along the last velocity vector.

            * - :py:attr:`~BALLISTIC`
              - The Ballistic Propagator defines an elliptical path that begins and ends at the Earth's surface. Specifying a fixed flight time, initial velocity or altitude can further refine the shape of the trajectory.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import LookAheadPropagator


