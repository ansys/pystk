PropagationChannel
==================

.. py:class:: ansys.stk.core.stkobjects.PropagationChannel

   Class defining the propagation channel.

.. py:currentmodule:: PropagationChannel

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.set_atmospheric_absorption_model`
              - Do not use this method, as it is deprecated. Use AtmosAbsorptionModelComponentLinking on IAgPropagationChannel instead. Sets the atmospheric absorption model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.set_rain_loss_model`
              - Do not use this method, as it is deprecated. Use RainLossModelComponentLinking on IAgPropagationChannel instead. Sets the rain loss model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.set_urban_terrestrial_loss_model`
              - Do not use this method, as it is deprecated. Use UrbanTerrestrialLossModelComponentLinking on IAgPropagationChannel instead. Sets the urban/terrestrial loss model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.set_clouds_and_fog_fading_loss_model`
              - Do not use this method, as it is deprecated. Use CloudsAndFogFadingLossModelComponentLinking on IAgPropagationChannel instead. Sets the CloudsAndFogFading loss model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.set_tropospheric_scintillation_fading_loss_model`
              - Do not use this method, as it is deprecated. Use TroposphericScintillationFadingLossModelComponentLinking on IAgPropagationChannel instead. Sets the Tropospheric Scintillation Fading loss model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.set_ionospheric_fading_loss_model`
              - Do not use this method, as it is deprecated. Use IonosphericFadingLossModelComponentLinking on IAgPropagationChannel instead. Sets the Ionospheric Fading loss model by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.enable_atmospheric_absorption`
              - Gets or sets the option to use the atmospheric absorption model.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.supported_atmospheric_absorption_models`
              - This property is deprecated. Use AtmosAbsorptionModelComponentLinking on IAgPropagationChannel instead. Gets an array of supported atmospheric absorption model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.atmospheric_absorption_model`
              - This property is deprecated. Use AtmosAbsorptionModelComponentLinking on IAgPropagationChannel instead. Gets the atmospheric absorption model.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.enable_rain_loss`
              - Gets or sets the option to use the rain loss model.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.supported_rain_loss_models`
              - This property is deprecated. Use RainLossModelComponentLinking on IAgPropagationChannel instead. Gets an array of supported rain loss model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.rain_loss_model`
              - This property is deprecated. Use RainLossModelComponentLinking on IAgPropagationChannel instead. Gets the rain loss model.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.custom_a`
              - Gets the Custom A propagation model.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.custom_b`
              - Gets the Custom B propagation model.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.custom_c`
              - Gets the Custom C propagation model.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.enable_itu_618_section2_p5`
              - Gets or sets the option to enable the ITU 618 Section 2.5 model for computing total propagation loss.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.enable_urban_terrestrial_loss`
              - Gets or sets the option to use the urban/terrestrial loss model.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.supported_urban_terrestrial_loss_models`
              - This property is deprecated. Use UrbanTerrestrialLossModelComponentLinking on IAgPropagationChannel instead. Gets an array of supported urban/terrestrial loss model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.urban_terrestrial_loss_model`
              - This property is deprecated. Use UrbanTerrestrialLossModelComponentLinking on IAgPropagationChannel instead. Gets the urban/terrestrial loss model.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.supported_clouds_and_fog_fading_loss_models`
              - This property is deprecated. Use CloudsAndFogFadingLossModelComponentLinking on IAgPropagationChannel instead. Gets an array of supported CloudsAndFog Fading loss model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.clouds_and_fog_fading_loss_model`
              - This property is deprecated. Use CloudsAndFogFadingLossModelComponentLinking on IAgPropagationChannel instead. Gets the CloudsAndFogFading loss model.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.supported_tropospheric_scintillation_fading_loss_models`
              - This property is deprecated. Use TroposphericScintillationFadingLossModelComponentLinking on IAgPropagationChannel instead. Gets an array of supported Tropospheric Scintillation Fading loss model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.tropospheric_scintillation_fading_loss_model`
              - This property is deprecated. Use TroposphericScintillationFadingLossModelComponentLinking on IAgPropagationChannel instead. Gets the Tropospheric Scintillation Fading loss model.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.supported_ionospheric_fading_loss_models`
              - This property is deprecated. Use IonosphericFadingLossModelComponentLinking on IAgPropagationChannel instead. Gets an array of supported Ionospheric Fading loss model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.ionospheric_fading_loss_model`
              - This property is deprecated. Use IonosphericFadingLossModelComponentLinking on IAgPropagationChannel instead. Gets the Ionospheric Fading loss model.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.enable_clouds_and_fog_fading_loss`
              - Gets or sets the option to use the clouds and fog fading loss model.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.enable_tropospheric_scintillation_fading_loss`
              - Gets or sets the option to use the tropospheric scintillation fading loss model.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.enable_ionospheric_fading_loss`
              - Gets or sets the option to use the ionoospheric fading loss model.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.atmos_absorption_model_component_linking`
              - Gets the link/embed controller for managing the atmospheric absorption model component.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.rain_loss_model_component_linking`
              - Gets the link/embed controller for managing the rain loss model component.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.urban_terrestrial_loss_model_component_linking`
              - Gets the link/embed controller for managing the urban terrestrial loss model component.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.clouds_and_fog_fading_loss_model_component_linking`
              - Gets the link/embed controller for managing the clouds and fog fading loss model component.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.tropospheric_scintillation_fading_loss_model_component_linking`
              - Gets the link/embed controller for managing the tropospheric scintillation fading loss model component.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.ionospheric_fading_loss_model_component_linking`
              - Gets the link/embed controller for managing the ionospheric fading loss model component.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import PropagationChannel


