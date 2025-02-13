LaserPropagationLossModels
==========================

.. py:class:: ansys.stk.core.stkobjects.LaserPropagationLossModels

   Bases: :py:class:`~ansys.stk.core.stkobjects.ILaserPropagationChannel`

   Class defining the properties for laser propagatoin models.

.. py:currentmodule:: LaserPropagationLossModels

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.LaserPropagationLossModels.set_atmospheric_loss_model`
              - Set the current atmospheric absorption loss model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaserPropagationLossModels.set_tropospheric_scintillation_loss_model`
              - Set the current tropospheric scintillation loss model by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.LaserPropagationLossModels.enable_atmospheric_loss_model`
              - Get or set the option for computing atmospheric absorption propagation loss.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaserPropagationLossModels.atmospheric_loss_model`
              - Get the laser atmospheric absorption loss model.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaserPropagationLossModels.enable_tropospheric_scintillation_loss_model`
              - Get or set the option for computing tropospheric scintillation propagation loss.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaserPropagationLossModels.tropospheric_scintillation_loss_model`
              - Get the laser propagation loss model.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import LaserPropagationLossModels


Property detail
---------------

.. py:property:: enable_atmospheric_loss_model
    :canonical: ansys.stk.core.stkobjects.LaserPropagationLossModels.enable_atmospheric_loss_model
    :type: bool

    Get or set the option for computing atmospheric absorption propagation loss.

.. py:property:: atmospheric_loss_model
    :canonical: ansys.stk.core.stkobjects.LaserPropagationLossModels.atmospheric_loss_model
    :type: ILaserAtmosphericLossModel

    Get the laser atmospheric absorption loss model.

.. py:property:: enable_tropospheric_scintillation_loss_model
    :canonical: ansys.stk.core.stkobjects.LaserPropagationLossModels.enable_tropospheric_scintillation_loss_model
    :type: bool

    Get or set the option for computing tropospheric scintillation propagation loss.

.. py:property:: tropospheric_scintillation_loss_model
    :canonical: ansys.stk.core.stkobjects.LaserPropagationLossModels.tropospheric_scintillation_loss_model
    :type: ILaserTroposphericScintillationLossModel

    Get the laser propagation loss model.


Method detail
-------------



.. py:method:: set_atmospheric_loss_model(self, model_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.LaserPropagationLossModels.set_atmospheric_loss_model

    Set the current atmospheric absorption loss model by name.

    :Parameters:

    **model_name** : :obj:`~str`

    :Returns:

        :obj:`~None`




.. py:method:: set_tropospheric_scintillation_loss_model(self, model_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.LaserPropagationLossModels.set_tropospheric_scintillation_loss_model

    Set the current tropospheric scintillation loss model by name.

    :Parameters:

    **model_name** : :obj:`~str`

    :Returns:

        :obj:`~None`


