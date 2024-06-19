IAttitudeControlFiniteThrustVector
==================================

.. py:class:: IAttitudeControlFiniteThrustVector

   IAttitudeControlFinite
   
   Properties for the Thrust Vector attitude control for a Finite Maneuver.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~attitude_update`
            * - :py:meth:`~thrust_axes_name`
            * - :py:meth:`~body_constraint_vector`
            * - :py:meth:`~thrust_vector`


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
    :type: IAgDirection

    Defines a constraint vector in spacecraft body coordinates to complete the attitude definition.

.. py:property:: thrust_vector
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteThrustVector.thrust_vector
    :type: IAgDirection

    Defines the thrust vector in the reference axes.


