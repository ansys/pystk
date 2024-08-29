Atmosphere
==========

.. py:class:: ansys.stk.core.stkobjects.Atmosphere

   Bases: :py:class:`~ansys.stk.core.stkobjects.IPlatformRFEnvironment`

   Class defining local atmosphere.

.. py:currentmodule:: Atmosphere

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Atmosphere.set_local_atmos_absorption_model`
              - Do not use this method, as it is deprecated. Use the PropagationChannel property to set the atmospheric absorption model.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Atmosphere.inherit_atmos_absorption_model`
              - This property is deprecated. Use the PropagationChannel property to enable or disable the atmospheric absorption model.
            * - :py:attr:`~ansys.stk.core.stkobjects.Atmosphere.supported_local_atmos_absorption_models`
              - This property is deprecated. Use the PropagationChannel property to determine the supported atmospheric absorption models.
            * - :py:attr:`~ansys.stk.core.stkobjects.Atmosphere.local_atmos_absorption_model`
              - This property is deprecated. Use the PropagationChannel property to get the atmospheric absorption model.
            * - :py:attr:`~ansys.stk.core.stkobjects.Atmosphere.enable_local_rain_data`
              - Gets or sets the option for enabling local rain data.
            * - :py:attr:`~ansys.stk.core.stkobjects.Atmosphere.local_rain_iso_height`
              - Gets or sets the local rain iso height.
            * - :py:attr:`~ansys.stk.core.stkobjects.Atmosphere.local_rain_rate`
              - Gets or sets the local rain rate.
            * - :py:attr:`~ansys.stk.core.stkobjects.Atmosphere.local_surface_temperature`
              - This property is deprecated. Gets or sets the local surface temperature.
            * - :py:attr:`~ansys.stk.core.stkobjects.Atmosphere.propagation_channel`
              - Gets the propagation channel.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Atmosphere


Property detail
---------------

.. py:property:: inherit_atmos_absorption_model
    :canonical: ansys.stk.core.stkobjects.Atmosphere.inherit_atmos_absorption_model
    :type: bool

    This property is deprecated. Use the PropagationChannel property to enable or disable the atmospheric absorption model.

.. py:property:: supported_local_atmos_absorption_models
    :canonical: ansys.stk.core.stkobjects.Atmosphere.supported_local_atmos_absorption_models
    :type: list

    This property is deprecated. Use the PropagationChannel property to determine the supported atmospheric absorption models.

.. py:property:: local_atmos_absorption_model
    :canonical: ansys.stk.core.stkobjects.Atmosphere.local_atmos_absorption_model
    :type: IAtmosphericAbsorptionModel

    This property is deprecated. Use the PropagationChannel property to get the atmospheric absorption model.

.. py:property:: enable_local_rain_data
    :canonical: ansys.stk.core.stkobjects.Atmosphere.enable_local_rain_data
    :type: bool

    Gets or sets the option for enabling local rain data.

.. py:property:: local_rain_iso_height
    :canonical: ansys.stk.core.stkobjects.Atmosphere.local_rain_iso_height
    :type: float

    Gets or sets the local rain iso height.

.. py:property:: local_rain_rate
    :canonical: ansys.stk.core.stkobjects.Atmosphere.local_rain_rate
    :type: float

    Gets or sets the local rain rate.

.. py:property:: local_surface_temperature
    :canonical: ansys.stk.core.stkobjects.Atmosphere.local_surface_temperature
    :type: float

    This property is deprecated. Gets or sets the local surface temperature.

.. py:property:: propagation_channel
    :canonical: ansys.stk.core.stkobjects.Atmosphere.propagation_channel
    :type: PropagationChannel

    Gets the propagation channel.


Method detail
-------------




.. py:method:: set_local_atmos_absorption_model(self, modelName: str) -> None
    :canonical: ansys.stk.core.stkobjects.Atmosphere.set_local_atmos_absorption_model

    Do not use this method, as it is deprecated. Use the PropagationChannel property to set the atmospheric absorption model.

    :Parameters:

    **modelName** : :obj:`~str`

    :Returns:

        :obj:`~None`











