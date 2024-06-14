IVehicleHPOPSRPModel
====================

.. py:class:: IVehicleHPOPSRPModel

   object
   
   HPOP Solar Radiation Pressure Model.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_model_type`
              - Change the active solar radiation pressure model type.
            * - :py:meth:`~is_model_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~model_type`
            * - :py:meth:`~model_supported_types`
            * - :py:meth:`~model`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleHPOPSRPModel


Property detail
---------------

.. py:property:: model_type
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPSRPModel.model_type
    :type: "SRP_MODEL"

    Returns a type of the active solar radiation pressure model.

.. py:property:: model_supported_types
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPSRPModel.model_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: model
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPSRPModel.model
    :type: "IAgSRPModelBase"

    Returns the active solar radiation pressure model.


Method detail
-------------


.. py:method:: set_model_type(self, sRPModel:"SRP_MODEL") -> None

    Change the active solar radiation pressure model type.

    :Parameters:

    **sRPModel** : :obj:`~"SRP_MODEL"`

    :Returns:

        :obj:`~None`

.. py:method:: is_model_type_supported(self, sRPModel:"SRP_MODEL") -> bool

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **sRPModel** : :obj:`~"SRP_MODEL"`

    :Returns:

        :obj:`~bool`



