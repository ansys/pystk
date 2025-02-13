VehicleHPOPSolarRadiationPressureModel
======================================

.. py:class:: ansys.stk.core.stkobjects.VehicleHPOPSolarRadiationPressureModel

   SRP Model Base CoClass.

.. py:currentmodule:: VehicleHPOPSolarRadiationPressureModel

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleHPOPSolarRadiationPressureModel.set_model_type`
              - Change the active solar radiation pressure model type.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleHPOPSolarRadiationPressureModel.is_model_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleHPOPSolarRadiationPressureModel.model_type`
              - Return a type of the active solar radiation pressure model.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleHPOPSolarRadiationPressureModel.model_supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleHPOPSolarRadiationPressureModel.model`
              - Return the active solar radiation pressure model.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleHPOPSolarRadiationPressureModel


Property detail
---------------

.. py:property:: model_type
    :canonical: ansys.stk.core.stkobjects.VehicleHPOPSolarRadiationPressureModel.model_type
    :type: SolarRadiationPressureModelType

    Return a type of the active solar radiation pressure model.

.. py:property:: model_supported_types
    :canonical: ansys.stk.core.stkobjects.VehicleHPOPSolarRadiationPressureModel.model_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: model
    :canonical: ansys.stk.core.stkobjects.VehicleHPOPSolarRadiationPressureModel.model
    :type: ISRPModelBase

    Return the active solar radiation pressure model.


Method detail
-------------


.. py:method:: set_model_type(self, srp_model: SolarRadiationPressureModelType) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleHPOPSolarRadiationPressureModel.set_model_type

    Change the active solar radiation pressure model type.

    :Parameters:

    **srp_model** : :obj:`~SolarRadiationPressureModelType`

    :Returns:

        :obj:`~None`

.. py:method:: is_model_type_supported(self, srp_model: SolarRadiationPressureModelType) -> bool
    :canonical: ansys.stk.core.stkobjects.VehicleHPOPSolarRadiationPressureModel.is_model_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **srp_model** : :obj:`~SolarRadiationPressureModelType`

    :Returns:

        :obj:`~bool`



