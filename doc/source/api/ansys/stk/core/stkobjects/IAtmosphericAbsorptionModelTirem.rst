IAtmosphericAbsorptionModelTirem
================================

.. py:class:: IAtmosphericAbsorptionModelTirem

   object
   
   Provide access to the properties and methods of the TIREM atmospheric absorption model.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~surface_temperature`
            * - :py:meth:`~surface_humidity`
            * - :py:meth:`~surface_conductivity`
            * - :py:meth:`~surface_refractivity`
            * - :py:meth:`~relative_permittivity`
            * - :py:meth:`~override_terrain_sample_resolution`
            * - :py:meth:`~terrain_sample_resolution`
            * - :py:meth:`~polarization_type`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAtmosphericAbsorptionModelTirem


Property detail
---------------

.. py:property:: surface_temperature
    :canonical: ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelTirem.surface_temperature
    :type: float

    Gets or sets the surface temperature.

.. py:property:: surface_humidity
    :canonical: ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelTirem.surface_humidity
    :type: float

    Gets or sets the surface humidity.

.. py:property:: surface_conductivity
    :canonical: ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelTirem.surface_conductivity
    :type: float

    Gets or sets the surface conductivity.

.. py:property:: surface_refractivity
    :canonical: ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelTirem.surface_refractivity
    :type: float

    Gets or sets the surface refractivity.

.. py:property:: relative_permittivity
    :canonical: ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelTirem.relative_permittivity
    :type: float

    Gets or sets the relative permittivity.

.. py:property:: override_terrain_sample_resolution
    :canonical: ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelTirem.override_terrain_sample_resolution
    :type: bool

    Gets or sets the option for overriding available terrain sample resolution.

.. py:property:: terrain_sample_resolution
    :canonical: ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelTirem.terrain_sample_resolution
    :type: float

    Gets or sets the terrain sample resolution.

.. py:property:: polarization_type
    :canonical: ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelTirem.polarization_type
    :type: "TIREM_POLARIZATION_TYPE"

    Gets or sets the polarization type.


