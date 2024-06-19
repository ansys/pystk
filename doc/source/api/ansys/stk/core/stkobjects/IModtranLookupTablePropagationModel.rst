IModtranLookupTablePropagationModel
===================================

.. py:class:: IModtranLookupTablePropagationModel

   object
   
   Provide access to the properties and methods of the MODTRAN lookup table model.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_aerosol_model_type_by_name`
              - Set the aerosol model type by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~aerosol_model_type`
            * - :py:meth:`~visibility`
            * - :py:meth:`~relative_humidity`
            * - :py:meth:`~surface_temperature`
            * - :py:meth:`~supported_aerosol_models`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IModtranLookupTablePropagationModel


Property detail
---------------

.. py:property:: aerosol_model_type
    :canonical: ansys.stk.core.stkobjects.IModtranLookupTablePropagationModel.aerosol_model_type
    :type: MODTRAN_AEROSOL_MODEL_TYPE

    Gets or sets the aerosol model type.

.. py:property:: visibility
    :canonical: ansys.stk.core.stkobjects.IModtranLookupTablePropagationModel.visibility
    :type: float

    Gets or sets the visibility.

.. py:property:: relative_humidity
    :canonical: ansys.stk.core.stkobjects.IModtranLookupTablePropagationModel.relative_humidity
    :type: float

    Gets or sets the relative humidity.

.. py:property:: surface_temperature
    :canonical: ansys.stk.core.stkobjects.IModtranLookupTablePropagationModel.surface_temperature
    :type: float

    Gets or sets the surface temperature.

.. py:property:: supported_aerosol_models
    :canonical: ansys.stk.core.stkobjects.IModtranLookupTablePropagationModel.supported_aerosol_models
    :type: list

    Gets an array of supported aerosol model names.


Method detail
-------------










.. py:method:: set_aerosol_model_type_by_name(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.IModtranLookupTablePropagationModel.set_aerosol_model_type_by_name

    Set the aerosol model type by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`

