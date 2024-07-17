SRPSpherical
============

.. py:class:: ansys.stk.core.stkobjects.astrogator.SRPSpherical

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   Spherical SRP propagator function.

.. py:currentmodule:: SRPSpherical

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SRPSpherical.atmos_altitude`
              - Gets or sets the atmospheric altitude for eclipse. A simple model to account for some measure of attenuation that simply increases the shape of the Earth by the defined altitude height, often taken to be 23 km. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SRPSpherical.shadow_model`
              - Gets or sets the shadow model type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SRPSpherical.sun_position`
              - Gets or sets the sun position computation.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SRPSpherical.eclipsing_bodies`
              - Other eclipsing bodies.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SRPSpherical.mean_flux`
              - Gets or sets the mean solar flux at 1 au (W/m^2).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SRPSpherical.luminosity`
              - Gets or sets the luminosity of sun. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SRPSpherical.solar_force_method`
              - Gets or sets the solar force method.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SRPSpherical.include_boundary_mitigation`
              - True if shadow boundary mitigation should be performed; the state of the satellite after crossing a shadow boundary will be corrected for errors possibly caused by the sudden change in SRP which occurred during the integration step.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SRPSpherical.use_sun_central_body_file_values`
              - True if solar values should come from the Sun.cb file.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SRPSpherical.solar_radius`
              - Gets or sets the solar radius value to use in eclipse calculations.  Uses Distance Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import SRPSpherical


Property detail
---------------

.. py:property:: atmos_altitude
    :canonical: ansys.stk.core.stkobjects.astrogator.SRPSpherical.atmos_altitude
    :type: float

    Gets or sets the atmospheric altitude for eclipse. A simple model to account for some measure of attenuation that simply increases the shape of the Earth by the defined altitude height, often taken to be 23 km. Uses Distance Dimension.

.. py:property:: shadow_model
    :canonical: ansys.stk.core.stkobjects.astrogator.SRPSpherical.shadow_model
    :type: SHADOW_MODEL

    Gets or sets the shadow model type.

.. py:property:: sun_position
    :canonical: ansys.stk.core.stkobjects.astrogator.SRPSpherical.sun_position
    :type: SUN_POSITION

    Gets or sets the sun position computation.

.. py:property:: eclipsing_bodies
    :canonical: ansys.stk.core.stkobjects.astrogator.SRPSpherical.eclipsing_bodies
    :type: ICentralBodyCollection

    Other eclipsing bodies.

.. py:property:: mean_flux
    :canonical: ansys.stk.core.stkobjects.astrogator.SRPSpherical.mean_flux
    :type: float

    Gets or sets the mean solar flux at 1 au (W/m^2).

.. py:property:: luminosity
    :canonical: ansys.stk.core.stkobjects.astrogator.SRPSpherical.luminosity
    :type: float

    Gets or sets the luminosity of sun. Dimensionless.

.. py:property:: solar_force_method
    :canonical: ansys.stk.core.stkobjects.astrogator.SRPSpherical.solar_force_method
    :type: SOLAR_FORCE_METHOD

    Gets or sets the solar force method.

.. py:property:: include_boundary_mitigation
    :canonical: ansys.stk.core.stkobjects.astrogator.SRPSpherical.include_boundary_mitigation
    :type: bool

    True if shadow boundary mitigation should be performed; the state of the satellite after crossing a shadow boundary will be corrected for errors possibly caused by the sudden change in SRP which occurred during the integration step.

.. py:property:: use_sun_central_body_file_values
    :canonical: ansys.stk.core.stkobjects.astrogator.SRPSpherical.use_sun_central_body_file_values
    :type: bool

    True if solar values should come from the Sun.cb file.

.. py:property:: solar_radius
    :canonical: ansys.stk.core.stkobjects.astrogator.SRPSpherical.solar_radius
    :type: float

    Gets or sets the solar radius value to use in eclipse calculations.  Uses Distance Dimension.


