IAttitudeControlFiniteThrustVector
==================================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteThrustVector

   IAttitudeControlFinite
   
   Properties for the Thrust Vector attitude control for a Finite Maneuver.

.. py:currentmodule:: IAttitudeControlFiniteThrustVector

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteThrustVector.attitude_update`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteThrustVector.thrust_axes_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteThrustVector.body_constraint_vector`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteThrustVector.thrust_vector`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IAttitudeControlFiniteThrustVector


Property detail
---------------

.. py:property:: attitude_update
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteThrustVector.attitude_update
    :type: ATTITUDE_UPDATE

    How and when the attitude will be updated.

.. py:property:: thrust_axes_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteThrustVector.thrust_axes_name
    :type: str

    Gets or sets the thrust axes.

.. py:property:: body_constraint_vector
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteThrustVector.body_constraint_vector
    :type: IDirection

    Defines a constraint vector in spacecraft body coordinates to complete the attitude definition.

.. py:property:: thrust_vector
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteThrustVector.thrust_vector
    :type: IDirection

    Defines the thrust vector in the reference axes.


