ManeuverType
============

.. py:class:: ansys.stk.core.stkobjects.astrogator.ManeuverType

   IntEnum


.. py:currentmodule:: ManeuverType

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~IMPULSIVE`
              - Impulsive - calculates a state by adding the defined delta-V vector to the velocity of the final state of the previous segment, adds this new state to the ephemeris, and passes it to the next segment.

            * - :py:attr:`~FINITE`
              - Finite - effectively a Propagate segment with thrust. Like Propagate segments, each point calculated by the propagator is added to the ephemeris, and propagation continues until a stopping condition is met.

            * - :py:attr:`~OPTIMAL_FINITE`
              - Optimal Finite.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ManeuverType


