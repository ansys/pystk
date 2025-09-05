State
=====

.. py:class:: ansys.stk.core.stkobjects.astrogator.State

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The orbit state.

.. py:currentmodule:: State

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.State.get_in_frame_name`
              - Get the orbit state in the specified frame.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.State.set_element_type`
              - Set the element type.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.State.cd`
              - Get or set the dimensionless drag coefficient associated with the drag area. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.State.coord_system_name`
              - Get the coordinate system.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.State.cr`
              - Get or set the reflectivity of the spacecraft used for solar radiation pressure calculations, where 2.0 is fully reflective and 1.0 is not reflective at all. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.State.drag_area`
              - Get or set the cross-sectional area of the spacecraft assumed perpendicular to the direction of motion, used for atmospheric drag calculations. Uses SmallArea Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.State.dry_mass`
              - Get or set the mass of the spacecraft exclusive of propellant. Uses Mass Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.State.element`
              - Return the currently selected element type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.State.element_type`
              - Get the element type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.State.epoch`
              - Get or set the epoch of the Orbit State. Uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.State.fuel_density`
              - Get or set the density of the fuel tank. Uses SmallDensity Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.State.fuel_mass`
              - Get or set the mass of the spacecraft propellant. Uses Mass Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.State.k1`
              - If you are using a non-spherical SRP model, this field defines the model's GPS solar radiation pressure K1 (scale) value. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.State.k2`
              - If you are using a non-spherical SRP model, this field defines the model's GPS solar radiation pressure K2 (scale) value. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.State.radiation_pressure_area`
              - Get or set the cross-sectional area of the spacecraft assumed perpendicular to the direction of central body radiation, used for central body radiation (albedo / thermal pressure) calculations. Uses Small Area Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.State.radiation_pressure_coefficient`
              - Get or set the reflectivity of the spacecraft used for central body radiation pressure (albedo / thermal pressure) calculations, where 2.0 is fully reflective and 1.0 is not reflective at all. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.State.srp_area`
              - Get or set the cross-sectional area of the spacecraft assumed perpendicular to the direction of solar radiation, used for solar radiation calculations. Uses SmallArea Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.State.tank_pressure`
              - Get or set the fuel tank pressure. Uses Pressure Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.State.tank_temperature`
              - Get or set the temperature of the fuel tank. Uses Temperature Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import State


Property detail
---------------

.. py:property:: cd
    :canonical: ansys.stk.core.stkobjects.astrogator.State.cd
    :type: float

    Get or set the dimensionless drag coefficient associated with the drag area. Dimensionless.

.. py:property:: coord_system_name
    :canonical: ansys.stk.core.stkobjects.astrogator.State.coord_system_name
    :type: str

    Get the coordinate system.

.. py:property:: cr
    :canonical: ansys.stk.core.stkobjects.astrogator.State.cr
    :type: float

    Get or set the reflectivity of the spacecraft used for solar radiation pressure calculations, where 2.0 is fully reflective and 1.0 is not reflective at all. Dimensionless.

.. py:property:: drag_area
    :canonical: ansys.stk.core.stkobjects.astrogator.State.drag_area
    :type: float

    Get or set the cross-sectional area of the spacecraft assumed perpendicular to the direction of motion, used for atmospheric drag calculations. Uses SmallArea Dimension.

.. py:property:: dry_mass
    :canonical: ansys.stk.core.stkobjects.astrogator.State.dry_mass
    :type: float

    Get or set the mass of the spacecraft exclusive of propellant. Uses Mass Dimension.

.. py:property:: element
    :canonical: ansys.stk.core.stkobjects.astrogator.State.element
    :type: IElement

    Return the currently selected element type.

.. py:property:: element_type
    :canonical: ansys.stk.core.stkobjects.astrogator.State.element_type
    :type: ElementSetType

    Get the element type.

.. py:property:: epoch
    :canonical: ansys.stk.core.stkobjects.astrogator.State.epoch
    :type: typing.Any

    Get or set the epoch of the Orbit State. Uses DateFormat Dimension.

.. py:property:: fuel_density
    :canonical: ansys.stk.core.stkobjects.astrogator.State.fuel_density
    :type: float

    Get or set the density of the fuel tank. Uses SmallDensity Dimension.

.. py:property:: fuel_mass
    :canonical: ansys.stk.core.stkobjects.astrogator.State.fuel_mass
    :type: float

    Get or set the mass of the spacecraft propellant. Uses Mass Dimension.

.. py:property:: k1
    :canonical: ansys.stk.core.stkobjects.astrogator.State.k1
    :type: float

    If you are using a non-spherical SRP model, this field defines the model's GPS solar radiation pressure K1 (scale) value. Dimensionless.

.. py:property:: k2
    :canonical: ansys.stk.core.stkobjects.astrogator.State.k2
    :type: float

    If you are using a non-spherical SRP model, this field defines the model's GPS solar radiation pressure K2 (scale) value. Dimensionless.

.. py:property:: radiation_pressure_area
    :canonical: ansys.stk.core.stkobjects.astrogator.State.radiation_pressure_area
    :type: float

    Get or set the cross-sectional area of the spacecraft assumed perpendicular to the direction of central body radiation, used for central body radiation (albedo / thermal pressure) calculations. Uses Small Area Dimension.

.. py:property:: radiation_pressure_coefficient
    :canonical: ansys.stk.core.stkobjects.astrogator.State.radiation_pressure_coefficient
    :type: float

    Get or set the reflectivity of the spacecraft used for central body radiation pressure (albedo / thermal pressure) calculations, where 2.0 is fully reflective and 1.0 is not reflective at all. Dimensionless.

.. py:property:: srp_area
    :canonical: ansys.stk.core.stkobjects.astrogator.State.srp_area
    :type: float

    Get or set the cross-sectional area of the spacecraft assumed perpendicular to the direction of solar radiation, used for solar radiation calculations. Uses SmallArea Dimension.

.. py:property:: tank_pressure
    :canonical: ansys.stk.core.stkobjects.astrogator.State.tank_pressure
    :type: float

    Get or set the fuel tank pressure. Uses Pressure Dimension.

.. py:property:: tank_temperature
    :canonical: ansys.stk.core.stkobjects.astrogator.State.tank_temperature
    :type: float

    Get or set the temperature of the fuel tank. Uses Temperature Dimension.


Method detail
-------------


















.. py:method:: get_in_frame_name(self, frame_name: str) -> State
    :canonical: ansys.stk.core.stkobjects.astrogator.State.get_in_frame_name

    Get the orbit state in the specified frame.

    :Parameters:

        **frame_name** : :obj:`~str`


    :Returns:

        :obj:`~State`











.. py:method:: set_element_type(self, element_type: ElementSetType) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.State.set_element_type

    Set the element type.

    :Parameters:

        **element_type** : :obj:`~ElementSetType`


    :Returns:

        :obj:`~None`





