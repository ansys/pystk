VehicleRadiationPressure
========================

.. py:class:: ansys.stk.core.stkobjects.VehicleRadiationPressure

   Bases: 

   Class defining solar radiation pressure on a vehicle.

.. py:currentmodule:: VehicleRadiationPressure

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleRadiationPressure.file`
              - File containing parameters defining a ground reflection model that defines albedo and emissivity properties of the central body surface.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleRadiationPressure.ck`
              - Coefficient of radiation pressure reflectivity of the satellite. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleRadiationPressure.area_mass_ratio`
              - Area exposed to radiation pressure (nominally along the radial direction) divided by the mass. Uses AreaPerMass Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleRadiationPressure.include_albedo`
              - Opt whether to consider albedo effects (i.e., radiation pressure caused by sunlight reflected off the lit part of the central body).
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleRadiationPressure.include_thermal`
              - Opt whether to consider thermal radiation pressure effects (i.e., radiation pressure caused by blackbody heat radiation of the central body).



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleRadiationPressure


Property detail
---------------

.. py:property:: file
    :canonical: ansys.stk.core.stkobjects.VehicleRadiationPressure.file
    :type: str

    File containing parameters defining a ground reflection model that defines albedo and emissivity properties of the central body surface.

.. py:property:: ck
    :canonical: ansys.stk.core.stkobjects.VehicleRadiationPressure.ck
    :type: float

    Coefficient of radiation pressure reflectivity of the satellite. Dimensionless.

.. py:property:: area_mass_ratio
    :canonical: ansys.stk.core.stkobjects.VehicleRadiationPressure.area_mass_ratio
    :type: float

    Area exposed to radiation pressure (nominally along the radial direction) divided by the mass. Uses AreaPerMass Dimension.

.. py:property:: include_albedo
    :canonical: ansys.stk.core.stkobjects.VehicleRadiationPressure.include_albedo
    :type: bool

    Opt whether to consider albedo effects (i.e., radiation pressure caused by sunlight reflected off the lit part of the central body).

.. py:property:: include_thermal
    :canonical: ansys.stk.core.stkobjects.VehicleRadiationPressure.include_thermal
    :type: bool

    Opt whether to consider thermal radiation pressure effects (i.e., radiation pressure caused by blackbody heat radiation of the central body).


