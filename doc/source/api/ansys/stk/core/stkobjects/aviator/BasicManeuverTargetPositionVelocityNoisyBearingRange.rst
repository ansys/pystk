BasicManeuverTargetPositionVelocityNoisyBearingRange
====================================================

.. py:class:: ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocityNoisyBearingRange

   Class defining the position and velocity strategy, Noisy Bearing Range.

.. py:currentmodule:: BasicManeuverTargetPositionVelocityNoisyBearingRange

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocityNoisyBearingRange.new_random_engine_seed`
              - Generate a new random engine seed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocityNoisyBearingRange.apply_position_velocity`
              - Apply the current position velocity strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocityNoisyBearingRange.cancel_position_velocity`
              - Cancel the current position velocity strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocityNoisyBearingRange.set_base_dynamic_state_link_name`
              - Set the BaseDynStateLinkName.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocityNoisyBearingRange.smoothing_constant`
              - Get or set the smoothing constant property.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocityNoisyBearingRange.velocity_time_step`
              - Get or set the velocity time step property.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocityNoisyBearingRange.angle_error_std_dev`
              - Get or set the angle error standard deviation property.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocityNoisyBearingRange.range_error_std_dev`
              - Get or set the range error standard deviation property.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import BasicManeuverTargetPositionVelocityNoisyBearingRange


Property detail
---------------

.. py:property:: smoothing_constant
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocityNoisyBearingRange.smoothing_constant
    :type: float

    Get or set the smoothing constant property.

.. py:property:: velocity_time_step
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocityNoisyBearingRange.velocity_time_step
    :type: float

    Get or set the velocity time step property.

.. py:property:: angle_error_std_dev
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocityNoisyBearingRange.angle_error_std_dev
    :type: float

    Get or set the angle error standard deviation property.

.. py:property:: range_error_std_dev
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocityNoisyBearingRange.range_error_std_dev
    :type: float

    Get or set the range error standard deviation property.


Method detail
-------------

.. py:method:: new_random_engine_seed(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocityNoisyBearingRange.new_random_engine_seed

    Generate a new random engine seed.

    :Returns:

        :obj:`~None`









.. py:method:: apply_position_velocity(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocityNoisyBearingRange.apply_position_velocity

    Apply the current position velocity strategy.

    :Returns:

        :obj:`~None`

.. py:method:: cancel_position_velocity(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocityNoisyBearingRange.cancel_position_velocity

    Cancel the current position velocity strategy.

    :Returns:

        :obj:`~None`

.. py:method:: set_base_dynamic_state_link_name(self, value: str) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocityNoisyBearingRange.set_base_dynamic_state_link_name

    Set the BaseDynStateLinkName.

    :Parameters:

        **value** : :obj:`~str`


    :Returns:

        :obj:`~None`

