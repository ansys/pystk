IPropagationChannel
===================

.. py:class:: ansys.stk.core.stkobjects.IPropagationChannel

   object
   
   Provide access to the properties and methods defining a propagation channel.

.. py:currentmodule:: IPropagationChannel

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IPropagationChannel.set_atmos_absorption_model`
              - Set the atmospheric absorption model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPropagationChannel.set_rain_loss_model`
              - Set the rain loss model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPropagationChannel.set_urban_terrestrial_loss_model`
              - Set the urban/terrestrial loss model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPropagationChannel.set_clouds_and_fog_fading_loss_model`
              - Set the CloudsAndFogFading loss model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPropagationChannel.set_tropospheric_scintillation_fading_loss_model`
              - Set the Tropospheric Scintillation Fading loss model by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPropagationChannel.set_ionospheric_fading_loss_model`
              - Set the Ionospheric Fading loss model by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IPropagationChannel.enable_atmos_absorption`
              - Gets or sets the option to use the atmospheric absorption model.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPropagationChannel.supported_atmos_absorption_models`
              - Gets an array of supported atmospheric absorption model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPropagationChannel.atmos_absorption_model`
              - Gets the atmospheric absorption model.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPropagationChannel.enable_rain_loss`
              - Gets or sets the option to use the rain loss model.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPropagationChannel.supported_rain_loss_models`
              - Gets an array of supported rain loss model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPropagationChannel.rain_loss_model`
              - Gets the rain loss model.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPropagationChannel.custom_a`
              - Gets the Custom A propagation model.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPropagationChannel.custom_b`
              - Gets the Custom B propagation model.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPropagationChannel.custom_c`
              - Gets the Custom C propagation model.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPropagationChannel.enable_itu_618_section2_p5`
              - Gets or sets the option to enable the ITU 618 Section 2.5 model for computing total propagation loss.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPropagationChannel.enable_urban_terrestrial_loss`
              - Gets or sets the option to use the urban/terrestrial loss model.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPropagationChannel.supported_urban_terrestrial_loss_models`
              - Gets an array of supported urban/terrestrial loss model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPropagationChannel.urban_terrestrial_loss_model`
              - Gets the urban/terrestrial loss model.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPropagationChannel.supported_clouds_and_fog_fading_loss_models`
              - Gets an array of supported CloudsAndFog Fading loss model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPropagationChannel.clouds_and_fog_fading_loss_model`
              - Gets the CloudsAndFogFading loss model.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPropagationChannel.supported_tropospheric_scintillation_fading_loss_models`
              - Gets an array of supported Tropospheric Scintillation Fading loss model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPropagationChannel.tropospheric_scintillation_fading_loss_model`
              - Gets the Tropospheric Scintillation Fading loss model.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPropagationChannel.supported_ionospheric_fading_loss_models`
              - Gets an array of supported Ionospheric Fading loss model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPropagationChannel.ionospheric_fading_loss_model`
              - Gets the Ionospheric Fading loss model.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPropagationChannel.enable_clouds_and_fog_fading_loss`
              - Gets or sets the option to use the clouds and fog fading loss model.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPropagationChannel.enable_tropospheric_scintillation_fading_loss`
              - Gets or sets the option to use the tropospheric scintillation fading loss model.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPropagationChannel.enable_ionospheric_fading_loss`
              - Gets or sets the option to use the ionoospheric fading loss model.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IPropagationChannel


Property detail
---------------

.. py:property:: enable_atmos_absorption
    :canonical: ansys.stk.core.stkobjects.IPropagationChannel.enable_atmos_absorption
    :type: bool

    Gets or sets the option to use the atmospheric absorption model.

.. py:property:: supported_atmos_absorption_models
    :canonical: ansys.stk.core.stkobjects.IPropagationChannel.supported_atmos_absorption_models
    :type: list

    Gets an array of supported atmospheric absorption model names.

.. py:property:: atmos_absorption_model
    :canonical: ansys.stk.core.stkobjects.IPropagationChannel.atmos_absorption_model
    :type: IAtmosphericAbsorptionModel

    Gets the atmospheric absorption model.

.. py:property:: enable_rain_loss
    :canonical: ansys.stk.core.stkobjects.IPropagationChannel.enable_rain_loss
    :type: bool

    Gets or sets the option to use the rain loss model.

.. py:property:: supported_rain_loss_models
    :canonical: ansys.stk.core.stkobjects.IPropagationChannel.supported_rain_loss_models
    :type: list

    Gets an array of supported rain loss model names.

.. py:property:: rain_loss_model
    :canonical: ansys.stk.core.stkobjects.IPropagationChannel.rain_loss_model
    :type: IRainLossModel

    Gets the rain loss model.

.. py:property:: custom_a
    :canonical: ansys.stk.core.stkobjects.IPropagationChannel.custom_a
    :type: ICustomPropagationModel

    Gets the Custom A propagation model.

.. py:property:: custom_b
    :canonical: ansys.stk.core.stkobjects.IPropagationChannel.custom_b
    :type: ICustomPropagationModel

    Gets the Custom B propagation model.

.. py:property:: custom_c
    :canonical: ansys.stk.core.stkobjects.IPropagationChannel.custom_c
    :type: ICustomPropagationModel

    Gets the Custom C propagation model.

.. py:property:: enable_itu_618_section2_p5
    :canonical: ansys.stk.core.stkobjects.IPropagationChannel.enable_itu_618_section2_p5
    :type: bool

    Gets or sets the option to enable the ITU 618 Section 2.5 model for computing total propagation loss.

