BasicManeuverTargetPositionVelNoisySurfTarget
=============================================

.. py:class:: ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelNoisySurfTarget

   Bases: 

   Class defining the position and velocity strategy, Noisy Surface Target.

.. py:currentmodule:: BasicManeuverTargetPositionVelNoisySurfTarget

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelNoisySurfTarget.new_random_engine_seed`
              - Generate a new random engine seed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelNoisySurfTarget.apply_position_vel`
              - Apply the current position velocity strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelNoisySurfTarget.cancel_position_vel`
              - Cancel the current position velocity strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelNoisySurfTarget.set_base_dynamic_state_link_name`
              - Set the BaseDynStateLinkName.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelNoisySurfTarget.measurement_time_step`
              - Gets or sets the measurement time step property.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelNoisySurfTarget.position_cep`
              - Gets or sets the position CEP property.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelNoisySurfTarget.course_error`
              - Gets or sets the course error property.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelNoisySurfTarget.speed_error`
              - Gets or sets the speed error property.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import BasicManeuverTargetPositionVelNoisySurfTarget


Property detail
---------------

.. py:property:: measurement_time_step
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelNoisySurfTarget.measurement_time_step
    :type: float

    Gets or sets the measurement time step property.

.. py:property:: position_cep
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelNoisySurfTarget.position_cep
    :type: float

    Gets or sets the position CEP property.

.. py:property:: course_error
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelNoisySurfTarget.course_error
    :type: float

    Gets or sets the course error property.

.. py:property:: speed_error
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelNoisySurfTarget.speed_error
    :type: float

    Gets or sets the speed error property.


Method detail
-------------

.. py:method:: new_random_engine_seed(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelNoisySurfTarget.new_random_engine_seed

    Generate a new random engine seed.

    :Returns:

        :obj:`~None`









.. py:method:: apply_position_vel(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelNoisySurfTarget.apply_position_vel

    Apply the current position velocity strategy.

    :Returns:

        :obj:`~None`

.. py:method:: cancel_position_vel(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelNoisySurfTarget.cancel_position_vel

    Cancel the current position velocity strategy.

    :Returns:

        :obj:`~None`

.. py:method:: set_base_dynamic_state_link_name(self, newVal: str) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverTargetPositionVelNoisySurfTarget.set_base_dynamic_state_link_name

    Set the BaseDynStateLinkName.

    :Parameters:

    **newVal** : :obj:`~str`

    :Returns:

        :obj:`~None`

