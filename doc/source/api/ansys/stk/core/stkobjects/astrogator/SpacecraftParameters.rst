SpacecraftParameters
====================

.. py:class:: ansys.stk.core.stkobjects.astrogator.SpacecraftParameters

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   Spacecraft parameters.

.. py:currentmodule:: SpacecraftParameters

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SpacecraftParameters.dry_mass`
              - Gets or sets the mass of the spacecraft exclusive of propellant. Uses Mass Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SpacecraftParameters.cd`
              - Gets or sets the dimensionless drag coefficient associated with the drag area. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SpacecraftParameters.drag_area`
              - Gets or sets the cross-sectional area of the spacecraft assumed perpendicular to the direction of motion, used for atmospheric drag calculations. Uses SmallArea Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SpacecraftParameters.cr`
              - Gets or sets the reflectivity of the spacecraft used for solar radiation pressure calculations, where 2.0 is fully reflective and 1.0 is not reflective at all. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SpacecraftParameters.solar_radiation_pressure_area`
              - Gets or sets the cross-sectional area of the spacecraft assumed perpendicular to the direction of solar radiation, used for solar radiation calculations. Uses SmallArea Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SpacecraftParameters.ck`
              - Gets or sets the reflectivity of the spacecraft used for central body radiation pressure (albedo / thermal pressure) calculations, where 2.0 is fully reflective and 1.0 is not reflective at all. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SpacecraftParameters.radiation_pressure_area`
              - Gets or sets the cross-sectional area of the spacecraft assumed perpendicular to the direction of central body radiation, used for central body radiation (albedo / thermal pressure) calculations. Uses SmallArea Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SpacecraftParameters.k1`
              - If you are using a non-spherical SRP model, this field defines the model's GPS solar radiation pressure K1 (scale) value. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SpacecraftParameters.k2`
              - If you are using a non-spherical SRP model, this field defines the model's GPS solar radiation pressure K2 (scale) value. Dimensionless.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import SpacecraftParameters


Property detail
---------------

.. py:property:: dry_mass
    :canonical: ansys.stk.core.stkobjects.astrogator.SpacecraftParameters.dry_mass
    :type: float

    Gets or sets the mass of the spacecraft exclusive of propellant. Uses Mass Dimension.

.. py:property:: cd
    :canonical: ansys.stk.core.stkobjects.astrogator.SpacecraftParameters.cd
    :type: float

    Gets or sets the dimensionless drag coefficient associated with the drag area. Dimensionless.

.. py:property:: drag_area
    :canonical: ansys.stk.core.stkobjects.astrogator.SpacecraftParameters.drag_area
    :type: float

    Gets or sets the cross-sectional area of the spacecraft assumed perpendicular to the direction of motion, used for atmospheric drag calculations. Uses SmallArea Dimension.

.. py:property:: cr
    :canonical: ansys.stk.core.stkobjects.astrogator.SpacecraftParameters.cr
    :type: float

    Gets or sets the reflectivity of the spacecraft used for solar radiation pressure calculations, where 2.0 is fully reflective and 1.0 is not reflective at all. Dimensionless.

.. py:property:: solar_radiation_pressure_area
    :canonical: ansys.stk.core.stkobjects.astrogator.SpacecraftParameters.solar_radiation_pressure_area
    :type: float

    Gets or sets the cross-sectional area of the spacecraft assumed perpendicular to the direction of solar radiation, used for solar radiation calculations. Uses SmallArea Dimension.

.. py:property:: ck
    :canonical: ansys.stk.core.stkobjects.astrogator.SpacecraftParameters.ck
    :type: float

    Gets or sets the reflectivity of the spacecraft used for central body radiation pressure (albedo / thermal pressure) calculations, where 2.0 is fully reflective and 1.0 is not reflective at all. Dimensionless.

.. py:property:: radiation_pressure_area
    :canonical: ansys.stk.core.stkobjects.astrogator.SpacecraftParameters.radiation_pressure_area
    :type: float

    Gets or sets the cross-sectional area of the spacecraft assumed perpendicular to the direction of central body radiation, used for central body radiation (albedo / thermal pressure) calculations. Uses SmallArea Dimension.

.. py:property:: k1
    :canonical: ansys.stk.core.stkobjects.astrogator.SpacecraftParameters.k1
    :type: float

    If you are using a non-spherical SRP model, this field defines the model's GPS solar radiation pressure K1 (scale) value. Dimensionless.

.. py:property:: k2
    :canonical: ansys.stk.core.stkobjects.astrogator.SpacecraftParameters.k2
    :type: float

    If you are using a non-spherical SRP model, this field defines the model's GPS solar radiation pressure K2 (scale) value. Dimensionless.


