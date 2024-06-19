IVehicleInterpolation
=====================

.. py:class:: IVehicleInterpolation

   object
   
   Interpolation interface.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~method`
            * - :py:meth:`~graphics_3d_pmu`
            * - :py:meth:`~order`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleInterpolation


Property detail
---------------

.. py:property:: method
    :canonical: ansys.stk.core.stkobjects.IVehicleInterpolation.method
    :type: VEHICLE_INTERPOLATION_METHOD

    Gets or sets the interpolation method.

.. py:property:: graphics_3d_pmu
    :canonical: ansys.stk.core.stkobjects.IVehicleInterpolation.graphics_3d_pmu
    :type: float

    Gets or sets the gravitational parameter used by the VOP method, in the range 1.993002209e+14 to 7.972008836e+14 for Earth based vehicles. Dimensionless.

.. py:property:: order
    :canonical: ansys.stk.core.stkobjects.IVehicleInterpolation.order
    :type: int

    Interpolation order. Dimensionless.


