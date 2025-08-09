ScenarioTimeStepType
====================

.. py:class:: ansys.stk.core.stkobjects.ScenarioTimeStepType

   IntEnum


.. py:currentmodule:: ScenarioTimeStepType

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~REAL_TIME`
              - Real time: the scenario animates in real time in accordance with the computer's internal clock.

            * - :py:attr:`~STEP`
              - Time step: the time interval that each animation step represents. The greater this value, the greater the distance a vehicle will move in the 2D and 3D windows each time the screen is refreshed.

            * - :py:attr:`~X_REAL_TIME`
              - X real time: the scenario animates at a specified multiple of real time.

            * - :py:attr:`~ARRAY`
              - Time array increment: the scenario steps through times in the time array at the specified value.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ScenarioTimeStepType


