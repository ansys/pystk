PropagationChannel
==================

.. py:class:: ansys.stk.core.stkobjects.PropagationChannel

   Class defining the propagation channel.

.. py:currentmodule:: PropagationChannel

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.atmospheric_absorption_model_component_linking`
              - Get the link/embed controller for managing the atmospheric absorption model component.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.clouds_and_fog_fading_loss_model_component_linking`
              - Get the link/embed controller for managing the clouds and fog fading loss model component.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.custom_a`
              - Get the Custom A propagation model.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.custom_b`
              - Get the Custom B propagation model.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.custom_c`
              - Get the Custom C propagation model.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.enable_atmospheric_absorption`
              - Get or set the option to use the atmospheric absorption model.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.enable_clouds_and_fog_fading_loss`
              - Get or set the option to use the clouds and fog fading loss model.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.enable_ionospheric_fading_loss`
              - Get or set the option to use the ionoospheric fading loss model.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.enable_itu_618_section2_p5`
              - Get or set the option to enable the ITU 618 Section 2.5 model for computing total propagation loss.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.enable_rain_loss`
              - Get or set the option to use the rain loss model.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.enable_tropospheric_scintillation_fading_loss`
              - Get or set the option to use the tropospheric scintillation fading loss model.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.enable_urban_terrestrial_loss`
              - Get or set the option to use the urban/terrestrial loss model.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.ionospheric_fading_loss_model_component_linking`
              - Get the link/embed controller for managing the ionospheric fading loss model component.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.rain_loss_model_component_linking`
              - Get the link/embed controller for managing the rain loss model component.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.tropospheric_scintillation_fading_loss_model_component_linking`
              - Get the link/embed controller for managing the tropospheric scintillation fading loss model component.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagationChannel.urban_terrestrial_loss_model_component_linking`
              - Get the link/embed controller for managing the urban terrestrial loss model component.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import PropagationChannel


Property detail
---------------

.. py:property:: atmospheric_absorption_model_component_linking
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.atmospheric_absorption_model_component_linking
    :type: IComponentLinkEmbedControl

    Get the link/embed controller for managing the atmospheric absorption model component.

.. py:property:: clouds_and_fog_fading_loss_model_component_linking
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.clouds_and_fog_fading_loss_model_component_linking
    :type: IComponentLinkEmbedControl

    Get the link/embed controller for managing the clouds and fog fading loss model component.

.. py:property:: custom_a
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.custom_a
    :type: CustomPropagationModel

    Get the Custom A propagation model.

.. py:property:: custom_b
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.custom_b
    :type: CustomPropagationModel

    Get the Custom B propagation model.

.. py:property:: custom_c
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.custom_c
    :type: CustomPropagationModel

    Get the Custom C propagation model.

.. py:property:: enable_atmospheric_absorption
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.enable_atmospheric_absorption
    :type: bool

    Get or set the option to use the atmospheric absorption model.

.. py:property:: enable_clouds_and_fog_fading_loss
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.enable_clouds_and_fog_fading_loss
    :type: bool

    Get or set the option to use the clouds and fog fading loss model.

.. py:property:: enable_ionospheric_fading_loss
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.enable_ionospheric_fading_loss
    :type: bool

    Get or set the option to use the ionoospheric fading loss model.

.. py:property:: enable_itu_618_section2_p5
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.enable_itu_618_section2_p5
    :type: bool

    Get or set the option to enable the ITU 618 Section 2.5 model for computing total propagation loss.

.. py:property:: enable_rain_loss
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.enable_rain_loss
    :type: bool

    Get or set the option to use the rain loss model.

.. py:property:: enable_tropospheric_scintillation_fading_loss
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.enable_tropospheric_scintillation_fading_loss
    :type: bool

    Get or set the option to use the tropospheric scintillation fading loss model.

.. py:property:: enable_urban_terrestrial_loss
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.enable_urban_terrestrial_loss
    :type: bool

    Get or set the option to use the urban/terrestrial loss model.

.. py:property:: ionospheric_fading_loss_model_component_linking
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.ionospheric_fading_loss_model_component_linking
    :type: IComponentLinkEmbedControl

    Get the link/embed controller for managing the ionospheric fading loss model component.

.. py:property:: rain_loss_model_component_linking
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.rain_loss_model_component_linking
    :type: IComponentLinkEmbedControl

    Get the link/embed controller for managing the rain loss model component.

.. py:property:: tropospheric_scintillation_fading_loss_model_component_linking
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.tropospheric_scintillation_fading_loss_model_component_linking
    :type: IComponentLinkEmbedControl

    Get the link/embed controller for managing the tropospheric scintillation fading loss model component.

.. py:property:: urban_terrestrial_loss_model_component_linking
    :canonical: ansys.stk.core.stkobjects.PropagationChannel.urban_terrestrial_loss_model_component_linking
    :type: IComponentLinkEmbedControl

    Get the link/embed controller for managing the urban terrestrial loss model component.


