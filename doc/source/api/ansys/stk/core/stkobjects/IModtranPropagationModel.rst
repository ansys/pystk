IModtranPropagationModel
========================

.. py:class:: ansys.stk.core.stkobjects.IModtranPropagationModel

   object
   
   Provide access to the properties and methods of the MODTRAN propagation model.

.. py:currentmodule:: IModtranPropagationModel

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IModtranPropagationModel.set_aerosol_model_type_by_name`
              - Set the aerosol model type by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IModtranPropagationModel.supported_aerosol_models`
              - Gets an array of supported aerosol model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.IModtranPropagationModel.aerosol_model_type`
              - Gets or sets the aerosol model type.
            * - :py:attr:`~ansys.stk.core.stkobjects.IModtranPropagationModel.visibility`
              - Gets or sets the visibility.
            * - :py:attr:`~ansys.stk.core.stkobjects.IModtranPropagationModel.relative_humidity`
              - Gets or sets the relative humidity.
            * - :py:attr:`~ansys.stk.core.stkobjects.IModtranPropagationModel.surface_temperature`
              - Gets or sets the surface temperature.
            * - :py:attr:`~ansys.stk.core.stkobjects.IModtranPropagationModel.cloud_model_type`
              - Gets or sets the cloud model type.
            * - :py:attr:`~ansys.stk.core.stkobjects.IModtranPropagationModel.override_cloud_thickness`
              - Gets or set the option for overriding the cloud thickness.
            * - :py:attr:`~ansys.stk.core.stkobjects.IModtranPropagationModel.cloud_thickness`
              - Gets or sets the cloud thickness value.
            * - :py:attr:`~ansys.stk.core.stkobjects.IModtranPropagationModel.override_cloud_altitude`
              - Gets or set the option for overriding the cloud altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.IModtranPropagationModel.cloud_altitude`
              - Gets or sets the cloud altitude value.
            * - :py:attr:`~ansys.stk.core.stkobjects.IModtranPropagationModel.write_start_time`
              - Gets or sets the time to start writing MODTRAN output files.
            * - :py:attr:`~ansys.stk.core.stkobjects.IModtranPropagationModel.write_num_time_steps`
              - Gets or sets the number of time steps to write MODTRAN output files.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IModtranPropagationModel


Property detail
---------------

.. py:property:: supported_aerosol_models
    :canonical: ansys.stk.core.stkobjects.IModtranPropagationModel.supported_aerosol_models
    :type: list

    Gets an array of supported aerosol model names.

.. py:property:: aerosol_model_type
    :canonical: ansys.stk.core.stkobjects.IModtranPropagationModel.aerosol_model_type
    :type: MODTRAN_AEROSOL_MODEL_TYPE

    Gets or sets the aerosol model type.

.. py:property:: visibility
    :canonical: ansys.stk.core.stkobjects.IModtranPropagationModel.visibility
    :type: float

    Gets or sets the visibility.

.. py:property:: relative_humidity
    :canonical: ansys.stk.core.stkobjects.IModtranPropagationModel.relative_humidity
    :type: float

    Gets or sets the relative humidity.

.. py:property:: surface_temperature
    :canonical: ansys.stk.core.stkobjects.IModtranPropagationModel.surface_temperature
    :type: float

    Gets or sets the surface temperature.

.. py:property:: cloud_model_type
    :canonical: ansys.stk.core.stkobjects.IModtranPropagationModel.cloud_model_type
    :type: MODTRAN_CLOUD_MODEL_TYPE

    Gets or sets the cloud model type.

.. py:property:: override_cloud_thickness
    :canonical: ansys.stk.core.stkobjects.IModtranPropagationModel.override_cloud_thickness
    :type: bool

    Gets or set the option for overriding the cloud thickness.

.. py:property:: cloud_thickness
    :canonical: ansys.stk.core.stkobjects.IModtranPropagationModel.cloud_thickness
    :type: float

    Gets or sets the cloud thickness value.

.. py:property:: override_cloud_altitude
    :canonical: ansys.stk.core.stkobjects.IModtranPropagationModel.override_cloud_altitude
    :type: bool

    Gets or set the option for overriding the cloud altitude.

.. py:property:: cloud_altitude
    :canonical: ansys.stk.core.stkobjects.IModtranPropagationModel.cloud_altitude
    :type: float

    Gets or sets the cloud altitude value.

.. py:property:: write_start_time
    :canonical: ansys.stk.core.stkobjects.IModtranPropagationModel.write_start_time
    :type: float

    Gets or sets the time to start writing MODTRAN output files.

.. py:property:: write_num_time_steps
    :canonical: ansys.stk.core.stkobjects.IModtranPropagationModel.write_num_time_steps
    :type: int

    Gets or sets the number of time steps to write MODTRAN output files.


Method detail
-------------




.. py:method:: set_aerosol_model_type_by_name(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.IModtranPropagationModel.set_aerosol_model_type_by_name

    Set the aerosol model type by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`





















