AttitudeControlFiniteThrustVector
=================================

.. py:class:: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteThrustVector

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFinite`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControl`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The thrust vector attitude control for a finite maneuver.

.. py:currentmodule:: AttitudeControlFiniteThrustVector

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteThrustVector.attitude_update`
              - How and when the attitude will be updated.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteThrustVector.thrust_axes_name`
              - Get or set the thrust axes.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteThrustVector.body_constraint_vector`
              - Define a constraint vector in spacecraft body coordinates to complete the attitude definition.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteThrustVector.thrust_vector`
              - Define the thrust vector in the reference axes.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import AttitudeControlFiniteThrustVector


Property detail
---------------

.. py:property:: attitude_update
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteThrustVector.attitude_update
    :type: AttitudeUpdate

    How and when the attitude will be updated.

.. py:property:: thrust_axes_name
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteThrustVector.thrust_axes_name
    :type: str

    Get or set the thrust axes.

.. py:property:: body_constraint_vector
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteThrustVector.body_constraint_vector
    :type: IDirection

    Define a constraint vector in spacecraft body coordinates to complete the attitude definition.

.. py:property:: thrust_vector
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteThrustVector.thrust_vector
    :type: IDirection

    Define the thrust vector in the reference axes.


