ISpacecraftParameters
=====================

.. py:class:: ISpacecraftParameters

   object
   
   Properties for spacecraft configuration.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~dry_mass`
            * - :py:meth:`~cd`
            * - :py:meth:`~drag_area`
            * - :py:meth:`~cr`
            * - :py:meth:`~solar_radiation_pressure_area`
            * - :py:meth:`~ck`
            * - :py:meth:`~radiation_pressure_area`
            * - :py:meth:`~k1`
            * - :py:meth:`~k2`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ISpacecraftParameters


Property detail
---------------

.. py:property:: dry_mass
    :canonical: ansys.stk.core.stkobjects.astrogator.ISpacecraftParameters.dry_mass
    :type: float

    Gets or sets the mass of the spacecraft exclusive of propellant. Uses Mass Dimension.

.. py:property:: cd
    :canonical: ansys.stk.core.stkobjects.astrogator.ISpacecraftParameters.cd
    :type: float

    Gets or sets the dimensionless drag coefficient associated with the drag area. Dimensionless.

.. py:property:: drag_area
    :canonical: ansys.stk.core.stkobjects.astrogator.ISpacecraftParameters.drag_area
    :type: float

    Gets or sets the cross-sectional area of the spacecraft assumed perpendicular to the direction of motion, used for atmospheric drag calculations. Uses SmallArea Dimension.

.. py:property:: cr
    :canonical: ansys.stk.core.stkobjects.astrogator.ISpacecraftParameters.cr
    :type: float

    Gets or sets the reflectivity of the spacecraft used for solar radiation pressure calculations, where 2.0 is fully reflective and 1.0 is not reflective at all. Dimensionless.

.. py:property:: solar_radiation_pressure_area
    :canonical: ansys.stk.core.stkobjects.astrogator.ISpacecraftParameters.solar_radiation_pressure_area
    :type: float

    Gets or sets the cross-sectional area of the spacecraft assumed perpendicular to the direction of solar radiation, used for solar radiation calculations. Uses SmallArea Dimension.

.. py:property:: ck
    :canonical: ansys.stk.core.stkobjects.astrogator.ISpacecraftParameters.ck
    :type: float

    Gets or sets the reflectivity of the spacecraft used for central body radiation pressure (albedo / thermal pressure) calculations, where 2.0 is fully reflective and 1.0 is not reflective at all. Dimensionless.

.. py:property:: radiation_pressure_area
    :canonical: ansys.stk.core.stkobjects.astrogator.ISpacecraftParameters.radiation_pressure_area
    :type: float

    Gets or sets the cross-sectional area of the spacecraft assumed perpendicular to the direction of central body radiation, used for central body radiation (albedo / thermal pressure) calculations. Uses SmallArea Dimension.

.. py:property:: k1
    :canonical: ansys.stk.core.stkobjects.astrogator.ISpacecraftParameters.k1
    :type: float

    If you are using a non-spherical SRP model, this field defines the model's GPS solar radiation pressure K1 (scale) value. Dimensionless.

.. py:property:: k2
    :canonical: ansys.stk.core.stkobjects.astrogator.ISpacecraftParameters.k2
    :type: float

    If you are using a non-spherical SRP model, this field defines the model's GPS solar radiation pressure K2 (scale) value. Dimensionless.


