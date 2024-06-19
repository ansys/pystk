IRFEnvironment
==============

.. py:class:: IRFEnvironment

   object
   
   Provide access to the properties and methods defining the RF environment.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~propagation_channel`
            * - :py:meth:`~supported_contour_rain_outage_percent_values`
            * - :py:meth:`~contour_rain_outage_percent`
            * - :py:meth:`~earth_temperature`
            * - :py:meth:`~supported_active_comm_systems`
            * - :py:meth:`~active_comm_system`
            * - :py:meth:`~magnetic_north_pole_latitude`
            * - :py:meth:`~magnetic_north_pole_longitude`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRFEnvironment


Property detail
---------------

.. py:property:: propagation_channel
    :canonical: ansys.stk.core.stkobjects.IRFEnvironment.propagation_channel
    :type: IAgPropagationChannel

    Gets the propagation channel.

.. py:property:: supported_contour_rain_outage_percent_values
    :canonical: ansys.stk.core.stkobjects.IRFEnvironment.supported_contour_rain_outage_percent_values
    :type: list

    Gets an array of supported contour rain outage percent values.

.. py:property:: contour_rain_outage_percent
    :canonical: ansys.stk.core.stkobjects.IRFEnvironment.contour_rain_outage_percent
    :type: float

    Gets or sets the contour rain outage percent.

.. py:property:: earth_temperature
    :canonical: ansys.stk.core.stkobjects.IRFEnvironment.earth_temperature
    :type: float

    Gets or sets the earth temperature.

.. py:property:: supported_active_comm_systems
    :canonical: ansys.stk.core.stkobjects.IRFEnvironment.supported_active_comm_systems
    :type: list

    Gets an array of supported active CommSystem objects.

.. py:property:: active_comm_system
    :canonical: ansys.stk.core.stkobjects.IRFEnvironment.active_comm_system
    :type: str

    Gets or sets the active CommSystem object.

.. py:property:: magnetic_north_pole_latitude
    :canonical: ansys.stk.core.stkobjects.IRFEnvironment.magnetic_north_pole_latitude
    :type: float

    Gets or sets magnetic north pole latitude.

.. py:property:: magnetic_north_pole_longitude
    :canonical: ansys.stk.core.stkobjects.IRFEnvironment.magnetic_north_pole_longitude
    :type: float

    Gets or sets magnetic north pole longitude.


