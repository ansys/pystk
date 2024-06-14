IPlatformRFEnvironment
======================

.. py:class:: IPlatformRFEnvironment

   object
   
   Provide access to the properties and methods defining the platform RF environment.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~enable_local_rain_data`
            * - :py:meth:`~local_rain_iso_height`
            * - :py:meth:`~local_rain_rate`
            * - :py:meth:`~local_surface_temperature`
            * - :py:meth:`~propagation_channel`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IPlatformRFEnvironment


Property detail
---------------

.. py:property:: enable_local_rain_data
    :canonical: ansys.stk.core.stkobjects.IPlatformRFEnvironment.enable_local_rain_data
    :type: bool

    Gets or sets the option for enabling local rain data.

.. py:property:: local_rain_iso_height
    :canonical: ansys.stk.core.stkobjects.IPlatformRFEnvironment.local_rain_iso_height
    :type: float

    Gets or sets the local rain iso height.

.. py:property:: local_rain_rate
    :canonical: ansys.stk.core.stkobjects.IPlatformRFEnvironment.local_rain_rate
    :type: float

    Gets or sets the local rain rate.

.. py:property:: local_surface_temperature
    :canonical: ansys.stk.core.stkobjects.IPlatformRFEnvironment.local_surface_temperature
    :type: float

    Gets or sets the local surface temperature.

.. py:property:: propagation_channel
    :canonical: ansys.stk.core.stkobjects.IPlatformRFEnvironment.propagation_channel
    :type: "IAgPropagationChannel"

    Gets the propagation channel.