.. py:property:: enable_urban_terrestrial_loss
    :canonical: ansys.stk.core.stkobjects.IPropagationChannel.enable_urban_terrestrial_loss
    :type: bool

    Gets or sets the option to use the urban/terrestrial loss model.

.. py:property:: supported_urban_terrestrial_loss_models
    :canonical: ansys.stk.core.stkobjects.IPropagationChannel.supported_urban_terrestrial_loss_models
    :type: list

    Gets an array of supported urban/terrestrial loss model names.

.. py:property:: urban_terrestrial_loss_model
    :canonical: ansys.stk.core.stkobjects.IPropagationChannel.urban_terrestrial_loss_model
    :type: IUrbanTerrestrialLossModel

    Gets the urban/terrestrial loss model.

.. py:property:: supported_clouds_and_fog_fading_loss_models
    :canonical: ansys.stk.core.stkobjects.IPropagationChannel.supported_clouds_and_fog_fading_loss_models
    :type: list

    Gets an array of supported CloudsAndFog Fading loss model names.

.. py:property:: clouds_and_fog_fading_loss_model
    :canonical: ansys.stk.core.stkobjects.IPropagationChannel.clouds_and_fog_fading_loss_model
    :type: ICloudsAndFogFadingLossModel

    Gets the CloudsAndFogFading loss model.

.. py:property:: supported_tropospheric_scintillation_fading_loss_models
    :canonical: ansys.stk.core.stkobjects.IPropagationChannel.supported_tropospheric_scintillation_fading_loss_models
    :type: list

    Gets an array of supported Tropospheric Scintillation Fading loss model names.

.. py:property:: tropospheric_scintillation_fading_loss_model
    :canonical: ansys.stk.core.stkobjects.IPropagationChannel.tropospheric_scintillation_fading_loss_model
    :type: ITroposphericScintillationFadingLossModel

    Gets the Tropospheric Scintillation Fading loss model.

.. py:property:: supported_ionospheric_fading_loss_models
    :canonical: ansys.stk.core.stkobjects.IPropagationChannel.supported_ionospheric_fading_loss_models
    :type: list

    Gets an array of supported Ionospheric Fading loss model names.

.. py:property:: ionospheric_fading_loss_model
    :canonical: ansys.stk.core.stkobjects.IPropagationChannel.ionospheric_fading_loss_model
    :type: IIonosphericFadingLossModel

    Gets the Ionospheric Fading loss model.

.. py:property:: enable_clouds_and_fog_fading_loss
    :canonical: ansys.stk.core.stkobjects.IPropagationChannel.enable_clouds_and_fog_fading_loss
    :type: bool

    Gets or sets the option to use the clouds and fog fading loss model.

.. py:property:: enable_tropospheric_scintillation_fading_loss
    :canonical: ansys.stk.core.stkobjects.IPropagationChannel.enable_tropospheric_scintillation_fading_loss
    :type: bool

    Gets or sets the option to use the tropospheric scintillation fading loss model.

.. py:property:: enable_ionospheric_fading_loss
    :canonical: ansys.stk.core.stkobjects.IPropagationChannel.enable_ionospheric_fading_loss
    :type: bool

    Gets or sets the option to use the ionoospheric fading loss model.


Method detail
-------------




.. py:method:: set_atmos_absorption_model(self, modelName: str) -> None
    :canonical: ansys.stk.core.stkobjects.IPropagationChannel.set_atmos_absorption_model

    Set the atmospheric absorption model by name.

    :Parameters:

    **modelName** : :obj:`~str`

    :Returns:

        :obj:`~None`





.. py:method:: set_rain_loss_model(self, modelName: str) -> None
    :canonical: ansys.stk.core.stkobjects.IPropagationChannel.set_rain_loss_model

    Set the rain loss model by name.

    :Parameters:

    **modelName** : :obj:`~str`

    :Returns:

        :obj:`~None`










.. py:method:: set_urban_terrestrial_loss_model(self, modelName: str) -> None
    :canonical: ansys.stk.core.stkobjects.IPropagationChannel.set_urban_terrestrial_loss_model

    Set the urban/terrestrial loss model by name.

    :Parameters:

    **modelName** : :obj:`~str`

    :Returns:

        :obj:`~None`



.. py:method:: set_clouds_and_fog_fading_loss_model(self, modelName: str) -> None
    :canonical: ansys.stk.core.stkobjects.IPropagationChannel.set_clouds_and_fog_fading_loss_model

    Set the CloudsAndFogFading loss model by name.

    :Parameters:

    **modelName** : :obj:`~str`

    :Returns:

        :obj:`~None`



.. py:method:: set_tropospheric_scintillation_fading_loss_model(self, modelName: str) -> None
    :canonical: ansys.stk.core.stkobjects.IPropagationChannel.set_tropospheric_scintillation_fading_loss_model

    Set the Tropospheric Scintillation Fading loss model by name.

    :Parameters:

    **modelName** : :obj:`~str`

    :Returns:

        :obj:`~None`



.. py:method:: set_ionospheric_fading_loss_model(self, modelName: str) -> None
    :canonical: ansys.stk.core.stkobjects.IPropagationChannel.set_ionospheric_fading_loss_model

    Set the Ionospheric Fading loss model by name.

    :Parameters:

    **modelName** : :obj:`~str`

    :Returns:

        :obj:`~None`








