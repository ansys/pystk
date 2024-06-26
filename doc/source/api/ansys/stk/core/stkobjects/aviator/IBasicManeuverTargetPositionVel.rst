IBasicManeuverTargetPositionVel
===============================

.. py:class:: ansys.stk.core.stkobjects.aviator.IBasicManeuverTargetPositionVel

   object
   
   Interface used to access target position and velocity strategies for basic maneuvers.

.. py:currentmodule:: IBasicManeuverTargetPositionVel

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverTargetPositionVel.apply_position_vel`
              - Apply the current position velocity strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverTargetPositionVel.cancel_position_vel`
              - Cancel the current position velocity strategy.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverTargetPositionVel.target_position_vel_type`
              - Gets or sets the target pos vel type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverTargetPositionVel.target_position_vel_type_string`
              - Gets or sets the target pos vel as a string value. Use this for custom models.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverTargetPositionVel.mode_as_noisy_brg_rng`
              - Get the options for a noisy bearing range velocity strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverTargetPositionVel.mode_as_noisy_surf_tgt`
              - Get the options for a noisy surface target position velocity strategy.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IBasicManeuverTargetPositionVel


Property detail
---------------

.. py:property:: target_position_vel_type
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverTargetPositionVel.target_position_vel_type
    :type: TARGET_POSITION_VEL_TYPE

    Gets or sets the target pos vel type.

.. py:property:: target_position_vel_type_string
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverTargetPositionVel.target_position_vel_type_string
    :type: str

    Gets or sets the target pos vel as a string value. Use this for custom models.

.. py:property:: mode_as_noisy_brg_rng
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverTargetPositionVel.mode_as_noisy_brg_rng
    :type: IBasicManeuverTargetPositionVelNoisyBrgRng

    Get the options for a noisy bearing range velocity strategy.

.. py:property:: mode_as_noisy_surf_tgt
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverTargetPositionVel.mode_as_noisy_surf_tgt
    :type: IBasicManeuverTargetPositionVelNoisySurfTgt

    Get the options for a noisy surface target position velocity strategy.


Method detail
-------------







.. py:method:: apply_position_vel(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverTargetPositionVel.apply_position_vel

    Apply the current position velocity strategy.

    :Returns:

        :obj:`~None`

.. py:method:: cancel_position_vel(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverTargetPositionVel.cancel_position_vel

    Cancel the current position velocity strategy.

    :Returns:

        :obj:`~None`

