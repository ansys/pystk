VehicleLOPSolarRadiationPressure
================================

.. py:class:: ansys.stk.core.stkobjects.VehicleLOPSolarRadiationPressure

   Class defining the solar radiation pressure model for the LOP propagator.

.. py:currentmodule:: VehicleLOPSolarRadiationPressure

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleLOPSolarRadiationPressure.use`
              - Opt whether to use SRP.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleLOPSolarRadiationPressure.cp`
              - Gets or sets the solar radiation pressure coefficient. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleLOPSolarRadiationPressure.atmos_height`
              - Height of atmosphere blockage used when calculating shadow entry and exit in solar radiation computations. Uses Distance Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleLOPSolarRadiationPressure


Property detail
---------------

.. py:property:: use
    :canonical: ansys.stk.core.stkobjects.VehicleLOPSolarRadiationPressure.use
    :type: bool

    Opt whether to use SRP.

.. py:property:: cp
    :canonical: ansys.stk.core.stkobjects.VehicleLOPSolarRadiationPressure.cp
    :type: float

    Gets or sets the solar radiation pressure coefficient. Dimensionless.

.. py:property:: atmos_height
    :canonical: ansys.stk.core.stkobjects.VehicleLOPSolarRadiationPressure.atmos_height
    :type: float

    Height of atmosphere blockage used when calculating shadow entry and exit in solar radiation computations. Uses Distance Dimension.


