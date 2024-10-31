RadiationPressure
=================

.. py:class:: ansys.stk.core.stkobjects.RadiationPressure

   Class defining solar radiation pressure on a vehicle.

.. py:currentmodule:: RadiationPressure

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadiationPressure.file`
              - File containing parameters defining a ground reflection model that defines albedo and emissivity properties of the central body surface.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadiationPressure.ck`
              - Coefficient of radiation pressure reflectivity of the satellite. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadiationPressure.area_mass_ratio`
              - Area exposed to radiation pressure (nominally along the radial direction) divided by the mass. Uses AreaPerMass Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadiationPressure.include_albedo`
              - Opt whether to consider albedo effects (i.e., radiation pressure caused by sunlight reflected off the lit part of the central body).
            * - :py:attr:`~ansys.stk.core.stkobjects.RadiationPressure.include_thermal`
              - Opt whether to consider thermal radiation pressure effects (i.e., radiation pressure caused by blackbody heat radiation of the central body).



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RadiationPressure


Property detail
---------------

.. py:property:: file
    :canonical: ansys.stk.core.stkobjects.RadiationPressure.file
    :type: str

    File containing parameters defining a ground reflection model that defines albedo and emissivity properties of the central body surface.

.. py:property:: ck
    :canonical: ansys.stk.core.stkobjects.RadiationPressure.ck
    :type: float

    Coefficient of radiation pressure reflectivity of the satellite. Dimensionless.

.. py:property:: area_mass_ratio
    :canonical: ansys.stk.core.stkobjects.RadiationPressure.area_mass_ratio
    :type: float

    Area exposed to radiation pressure (nominally along the radial direction) divided by the mass. Uses AreaPerMass Dimension.

.. py:property:: include_albedo
    :canonical: ansys.stk.core.stkobjects.RadiationPressure.include_albedo
    :type: bool

    Opt whether to consider albedo effects (i.e., radiation pressure caused by sunlight reflected off the lit part of the central body).

.. py:property:: include_thermal
    :canonical: ansys.stk.core.stkobjects.RadiationPressure.include_thermal
    :type: bool

    Opt whether to consider thermal radiation pressure effects (i.e., radiation pressure caused by blackbody heat radiation of the central body).


