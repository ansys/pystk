IVehicleHPOPSolarRadiationPressureOptions
=========================================

.. py:class:: IVehicleHPOPSolarRadiationPressureOptions

   object
   
   Interface for additional solar radiation pressure options.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~method_to_compute_sun_position`
            * - :py:meth:`~atmos_altitude_of_earth_shape_for_eclipse`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleHPOPSolarRadiationPressureOptions


Property detail
---------------

.. py:property:: method_to_compute_sun_position
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPSolarRadiationPressureOptions.method_to_compute_sun_position
    :type: METHOD_TO_COMPUTE_SUN_POSITION

    Specifies the direction of the Sun for SRP computations.

.. py:property:: atmos_altitude_of_earth_shape_for_eclipse
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPSolarRadiationPressureOptions.atmos_altitude_of_earth_shape_for_eclipse
    :type: float

    Atmospheric altitude for the shape of the Earth for eclipses. Uses Distance Dimension.


