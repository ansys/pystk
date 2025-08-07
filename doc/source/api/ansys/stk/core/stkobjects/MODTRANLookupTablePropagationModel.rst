MODTRANLookupTablePropagationModel
==================================

.. py:class:: ansys.stk.core.stkobjects.MODTRANLookupTablePropagationModel

   Bases: :py:class:`~ansys.stk.core.stkobjects.ILaserAtmosphericLossModel`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining an MODTRAN-based lookup table propagation model.

.. py:currentmodule:: MODTRANLookupTablePropagationModel

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MODTRANLookupTablePropagationModel.set_aerosol_model_type_by_name`
              - Set the aerosol model type by name.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MODTRANLookupTablePropagationModel.aerosol_model_type`
              - Get or set the aerosol model type.
            * - :py:attr:`~ansys.stk.core.stkobjects.MODTRANLookupTablePropagationModel.relative_humidity`
              - Get or set the relative humidity.
            * - :py:attr:`~ansys.stk.core.stkobjects.MODTRANLookupTablePropagationModel.supported_aerosol_models`
              - Get an array of supported aerosol model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.MODTRANLookupTablePropagationModel.surface_temperature`
              - Get or set the surface temperature.
            * - :py:attr:`~ansys.stk.core.stkobjects.MODTRANLookupTablePropagationModel.visibility`
              - Get or set the visibility.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import MODTRANLookupTablePropagationModel


Property detail
---------------

.. py:property:: aerosol_model_type
    :canonical: ansys.stk.core.stkobjects.MODTRANLookupTablePropagationModel.aerosol_model_type
    :type: ModtranAerosolModelType

    Get or set the aerosol model type.

.. py:property:: relative_humidity
    :canonical: ansys.stk.core.stkobjects.MODTRANLookupTablePropagationModel.relative_humidity
    :type: float

    Get or set the relative humidity.

.. py:property:: supported_aerosol_models
    :canonical: ansys.stk.core.stkobjects.MODTRANLookupTablePropagationModel.supported_aerosol_models
    :type: list

    Get an array of supported aerosol model names.

.. py:property:: surface_temperature
    :canonical: ansys.stk.core.stkobjects.MODTRANLookupTablePropagationModel.surface_temperature
    :type: float

    Get or set the surface temperature.

.. py:property:: visibility
    :canonical: ansys.stk.core.stkobjects.MODTRANLookupTablePropagationModel.visibility
    :type: float

    Get or set the visibility.


Method detail
-------------





.. py:method:: set_aerosol_model_type_by_name(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.MODTRANLookupTablePropagationModel.set_aerosol_model_type_by_name

    Set the aerosol model type by name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~None`






