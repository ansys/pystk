SpaceEnvironmentVehicleTemperature
==================================

.. py:class:: ansys.stk.core.stkobjects.SpaceEnvironmentVehicleTemperature

   Vehicle Temperature settings.

.. py:currentmodule:: SpaceEnvironmentVehicleTemperature

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentVehicleTemperature.compute_temperature`
              - Compute vehicle temperature. Uses DateFormat and Temperature Dimensions.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentVehicleTemperature.earth_albedo`
              - Gets or sets the Earth's albedo. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentVehicleTemperature.material_emissivity`
              - Gets or sets the material emissivity. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentVehicleTemperature.material_absorptivity`
              - Gets or sets the material absorptivity. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentVehicleTemperature.dissipation`
              - Gets or sets the internal dissipation. Uses Power Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentVehicleTemperature.cross_sectional_area`
              - Area used in thermal model. For plate, equals its surface area; for spehere, equals pi*radius^2. Uses SmallArea Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentVehicleTemperature.shape_model`
              - Thermal shape model.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentVehicleTemperature.normal_vector`
              - Plate normal vector.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SpaceEnvironmentVehicleTemperature


Property detail
---------------

.. py:property:: earth_albedo
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentVehicleTemperature.earth_albedo
    :type: float

    Gets or sets the Earth's albedo. Dimensionless.

.. py:property:: material_emissivity
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentVehicleTemperature.material_emissivity
    :type: float

    Gets or sets the material emissivity. Dimensionless.

.. py:property:: material_absorptivity
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentVehicleTemperature.material_absorptivity
    :type: float

    Gets or sets the material absorptivity. Dimensionless.

.. py:property:: dissipation
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentVehicleTemperature.dissipation
    :type: float

    Gets or sets the internal dissipation. Uses Power Dimension.

.. py:property:: cross_sectional_area
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentVehicleTemperature.cross_sectional_area
    :type: float

    Area used in thermal model. For plate, equals its surface area; for spehere, equals pi*radius^2. Uses SmallArea Dimension.

.. py:property:: shape_model
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentVehicleTemperature.shape_model
    :type: VEHICLE_SPACE_ENVIRONMENT_SHAPE_MODEL

    Thermal shape model.

.. py:property:: normal_vector
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentVehicleTemperature.normal_vector
    :type: str

    Plate normal vector.


Method detail
-------------















.. py:method:: compute_temperature(self, time: typing.Any) -> float
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentVehicleTemperature.compute_temperature

    Compute vehicle temperature. Uses DateFormat and Temperature Dimensions.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~float`

