BasicManeuverTargetPositionVelocityNoisySurfTarget
==================================================

.. py:class:: ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocityNoisySurfTarget

   Class defining the position and velocity strategy, Noisy Surface Target.

.. py:currentmodule:: BasicManeuverTargetPositionVelocityNoisySurfTarget

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocityNoisySurfTarget.new_random_engine_seed`
              - Generate a new random engine seed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocityNoisySurfTarget.apply_position_velocity`
              - Apply the current position velocity strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocityNoisySurfTarget.cancel_position_velocity`
              - Cancel the current position velocity strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocityNoisySurfTarget.set_base_dynamic_state_link_name`
              - Set the BaseDynStateLinkName.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocityNoisySurfTarget.measurement_time_step`
              - Get or set the measurement time step property.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocityNoisySurfTarget.position_cep`
              - Get or set the position CEP property.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocityNoisySurfTarget.course_error`
              - Get or set the course error property.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocityNoisySurfTarget.speed_error`
              - Get or set the speed error property.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import BasicManeuverTargetPositionVelocityNoisySurfTarget


Property detail
---------------

.. py:property:: measurement_time_step
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocityNoisySurfTarget.measurement_time_step
    :type: float

    Get or set the measurement time step property.

.. py:property:: position_cep
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocityNoisySurfTarget.position_cep
    :type: float

    Get or set the position CEP property.

.. py:property:: course_error
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocityNoisySurfTarget.course_error
    :type: float

    Get or set the course error property.

.. py:property:: speed_error
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocityNoisySurfTarget.speed_error
    :type: float

    Get or set the speed error property.


Method detail
-------------

.. py:method:: new_random_engine_seed(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocityNoisySurfTarget.new_random_engine_seed

    Generate a new random engine seed.

    :Returns:

        :obj:`~None`









.. py:method:: apply_position_velocity(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocityNoisySurfTarget.apply_position_velocity

    Apply the current position velocity strategy.

    :Returns:

        :obj:`~None`

.. py:method:: cancel_position_velocity(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocityNoisySurfTarget.cancel_position_velocity

    Cancel the current position velocity strategy.

    :Returns:

        :obj:`~None`

.. py:method:: set_base_dynamic_state_link_name(self, value: str) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelocityNoisySurfTarget.set_base_dynamic_state_link_name

    Set the BaseDynStateLinkName.

    :Parameters:

    **value** : :obj:`~str`

    :Returns:

        :obj:`~None`

