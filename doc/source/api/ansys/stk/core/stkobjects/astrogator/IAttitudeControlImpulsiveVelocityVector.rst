IAttitudeControlImpulsiveVelocityVector
=======================================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveVelocityVector

   IAttitudeControlImpulsive
   
   Properties for the Velocity Vector attitude control for an Impulsive Maneuver.

.. py:currentmodule:: IAttitudeControlImpulsiveVelocityVector

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveVelocityVector.delta_v_magnitude`
              - Gets or sets the size of the delta-V to be applied to the orbit along the velocity vector. Uses Rate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveVelocityVector.body_constraint_vector`
              - Defines a constraint vector in spacecraft body coordinates to complete the attitude definition.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IAttitudeControlImpulsiveVelocityVector


Property detail
---------------

.. py:property:: delta_v_magnitude
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveVelocityVector.delta_v_magnitude
    :type: float

    Gets or sets the size of the delta-V to be applied to the orbit along the velocity vector. Uses Rate Dimension.

.. py:property:: body_constraint_vector
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveVelocityVector.body_constraint_vector
    :type: IDirection

    Defines a constraint vector in spacecraft body coordinates to complete the attitude definition.


