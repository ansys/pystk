LaserPropagationChannel
=======================

.. py:class:: ansys.stk.core.stkobjects.LaserPropagationChannel

   Class defining the properties for laser propagatoin models.

.. py:currentmodule:: LaserPropagationChannel

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.LaserPropagationChannel.atmospheric_loss_model_component_linking`
              - Get the link/embed controller for managing the atmospheric loss model component.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaserPropagationChannel.enable_atmospheric_loss_model`
              - Get or set the option for computing atmospheric absorption propagation loss.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaserPropagationChannel.enable_tropospheric_scintillation_loss_model`
              - Get or set the option for computing tropospheric scintillation propagation loss.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaserPropagationChannel.tropospheric_scintillation_loss_model_component_linking`
              - Get the link/embed controller for managing the tropospheric scintillation loss model component.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import LaserPropagationChannel


Property detail
---------------

.. py:property:: atmospheric_loss_model_component_linking
    :canonical: ansys.stk.core.stkobjects.LaserPropagationChannel.atmospheric_loss_model_component_linking
    :type: IComponentLinkEmbedControl

    Get the link/embed controller for managing the atmospheric loss model component.

.. py:property:: enable_atmospheric_loss_model
    :canonical: ansys.stk.core.stkobjects.LaserPropagationChannel.enable_atmospheric_loss_model
    :type: bool

    Get or set the option for computing atmospheric absorption propagation loss.

.. py:property:: enable_tropospheric_scintillation_loss_model
    :canonical: ansys.stk.core.stkobjects.LaserPropagationChannel.enable_tropospheric_scintillation_loss_model
    :type: bool

    Get or set the option for computing tropospheric scintillation propagation loss.

.. py:property:: tropospheric_scintillation_loss_model_component_linking
    :canonical: ansys.stk.core.stkobjects.LaserPropagationChannel.tropospheric_scintillation_loss_model_component_linking
    :type: IComponentLinkEmbedControl

    Get the link/embed controller for managing the tropospheric scintillation loss model component.


