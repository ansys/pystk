MODTRANPropagationModel
=======================

.. py:class:: ansys.stk.core.stkobjects.MODTRANPropagationModel

   Bases: :py:class:`~ansys.stk.core.stkobjects.ILaserAtmosphericLossModel`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining a MODTRAN propagation model.

.. py:currentmodule:: MODTRANPropagationModel

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MODTRANPropagationModel.set_aerosol_model_type_by_name`
              - Set the aerosol model type by name.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.MODTRANPropagationModel.supported_aerosol_models`
              - Get an array of supported aerosol model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.MODTRANPropagationModel.aerosol_model_type`
              - Get or set the aerosol model type.
            * - :py:attr:`~ansys.stk.core.stkobjects.MODTRANPropagationModel.visibility`
              - Get or set the visibility.
            * - :py:attr:`~ansys.stk.core.stkobjects.MODTRANPropagationModel.relative_humidity`
              - Get or set the relative humidity.
            * - :py:attr:`~ansys.stk.core.stkobjects.MODTRANPropagationModel.surface_temperature`
              - Get or set the surface temperature.
            * - :py:attr:`~ansys.stk.core.stkobjects.MODTRANPropagationModel.cloud_model_type`
              - Get or set the cloud model type.
            * - :py:attr:`~ansys.stk.core.stkobjects.MODTRANPropagationModel.override_cloud_thickness`
              - Get or set the option for overriding the cloud thickness.
            * - :py:attr:`~ansys.stk.core.stkobjects.MODTRANPropagationModel.cloud_thickness`
              - Get or set the cloud thickness value.
            * - :py:attr:`~ansys.stk.core.stkobjects.MODTRANPropagationModel.override_cloud_altitude`
              - Get or set the option for overriding the cloud altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.MODTRANPropagationModel.cloud_altitude`
              - Get or set the cloud altitude value.
            * - :py:attr:`~ansys.stk.core.stkobjects.MODTRANPropagationModel.write_start_time`
              - Get or set the time to start writing MODTRAN output files.
            * - :py:attr:`~ansys.stk.core.stkobjects.MODTRANPropagationModel.number_of_time_steps_to_write`
              - Get or set the number of time steps to write MODTRAN output files.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import MODTRANPropagationModel


Property detail
---------------

.. py:property:: supported_aerosol_models
    :canonical: ansys.stk.core.stkobjects.MODTRANPropagationModel.supported_aerosol_models
    :type: list

    Get an array of supported aerosol model names.

.. py:property:: aerosol_model_type
    :canonical: ansys.stk.core.stkobjects.MODTRANPropagationModel.aerosol_model_type
    :type: ModtranAerosolModelType

    Get or set the aerosol model type.

.. py:property:: visibility
    :canonical: ansys.stk.core.stkobjects.MODTRANPropagationModel.visibility
    :type: float

    Get or set the visibility.

.. py:property:: relative_humidity
    :canonical: ansys.stk.core.stkobjects.MODTRANPropagationModel.relative_humidity
    :type: float

    Get or set the relative humidity.

.. py:property:: surface_temperature
    :canonical: ansys.stk.core.stkobjects.MODTRANPropagationModel.surface_temperature
    :type: float

    Get or set the surface temperature.

.. py:property:: cloud_model_type
    :canonical: ansys.stk.core.stkobjects.MODTRANPropagationModel.cloud_model_type
    :type: ModtranCloudModelType

    Get or set the cloud model type.

.. py:property:: override_cloud_thickness
    :canonical: ansys.stk.core.stkobjects.MODTRANPropagationModel.override_cloud_thickness
    :type: bool

    Get or set the option for overriding the cloud thickness.

.. py:property:: cloud_thickness
    :canonical: ansys.stk.core.stkobjects.MODTRANPropagationModel.cloud_thickness
    :type: float

    Get or set the cloud thickness value.

.. py:property:: override_cloud_altitude
    :canonical: ansys.stk.core.stkobjects.MODTRANPropagationModel.override_cloud_altitude
    :type: bool

    Get or set the option for overriding the cloud altitude.

.. py:property:: cloud_altitude
    :canonical: ansys.stk.core.stkobjects.MODTRANPropagationModel.cloud_altitude
    :type: float

    Get or set the cloud altitude value.

.. py:property:: write_start_time
    :canonical: ansys.stk.core.stkobjects.MODTRANPropagationModel.write_start_time
    :type: float

    Get or set the time to start writing MODTRAN output files.

.. py:property:: number_of_time_steps_to_write
    :canonical: ansys.stk.core.stkobjects.MODTRANPropagationModel.number_of_time_steps_to_write
    :type: int

    Get or set the number of time steps to write MODTRAN output files.


Method detail
-------------




.. py:method:: set_aerosol_model_type_by_name(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.MODTRANPropagationModel.set_aerosol_model_type_by_name

    Set the aerosol model type by name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~None`





















