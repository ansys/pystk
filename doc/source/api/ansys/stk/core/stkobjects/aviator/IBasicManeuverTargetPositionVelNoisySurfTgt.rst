IBasicManeuverTargetPositionVelNoisySurfTgt
===========================================

.. py:class:: ansys.stk.core.stkobjects.aviator.IBasicManeuverTargetPositionVelNoisySurfTgt

   object
   
   Interface used to access target position and velocity strategy, Surf Tgt Pos Vel.

.. py:currentmodule:: IBasicManeuverTargetPositionVelNoisySurfTgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverTargetPositionVelNoisySurfTgt.new_random_engine_seed`
              - Generate a new random engine seed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverTargetPositionVelNoisySurfTgt.apply_position_vel`
              - Apply the current position velocity strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverTargetPositionVelNoisySurfTgt.cancel_position_vel`
              - Cancel the current position velocity strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverTargetPositionVelNoisySurfTgt.set_base_dyn_state_link_name`
              - Set the BaseDynStateLinkName.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverTargetPositionVelNoisySurfTgt.measurement_time_step`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverTargetPositionVelNoisySurfTgt.position_cep`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverTargetPositionVelNoisySurfTgt.course_error`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverTargetPositionVelNoisySurfTgt.speed_error`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IBasicManeuverTargetPositionVelNoisySurfTgt


Property detail
---------------

.. py:property:: measurement_time_step
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverTargetPositionVelNoisySurfTgt.measurement_time_step
    :type: float

    Gets or sets the measurement time step property.

.. py:property:: position_cep
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverTargetPositionVelNoisySurfTgt.position_cep
    :type: float

    Gets or sets the position CEP property.

.. py:property:: course_error
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverTargetPositionVelNoisySurfTgt.course_error
    :type: float

    Gets or sets the course error property.

.. py:property:: speed_error
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverTargetPositionVelNoisySurfTgt.speed_error
    :type: float

    Gets or sets the speed error property.


Method detail
-------------

.. py:method:: new_random_engine_seed(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverTargetPositionVelNoisySurfTgt.new_random_engine_seed

    Generate a new random engine seed.

    :Returns:

        :obj:`~None`









.. py:method:: apply_position_vel(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverTargetPositionVelNoisySurfTgt.apply_position_vel

    Apply the current position velocity strategy.

    :Returns:

        :obj:`~None`

.. py:method:: cancel_position_vel(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverTargetPositionVelNoisySurfTgt.cancel_position_vel

    Cancel the current position velocity strategy.

    :Returns:

        :obj:`~None`

.. py:method:: set_base_dyn_state_link_name(self, newVal: str) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverTargetPositionVelNoisySurfTgt.set_base_dyn_state_link_name

    Set the BaseDynStateLinkName.

    :Parameters:

    **newVal** : :obj:`~str`

    :Returns:

        :obj:`~None`

