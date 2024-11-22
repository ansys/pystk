ILaserPropagationChannel
========================

.. py:class:: ansys.stk.core.stkobjects.ILaserPropagationChannel

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
              - Do not use this method, as it is deprecated. Use AtmosphericLossModelComponentLinking on IAgLaserPropagationChannel instead. Sets the current atmospheric absorption loss model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaserPropagationChannel.set_tropospheric_scintillation_loss_model`
              - Do not use this method, as it is deprecated. Use TroposphericScintillationLossModelComponentLinking on IAgLaserPropagationChannel instead. Sets the current tropospheric scintillation loss model by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ILaserPropagationChannel.enable_atmospheric_loss_model`
              - Gets or set the option for computing atmospheric absorption propagation loss.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaserPropagationChannel.atmospheric_loss_model`
              - This property is deprecated. Use AtmosphericLossModelComponentLinking on IAgLaserPropagationChannel instead. Gets the laser atmospheric absorption loss model.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaserPropagationChannel.enable_tropospheric_scintillation_loss_model`
              - Gets or set the option for computing tropospheric scintillation propagation loss.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaserPropagationChannel.tropospheric_scintillation_loss_model`
              - This property is deprecated. Use TroposphericScintillationLossModelComponentLinking on IAgLaserPropagationChannel instead. Gets the laser propagation loss model.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaserPropagationChannel.atmospheric_loss_model_component_linking`
              - Gets the link/embed controller for managing the atmospheric loss model component.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILaserPropagationChannel.tropospheric_scintillation_loss_model_component_linking`
              - Gets the link/embed controller for managing the tropospheric scintillation loss model component.


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

    This property is deprecated. Use AtmosphericLossModelComponentLinking on IAgLaserPropagationChannel instead. Gets the laser atmospheric absorption loss model.

.. py:property:: enable_tropospheric_scintillation_loss_model
    :canonical: ansys.stk.core.stkobjects.ILaserPropagationChannel.enable_tropospheric_scintillation_loss_model
    :type: bool

    Gets or set the option for computing tropospheric scintillation propagation loss.

.. py:property:: tropospheric_scintillation_loss_model
    :canonical: ansys.stk.core.stkobjects.ILaserPropagationChannel.tropospheric_scintillation_loss_model
    :type: ILaserTroposphericScintillationLossModel

    This property is deprecated. Use TroposphericScintillationLossModelComponentLinking on IAgLaserPropagationChannel instead. Gets the laser propagation loss model.

.. py:property:: atmospheric_loss_model_component_linking
    :canonical: ansys.stk.core.stkobjects.ILaserPropagationChannel.atmospheric_loss_model_component_linking
    :type: IComponentLinkEmbedControl

    Gets the link/embed controller for managing the atmospheric loss model component.

.. py:property:: tropospheric_scintillation_loss_model_component_linking
    :canonical: ansys.stk.core.stkobjects.ILaserPropagationChannel.tropospheric_scintillation_loss_model_component_linking
    :type: IComponentLinkEmbedControl

    Gets the link/embed controller for managing the tropospheric scintillation loss model component.


Method detail
-------------



.. py:method:: set_atmospheric_loss_model(self, model_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.ILaserPropagationChannel.set_atmospheric_loss_model

    Do not use this method, as it is deprecated. Use AtmosphericLossModelComponentLinking on IAgLaserPropagationChannel instead. Sets the current atmospheric absorption loss model by name.

    :Parameters:

    **model_name** : :obj:`~str`

    :Returns:

        :obj:`~None`




.. py:method:: set_tropospheric_scintillation_loss_model(self, model_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.ILaserPropagationChannel.set_tropospheric_scintillation_loss_model

    Do not use this method, as it is deprecated. Use TroposphericScintillationLossModelComponentLinking on IAgLaserPropagationChannel instead. Sets the current tropospheric scintillation loss model by name.

    :Parameters:

    **model_name** : :obj:`~str`

    :Returns:

        :obj:`~None`




