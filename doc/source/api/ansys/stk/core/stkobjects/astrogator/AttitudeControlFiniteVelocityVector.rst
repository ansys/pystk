AttitudeControlFiniteVelocityVector
===================================

.. py:class:: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteVelocityVector

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFinite`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControl`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The velocity vector attitude control for a finite maneuver.

.. py:currentmodule:: AttitudeControlFiniteVelocityVector

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteVelocityVector.attitude_update`
              - How and when the attitude will be updated.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteVelocityVector.body_constraint_vector`
              - Defines a constraint vector in spacecraft body coordinates to complete the attitude definition.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import AttitudeControlFiniteVelocityVector


Property detail
---------------

.. py:property:: attitude_update
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteVelocityVector.attitude_update
    :type: ATTITUDE_UPDATE

    How and when the attitude will be updated.

.. py:property:: body_constraint_vector
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteVelocityVector.body_constraint_vector
    :type: IDirection

    Defines a constraint vector in spacecraft body coordinates to complete the attitude definition.


