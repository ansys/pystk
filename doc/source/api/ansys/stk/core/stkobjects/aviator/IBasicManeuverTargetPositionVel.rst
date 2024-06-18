IBasicManeuverTargetPositionVel
===============================

.. py:class:: IBasicManeuverTargetPositionVel

   object
   
   Interface used to access target position and velocity strategies for basic maneuvers.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~apply_position_vel`
              - Apply the current position velocity strategy.
            * - :py:meth:`~cancel_position_vel`
              - Cancel the current position velocity strategy.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~target_position_vel_type`
            * - :py:meth:`~target_position_vel_type_string`
            * - :py:meth:`~mode_as_noisy_brg_rng`
            * - :py:meth:`~mode_as_noisy_surf_tgt`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IBasicManeuverTargetPositionVel


Property detail
---------------

.. py:property:: target_position_vel_type
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverTargetPositionVel.target_position_vel_type
    :type: "TARGET_POSITION_VEL_TYPE"

    Gets or sets the target pos vel type.

.. py:property:: target_position_vel_type_string
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverTargetPositionVel.target_position_vel_type_string
    :type: str

    Gets or sets the target pos vel as a string value. Use this for custom models.

.. py:property:: mode_as_noisy_brg_rng
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverTargetPositionVel.mode_as_noisy_brg_rng
    :type: "IAgAvtrBasicManeuverTargetPosVelNoisyBrgRng"

    Get the options for a noisy bearing range velocity strategy.

.. py:property:: mode_as_noisy_surf_tgt
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverTargetPositionVel.mode_as_noisy_surf_tgt
    :type: "IAgAvtrBasicManeuverTargetPosVelNoisySurfTgt"

    Get the options for a noisy surface target position velocity strategy.


Method detail
-------------







.. py:method:: apply_position_vel(self) -> None

    Apply the current position velocity strategy.

    :Returns:

        :obj:`~None`

.. py:method:: cancel_position_vel(self) -> None

    Cancel the current position velocity strategy.

    :Returns:

        :obj:`~None`