Property detail
---------------

.. py:property:: enable_atmospheric_absorption
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.enable_atmospheric_absorption
    :type: bool

    Gets or sets the option to use the atmospheric absorption model.

.. py:property:: supported_atmospheric_absorption_models
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.supported_atmospheric_absorption_models
    :type: list

    This property is deprecated. Use AtmosAbsorptionModelComponentLinking on IAgPropagationChannel instead. Gets an array of supported atmospheric absorption model names.

.. py:property:: atmospheric_absorption_model
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.atmospheric_absorption_model
    :type: IAtmosphericAbsorptionModel

    This property is deprecated. Use AtmosAbsorptionModelComponentLinking on IAgPropagationChannel instead. Gets the atmospheric absorption model.

.. py:property:: enable_rain_loss
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.enable_rain_loss
    :type: bool

    Gets or sets the option to use the rain loss model.

.. py:property:: supported_rain_loss_models
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.supported_rain_loss_models
    :type: list

    This property is deprecated. Use RainLossModelComponentLinking on IAgPropagationChannel instead. Gets an array of supported rain loss model names.

.. py:property:: rain_loss_model
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.rain_loss_model
    :type: IRainLossModel

    This property is deprecated. Use RainLossModelComponentLinking on IAgPropagationChannel instead. Gets the rain loss model.

.. py:property:: custom_a
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.custom_a
    :type: CustomPropagationModel

    Gets the Custom A propagation model.

.. py:property:: custom_b
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.custom_b
    :type: CustomPropagationModel

    Gets the Custom B propagation model.

.. py:property:: custom_c
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.custom_c
    :type: CustomPropagationModel

    Gets the Custom C propagation model.

.. py:property:: enable_itu_618_section2_p5
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.enable_itu_618_section2_p5
    :type: bool

    Gets or sets the option to enable the ITU 618 Section 2.5 model for computing total propagation loss.

.. py:property:: enable_urban_terrestrial_loss
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.enable_urban_terrestrial_loss
    :type: bool

    Gets or sets the option to use the urban/terrestrial loss model.

.. py:property:: supported_urban_terrestrial_loss_models
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.supported_urban_terrestrial_loss_models
    :type: list

    This property is deprecated. Use UrbanTerrestrialLossModelComponentLinking on IAgPropagationChannel instead. Gets an array of supported urban/terrestrial loss model names.

.. py:property:: urban_terrestrial_loss_model
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.urban_terrestrial_loss_model
    :type: IUrbanTerrestrialLossModel

    This property is deprecated. Use UrbanTerrestrialLossModelComponentLinking on IAgPropagationChannel instead. Gets the urban/terrestrial loss model.

.. py:property:: supported_clouds_and_fog_fading_loss_models
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.supported_clouds_and_fog_fading_loss_models
    :type: list

    This property is deprecated. Use CloudsAndFogFadingLossModelComponentLinking on IAgPropagationChannel instead. Gets an array of supported CloudsAndFog Fading loss model names.

.. py:property:: clouds_and_fog_fading_loss_model
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.clouds_and_fog_fading_loss_model
    :type: ICloudsAndFogFadingLossModel

    This property is deprecated. Use CloudsAndFogFadingLossModelComponentLinking on IAgPropagationChannel instead. Gets the CloudsAndFogFading loss model.

.. py:property:: supported_tropospheric_scintillation_fading_loss_models
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.supported_tropospheric_scintillation_fading_loss_models
    :type: list

    This property is deprecated. Use TroposphericScintillationFadingLossModelComponentLinking on IAgPropagationChannel instead. Gets an array of supported Tropospheric Scintillation Fading loss model names.

.. py:property:: tropospheric_scintillation_fading_loss_model
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.tropospheric_scintillation_fading_loss_model
    :type: ITroposphericScintillationFadingLossModel

    This property is deprecated. Use TroposphericScintillationFadingLossModelComponentLinking on IAgPropagationChannel instead. Gets the Tropospheric Scintillation Fading loss model.

