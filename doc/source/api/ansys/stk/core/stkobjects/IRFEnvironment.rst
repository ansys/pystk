IRFEnvironment
==============

.. py:class:: ansys.stk.core.stkobjects.IRFEnvironment

   object
   
   Provide access to the properties and methods defining the RF environment.

.. py:currentmodule:: IRFEnvironment

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IRFEnvironment.propagation_channel`
              - Gets the propagation channel.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRFEnvironment.supported_contour_rain_outage_percent_values`
              - Gets an array of supported contour rain outage percent values.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRFEnvironment.contour_rain_outage_percent`
              - Gets or sets the contour rain outage percent.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRFEnvironment.earth_temperature`
              - Gets or sets the earth temperature.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRFEnvironment.supported_active_comm_systems`
              - Gets an array of supported active CommSystem objects.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRFEnvironment.active_comm_system`
              - Gets or sets the active CommSystem object.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRFEnvironment.magnetic_north_pole_latitude`
              - Gets or sets magnetic north pole latitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRFEnvironment.magnetic_north_pole_longitude`
              - Gets or sets magnetic north pole longitude.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRFEnvironment


Property detail
---------------

.. py:property:: propagation_channel
    :canonical: ansys.stk.core.stkobjects.IRFEnvironment.propagation_channel
    :type: IPropagationChannel

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


