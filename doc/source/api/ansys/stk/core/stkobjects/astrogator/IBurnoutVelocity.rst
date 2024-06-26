IBurnoutVelocity
================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IBurnoutVelocity

   object
   
   Properties for the burnout velocity of a Launch segment.

.. py:currentmodule:: IBurnoutVelocity

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IBurnoutVelocity.burnout_option`
              - Select to use the fixed or inertial frame.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IBurnoutVelocity.fixed_velocity`
              - Gets or sets the velocity magnitude . Uses Rate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IBurnoutVelocity.inertial_velocity`
              - Gets or sets the velocity magnitude. Uses Rate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IBurnoutVelocity.inertial_velocity_azimuth`
              - Gets or sets the inertial velocity azimuth. Inertial velocity azimuth is the angle from the projection of north in the local horizontal plane to the inertial velocity vector, right handed. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IBurnoutVelocity.inertial_horizontal_fpa`
              - Inertial horizontal flight path angle is the angle from the local horizontal to the inertial velocity vector, positive towards radius. It is also 90 degrees minus vertical flight path angle. Uses Angle Dimension.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IBurnoutVelocity


Property detail
---------------

.. py:property:: burnout_option
    :canonical: ansys.stk.core.stkobjects.astrogator.IBurnoutVelocity.burnout_option
    :type: BURNOUT_OPTIONS

    Select to use the fixed or inertial frame.

.. py:property:: fixed_velocity
    :canonical: ansys.stk.core.stkobjects.astrogator.IBurnoutVelocity.fixed_velocity
    :type: float

    Gets or sets the velocity magnitude . Uses Rate Dimension.

.. py:property:: inertial_velocity
    :canonical: ansys.stk.core.stkobjects.astrogator.IBurnoutVelocity.inertial_velocity
    :type: float

    Gets or sets the velocity magnitude. Uses Rate Dimension.

.. py:property:: inertial_velocity_azimuth
    :canonical: ansys.stk.core.stkobjects.astrogator.IBurnoutVelocity.inertial_velocity_azimuth
    :type: typing.Any

    Gets or sets the inertial velocity azimuth. Inertial velocity azimuth is the angle from the projection of north in the local horizontal plane to the inertial velocity vector, right handed. Uses Angle Dimension.

.. py:property:: inertial_horizontal_fpa
    :canonical: ansys.stk.core.stkobjects.astrogator.IBurnoutVelocity.inertial_horizontal_fpa
    :type: typing.Any

    Inertial horizontal flight path angle is the angle from the local horizontal to the inertial velocity vector, positive towards radius. It is also 90 degrees minus vertical flight path angle. Uses Angle Dimension.