.. py:property:: supported_ionospheric_fading_loss_models
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.supported_ionospheric_fading_loss_models
    :type: list

    This property is deprecated. Use IonosphericFadingLossModelComponentLinking on IAgPropagationChannel instead. Gets an array of supported Ionospheric Fading loss model names.

.. py:property:: ionospheric_fading_loss_model
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.ionospheric_fading_loss_model
    :type: IIonosphericFadingLossModel

    This property is deprecated. Use IonosphericFadingLossModelComponentLinking on IAgPropagationChannel instead. Gets the Ionospheric Fading loss model.

.. py:property:: enable_clouds_and_fog_fading_loss
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.enable_clouds_and_fog_fading_loss
    :type: bool

    Gets or sets the option to use the clouds and fog fading loss model.

.. py:property:: enable_tropospheric_scintillation_fading_loss
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.enable_tropospheric_scintillation_fading_loss
    :type: bool

    Gets or sets the option to use the tropospheric scintillation fading loss model.

.. py:property:: enable_ionospheric_fading_loss
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.enable_ionospheric_fading_loss
    :type: bool

    Gets or sets the option to use the ionoospheric fading loss model.

.. py:property:: atmos_absorption_model_component_linking
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.atmos_absorption_model_component_linking
    :type: IComponentLinkEmbedControl

    Gets the link/embed controller for managing the atmospheric absorption model component.

.. py:property:: rain_loss_model_component_linking
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.rain_loss_model_component_linking
    :type: IComponentLinkEmbedControl

    Gets the link/embed controller for managing the rain loss model component.

.. py:property:: urban_terrestrial_loss_model_component_linking
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.urban_terrestrial_loss_model_component_linking
    :type: IComponentLinkEmbedControl

    Gets the link/embed controller for managing the urban terrestrial loss model component.

.. py:property:: clouds_and_fog_fading_loss_model_component_linking
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.clouds_and_fog_fading_loss_model_component_linking
    :type: IComponentLinkEmbedControl

    Gets the link/embed controller for managing the clouds and fog fading loss model component.

.. py:property:: tropospheric_scintillation_fading_loss_model_component_linking
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.tropospheric_scintillation_fading_loss_model_component_linking
    :type: IComponentLinkEmbedControl

    Gets the link/embed controller for managing the tropospheric scintillation fading loss model component.

.. py:property:: ionospheric_fading_loss_model_component_linking
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.ionospheric_fading_loss_model_component_linking
    :type: IComponentLinkEmbedControl

    Gets the link/embed controller for managing the ionospheric fading loss model component.


Method detail
-------------




.. py:method:: set_atmospheric_absorption_model(self, model_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.set_atmospheric_absorption_model

    Do not use this method, as it is deprecated. Use AtmosAbsorptionModelComponentLinking on IAgPropagationChannel instead. Sets the atmospheric absorption model by name.

    :Parameters:

    **model_name** : :obj:`~str`

    :Returns:

        :obj:`~None`





.. py:method:: set_rain_loss_model(self, model_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.set_rain_loss_model

    Do not use this method, as it is deprecated. Use RainLossModelComponentLinking on IAgPropagationChannel instead. Sets the rain loss model by name.

    :Parameters:

    **model_name** : :obj:`~str`

    :Returns:

        :obj:`~None`










.. py:method:: set_urban_terrestrial_loss_model(self, model_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.set_urban_terrestrial_loss_model

    Do not use this method, as it is deprecated. Use UrbanTerrestrialLossModelComponentLinking on IAgPropagationChannel instead. Sets the urban/terrestrial loss model by name.

    :Parameters:

    **model_name** : :obj:`~str`

    :Returns:

        :obj:`~None`



.. py:method:: set_clouds_and_fog_fading_loss_model(self, model_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.set_clouds_and_fog_fading_loss_model

    Do not use this method, as it is deprecated. Use CloudsAndFogFadingLossModelComponentLinking on IAgPropagationChannel instead. Sets the CloudsAndFogFading loss model by name.

    :Parameters:

    **model_name** : :obj:`~str`

    :Returns:

        :obj:`~None`



.. py:method:: set_tropospheric_scintillation_fading_loss_model(self, model_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.set_tropospheric_scintillation_fading_loss_model

    Do not use this method, as it is deprecated. Use TroposphericScintillationFadingLossModelComponentLinking on IAgPropagationChannel instead. Sets the Tropospheric Scintillation Fading loss model by name.

    :Parameters:

    **model_name** : :obj:`~str`

    :Returns:

        :obj:`~None`



.. py:method:: set_ionospheric_fading_loss_model(self, model_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.set_ionospheric_fading_loss_model

    Do not use this method, as it is deprecated. Use IonosphericFadingLossModelComponentLinking on IAgPropagationChannel instead. Sets the Ionospheric Fading loss model by name.

    :Parameters:

    **model_name** : :obj:`~str`

    :Returns:

        :obj:`~None`














