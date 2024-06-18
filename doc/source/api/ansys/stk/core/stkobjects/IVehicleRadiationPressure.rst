IVehicleRadiationPressure
=========================

.. py:class:: IVehicleRadiationPressure

   object
   
   Interface for additional radiation pressure options.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~file`
            * - :py:meth:`~ck`
            * - :py:meth:`~area_mass_ratio`
            * - :py:meth:`~include_albedo`
            * - :py:meth:`~include_thermal`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleRadiationPressure


Property detail
---------------

.. py:property:: file
    :canonical: ansys.stk.core.stkobjects.IVehicleRadiationPressure.file
    :type: str

    File containing parameters defining a ground reflection model that defines albedo and emissivity properties of the central body surface.

.. py:property:: ck
    :canonical: ansys.stk.core.stkobjects.IVehicleRadiationPressure.ck
    :type: float

    Coefficient of radiation pressure reflectivity of the satellite. Dimensionless.

.. py:property:: area_mass_ratio
    :canonical: ansys.stk.core.stkobjects.IVehicleRadiationPressure.area_mass_ratio
    :type: float

    Area exposed to radiation pressure (nominally along the radial direction) divided by the mass. Uses AreaPerMass Dimension.

.. py:property:: include_albedo
    :canonical: ansys.stk.core.stkobjects.IVehicleRadiationPressure.include_albedo
    :type: bool

    Opt whether to consider albedo effects (i.e., radiation pressure caused by sunlight reflected off the lit part of the central body).

.. py:property:: include_thermal
    :canonical: ansys.stk.core.stkobjects.IVehicleRadiationPressure.include_thermal
    :type: bool

    Opt whether to consider thermal radiation pressure effects (i.e., radiation pressure caused by blackbody heat radiation of the central body).


