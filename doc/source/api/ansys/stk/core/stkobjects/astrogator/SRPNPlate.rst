SRPNPlate
=========

.. py:class:: ansys.stk.core.stkobjects.astrogator.SRPNPlate

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   NPlate SRP propagator function.

.. py:currentmodule:: SRPNPlate

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SRPNPlate.atmosphere_altitude`
              - Get or set the atmospheric altitude for eclipse. A simple model to account for some measure of attenuation that simply increases the shape of the Earth by the defined altitude height, often taken to be 23 km. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SRPNPlate.eclipsing_bodies`
              - Other eclipsing bodies.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SRPNPlate.include_boundary_mitigation`
              - True if shadow boundary mitigation should be performed; the state of the satellite after crossing a shadow boundary will be corrected for errors possibly caused by the sudden change in SRP which occurred during the integration step.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SRPNPlate.luminosity`
              - Get or set the luminosity of sun. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SRPNPlate.mean_flux`
              - Get or set the mean solar flux at 1 au (W/m^2).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SRPNPlate.n_plate_definition_file`
              - Full path of NPlate definition file.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SRPNPlate.shadow_model`
              - Get or set the shadow model type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SRPNPlate.solar_force_method`
              - Get or set the solar force method.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SRPNPlate.solar_radius`
              - Get or set the solar radius value to use in eclipse calculations.  Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SRPNPlate.sun_position`
              - Get or set the sun position computation.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SRPNPlate.use_sun_central_body_file_values`
              - True if solar values should come from the Sun.cb file.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import SRPNPlate


Property detail
---------------

.. py:property:: atmosphere_altitude
    :canonical: ansys.stk.core.stkobjects.astrogator.SRPNPlate.atmosphere_altitude
    :type: float

    Get or set the atmospheric altitude for eclipse. A simple model to account for some measure of attenuation that simply increases the shape of the Earth by the defined altitude height, often taken to be 23 km. Uses Distance Dimension.

.. py:property:: eclipsing_bodies
    :canonical: ansys.stk.core.stkobjects.astrogator.SRPNPlate.eclipsing_bodies
    :type: CentralBodyComponentCollection

    Other eclipsing bodies.

.. py:property:: include_boundary_mitigation
    :canonical: ansys.stk.core.stkobjects.astrogator.SRPNPlate.include_boundary_mitigation
    :type: bool

    True if shadow boundary mitigation should be performed; the state of the satellite after crossing a shadow boundary will be corrected for errors possibly caused by the sudden change in SRP which occurred during the integration step.

.. py:property:: luminosity
    :canonical: ansys.stk.core.stkobjects.astrogator.SRPNPlate.luminosity
    :type: float

    Get or set the luminosity of sun. Dimensionless.

.. py:property:: mean_flux
    :canonical: ansys.stk.core.stkobjects.astrogator.SRPNPlate.mean_flux
    :type: float

    Get or set the mean solar flux at 1 au (W/m^2).

.. py:property:: n_plate_definition_file
    :canonical: ansys.stk.core.stkobjects.astrogator.SRPNPlate.n_plate_definition_file
    :type: str

    Full path of NPlate definition file.

.. py:property:: shadow_model
    :canonical: ansys.stk.core.stkobjects.astrogator.SRPNPlate.shadow_model
    :type: ShadowModel

    Get or set the shadow model type.

.. py:property:: solar_force_method
    :canonical: ansys.stk.core.stkobjects.astrogator.SRPNPlate.solar_force_method
    :type: SolarForceMethod

    Get or set the solar force method.

.. py:property:: solar_radius
    :canonical: ansys.stk.core.stkobjects.astrogator.SRPNPlate.solar_radius
    :type: float

    Get or set the solar radius value to use in eclipse calculations.  Uses Distance Dimension.

.. py:property:: sun_position
    :canonical: ansys.stk.core.stkobjects.astrogator.SRPNPlate.sun_position
    :type: SunPosition

    Get or set the sun position computation.

.. py:property:: use_sun_central_body_file_values
    :canonical: ansys.stk.core.stkobjects.astrogator.SRPNPlate.use_sun_central_body_file_values
    :type: bool

    True if solar values should come from the Sun.cb file.


