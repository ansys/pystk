IBasicManeuverTargetPositionVelNoisyBrgRng
==========================================

.. py:class:: IBasicManeuverTargetPositionVelNoisyBrgRng

   object
   
   Interface used to access target position and velocity strategy, NoisyBrnRng.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~new_random_engine_seed`
              - Generate a new random engine seed.
            * - :py:meth:`~apply_position_vel`
              - Apply the current position velocity strategy.
            * - :py:meth:`~cancel_position_vel`
              - Cancel the current position velocity strategy.
            * - :py:meth:`~set_base_dyn_state_link_name`
              - Set the BaseDynStateLinkName.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~smoothing_constant`
            * - :py:meth:`~velocity_time_step`
            * - :py:meth:`~angle_error_std_dev`
            * - :py:meth:`~range_error_std_dev`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IBasicManeuverTargetPositionVelNoisyBrgRng


Property detail
---------------

.. py:property:: smoothing_constant
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverTargetPositionVelNoisyBrgRng.smoothing_constant
    :type: float

    Gets or sets the smoothing constant property.

.. py:property:: velocity_time_step
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverTargetPositionVelNoisyBrgRng.velocity_time_step
    :type: float

    Gets or sets the velocity time step property.

.. py:property:: angle_error_std_dev
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverTargetPositionVelNoisyBrgRng.angle_error_std_dev
    :type: float

    Gets or sets the angle error standard deviation property.

.. py:property:: range_error_std_dev
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverTargetPositionVelNoisyBrgRng.range_error_std_dev
    :type: float

    Gets or sets the range error standard deviation property.


Method detail
-------------

.. py:method:: new_random_engine_seed(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverTargetPositionVelNoisyBrgRng.new_random_engine_seed

    Generate a new random engine seed.

    :Returns:

        :obj:`~None`









.. py:method:: apply_position_vel(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverTargetPositionVelNoisyBrgRng.apply_position_vel

    Apply the current position velocity strategy.

    :Returns:

        :obj:`~None`

.. py:method:: cancel_position_vel(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverTargetPositionVelNoisyBrgRng.cancel_position_vel

    Cancel the current position velocity strategy.

    :Returns:

        :obj:`~None`

.. py:method:: set_base_dyn_state_link_name(self, newVal: str) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverTargetPositionVelNoisyBrgRng.set_base_dyn_state_link_name

    Set the BaseDynStateLinkName.

    :Parameters:

    **newVal** : :obj:`~str`

    :Returns:

        :obj:`~None`

