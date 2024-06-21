IAttitudeControlFiniteAntiVelocityVector
========================================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteAntiVelocityVector

   IAttitudeControlFinite
   
   Properties for the Anti-Velocity Vector attitude control for a Finite Maneuver.

.. py:currentmodule:: IAttitudeControlFiniteAntiVelocityVector

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteAntiVelocityVector.attitude_update`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteAntiVelocityVector.body_constraint_vector`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IAttitudeControlFiniteAntiVelocityVector


Property detail
---------------

.. py:property:: attitude_update
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteAntiVelocityVector.attitude_update
    :type: ATTITUDE_UPDATE

    How and when the attitude will be updated.

.. py:property:: body_constraint_vector
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteAntiVelocityVector.body_constraint_vector
    :type: IDirection

    Defines a constraint vector in spacecraft body coordinates to complete the attitude definition.


