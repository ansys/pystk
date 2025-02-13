VehicleSlewTimingBetweenTargetType
==================================

.. py:class:: ansys.stk.core.stkobjects.VehicleSlewTimingBetweenTargetType

   IntEnum


.. py:currentmodule:: VehicleSlewTimingBetweenTargetType

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - Unsupported or unknown slew option.

            * - :py:attr:`~OPTIMAL`
              - Change attitude whenever the slew can be performed most efficiently.

            * - :py:attr:`~SLEW_AFTER_TARGET_ACQUISITION`
              - Start slewing toward a new target after it is in view.

            * - :py:attr:`~SLEW_AFTER_TARGET_LOSS`
              - Start slewing away from current target after it is out-of-view.

            * - :py:attr:`~SLEW_BEFORE_TARGET_ACQUISITION`
              - Finish slewing toward a new target before it is in view.

            * - :py:attr:`~SLEW_BEFORE_TARGET_LOSS`
              - Finish slewing away from current target before it is out-of-view.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleSlewTimingBetweenTargetType


