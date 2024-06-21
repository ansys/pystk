IVehicleProfileYawToNadir
=========================

.. py:class:: ansys.stk.core.stkobjects.IVehicleProfileYawToNadir

   IVehicleAttitudeProfile
   
   A profile useful for satellites with highly elliptical orbits.

.. py:currentmodule:: IVehicleProfileYawToNadir

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleProfileYawToNadir.inertial`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleProfileYawToNadir


Property detail
---------------

.. py:property:: inertial
    :canonical: ansys.stk.core.stkobjects.IVehicleProfileYawToNadir.inertial
    :type: IDirection

    Get the body-fixed Z axis is fixed in inertial space using the selected coordinate type. The X axis is then constrained, via motion in the yaw sense about the body-fixed Z axis, toward the nadir direction.


