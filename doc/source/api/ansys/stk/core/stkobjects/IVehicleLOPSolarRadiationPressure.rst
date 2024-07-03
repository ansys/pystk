IVehicleLOPSolarRadiationPressure
=================================

.. py:class:: ansys.stk.core.stkobjects.IVehicleLOPSolarRadiationPressure

   object
   
   Solar radiation pressure interface for LOP propagator.

.. py:currentmodule:: IVehicleLOPSolarRadiationPressure

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleLOPSolarRadiationPressure.use`
              - Opt whether to use SRP.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleLOPSolarRadiationPressure.cp`
              - Gets or sets the solar radiation pressure coefficient. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleLOPSolarRadiationPressure.atmos_height`
              - Height of atmosphere blockage used when calculating shadow entry and exit in solar radiation computations. Uses Distance Dimension.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleLOPSolarRadiationPressure


Property detail
---------------

.. py:property:: use
    :canonical: ansys.stk.core.stkobjects.IVehicleLOPSolarRadiationPressure.use
    :type: bool

    Opt whether to use SRP.

.. py:property:: cp
    :canonical: ansys.stk.core.stkobjects.IVehicleLOPSolarRadiationPressure.cp
    :type: float

    Gets or sets the solar radiation pressure coefficient. Dimensionless.

.. py:property:: atmos_height
    :canonical: ansys.stk.core.stkobjects.IVehicleLOPSolarRadiationPressure.atmos_height
    :type: float

    Height of atmosphere blockage used when calculating shadow entry and exit in solar radiation computations. Uses Distance Dimension.


