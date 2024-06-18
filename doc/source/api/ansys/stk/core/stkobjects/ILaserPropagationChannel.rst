ILaserPropagationChannel
========================

.. py:class:: ILaserPropagationChannel

   object
   
   Provide access to laser propagation loss models.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_atmospheric_loss_model`
              - Set the current atmospheric absorption loss model by name.
            * - :py:meth:`~set_tropospheric_scintillation_loss_model`
              - Set the current tropospheric scintillation loss model by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~enable_atmospheric_loss_model`
            * - :py:meth:`~atmospheric_loss_model`
            * - :py:meth:`~enable_tropospheric_scintillation_loss_model`
            * - :py:meth:`~tropospheric_scintillation_loss_model`


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
    :type: "IAgLaserAtmosphericLossModel"

    Gets the laser atmospheric absorption loss model.

.. py:property:: enable_tropospheric_scintillation_loss_model
    :canonical: ansys.stk.core.stkobjects.ILaserPropagationChannel.enable_tropospheric_scintillation_loss_model
    :type: bool

    Gets or set the option for computing tropospheric scintillation propagation loss.

.. py:property:: tropospheric_scintillation_loss_model
    :canonical: ansys.stk.core.stkobjects.ILaserPropagationChannel.tropospheric_scintillation_loss_model
    :type: "IAgLaserTroposphericScintillationLossModel"

    Gets the laser propagation loss model.


Method detail
-------------



.. py:method:: set_atmospheric_loss_model(self, modelName:str) -> None

    Set the current atmospheric absorption loss model by name.

    :Parameters:

    **modelName** : :obj:`~str`

    :Returns:

        :obj:`~None`




.. py:method:: set_tropospheric_scintillation_loss_model(self, modelName:str) -> None

    Set the current tropospheric scintillation loss model by name.

    :Parameters:

    **modelName** : :obj:`~str`

    :Returns:

        :obj:`~None`


