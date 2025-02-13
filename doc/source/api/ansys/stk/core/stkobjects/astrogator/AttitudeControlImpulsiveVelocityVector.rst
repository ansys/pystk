AttitudeControlImpulsiveVelocityVector
======================================

.. py:class:: ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveVelocityVector

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsive`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControl`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The velocity vector attitude control for an impulsive maneuver.

.. py:currentmodule:: AttitudeControlImpulsiveVelocityVector

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveVelocityVector.delta_v_magnitude`
              - Get or set the size of the delta-V to be applied to the orbit along the velocity vector. Uses Rate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveVelocityVector.body_constraint_vector`
              - Define a constraint vector in spacecraft body coordinates to complete the attitude definition.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import AttitudeControlImpulsiveVelocityVector


Property detail
---------------

.. py:property:: delta_v_magnitude
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveVelocityVector.delta_v_magnitude
    :type: float

    Get or set the size of the delta-V to be applied to the orbit along the velocity vector. Uses Rate Dimension.

.. py:property:: body_constraint_vector
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveVelocityVector.body_constraint_vector
    :type: IDirection

    Define a constraint vector in spacecraft body coordinates to complete the attitude definition.


