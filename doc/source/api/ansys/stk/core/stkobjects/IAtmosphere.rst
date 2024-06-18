IAtmosphere
===========

.. py:class:: IAtmosphere

   object
   
   Provide access to the properties and methods defining the local atmosphere.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_local_atmos_absorption_model`
              - Do not use this method, as it is deprecated. Use the PropagationChannel property to set the atmospheric absorption model.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~inherit_atmos_absorption_model`
            * - :py:meth:`~supported_local_atmos_absorption_models`
            * - :py:meth:`~local_atmos_absorption_model`
            * - :py:meth:`~enable_local_rain_data`
            * - :py:meth:`~local_rain_iso_height`
            * - :py:meth:`~local_rain_rate`
            * - :py:meth:`~local_surface_temperature`
            * - :py:meth:`~propagation_channel`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAtmosphere


Property detail
---------------

.. py:property:: inherit_atmos_absorption_model
    :canonical: ansys.stk.core.stkobjects.IAtmosphere.inherit_atmos_absorption_model
    :type: bool

    This property is deprecated. Use the PropagationChannel property to enable or disable the atmospheric absorption model.

.. py:property:: supported_local_atmos_absorption_models
    :canonical: ansys.stk.core.stkobjects.IAtmosphere.supported_local_atmos_absorption_models
    :type: list

    This property is deprecated. Use the PropagationChannel property to determine the supported atmospheric absorption models.

.. py:property:: local_atmos_absorption_model
    :canonical: ansys.stk.core.stkobjects.IAtmosphere.local_atmos_absorption_model
    :type: "IAgAtmosphericAbsorptionModel"

    This property is deprecated. Use the PropagationChannel property to get the atmospheric absorption model.

.. py:property:: enable_local_rain_data
    :canonical: ansys.stk.core.stkobjects.IAtmosphere.enable_local_rain_data
    :type: bool

    Gets or sets the option for enabling local rain data.

.. py:property:: local_rain_iso_height
    :canonical: ansys.stk.core.stkobjects.IAtmosphere.local_rain_iso_height
    :type: float

    Gets or sets the local rain iso height.

.. py:property:: local_rain_rate
    :canonical: ansys.stk.core.stkobjects.IAtmosphere.local_rain_rate
    :type: float

    Gets or sets the local rain rate.

.. py:property:: local_surface_temperature
    :canonical: ansys.stk.core.stkobjects.IAtmosphere.local_surface_temperature
    :type: float

    This property is deprecated. Gets or sets the local surface temperature.

.. py:property:: propagation_channel
    :canonical: ansys.stk.core.stkobjects.IAtmosphere.propagation_channel
    :type: "IAgPropagationChannel"

    Gets the propagation channel.


Method detail
-------------




.. py:method:: set_local_atmos_absorption_model(self, modelName:str) -> None

    Do not use this method, as it is deprecated. Use the PropagationChannel property to set the atmospheric absorption model.

    :Parameters:

    **modelName** : :obj:`~str`

    :Returns:

        :obj:`~None`











