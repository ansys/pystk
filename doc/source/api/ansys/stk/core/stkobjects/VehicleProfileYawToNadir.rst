VehicleProfileYawToNadir
========================

.. py:class:: ansys.stk.core.stkobjects.VehicleProfileYawToNadir

   Bases: :py:class:`~ansys.stk.core.stkobjects.IVehicleAttitudeProfile`

   A profile useful for satellites with highly elliptical orbits.

.. py:currentmodule:: VehicleProfileYawToNadir

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleProfileYawToNadir.inertial`
              - Get the body-fixed Z axis is fixed in inertial space using the selected coordinate type. The X axis is then constrained, via motion in the yaw sense about the body-fixed Z axis, toward the nadir direction.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleProfileYawToNadir


Property detail
---------------

.. py:property:: inertial
    :canonical: ansys.stk.core.stkobjects.VehicleProfileYawToNadir.inertial
    :type: IDirection

    Get the body-fixed Z axis is fixed in inertial space using the selected coordinate type. The X axis is then constrained, via motion in the yaw sense about the body-fixed Z axis, toward the nadir direction.


