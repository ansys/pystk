IBasicManeuverTargetPositionVelNoisySurfTgt
===========================================

.. py:class:: IBasicManeuverTargetPositionVelNoisySurfTgt

   object
   
   Interface used to access target position and velocity strategy, Surf Tgt Pos Vel.

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

            * - :py:meth:`~measurement_time_step`
            * - :py:meth:`~position_cep`
            * - :py:meth:`~course_error`
            * - :py:meth:`~speed_error`


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

    Generate a new random engine seed.

    :Returns:

        :obj:`~None`









.. py:method:: apply_position_vel(self) -> None

    Apply the current position velocity strategy.

    :Returns:

        :obj:`~None`

.. py:method:: cancel_position_vel(self) -> None

    Cancel the current position velocity strategy.

    :Returns:

        :obj:`~None`

.. py:method:: set_base_dyn_state_link_name(self, newVal:str) -> None

    Set the BaseDynStateLinkName.

    :Parameters:

    **newVal** : :obj:`~str`

    :Returns:

        :obj:`~None`

