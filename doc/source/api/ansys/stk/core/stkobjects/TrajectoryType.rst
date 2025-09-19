TrajectoryType
==============

.. py:class:: ansys.stk.core.stkobjects.TrajectoryType

   IntEnum


.. py:currentmodule:: TrajectoryType

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~POINT`
              - Displays a point at the current animation time.

            * - :py:attr:`~TRACE`
              - Displays a sampled trajectory of a point. This sampled trajectory displays where the point is over time without animating the scenario.

            * - :py:attr:`~LINE`
              - Displays a line connecting all sampled points in the trajectory and displays lines from each sampled point in the trajectory to the center of the reference coordinate system in which the trajectory is computed.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import TrajectoryType


