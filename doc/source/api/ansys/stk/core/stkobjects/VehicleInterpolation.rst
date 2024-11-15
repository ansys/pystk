VehicleInterpolation
====================

.. py:class:: ansys.stk.core.stkobjects.VehicleInterpolation

   Class defining interpolation for the HPOP integrator.

.. py:currentmodule:: VehicleInterpolation

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleInterpolation.method`
              - Gets or sets the interpolation method.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleInterpolation.vop_mu`
              - Gets or sets the gravitational parameter used by the VOP method, in the range 1.993002209e+14 to 7.972008836e+14 for Earth based vehicles. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleInterpolation.order`
              - Interpolation order. Dimensionless.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleInterpolation


Property detail
---------------

.. py:property:: method
    :canonical: ansys.stk.core.stkobjects.VehicleInterpolation.method
    :type: VEHICLE_INTERPOLATION_METHOD

    Gets or sets the interpolation method.

.. py:property:: vop_mu
    :canonical: ansys.stk.core.stkobjects.VehicleInterpolation.vop_mu
    :type: float

    Gets or sets the gravitational parameter used by the VOP method, in the range 1.993002209e+14 to 7.972008836e+14 for Earth based vehicles. Dimensionless.

.. py:property:: order
    :canonical: ansys.stk.core.stkobjects.VehicleInterpolation.order
    :type: int

    Interpolation order. Dimensionless.


