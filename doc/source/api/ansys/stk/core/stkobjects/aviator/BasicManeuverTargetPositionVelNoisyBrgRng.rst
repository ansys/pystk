BasicManeuverTargetPositionVelNoisyBrgRng
=========================================

.. py:class:: ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelNoisyBrgRng

   Bases: 

   Class defining the position and velocity strategy, Noisy Bearing Range.

.. py:currentmodule:: BasicManeuverTargetPositionVelNoisyBrgRng

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelNoisyBrgRng.new_random_engine_seed`
              - Generate a new random engine seed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelNoisyBrgRng.apply_position_vel`
              - Apply the current position velocity strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelNoisyBrgRng.cancel_position_vel`
              - Cancel the current position velocity strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelNoisyBrgRng.set_base_dyn_state_link_name`
              - Set the BaseDynStateLinkName.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelNoisyBrgRng.smoothing_constant`
              - Gets or sets the smoothing constant property.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelNoisyBrgRng.velocity_time_step`
              - Gets or sets the velocity time step property.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelNoisyBrgRng.angle_error_std_dev`
              - Gets or sets the angle error standard deviation property.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelNoisyBrgRng.range_error_std_dev`
              - Gets or sets the range error standard deviation property.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import BasicManeuverTargetPositionVelNoisyBrgRng


Property detail
---------------

.. py:property:: smoothing_constant
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelNoisyBrgRng.smoothing_constant
    :type: float

    Gets or sets the smoothing constant property.

.. py:property:: velocity_time_step
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelNoisyBrgRng.velocity_time_step
    :type: float

    Gets or sets the velocity time step property.

.. py:property:: angle_error_std_dev
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelNoisyBrgRng.angle_error_std_dev
    :type: float

    Gets or sets the angle error standard deviation property.

.. py:property:: range_error_std_dev
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelNoisyBrgRng.range_error_std_dev
    :type: float

    Gets or sets the range error standard deviation property.


Method detail
-------------

.. py:method:: new_random_engine_seed(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelNoisyBrgRng.new_random_engine_seed

    Generate a new random engine seed.

    :Returns:

        :obj:`~None`









.. py:method:: apply_position_vel(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelNoisyBrgRng.apply_position_vel

    Apply the current position velocity strategy.

    :Returns:

        :obj:`~None`

.. py:method:: cancel_position_vel(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelNoisyBrgRng.cancel_position_vel

    Cancel the current position velocity strategy.

    :Returns:

        :obj:`~None`

.. py:method:: set_base_dyn_state_link_name(self, newVal: str) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelNoisyBrgRng.set_base_dyn_state_link_name

    Set the BaseDynStateLinkName.

    :Parameters:

    **newVal** : :obj:`~str`

    :Returns:

        :obj:`~None`

