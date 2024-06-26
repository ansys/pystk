ATTITUDE_UPDATE
===============

.. py:class:: ansys.stk.core.stkobjects.astrogator.ATTITUDE_UPDATE

   IntEnum


.. py:currentmodule:: ATTITUDE_UPDATE

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~DURING_BURN`
              - Update during burn - updated throughout the maneuver so as to maintain the required thrust direction. This forces the thrust vector to the specified direction at every instant throughout the burn.

            * - :py:attr:`~INERTIAL_AT_IGNITION`
              - Inertial at ignition - specified by Attitude Control at ignition and remains the same throughout the maneuver. This fixes the thrust direction in the inertial direction calculated at the beginning of the burn and is used for inertially fixed spacecraft.

            * - :py:attr:`~INERTIAL_AT_START`
              - Inertial at start - specified by Attitude Control at the beginning of the maneuver segment and remains the same throughout the maneuver.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ATTITUDE_UPDATE


