IState
======

.. py:class:: IState

   object
   
   Spacecraft Parameters properties for the spacecraft configuration.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_element_type`
              - Set the element type.
            * - :py:meth:`~get_in_frame_name`
              - Get the orbit state in the specified frame.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~element_type`
            * - :py:meth:`~element`
            * - :py:meth:`~epoch`
            * - :py:meth:`~coord_system_name`
            * - :py:meth:`~dry_mass`
            * - :py:meth:`~fuel_mass`
            * - :py:meth:`~drag_area`
            * - :py:meth:`~srp_area`
            * - :py:meth:`~tank_pressure`
            * - :py:meth:`~tank_temperature`
            * - :py:meth:`~fuel_density`
            * - :py:meth:`~cr`
            * - :py:meth:`~cd`
            * - :py:meth:`~radiation_pressure_coeff`
            * - :py:meth:`~radiation_pressure_area`
            * - :py:meth:`~k1`
            * - :py:meth:`~k2`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IState


Property detail
---------------

.. py:property:: element_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IState.element_type
    :type: ELEMENT_TYPE

    Get the element type.

.. py:property:: element
    :canonical: ansys.stk.core.stkobjects.astrogator.IState.element
    :type: IAgVAElement

    Returns the currently selected element type.

.. py:property:: epoch
    :canonical: ansys.stk.core.stkobjects.astrogator.IState.epoch
    :type: typing.Any

    Gets or sets the epoch of the Orbit State. Uses DateFormat Dimension.

.. py:property:: coord_system_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IState.coord_system_name
    :type: str

    Get the coordinate system.

.. py:property:: dry_mass
    :canonical: ansys.stk.core.stkobjects.astrogator.IState.dry_mass
    :type: float

    Gets or sets the mass of the spacecraft exclusive of propellant. Uses Mass Dimension.

.. py:property:: fuel_mass
    :canonical: ansys.stk.core.stkobjects.astrogator.IState.fuel_mass
    :type: float

    Gets or sets the mass of the spacecraft propellant. Uses Mass Dimension.

.. py:property:: drag_area
    :canonical: ansys.stk.core.stkobjects.astrogator.IState.drag_area
    :type: float

    Gets or sets the cross-sectional area of the spacecraft assumed perpendicular to the direction of motion, used for atmospheric drag calculations. Uses SmallArea Dimension.

.. py:property:: srp_area
    :canonical: ansys.stk.core.stkobjects.astrogator.IState.srp_area
    :type: float

    Gets or sets the cross-sectional area of the spacecraft assumed perpendicular to the direction of solar radiation, used for solar radiation calculations. Uses SmallArea Dimension.

.. py:property:: tank_pressure
    :canonical: ansys.stk.core.stkobjects.astrogator.IState.tank_pressure
    :type: float

    Gets or sets the fuel tank pressure. Uses Pressure Dimension.

.. py:property:: tank_temperature
    :canonical: ansys.stk.core.stkobjects.astrogator.IState.tank_temperature
    :type: float

    Gets or sets the temperature of the fuel tank. Uses Temperature Dimension.

.. py:property:: fuel_density
    :canonical: ansys.stk.core.stkobjects.astrogator.IState.fuel_density
    :type: float

    Gets or sets the density of the fuel tank. Uses SmallDensity Dimension.

.. py:property:: cr
    :canonical: ansys.stk.core.stkobjects.astrogator.IState.cr
    :type: float

    Gets or sets the reflectivity of the spacecraft used for solar radiation pressure calculations, where 2.0 is fully reflective and 1.0 is not reflective at all. Dimensionless.

.. py:property:: cd
    :canonical: ansys.stk.core.stkobjects.astrogator.IState.cd
    :type: float

    Gets or sets the dimensionless drag coefficient associated with the drag area. Dimensionless.

.. py:property:: radiation_pressure_coeff
    :canonical: ansys.stk.core.stkobjects.astrogator.IState.radiation_pressure_coeff
    :type: float

    Gets or sets the reflectivity of the spacecraft used for central body radiation pressure (albedo / thermal pressure) calculations, where 2.0 is fully reflective and 1.0 is not reflective at all. Dimensionless.

.. py:property:: radiation_pressure_area
    :canonical: ansys.stk.core.stkobjects.astrogator.IState.radiation_pressure_area
    :type: float

    Gets or sets the cross-sectional area of the spacecraft assumed perpendicular to the direction of central body radiation, used for central body radiation (albedo / thermal pressure) calculations. Uses Small Area Dimension.

.. py:property:: k1
    :canonical: ansys.stk.core.stkobjects.astrogator.IState.k1
    :type: float

    If you are using a non-spherical SRP model, this field defines the model's GPS solar radiation pressure K1 (scale) value. Dimensionless.

.. py:property:: k2
    :canonical: ansys.stk.core.stkobjects.astrogator.IState.k2
    :type: float

    If you are using a non-spherical SRP model, this field defines the model's GPS solar radiation pressure K2 (scale) value. Dimensionless.


Method detail
-------------


.. py:method:: set_element_type(self, elementType: ELEMENT_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IState.set_element_type

    Set the element type.

    :Parameters:

    **elementType** : :obj:`~ELEMENT_TYPE`

    :Returns:

        :obj:`~None`































.. py:method:: get_in_frame_name(self, frameName: str) -> IState
    :canonical: ansys.stk.core.stkobjects.astrogator.IState.get_in_frame_name

    Get the orbit state in the specified frame.

    :Parameters:

    **frameName** : :obj:`~str`

    :Returns:

        :obj:`~IState`

