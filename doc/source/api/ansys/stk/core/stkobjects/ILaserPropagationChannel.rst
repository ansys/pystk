ILaserPropagationChannel
========================

.. py:class:: ansys.stk.core.stkobjects.ILaserPropagationChannel

   object
   
   Provide access to laser propagation loss models.

.. py:currentmodule:: ILaserPropagationChannel

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ILaserPropagationChannel.set_atmospheric_loss_model`
              - Set the current atmospheric absorption loss model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaserPropagationChannel.set_tropospheric_scintillation_loss_model`
              - Set the current tropospheric scintillation loss model by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ILaserPropagationChannel.enable_atmospheric_loss_model`
              - Gets or set the option for computing atmospheric absorption propagation loss.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaserPropagationChannel.atmospheric_loss_model`
              - Gets the laser atmospheric absorption loss model.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaserPropagationChannel.enable_tropospheric_scintillation_loss_model`
              - Gets or set the option for computing tropospheric scintillation propagation loss.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaserPropagationChannel.tropospheric_scintillation_loss_model`
              - Gets the laser propagation loss model.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ILaserPropagationChannel


Property detail
---------------

.. py:property:: enable_atmospheric_loss_model
    :canonical: ansys.stk.core.stkobjects.ILaserPropagationChannel.enable_atmospheric_loss_model
    :type: bool

    Gets or set the option for computing atmospheric absorption propagation loss.

.. py:property:: atmospheric_loss_model
    :canonical: ansys.stk.core.stkobjects.ILaserPropagationChannel.atmospheric_loss_model
    :type: ILaserAtmosphericLossModel

    Gets the laser atmospheric absorption loss model.

.. py:property:: enable_tropospheric_scintillation_loss_model
    :canonical: ansys.stk.core.stkobjects.ILaserPropagationChannel.enable_tropospheric_scintillation_loss_model
    :type: bool

    Gets or set the option for computing tropospheric scintillation propagation loss.

.. py:property:: tropospheric_scintillation_loss_model
    :canonical: ansys.stk.core.stkobjects.ILaserPropagationChannel.tropospheric_scintillation_loss_model
    :type: ILaserTroposphericScintillationLossModel

    Gets the laser propagation loss model.


Method detail
-------------



.. py:method:: set_atmospheric_loss_model(self, modelName: str) -> None
    :canonical: ansys.stk.core.stkobjects.ILaserPropagationChannel.set_atmospheric_loss_model

    Set the current atmospheric absorption loss model by name.

    :Parameters:

    **modelName** : :obj:`~str`

    :Returns:

        :obj:`~None`




.. py:method:: set_tropospheric_scintillation_loss_model(self, modelName: str) -> None
    :canonical: ansys.stk.core.stkobjects.ILaserPropagationChannel.set_tropospheric_scintillation_loss_model

    Set the current tropospheric scintillation loss model by name.

    :Parameters:

    **modelName** : :obj:`~str`

    :Returns:

        :obj:`~None`


