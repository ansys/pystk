IAtmosphericAbsorptionModelTIREM
================================

.. py:class:: ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelTIREM

   Provide access to the properties and methods of the TIREM atmospheric absorption model.

.. py:currentmodule:: IAtmosphericAbsorptionModelTIREM

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelTIREM.surface_temperature`
              - Get or set the surface temperature.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelTIREM.surface_humidity`
              - Get or set the surface humidity.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelTIREM.surface_conductivity`
              - Get or set the surface conductivity.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelTIREM.surface_refractivity`
              - Get or set the surface refractivity.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelTIREM.relative_permittivity`
              - Get or set the relative permittivity.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelTIREM.override_terrain_sample_resolution`
              - Get or set the option for overriding available terrain sample resolution.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelTIREM.terrain_sample_resolution`
              - Get or set the terrain sample resolution.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelTIREM.polarization_type`
              - Get or set the polarization type.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAtmosphericAbsorptionModelTIREM


Property detail
---------------

.. py:property:: surface_temperature
    :canonical: ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelTIREM.surface_temperature
    :type: float

    Get or set the surface temperature.

.. py:property:: surface_humidity
    :canonical: ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelTIREM.surface_humidity
    :type: float

    Get or set the surface humidity.

.. py:property:: surface_conductivity
    :canonical: ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelTIREM.surface_conductivity
    :type: float

    Get or set the surface conductivity.

.. py:property:: surface_refractivity
    :canonical: ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelTIREM.surface_refractivity
    :type: float

    Get or set the surface refractivity.

.. py:property:: relative_permittivity
    :canonical: ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelTIREM.relative_permittivity
    :type: float

    Get or set the relative permittivity.

.. py:property:: override_terrain_sample_resolution
    :canonical: ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelTIREM.override_terrain_sample_resolution
    :type: bool

    Get or set the option for overriding available terrain sample resolution.

.. py:property:: terrain_sample_resolution
    :canonical: ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelTIREM.terrain_sample_resolution
    :type: float

    Get or set the terrain sample resolution.

.. py:property:: polarization_type
    :canonical: ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelTIREM.polarization_type
    :type: TIREMPolarizationType

    Get or set the polarization type.


