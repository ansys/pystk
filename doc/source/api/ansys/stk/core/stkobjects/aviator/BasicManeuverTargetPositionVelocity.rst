BasicManeuverTargetPositionVelocity
===================================

.. py:class:: ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocity

   Class defining the target position and velocity strategies for basic maneuvers.

.. py:currentmodule:: BasicManeuverTargetPositionVelocity

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocity.apply_position_velocity`
              - Apply the current position velocity strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocity.cancel_position_velocity`
              - Cancel the current position velocity strategy.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocity.target_position_velocity_type`
              - Get or set the target pos vel type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocity.target_position_velocity_type_string`
              - Get or set the target pos vel as a string value. Use this for custom models.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocity.mode_as_noisy_bearing_range`
              - Get the options for a noisy bearing range velocity strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocity.mode_as_noisy_surf_target`
              - Get the options for a noisy surface target position velocity strategy.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import BasicManeuverTargetPositionVelocity


Property detail
---------------

.. py:property:: target_position_velocity_type
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocity.target_position_velocity_type
    :type: TargetPositionVelocityType

    Get or set the target pos vel type.

.. py:property:: target_position_velocity_type_string
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocity.target_position_velocity_type_string
    :type: str

    Get or set the target pos vel as a string value. Use this for custom models.

.. py:property:: mode_as_noisy_bearing_range
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocity.mode_as_noisy_bearing_range
    :type: BasicManeuverTargetPositionVelocityNoisyBearingRange

    Get the options for a noisy bearing range velocity strategy.

.. py:property:: mode_as_noisy_surf_target
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocity.mode_as_noisy_surf_target
    :type: BasicManeuverTargetPositionVelocityNoisySurfTarget

    Get the options for a noisy surface target position velocity strategy.


Method detail
-------------







.. py:method:: apply_position_velocity(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocity.apply_position_velocity

    Apply the current position velocity strategy.

    :Returns:

        :obj:`~None`

.. py:method:: cancel_position_velocity(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocity.cancel_position_velocity

    Cancel the current position velocity strategy.

    :Returns:

        :obj:`~None`

